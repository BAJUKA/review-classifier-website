from django.shortcuts import render

def Kerala_FloodsView(request):
    template_name = 'disasters/kerala_floods.html'
    return render(request, template_name)

def Indonesian_TsunamiView(request):
    template_name = 'disasters/indonesian_tsunami.html'
    return render(request, template_name)

def Cyclone_TitliView(request):
    template_name = 'disasters/cyclone_titli.html'
    return render(request, template_name)

def Hurricane_MichaelView(request):
    template_name = 'disasters/hurricane_michael.html'
    return render(request, template_name)