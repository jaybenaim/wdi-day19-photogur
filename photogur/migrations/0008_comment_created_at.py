# Generated by Django 2.2.3 on 2019-07-31 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photogur', '0007_remove_comment_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]