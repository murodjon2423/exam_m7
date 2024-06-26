# Generated by Django 5.0.3 on 2024-04-23 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Added',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('city', models.CharField(max_length=100)),
                ('export', models.IntegerField()),
                ('income', models.DecimalField(decimal_places=2, max_digits=20)),
                ('company', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='added/')),
            ],
            options={
                'verbose_name_plural': 'Added',
                'db_table': 'added',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('city', models.TextField()),
                ('date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='events/')),
                ('added', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Events',
                'db_table': 'events',
            },
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Home',
                'db_table': 'homes',
            },
        ),
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('decriptions', models.TextField()),
                ('position', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='humans/')),
            ],
            options={
                'verbose_name_plural': 'Humans',
                'db_table': 'humans',
            },
        ),
    ]
