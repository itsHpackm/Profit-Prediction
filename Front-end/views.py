from django.shortcuts import render
import pickle 


# Create your views here.
def StateOneHotEncoder(state):
    oneHotEncoder = []
    if state == 'New York':
        oneHotEncoder.append(0)
        oneHotEncoder.append(0)
        oneHotEncoder.append(1)
    elif state == 'California':
        oneHotEncoder.append(1)
        oneHotEncoder.append(0)
        oneHotEncoder.append(0)
    else:
        oneHotEncoder.append(0)
        oneHotEncoder.append(1)
        oneHotEncoder.append(0)
    return oneHotEncoder


def ProfitPredict(rndSpend, administration, marketingSpend, state):
    rfeModel = pickle.load(open('C:/Users/assem/model.pkl', 'rb'))
    listVar = StateOneHotEncoder(state)
    listVar.extend([rndSpend,administration,marketingSpend])
    y_pred = rfeModel.predict([listVar])
    return y_pred[0]


def getForm(request):
    if request.method == 'POST':
        rnDSpend = request.POST.get('RnDSpend')
        administration = request.POST.get('Administration')
        marketingSpend = request.POST.get('MarketingSpend')
        state = request.POST['state']
        print(rnDSpend, '---', administration, '---', marketingSpend, '---', state)
        profit = ProfitPredict(rnDSpend, administration, marketingSpend, state)
        context = {'profit': profit,'rnDSpend':rnDSpend,'administration':administration,'MarketingSpend':marketingSpend,'state':state}
    return render(request, 'ProfitPrediction/results.html', context)


def index(request):
    return render(request, 'ProfitPrediction/index.html')
