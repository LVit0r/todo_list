# Generated by Django 5.0.3 on 2024-04-02 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarefa', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
