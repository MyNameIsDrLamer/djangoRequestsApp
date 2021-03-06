# Generated by Django 3.2.7 on 2021-11-25 06:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Condition_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Condition', models.CharField(db_index=True, max_length=15)),
            ],
            options={
                'verbose_name': 'Состояние',
                'verbose_name_plural': 'Состояние',
            },
        ),
        migrations.CreateModel(
            name='Full_name_of_the_performer_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name_of_the_performer', models.CharField(db_index=True, max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Исполнитель',
                'verbose_name_plural': 'Исполнитель',
            },
        ),
        migrations.CreateModel(
            name='Type_of_work_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type_of_work', models.CharField(db_index=True, max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Вид работ',
                'verbose_name_plural': 'Вид работ',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customers_full_name', models.CharField(max_length=50, verbose_name='Заказчик')),
                ('Lecture_hall', models.CharField(max_length=10, verbose_name='Аудитория')),
                ('Description', models.TextField(blank=True, max_length=150, verbose_name='Описание')),
                ('Comment', models.TextField(blank=True, max_length=150, verbose_name='Комментарий исполнителя')),
                ('Files', models.FileField(blank=True, upload_to='static/files/%Y/%m/%d/', verbose_name='Загрузка файла')),
                ('Request_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')),
                ('Condition', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='request.condition_list', verbose_name='Состояние')),
                ('Performer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='request.full_name_of_the_performer_list', verbose_name='Исполнитель')),
                ('Work', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='request.type_of_work_list', verbose_name='Тип работ')),
            ],
            options={
                'verbose_name': 'Заявки',
                'verbose_name_plural': 'Заявки',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalType_of_work_list',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('Type_of_work', models.CharField(db_index=True, max_length=50)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Вид работ',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalRequest',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('Customers_full_name', models.CharField(max_length=50, verbose_name='Заказчик')),
                ('Lecture_hall', models.CharField(max_length=10, verbose_name='Аудитория')),
                ('Description', models.TextField(blank=True, max_length=150, verbose_name='Описание')),
                ('Comment', models.TextField(blank=True, max_length=150, verbose_name='Комментарий исполнителя')),
                ('Files', models.TextField(blank=True, max_length=100, verbose_name='Загрузка файла')),
                ('Request_date', models.DateTimeField(blank=True, editable=False, verbose_name='Дата заявки')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('Condition', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='request.condition_list', verbose_name='Состояние')),
                ('Performer', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='request.full_name_of_the_performer_list', verbose_name='Исполнитель')),
                ('Work', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='request.type_of_work_list', verbose_name='Тип работ')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Заявки',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalFull_name_of_the_performer_list',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('Full_name_of_the_performer', models.CharField(db_index=True, max_length=50)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Исполнитель',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCondition_list',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('Condition', models.CharField(db_index=True, max_length=15)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Состояние',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
