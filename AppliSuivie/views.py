from django.shortcuts import render

# Create your views here.
def home(request):
    
    return render(request,'AppliSuivie/index.html')
#
def forecast(request):
    return render(request,'AppliSuivie/previsions.html')
#
def alerts(request):
    return render(request,'AppliSuivie/alerts.html')
#
def settings(request):
    return render(request,'AppliSuivie/parametre.html')
#
def transactions(request):
    return render(request,'AppliSuivie/transaction.html')
#
def report(request):
    return render(request,'AppliSuivie/rapport.html')