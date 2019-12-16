# Generated by Django 3.0 on 2019-12-16 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('referer', models.TextField()),
                ('amount', models.FloatField()),
                ('balance', models.FloatField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
