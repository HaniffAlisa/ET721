# Generated by Django 5.1.2 on 2024-11-04 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dolist", "0002_remove_todolist_completed_remove_todolist_text_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="todolist",
            name="completed",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="todolist",
            name="title",
            field=models.CharField(max_length=100),
        ),
    ]
