# Generated by Django 3.2.3 on 2021-05-25 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0015_alter_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='pictures/user.png', upload_to='pictures/'),
        ),
    ]
