from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def home(request):

    name = "Md Rakib Hassan"
    des  = "Software Engineer"
    dep  = "Information Technology"
    hobby = ['Playing Cricket', 'Programming', 'Reading Book']

    parents = {
        'father_name': 'Md Shahjahan Mia',
        'mother_name': "Rashida Bagum",
        'city': 'Chandpure',
    }

    context = {
        'name': name,
        'designation': des,
        'department' : dep,
        'hobby' : hobby,
        'parents' : parents,
    }

    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')
