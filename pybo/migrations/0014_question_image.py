# Generated by Django 3.1.3 on 2021-09-07 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0013_remove_question_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, default='images/네이버_로고.jpg', null=True, upload_to='images/'),
        ),
    ]