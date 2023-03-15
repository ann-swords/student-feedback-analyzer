from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

UNITS = (
    ('1', 'Unit1'),
    ('2', 'Unit2'),
    ('3', 'Unit3'),
    ('4', 'Unit4'),
)

class Deliverable(models.Model):
    date = models.DateField('deliverable Submission Date')
    units = models.CharField(
        'Unit',
        max_length=1,
        choices = UNITS,
        default=UNITS[0][0]
    )
    hmwname = models.CharField('deliverable Name', max_length=120)
    githubrepo = models.CharField('github Repository Link', max_length=120)
    comments = models.CharField(max_length=300)
    analysis = models.CharField(max_length=10)
     # Add the foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.hmwname

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_units_display()} on {self.date}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'del_id': self.id})

    # change the default sort
    class Meta:
        ordering = ['-date']