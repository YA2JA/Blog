# Generated by Django 2.2.12 on 2020-08-10 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='_pub_date',
            field=models.DateField(verbose_name='Дата публикации'),
        ),
    ]
