from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Profile, Education, Skill, Service, Project
from .forms import ContactForm
# Create your views here.



def home(request):
    profile = Profile.objects.first()
    education = Education.objects.all()
    skills = Skill.objects.all()
    services = Service.objects.all()
    projects = Project.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre message a bien été envoyé. Merci !")
            return redirect('home')
        else:
            messages.error(request, "Merci de corriger les erreurs du formulaire.")
    else:
        form = ContactForm()

    context = {
        'profile': profile,
        'education': education,
        'skills': skills,
        'services': services,
        'projects': projects,
        'form': form,
    }
    return render(request, 'main/home.html', context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'main/project_detail.html', {'project': project})