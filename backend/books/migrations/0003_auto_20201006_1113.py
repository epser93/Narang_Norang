# Generated by Django 2.1.15 on 2020-10-06 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20200924_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voicestorage',
            name='voice_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='voices.VoiceModel'),
        ),
    ]
