# Generated by Django 4.1.3 on 2022-12-06 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_deliverable_options_deliverable_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverable',
            name='analysis',
            field=models.CharField(default='natural', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deliverable',
            name='date',
            field=models.DateField(verbose_name='deliverable Submission Date'),
        ),
        migrations.AlterField(
            model_name='deliverable',
            name='githubrepo',
            field=models.CharField(max_length=120, verbose_name='github Repository Link'),
        ),
        migrations.AlterField(
            model_name='deliverable',
            name='hmwname',
            field=models.CharField(max_length=120, verbose_name='deliverable Name'),
        ),
        migrations.AlterField(
            model_name='deliverable',
            name='units',
            field=models.CharField(choices=[('1', 'Unit1'), ('2', 'Unit2'), ('3', 'Unit3'), ('4', 'Unit4')], default='1', max_length=1, verbose_name='Unit'),
        ),
    ]
