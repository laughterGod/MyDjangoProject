# Generated by Django 2.2.3 on 2019-08-06 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
        migrations.CreateModel(
            name='KS3Models',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'ks3日存储量计量查询',
                'verbose_name_plural': 'ks3日存储量计量查询',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HiMyserver.Question')),
            ],
        ),
    ]
