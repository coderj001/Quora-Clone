# Generated by Django 3.2.3 on 2021-05-14 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_created=True)),
                ('Answare', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('answered_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to=settings.AUTH_USER_MODEL, verbose_name='Answered By')),
            ],
            options={
                'verbose_name': 'Answere',
                'verbose_name_plural': 'Answeres',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='answers',
            field=models.ManyToManyField(related_name='question', to='core.Answer', verbose_name='Answers'),
        ),
    ]
