# Generated by Django 3.2.5 on 2021-07-07 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('qna', '0002_comment_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('content', models.TextField()),
                ('isfile', models.BooleanField(default=False)),
                ('pubdate', models.DateTimeField(auto_now_add=True)),
                ('chapter', models.IntegerField()),
                ('page', models.IntegerField()),
                ('qnum', models.CharField(max_length=100)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qna.room')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile')),
            ],
        ),
    ]
