# Generated by Django 3.1.3 on 2021-09-07 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0010_remove_question_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, default='https://image.ahnlab.com/img_upload/kr/site/images2/info/img_info12.jpg', null=True, upload_to='images/'),
        ),
    ]
