# Generated by Django 4.2.2 on 2023-06-14 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_posts', '0003_comment_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created_at',), 'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
    ]