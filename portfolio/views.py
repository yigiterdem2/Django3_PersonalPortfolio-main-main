from django.shortcuts import render,redirect,HttpResponse
from .models import Project, About, Skills_Value, Skills_About, Title
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.

def home(request):
    projects = Project.objects.all()
    about = About.objects.all()
    skills_about = Skills_About.objects.all()
    skills_value = Skills_Value.objects.all().order_by('-value')
    titles=Title.objects.all()
    context = {
        "projects" : projects,
        "about" : about,
        "skill_about" : skills_about,
        "skill_value" : skills_value,
        "titles" : titles,
        }
    return render(request, 'portfolio/home.html', context)
def login(request):
    return render(request, 'portfolio/login.html')
def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email= form.cleaned_data['email']
            message=form.cleaned_data['message']
            EmailMessage(
                'contact submission from {}'.format(name),message,
                'form-response@example.com',
                ['test.mailtrap1234@gmail.com'],
                [],
                reply_to=[email]
            ).send()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
def success(request):
    return HttpResponse('BAŞARILI')