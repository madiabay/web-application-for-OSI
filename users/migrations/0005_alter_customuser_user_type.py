# Generated by Django 4.1.7 on 2023-03-16 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('Liver', 'Liver'), ('Chairman', 'Chairman')], max_length=30, verbose_name='user type'),
        ),
    ]