# Generated by Django 2.2.7 on 2019-12-12 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tecrubeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yatkinlik', models.CharField(max_length=200)),
                ('kaynakekipman', models.CharField(max_length=200)),
                ('uzmanlik', models.CharField(max_length=200)),
            ],
        ),
    ]