# Generated by Django 3.1.6 on 2021-02-13 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='pub_date',
            new_name='publication_date',
        ),
    ]
