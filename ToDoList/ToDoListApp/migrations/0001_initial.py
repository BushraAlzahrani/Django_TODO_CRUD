# Generated by Django 4.0.4 on 2022-05-26 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(help_text='The user to do item.', max_length=50)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
