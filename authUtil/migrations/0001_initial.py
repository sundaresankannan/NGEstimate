# Generated by Django 2.0.6 on 2018-08-29 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_mstr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_id', models.CharField(max_length=20)),
                ('login_pwd', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=18)),
                ('first_name', models.CharField(max_length=13)),
                ('startdate', models.DateTimeField()),
                ('enddate', models.DateTimeField()),
            ],
        ),
    ]