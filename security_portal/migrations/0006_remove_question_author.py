# Generated by Django 3.1.3 on 2021-09-07 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security_portal', '0005_question_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='author',
        ),
    ]
