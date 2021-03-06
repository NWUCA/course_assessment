# Generated by Django 3.2 on 2021-04-19 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_assessment', '0006_auto_20210413_1714'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['school']},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['created_by']},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ['school']},
        ),
        migrations.AlterField(
            model_name='review',
            name='anonymous',
            field=models.BooleanField(verbose_name='匿名评价'),
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.SmallIntegerField(verbose_name='打分 (满分 5 分)'),
        ),
    ]
