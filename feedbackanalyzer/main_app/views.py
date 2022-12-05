from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Deliverable
from django.http import HttpResponse
from monkeylearn import MonkeyLearn
import environ

env = environ.Env()
environ.Env.read_env()

# Create your views here.


# ml = MonkeyLearn(env('MONKEY_LEARN_PASS'))
# a_data = Deliverable.objects.get(id=1)
# response = ml.classifiers.classify(
#     model_id='cl_NDBChtr7',
#     data=[
#         a_data.comments
#     ]
# )

# print(response.body[0]['classifications'][0]['tag_name'])

# Classes:
# class deliverableCreate():
#   model = Cat
#   fields = ['name', 'breed', 'description', 'age']


# Classes:
class DeliverableCreate(CreateView):
  model = Deliverable
  fields = '__all__'



# Home Pages:
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')


# Auth
def signup(request):
  return 'Hi'

def login(request):
  return 'Hi'



# Units:
def unit1(request):
  deliverables = Deliverable.objects.filter(units='1')
  return render(request, 'units/unit1.html', {'deliverables': deliverables})

def unit2(request):
  deliverables = Deliverable.objects.filter(units='2')
  return render(request, 'units/unit2.html', {'deliverables': deliverables})

def unit3(request):
  deliverables = Deliverable.objects.filter(units='3')
  return render(request, 'units/unit3.html', {'deliverables': deliverables})

def unit4(request):
  deliverables = Deliverable.objects.filter(units='4')
  return render(request, 'units/unit4.html', {'deliverables': deliverables})

#Deliverables:
def deliverables_index(request):
  deliverables = Deliverable.objects.all()
  return render(request, 'deliverables/index.html', {'deliverables': deliverables})


# def analyzer(request):
#   deliverables = Deliverable.objects.all()
#   return render(request, 'deliverables/analyzer.html', {'analyze': response.body[0]['classifications'][0]['tag_name']})
