# Generated by Django 3.1.3 on 2021-09-07 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0015_remove_question_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, default='images/no_img.jpg', null=True, upload_to='images/'),
        ),
    ]
