# Generated by Django 2.1.5 on 2019-01-19 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkins', '0003_delete_slots'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_1', models.CharField(blank=True, choices=[('INFT', 'Information Tech.'), ('CMPN', 'Computer Science'), ('ETRX', 'Electronics'), ('EXTC', 'Electronics & Tele.'), ('BIOM', 'Biomedical'), ('MMS', 'Management Studies')], default=None, max_length=15)),
                ('slot_2', models.CharField(blank=True, choices=[('INFT', 'Information Tech.'), ('CMPN', 'Computer Science'), ('ETRX', 'Electronics'), ('EXTC', 'Electronics & Tele.'), ('BIOM', 'Biomedical'), ('MMS', 'Management Studies')], default=None, max_length=15)),
                ('slot_3', models.CharField(blank=True, choices=[('INFT', 'Information Tech.'), ('CMPN', 'Computer Science'), ('ETRX', 'Electronics'), ('EXTC', 'Electronics & Tele.'), ('BIOM', 'Biomedical'), ('MMS', 'Management Studies')], default=None, max_length=15)),
                ('slot_4', models.CharField(blank=True, choices=[('INFT', 'Information Tech.'), ('CMPN', 'Computer Science'), ('ETRX', 'Electronics'), ('EXTC', 'Electronics & Tele.'), ('BIOM', 'Biomedical'), ('MMS', 'Management Studies')], default=None, max_length=15)),
                ('slot_5', models.CharField(blank=True, choices=[('INFT', 'Information Tech.'), ('CMPN', 'Computer Science'), ('ETRX', 'Electronics'), ('EXTC', 'Electronics & Tele.'), ('BIOM', 'Biomedical'), ('MMS', 'Management Studies')], default=None, max_length=15)),
                ('slot_6', models.CharField(blank=True, choices=[('INFT', 'Information Tech.'), ('CMPN', 'Computer Science'), ('ETRX', 'Electronics'), ('EXTC', 'Electronics & Tele.'), ('BIOM', 'Biomedical'), ('MMS', 'Management Studies')], default=None, max_length=15)),
                ('slot_7', models.CharField(blank=True, choices=[('INFT', 'Information Tech.'), ('CMPN', 'Computer Science'), ('ETRX', 'Electronics'), ('EXTC', 'Electronics & Tele.'), ('BIOM', 'Biomedical'), ('MMS', 'Management Studies')], default=None, max_length=15)),
                ('slot_8', models.CharField(blank=True, choices=[('INFT', 'Information Tech.'), ('CMPN', 'Computer Science'), ('ETRX', 'Electronics'), ('EXTC', 'Electronics & Tele.'), ('BIOM', 'Biomedical'), ('MMS', 'Management Studies')], default=None, max_length=15)),
                ('slot_9', models.CharField(blank=True, choices=[('INFT', 'Information Tech.'), ('CMPN', 'Computer Science'), ('ETRX', 'Electronics'), ('EXTC', 'Electronics & Tele.'), ('BIOM', 'Biomedical'), ('MMS', 'Management Studies')], default=None, max_length=15)),
                ('total_seats_1', models.IntegerField(blank=True, default=0)),
                ('total_seats_2', models.IntegerField(blank=True, default=0)),
                ('total_seats_3', models.IntegerField(blank=True, default=0)),
                ('vacant_seats_1', models.IntegerField(blank=True, default=0)),
                ('vacant_seats_2', models.IntegerField(blank=True, default=0)),
                ('vacant_seats_3', models.IntegerField(blank=True, default=0)),
                ('reserved', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]