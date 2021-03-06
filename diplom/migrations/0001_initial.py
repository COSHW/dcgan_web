# Generated by Django 2.2.7 on 2020-05-04 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PictureModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_name', models.CharField(max_length=100)),
                ('file_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diplom.ModelsModel')),
            ],
        ),
    ]
