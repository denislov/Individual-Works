# Generated by Django 2.1.4 on 2019-02-20 12:46

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('author', models.CharField(max_length=32)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='blogarticle',
            name='classify',
            field=models.ForeignKey(on_delete=True, to='Blog.Sort'),
        ),
    ]