# Generated by Django 2.1.15 on 2020-09-23 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200921_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favorite',
            field=models.ManyToManyField(related_name='like_user', to='books.Fairytale'),
        ),
    ]
