# Generated by Django 3.1.2 on 2020-10-01 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lister', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='YTApiKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apiKey', models.CharField(max_length=55)),
                ('timesUsed', models.TimeField(default=0)),
            ],
        ),
    ]
