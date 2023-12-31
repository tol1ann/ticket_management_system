# Generated by Django 4.2.7 on 2023-11-23 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('re', 'resolved'), ('un', 'unresolved'), ('fr', 'freezed')], default='un', max_length=16)),
                ('comment', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
