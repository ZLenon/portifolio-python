from django.db import migrations, models
import django.db.models.deletion

make_migration = migrations.Migration


class Migration(make_migration):
    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("github_url", models.URLField()),
                ("keyword", models.CharField(max_length=100)),
                ("key_skill", models.CharField(max_length=100)),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="projects",
                        to="projects.profile",
                    ),
                ),
            ],
        ),
    ]
