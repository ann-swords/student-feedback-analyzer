# Generated by Django 4.1.3 on 2023-03-25 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_deliverable_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliverable',
            name='analysis',
        ),
        migrations.CreateModel(
            name='AnalyzedData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analysis', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deliverable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.deliverable')),
            ],
        ),
    ]