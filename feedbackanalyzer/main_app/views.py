from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Deliverable
from django.http import HttpResponse
from monkeylearn import MonkeyLearn
import environ

env = environ.Env()
environ.Env.read_env()

# Create your views here.

# Classes:
class DeliverableCreate(CreateView):
  model = Deliverable
  fields = ['units', 'hmwname', 'githubrepo', 'comments', 'date']


class DeliverableUpdate(UpdateView):
  model = Deliverable
  fields = ['units', 'hmwname', 'githubrepo', 'comments']

class DeliverableDelete(DeleteView):
  model = Deliverable
  success_url = '/deliverables/'



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

def deliverable_detail(request, del_id):
  deliverables = Deliverable.objects.get(id=del_id)
  return render(request, 'deliverables/detail.html', {'deliverables': deliverables})


# function that analyzes the comments using sentiment analysis.
def analyzer(request):
  ml = MonkeyLearn(env('MONKEY_LEARN_PASS'))
  b_data = Deliverable.objects.latest('id')
  response = ml.classifiers.classify(
  model_id='cl_NDBChtr7',
  data=[
      b_data.comments
  ]
  )
  b_data = b_data.id
  a_data = Deliverable.objects.filter(id=b_data).update(analysis = response.body[0]['classifications'][0]['tag_name'])
  # deliverables = Deliverable.objects.all()

# Counting each unit's positive and negative homeworks.
# UNIT1
  unit1_pos = Deliverable.objects.filter(units='1', analysis='positive').count()
  unit1_pos = int(unit1_pos)

  unit1_neg = Deliverable.objects.filter(units='1', analysis='negative').count()
  unit1_neg = int(unit1_neg)
# UNIT2
  unit2_pos = Deliverable.objects.filter(units='2', analysis='positive').count()
  unit2_pos = int(unit2_pos)

  unit2_neg = Deliverable.objects.filter(units='2', analysis='negative').count()
  unit2_neg = int(unit2_neg)
  # UNIT3
  unit3_pos = Deliverable.objects.filter(units='3', analysis='positive').count()
  unit3_pos = int(unit3_pos)

  unit3_neg = Deliverable.objects.filter(units='3', analysis='negative').count()
  unit3_neg = int(unit3_neg)
  # UNIT4
  unit4_pos = Deliverable.objects.filter(units='4', analysis='positive').count()
  unit4_pos = int(unit4_pos)

  unit4_neg = Deliverable.objects.filter(units='4', analysis='negative').count()
  unit4_neg = int(unit4_neg)


  return render(request, 'deliverables/analyzer.html', {'unit1_pos': unit1_pos, 'unit1_neg': unit1_neg, 'unit2_pos': unit2_pos, 'unit2_neg': unit2_neg, 'unit3_pos': unit3_pos, 'unit3_neg': unit3_neg, 'unit4_pos': unit4_pos, 'unit4_neg': unit4_neg,})

