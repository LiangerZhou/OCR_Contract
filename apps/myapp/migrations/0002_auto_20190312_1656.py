# Generated by Django 2.1.7 on 2019-03-12 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('name', models.CharField(max_length=150, unique=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=150)),
                ('hash_number', models.CharField(max_length=150)),
                ('opinion', models.TextField()),
                ('money', models.FloatField()),
                ('type', models.CharField(max_length=150)),
                ('summary', models.CharField(max_length=150)),
                ('dept', models.CharField(max_length=150)),
                ('verify', models.BooleanField()),
                ('responsible_person', models.CharField(max_length=150)),
                ('supplier_id', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Contract_Location',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('contract_id', models.IntegerField()),
                ('location', models.FilePathField()),
                ('create_time', models.DateTimeField()),
                ('create_by', models.CharField(max_length=150)),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Contract_Oprea',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('contract_id', models.IntegerField()),
                ('scan_id', models.IntegerField()),
                ('opera_type', models.IntegerField()),
                ('opera_by', models.CharField(max_length=150)),
                ('opera_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('opera_info', models.CharField(max_length=150)),
                ('opera_type', models.CharField(max_length=150)),
                ('server_ip', models.CharField(max_length=150)),
                ('menu_name', models.CharField(max_length=150)),
                ('result', models.CharField(max_length=150)),
                ('session_id', models.CharField(max_length=150)),
                ('opera_by', models.CharField(max_length=150)),
                ('opera_time', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Login_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=150)),
                ('time', models.DateTimeField()),
                ('ip', models.CharField(max_length=150)),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField()),
                ('create_by', models.CharField(max_length=150)),
                ('update_time', models.DateTimeField()),
                ('update_by', models.CharField(max_length=150)),
                ('parent_id', models.IntegerField()),
                ('name', models.CharField(max_length=150)),
                ('icon', models.ImageField(upload_to='')),
                ('url', models.URLField()),
                ('server_url', models.URLField()),
                ('type', models.CharField(max_length=150)),
                ('tips', models.TextField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OneClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Scan_Info',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('contract_id', models.IntegerField()),
                ('name', models.CharField(max_length=150)),
                ('location', models.FilePathField()),
                ('status', models.IntegerField()),
                ('verify_result', models.IntegerField()),
                ('review_result', models.IntegerField()),
                ('review_by', models.CharField(max_length=150)),
                ('create_time', models.DateTimeField()),
                ('create_by', models.CharField(max_length=150)),
                ('update_time', models.DateTimeField()),
                ('update_by', models.CharField(max_length=150)),
                ('review_remark', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('learn', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('manager', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=100)),
                ('remark', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('teach', models.CharField(max_length=150)),
                ('student', models.ManyToManyField(through='myapp.OneClass', to='myapp.Student')),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='book_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AddField(
            model_name='oneclass',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Student'),
        ),
        migrations.AddField(
            model_name='oneclass',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Teacher'),
        ),
    ]
