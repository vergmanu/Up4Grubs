# Generated by Django 4.0.3 on 2022-04-16 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grub',
            name='type',
            field=models.CharField(choices=[('Fresh Produce', 'Fresh'), ('Pantry', 'Pantry')], default='Fresh Produce', max_length=50),
        ),
    ]
