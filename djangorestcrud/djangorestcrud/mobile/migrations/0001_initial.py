# Generated by Django 4.0.2 on 2022-10-30 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_name', models.CharField(max_length=100)),
                ('phone_model', models.CharField(max_length=100)),
                ('make', models.IntegerField()),
            ],
            options={
                'db_table': 'phone',
            },
        ),
    ]
