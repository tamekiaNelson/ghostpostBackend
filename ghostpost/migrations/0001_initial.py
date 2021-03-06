# Generated by Django 3.0.2 on 2020-01-15 14:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GhostPoster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=280)),
                ('is_boast', models.BooleanField(default=True)),
                ('up_votes', models.IntegerField(default=0)),
                ('down_votes', models.IntegerField(default=0)),
                ('total_votes', models.IntegerField(default=0)),
                ('submission_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
