# Generated by Django 4.0.5 on 2022-07-07 14:18

from django.db import migrations


def write_author(apps, schema_editor):
    # We can't import the Question model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Question = apps.get_model('polls', 'Question')
    user = apps.get_model('auth', 'User').objects.get_or_create(id=1)
    for question in Question.objects.all():
        question.author = user
        question.save()

class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_question_author'),
    ]

    operations = [
        migrations.RunPython(write_author),
    ]
