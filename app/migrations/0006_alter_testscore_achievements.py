# Generated by Django 5.1.3 on 2024-12-14 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_testscore_achievements_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testscore',
            name='achievements',
            field=models.TextField(blank=True, null=True),
        ),
    ]