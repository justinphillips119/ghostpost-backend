# Generated by Django 3.1.2 on 2020-10-05 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ghostpostmodel',
            name='post_type',
            field=models.CharField(choices=[('Boast', 'Boast'), ('Roast', 'Roast')], default='Boast', max_length=5),
        ),
    ]
