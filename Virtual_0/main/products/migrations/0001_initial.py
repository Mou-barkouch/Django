# Generated by Django 4.0.4 on 2022-06-05 02:36

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
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('active', models.BooleanField(default=True)),
                ('category', models.CharField(blank=True, choices=[('banana', 'banana'), ('apple', 'Apple')], max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Phone',
                'ordering': ['-price'],
            },
        ),
    ]