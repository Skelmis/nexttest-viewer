# Generated by Django 4.0.4 on 2022-07-09 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='description',
            field=models.TextField(blank=True, help_text='A description to display on the page'),
        ),
    ]