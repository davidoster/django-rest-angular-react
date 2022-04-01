# Generated by Django 4.0.3 on 2022-03-29 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=70)),
                ('description', models.TextField(max_length=200)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
