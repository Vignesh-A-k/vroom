from django.shortcuts import render

def main(request):
    context = {}
    return render(request, 'store/main.html', context)
def store(request):
    context = {}
    return render(request, 'store/store.html', context)
def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
