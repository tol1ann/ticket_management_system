# Generated by Django 4.2.7 on 2023-12-02 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0012_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='message',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.message'),
        ),
    ]
