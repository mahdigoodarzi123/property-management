# Generated by Django 5.0.6 on 2024-05-28 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, verbose_name='کد اموال')),
                ('group', models.CharField(max_length=100, verbose_name='گروه')),
                ('description', models.TextField(verbose_name='شرح')),
                ('location', models.CharField(choices=[('مروارید', 'مروارید'), ('دفتر مرکزی', 'دفتر مرکزی')], max_length=20, verbose_name='محل')),
                ('floor', models.CharField(choices=[('لابی', 'لابی'), ('طبقه یک', 'طبقه یک'), ('طبقه دو', 'طبقه دو'), ('طبقه سه', 'طبقه سه'), ('طبقه چهار', 'طبقه چهار'), ('طبقه پنج', 'طبقه پنج'), ('طبقه شش', 'طبقه شش')], max_length=20, verbose_name='طبقه')),
                ('status', models.CharField(max_length=100, verbose_name='وضعیت')),
                ('census_1403', models.CharField(blank=True, max_length=100, null=True, verbose_name='سرشماری 1403')),
                ('room', models.CharField(blank=True, max_length=100, null=True, verbose_name='اتاق')),
                ('user', models.CharField(max_length=100, verbose_name='استفاده کننده')),
                ('vendor', models.CharField(blank=True, max_length=100, null=True, verbose_name='فروشنده')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
            ],
        ),
    ]
