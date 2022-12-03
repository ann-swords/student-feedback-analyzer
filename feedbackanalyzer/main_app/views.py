from django.shortcuts import render
from django.http import HttpResponse
from monkeylearn import MonkeyLearn

# Create your views here.


# ml = MonkeyLearn('370193db144a959e07e484106ffa2388496c9eac')

# response = ml.classifiers.classify(
#     model_id='cl_NDBChtr7',
#     data=[
#         "the homework was so hard for me I was not able to solve most of it.",
#     ]
# )

def home(request):
  return render(request, 'home.html')

# print(response.body)
def signup(request):
  return 'Hi'

def login(request):
  return 'Hi'

def about(request):
  return render(request, 'about.html')



# Units:
def unit1(request):
  return render(request, 'units/unit1.html')

def unit2(request):
  return render(request, 'units/unit2.html')

def unit3(request):
  return render(request, 'units/unit3.html')

def unit4(request):
  return render(request, 'units/unit4.html')