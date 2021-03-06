# Generated by Django 3.2.9 on 2021-12-08 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.IntegerField(null=True)),
                ('img', models.ImageField(null=True, upload_to='PrimaryImages')),
                ('desc', models.TextField(null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='property.category')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_img', models.ImageField(upload_to='images/product_images')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='property.property')),
            ],
            options={
                'verbose_name_plural': 'Product Images',
            },
        ),
    ]
