# Generated by Django 2.2.11 on 2021-04-30 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookName', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('bookId', models.IntegerField()),
                ('price', models.IntegerField()),
                ('publicationDate', models.DateField()),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
