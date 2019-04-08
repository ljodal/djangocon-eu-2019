# Generated by Django 2.2 on 2019-04-07 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyBudget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('target', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AddConstraint(
            model_name='monthlybudget',
            constraint=models.CheckConstraint(check=models.Q(month__in=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)), name='check_valid_month'),
        ),
        migrations.AlterUniqueTogether(
            name='monthlybudget',
            unique_together={('year', 'month')},
        ),
    ]