# Generated by Django 2.1.5 on 2020-11-18 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Netfeelex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titre_film', models.CharField(max_length=200)),
                ('Contenu_film', models.TextField()),
                ('Date_publication', models.DateTimeField(verbose_name='Date publié')),
            ],
        ),
    ]
