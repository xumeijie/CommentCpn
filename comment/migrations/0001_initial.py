# Generated by Django 3.2.5 on 2021-12-19 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, '文章评论'), (2, '留言'), (3, '其他')], default=1, verbose_name='指向哪里')),
                ('article', models.IntegerField(default=0, null=True, verbose_name='如果该评论不是指向文章的话那么值为0')),
                ('date_joined', models.DateField(auto_now_add=True, verbose_name='发表评论的时间')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parentC', to='comment.comment', verbose_name='指向本条评论的父级评论')),
                ('replay', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='repliesC', to='model.userinfo', verbose_name='指向本条评论的回复对象')),
                ('root', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rootC', to='comment.comment', verbose_name='指向本条评论的根评论')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.userinfo', verbose_name='发表该评论的用户')),
            ],
            options={
                'db_table': 'comment',
            },
        ),
    ]
