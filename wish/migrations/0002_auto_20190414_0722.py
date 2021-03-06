# Generated by Django 2.2 on 2019-04-14 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wish', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wish',
            options={'verbose_name_plural': 'wishes'},
        ),
        migrations.RemoveField(
            model_name='wish',
            name='reserved',
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('wish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wish.Wish')),
            ],
        ),
    ]
