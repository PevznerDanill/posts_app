# Generated by Django 4.2.2 on 2023-06-14 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_posts', '0004_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created_at',), 'verbose_name': 'comment', 'verbose_name_plural': 'comments'},
        ),
    ]