# Generated by Django 3.1.7 on 2021-03-07 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210226_2253'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Visitor',
        ),
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('EMPLOYEE', 'Employee'), ('MEMBER', 'Member')], default='MEMBER', max_length=50),
        ),
    ]