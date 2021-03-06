# Generated by Django 3.2.6 on 2021-08-11 12:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("socialaccount", "0003_extra_data_default_dict"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("frequency_in_days", models.IntegerField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "linkedin_url",
                    models.URLField(blank=True, max_length=100, null=True),
                ),
                ("twitter_url", models.URLField(blank=True, max_length=100, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="InteractionType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("slug", models.SlugField()),
                ("name", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="PhoneNumber",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("phone_number", models.CharField(max_length=50)),
                (
                    "contact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="phone_numbers",
                        to="networking_base.contact",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Interaction",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("was_at", models.DateTimeField()),
                (
                    "contacts",
                    models.ManyToManyField(
                        related_name="interactions", to="networking_base.Contact"
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="networking_base.interactiontype",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="interactions",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GoogleEmail",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("gmail_message_id", models.CharField(max_length=100)),
                ("data", models.JSONField()),
                (
                    "interaction",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="google_emails",
                        to="networking_base.interaction",
                    ),
                ),
                (
                    "social_account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="socialaccount.socialaccount",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GoogleCalendarEvent",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("google_calendar_id", models.CharField(max_length=100)),
                ("data", models.JSONField()),
                (
                    "interaction",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="google_calendar_events",
                        to="networking_base.interaction",
                    ),
                ),
                (
                    "social_account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="socialaccount.socialaccount",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ContactDuplicate",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("similarity", models.FloatField()),
                (
                    "contact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="networking_base.contact",
                    ),
                ),
                (
                    "other_contact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="networking_base.contact",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EmailAddress",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=100)),
                (
                    "contact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="email_addresses",
                        to="networking_base.contact",
                    ),
                ),
            ],
            options={
                "unique_together": {("contact", "email")},
            },
        ),
    ]
