# Generated by Django 4.1.5 on 2023-02-20 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users_app", "0004_alter_profile_user_skill"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="email",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="name",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="username",
        ),
        migrations.AddField(
            model_name="todo_list",
            name="name",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="todo_list",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users_app.profile",
            ),
        ),
        migrations.AddField(
            model_name="todo_list",
            name="text",
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.DeleteModel(
            name="Skill",
        ),
    ]