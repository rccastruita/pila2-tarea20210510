from django.shortcuts import render
from django.views.generic import ListView

from .models import Curriculum, Experiencia

# Create your views here.


class CurriculumListView(ListView):
    model = Curriculum
    template_name = 'curriculum_list.html'
    context_object_name = 'curriculums'
