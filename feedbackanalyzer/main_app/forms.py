from django.forms import ModelForm
from .models import Deliverable

class DeliverableForm(ModelForm):
  class Meta:
    model = Deliverable
    fields = '__all__'