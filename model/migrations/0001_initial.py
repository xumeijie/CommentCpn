# Generated by Django 3.2.5 on 2021-12-19 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=36, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, verbose_name='用户名')),
                ('pwd', models.CharField(max_length=64, verbose_name='密码')),
                ('avatar', models.CharField(max_length=256, null=True)),
                ('nickname', models.CharField(max_length=18, null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
