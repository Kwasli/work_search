# Generated by Django 3.2.9 on 2022-06-04 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20220604_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='BanerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='baners/')),
                ('add_link', models.URLField()),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Картинка для банера',
                'verbose_name_plural': 'Картинки для банера',
                'ordering': ['-created'],
            },
        ),
    ]