# Generated by Django 3.0.2 on 2020-01-15 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authblog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='greetings',
            old_name='text',
            new_name='description',
        ),
        migrations.AddField(
            model_name='greetings',
            name='title',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
