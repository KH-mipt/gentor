from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'Chosing_Style/home.html', {})

def page_1(request):
    return render(request, 'Chosing_Style/page_1.html', {})

def page_2(request):
    return render(request, 'Chosing_Style/page_2.html', {})

def page_3(request):
    return render(request, 'Chosing_Style/page_3.html', {})

def page_11(request):
    return render(request, 'Chosing_Style/page_11.html', {})

def page_12(request):
    return render(request, 'Chosing_Style/page_12.html', {})

def page_13(request):
    return render(request, 'Chosing_Style/page_13.html', {})

def page_21(request):
    return render(request, 'Chosing_Style/page_21.html', {})

def page_22(request):
    return render(request, 'Chosing_Style/page_22.html', {})

def page_23(request):
    return render(request, 'Chosing_Style/page_23.html', {})

def page_31(request):
    return render(request, 'Chosing_Style/page_31.html', {})

def page_32(request):
    return render(request, 'Chosing_Style/page_32.html', {})

def page_33(request):
    return render(request, 'Chosing_Style/page_33.html', {})
