# Generated by Django 3.1.6 on 2021-02-18 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://cdn.dribbble.com/users/1012566/screenshots/4187820/topic-2.jpg?compress=1&resize=800x600', max_length=500),
        ),
    ]
