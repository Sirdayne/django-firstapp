# Generated by Django 2.2.2 on 2019-06-08 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('startTime', models.TextField()),
                ('endTime', models.TextField()),
                ('userId', models.TextField()),
            ],
        ),
    ]
