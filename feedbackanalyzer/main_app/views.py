from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Deliverable, AnalyzedData
from django.http import HttpResponse
from monkeylearn import MonkeyLearn
import environ
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Import the decorators for Function based Views only
from django.contrib.auth.decorators import login_required
# Import the decorators for Class based Views only
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

env = environ.Env()
environ.Env.read_env()

# Create your views here.

# Classes:
class DeliverableCreate(CreateView):
  model = Deliverable
  fields = ['units', 'hmwname', 'githubrepo', 'comments', 'date']

# attach the user to the data comes in from the form
  def form_valid(self, form):
      # self.request.user is the logged user
      form.instance.user = self.request.user
      # Allows the createView form_valid methd to do it's normal work
      return super().form_valid(form)


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



# Units:
def unit1(request):
  deliverables = Deliverable.objects.filter(units='1', user=request.user)
  return render(request, 'units/unit1.html', {'deliverables': deliverables})

def unit2(request):
  deliverables = Deliverable.objects.filter(units='2', user=request.user)
  return render(request, 'units/unit2.html', {'deliverables': deliverables})

def unit3(request):
  deliverables = Deliverable.objects.filter(units='3', user=request.user)
  return render(request, 'units/unit3.html', {'deliverables': deliverables})

def unit4(request):
  deliverables = Deliverable.objects.filter(units='4', user=request.user)
  return render(request, 'units/unit4.html', {'deliverables': deliverables})

#Deliverables:
def deliverables_index(request):
  # deliverables = Deliverable.objects.all()
  deliverables = Deliverable.objects.filter(user=request.user)
  return render(request, 'deliverables/index.html', {'deliverables': deliverables})

def deliverable_detail(request, del_id):
  deliverables = Deliverable.objects.get(id=del_id)
  return render(request, 'deliverables/detail.html', {'deliverables': deliverables})


# function that analyzes the comments using sentiment analysis.
def analyzer(request):
  unit1 = int(Deliverable.objects.filter(units='1').count())
  unit2 = int(Deliverable.objects.filter(units='2').count())
  unit3 = int(Deliverable.objects.filter(units='3').count())
  unit4 = int(Deliverable.objects.filter(units='4').count())

  # ml = MonkeyLearn(env('MONKEY_LEARN_PASS'))
  ml = MonkeyLearn('83bd8a3d57b774de0e8c38dac7db5cf99d75d896')
  b_data = Deliverable.objects.latest('id')
  response = ml.classifiers.classify(
  model_id='cl_NDBChtr7',
  data=[
      b_data.comments
  ]
  )
  b_data = b_data.id
  analysis = response.body[0]['classifications'][0]['tag_name']
  analyzed_data = AnalyzedData(deliverable_id=b_data, analysis=analysis, created_at=timezone.now())
  analyzed_data.save()
  # a_data = Deliverable.objects.filter(id=b_data).update(analysis = response.body[0]['classifications'][0]['tag_name'])
  # deliverables = Deliverable.objects.all()

  return render(request, 'deliverables/analyzer.html', {'unit1':unit1, 'unit2':unit2, 'unit3':unit3, 'unit4':unit4})


# Counting each unit's positive and negative homeworks.(through charts)
# UNIT1
def unit1_feedback(request):
  unit1_pos = AnalyzedData.objects.filter(deliverable__units='1', analysis='positive').count()
  unit1_pos = int(unit1_pos)

  unit1_neg = AnalyzedData.objects.filter(deliverable__units='1', analysis='negative').count()
  unit1_neg = int(unit1_neg)


  unit1_nat = AnalyzedData.objects.filter(deliverable__units='1', analysis='neutral').count()
  unit1_nat = int(unit1_nat)

  unit1 = Deliverable.objects.filter(units='1')

  return render(request, 'deliverables/analyze_unit1.html', {'unit1_pos': unit1_pos, 'unit1_neg': unit1_neg, 'unit1':unit1, 'unit1_nat':unit1_nat})


  # UNIT2
def unit2_feedback(request):
  unit2_pos = AnalyzedData.objects.filter(deliverable__units='2', analysis='positive').count()
  unit2_pos = int(unit2_pos)

  unit2_neg = AnalyzedData.objects.filter(deliverable__units='2', analysis='negative').count()
  unit2_neg = int(unit2_neg)

  unit2_nat = AnalyzedData.objects.filter(deliverable__units='2', analysis='neutral').count()
  unit2_nat = int(unit2_nat)

  unit2 = Deliverable.objects.filter(units='2')

  return render(request, 'deliverables/analyze_unit2.html', {'unit2_pos': unit2_pos, 'unit2_neg': unit2_neg, 'unit2_nat':unit2_nat, 'unit2':unit2})

 # UNIT3
def unit3_feedback(request):
  unit3_pos = AnalyzedData.objects.filter(deliverable__units='3', analysis='positive').count()
  unit3_pos = int(unit3_pos)

  unit3_neg = AnalyzedData.objects.filter(deliverable__units='3', analysis='negative').count()
  unit3_neg = int(unit3_neg)

  unit3_nat = AnalyzedData.objects.filter(deliverable__units='3', analysis='neutral').count()
  unit3_nat = int(unit3_nat)

  unit3 = Deliverable.objects.filter(units='3')

  return render(request, 'deliverables/analyze_unit3.html', {'unit3_pos': unit3_pos, 'unit3_neg': unit3_neg, 'unit3_nat':unit3_nat, 'unit3':unit3})

   # UNIT4
def unit4_feedback(request):
  unit4_pos = AnalyzedData.objects.filter(deliverable__units='4', analysis='positive').count()
  unit4_pos = int(unit4_pos)

  unit4_neg = AnalyzedData.objects.filter(deliverable__units='4', analysis='negative').count()
  unit4_neg = int(unit4_neg)

  unit4_nat = AnalyzedData.objects.filter(deliverable__units='4', analysis='neutral').count()  
  unit4_nat = int(unit4_nat)

  unit4 = Deliverable.objects.filter(units='4')

  return render(request, 'deliverables/analyze_unit4.html', {'unit4_pos': unit4_pos, 'unit4_neg': unit4_neg, 'unit4_nat':unit4_nat, 'unit4':unit4})


# Sign Up View Function:
def signup(request):
    error_message = ''
    if request.method == 'POST':
        # Make a 'user' form object with the data from the browser
        form = UserCreationForm(request.POST)

        if form.is_valid():
            # save user to db
            user = form.save()
            # Log in the user automatically once they sign up
            login(request, user)
            return redirect('index')
        
        else:
            error_message = 'Invalid: Please Try Again!'

    # If there's a bad post or get request:
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)