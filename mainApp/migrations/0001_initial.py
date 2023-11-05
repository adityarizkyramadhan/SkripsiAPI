# Generated by Django 4.2.7 on 2023-11-05 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=500)),
                ('email', models.EmailField(db_column='email', max_length=500, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('label', models.CharField(db_column='label', max_length=500)),
                ('sound_uri', models.TextField(db_column='sound_uri')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_column='date_created')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='data', to='mainApp.users')),
            ],
        ),
    ]
