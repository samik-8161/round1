# Generated by Django 2.2.3 on 2019-08-30 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0019_remove_profile_visited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='buff_cntr',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='year',
            field=models.CharField(choices=[('FE', 'FE'), ('SE', 'SE')], default='FE', max_length=2),
        ),
        migrations.AlterField(
            model_name='response',
            name='resp',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]