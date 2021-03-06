# Generated by Django 3.1.1 on 2020-09-24 15:50

import ckeditor_uploader.fields
from django.db import migrations, models
import jbatistaconstrucao.core.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('photo', models.FileField(upload_to='', validators=[jbatistaconstrucao.core.validators.validate_file_extension], verbose_name='photo')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='content')),
            ],
            options={
                'verbose_name': 'portfolio',
                'verbose_name_plural': 'portfolios',
            },
        ),
    ]
