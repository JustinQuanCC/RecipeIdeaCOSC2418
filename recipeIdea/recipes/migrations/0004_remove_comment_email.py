# Generated by Django 4.1.3 on 2022-12-04 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
    ]
