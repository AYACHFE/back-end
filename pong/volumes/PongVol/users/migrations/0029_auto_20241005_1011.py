# Generated by Django 3.2.5 on 2024-10-05 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='staticfiles/images/profiles/default.png', upload_to='staticfiles/images/profiles/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='default_name', max_length=255, unique=True),
        ),
    ]
