# Generated by Django 3.0.5 on 2020-04-19 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_remove_patient_patient_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoronaTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corona_test_id', models.IntegerField(default=0)),
                ('test_taken_date', models.DateTimeField(verbose_name='date test taken')),
                ('test_result', models.CharField(choices=[('Positive', 'Positive'), ('Negative', 'Negative'), ('NA', 'NA')], default='NA', max_length=8)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='CallPatient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call_time', models.DateTimeField(verbose_name='date and time called patient')),
                ('call_status', models.CharField(choices=[('Positive', 'Positive'), ('Negative', 'Negative')], default='Negative', max_length=8)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Patient')),
            ],
        ),
    ]