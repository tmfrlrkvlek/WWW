# Generated by Django 3.2.5 on 2021-07-09 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0004_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qna',
            name='qnum',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
