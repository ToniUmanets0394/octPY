# Generated by Django 2.2.4 on 2020-03-26 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_question_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=10),
        ),
    ]