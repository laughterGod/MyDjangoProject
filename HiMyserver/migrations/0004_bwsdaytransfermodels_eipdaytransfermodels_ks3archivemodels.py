# Generated by Django 2.2.4 on 2019-08-03 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HiMyserver', '0003_auto_20190802_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='BWSDayTransferModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'bws日流量计量查询',
                'verbose_name_plural': 'bws日流量计量查询',
            },
        ),
        migrations.CreateModel(
            name='EIPDayTransferModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'eip日流量计量查询',
                'verbose_name_plural': 'eip日流量计量查询',
            },
        ),
        migrations.CreateModel(
            name='KS3ArchiveModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'ks3归档存储量计量查询',
                'verbose_name_plural': 'ks3归档存储量计量查询',
            },
        ),
    ]