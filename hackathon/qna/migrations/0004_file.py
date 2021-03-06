# Generated by Django 3.2.5 on 2021-07-07 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('qna', '0003_qna'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=1)),
                ('filename', models.FileField(upload_to='')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile')),
                ('qna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qna.qna')),
            ],
        ),
    ]
