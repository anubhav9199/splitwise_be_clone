# Generated by Django 4.2.7 on 2024-02-21 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('updated_at', models.DateTimeField(auto_created=True, auto_now=True)),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('split_type', models.IntegerField(choices=[(0, 'EQUAL'), (1, 'UNEQUAL'), (2, 'PERCENTAGE')], default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserOwePayment',
            fields=[
                ('updated_at', models.DateTimeField(auto_created=True, auto_now=True)),
                ('created_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('status', models.IntegerField(choices=[(0, 'PENDING'), (1, 'COMPLETE')], default=0)),
                ('payment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='splitwise.payment')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
