# Generated by Django 5.0.3 on 2024-03-30 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_games_delete_coinflip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side', models.CharField(max_length=10)),
                ('time_res', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Games',
        ),
    ]