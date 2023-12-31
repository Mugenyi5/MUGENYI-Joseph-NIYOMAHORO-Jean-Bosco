# Generated by Django 4.2.3 on 2023-07-20 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('Technology', 'Technology'), ('Business', 'Business'), ('Social', 'Social')], max_length=100)),
                ('venue', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('is_fee', models.BooleanField(default=True)),
            ],
        ),
    ]
