# Generated by Django 4.2.3 on 2024-05-14 13:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shrfntod', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=datetime.datetime(2024, 5, 14, 13, 34, 59, 455120, tzinfo=datetime.timezone.utc), null=True, verbose_name='تاريخ البوست')),
                ('title', models.CharField(max_length=500)),
                ('content', models.TextField(verbose_name='متحوى البوست')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('created_dt', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_dt', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ التعديل')),
                ('albumID', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shrfntod.album', verbose_name='الألبوم')),
                ('created_py', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_py', to=settings.AUTH_USER_MODEL, verbose_name='المُنشئ')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('updated_py', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_py', to=settings.AUTH_USER_MODEL, verbose_name='المُعدل')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
