# Generated by Django 2.0.5 on 2018-06-03 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isActive', models.BooleanField(db_column='is_active', db_index=True, default=True)),
                ('createdDate', models.DateTimeField(auto_now_add=True, db_column='created_date', db_index=True)),
                ('lastModifiedDate', models.DateTimeField(auto_now=True, db_column='last_modified_date', db_index=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'todo_list',
            },
        ),
        migrations.CreateModel(
            name='TodoListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isActive', models.BooleanField(db_column='is_active', db_index=True, default=True)),
                ('createdDate', models.DateTimeField(auto_now_add=True, db_column='created_date', db_index=True)),
                ('lastModifiedDate', models.DateTimeField(auto_now=True, db_column='last_modified_date', db_index=True)),
                ('description', models.CharField(max_length=255)),
                ('todoList', models.ForeignKey(db_column='fk_id_todo_list', on_delete=django.db.models.deletion.CASCADE, to='api.TodoList')),
            ],
            options={
                'db_table': 'todo_list_item',
            },
        ),
    ]
