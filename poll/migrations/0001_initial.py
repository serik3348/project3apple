# Generated by Django 4.0.4 on 2022-04-22 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='POST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, max_length=100)),
                ('first_name', models.CharField(db_index=True, max_length=100)),
                ('last_name', models.TextField(max_length=500)),
                ('phone_number', models.CharField(max_length=500)),
                ('birthday', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=500)),
            ],
        ),
    ]
