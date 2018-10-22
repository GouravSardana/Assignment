from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from medical_detail.models import Disease


class Homepage(TemplateView):
    template_name='index.html'


class Upload(TemplateView):
    template_name = 'upload.html'
    def post(self, request, *args, **kwargs):
        name = self.request.POST.get('name')
        symptoms = self.request.POST.get('symptoms')
        causes = self.request.POST.get('causes')
        diagnosis = self.request.POST.get('diagnosis')
        treatment = self.request.POST.get('treatment')
        prevention = self.request.POST.get('prevention')

        form = Disease(name=name, symptoms=symptoms, causes=causes, diagnosis=diagnosis, treatment=treatment, prevention=prevention)  # = wala model ka naam
        form.save()
        print(form)
        return render(request, 'index.html')


class Content(ListView):
    template_name = 'content.html'
    queryset = Disease.objects.all()
