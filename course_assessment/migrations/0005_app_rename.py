# Generated by Django 3.1.7 on 2021-04-04 16:29

from django.db import migrations


def rename_content_types(apps, schema_editor):
    content_type = apps.get_model('contenttypes', 'ContentType')
    content_type.objects.filter(app_label='core').update(app_label='course_assessment')


class Migration(migrations.Migration):

    dependencies = [
        ('course_assessment', '0004_auto_20201229_0459'),
    ]

    operations = [
        migrations.RunPython(rename_content_types),
        migrations.AlterModelTable('course', 'course_assessment_course'),
        migrations.AlterModelTable('review', 'course_assessment_review'),
        migrations.AlterModelTable('school', 'course_assessment_school'),
        migrations.AlterModelTable('teacher', 'course_assessment_teacher'),
    ]
