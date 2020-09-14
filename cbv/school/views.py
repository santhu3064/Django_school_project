from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from school.models import School, Student
from django.utils import timezone
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class SchoolListView(ListView):
    model = School

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model = School
    template_name = 'school/school_detail.html'


class SchoolCreateView(CreateView):
    model = School
    fields = '__all__'


class SchoolUpdateView(UpdateView):
    model = School
    fields = ['name', 'principal']

class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy('school:list')

class StudentCreateView(CreateView):
    model = Student
    # fields = '__all__'
    fields = ['name', 'age']

    def form_valid(self, form):
        form.instance.school = School.objects.get(pk=self.kwargs.get('pk'))
        return super(StudentCreateView, self).form_valid(form)

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'age']

class StudentDeleteView(DeleteView):
    model = Student

    def get_success_url(self):
        # Assuming there is a ForeignKey from Comment to Post in your model
        school = self.object.school
        return reverse_lazy('school:detail', kwargs={'pk': school.id})



