from django.shortcuts import render

# Create your views here.
def home(request):

    name = "Md Rakib Hassan"
    des  = "Software Engineer"
    dep  = "Information Technology"
    hobby = ['Playing Cricket', 'Programming', 'Reading Book']

    context = {
        'name': name,
        'designation': des,
        'department' : dep,
        'hobby' : hobby,
    }

    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')
