# Generated by Django 5.0.4 on 2024-05-23 10:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0005_alter_book_y_pub'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_email', models.EmailField(max_length=90)),
                ('amount', models.IntegerField()),
                ('stripe_payment_intent', models.CharField(max_length=200)),
                ('has_paid', models.BooleanField(default=False)),
                ('ordered_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommender.book')),
            ],
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
    ]
