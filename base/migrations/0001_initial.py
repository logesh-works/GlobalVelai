# Generated by Django 5.1.6 on 2025-02-19 11:43

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Applicant",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_suspended", models.BooleanField(default=False)),
                ("created_on", models.DateField(auto_now_add=True)),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Others")],
                        max_length=50,
                    ),
                ),
                ("phone_number", models.BigIntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("address", models.TextField()),
                ("city", models.CharField(max_length=255)),
                ("pincode", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="AwardsDetails",
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
                ("award_name", models.CharField(max_length=255)),
                ("awarded_organisation", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="CountryList",
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
                (
                    "country_name",
                    models.CharField(
                        default=None, max_length=255, verbose_name="Country Name"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DegreeList",
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
                (
                    "degree_name",
                    models.CharField(
                        default=None, max_length=255, verbose_name="Degree Name"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FieldsList",
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
                (
                    "field_name",
                    models.CharField(
                        default=None, max_length=255, verbose_name="Field Name"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SkillList",
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
                (
                    "skill_name",
                    models.CharField(
                        default=None, max_length=255, verbose_name="Skill Name"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StateList",
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
                (
                    "state_name",
                    models.CharField(
                        default=None, max_length=255, verbose_name="State Name"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CertificationDetails",
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
                ("certificate_name", models.CharField(max_length=255)),
                ("year_of_certification", models.IntegerField()),
                (
                    "applicant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="base.applicant"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="applicant",
            name="country",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="base.countrylist"
            ),
        ),
        migrations.CreateModel(
            name="EducationDetails",
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
                ("year_of_passing", models.IntegerField()),
                ("school", models.CharField(max_length=255)),
                (
                    "applicant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="base.applicant"
                    ),
                ),
                (
                    "degree",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="base.degreelist",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CompanyProfile",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("company_name", models.CharField(max_length=255)),
                ("phone_number", models.BigIntegerField()),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("address", models.TextField()),
                ("city", models.CharField(max_length=255)),
                ("state", models.CharField(max_length=255)),
                ("pincode", models.IntegerField()),
                ("country", models.CharField(max_length=255)),
                ("website", models.URLField(blank=True, null=True)),
                (
                    "industry_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="base.fieldslist",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PreferenceDetails",
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
                ("position", models.CharField(max_length=255)),
                ("available_from", models.DateField()),
                ("has_passport", models.BooleanField(default=False)),
                (
                    "salary_expectation",
                    models.CharField(
                        choices=[("4L", "4L"), ("5L", "5L"), ("6L+", "6L+")],
                        max_length=230,
                    ),
                ),
                (
                    "applicant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="base.applicant"
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="base.countrylist",
                    ),
                ),
                ("industry", models.ManyToManyField(to="base.fieldslist")),
            ],
        ),
        migrations.CreateModel(
            name="JobPostings",
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
                ("is_suspended", models.BooleanField(default=False)),
                ("vacancies", models.IntegerField()),
                ("posted_on", models.DateField(auto_now_add=True)),
                ("is_fulfilled", models.BooleanField(default=False)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.companyprofile",
                    ),
                ),
                ("required_skill", models.ManyToManyField(to="base.skilllist")),
            ],
        ),
        migrations.CreateModel(
            name="EmploymentHistory",
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
                ("job_title", models.CharField(max_length=255)),
                ("employer", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=255)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="base.countrylist",
                    ),
                ),
                (
                    "state",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="base.statelist",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="applicant",
            name="state",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="base.statelist"
            ),
        ),
        migrations.CreateModel(
            name="WorkDetails",
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
                (
                    "years_of_experience",
                    models.CharField(
                        choices=[
                            ("1", "1"),
                            ("2", "2"),
                            ("3", "3"),
                            ("4", "4"),
                            ("5", "5"),
                            ("6", "6"),
                            ("7", "7"),
                            ("8", "8"),
                            ("9", "9"),
                            ("10+", "10+"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "applicant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="base.applicant"
                    ),
                ),
                ("skill", models.ManyToManyField(to="base.skilllist")),
            ],
        ),
    ]
