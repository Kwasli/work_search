# Generated by Django 3.2.9 on 2022-06-23 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='summary',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='Резюме'),
        ),
    ]