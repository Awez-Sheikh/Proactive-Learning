# Generated by Django 5.1.3 on 2024-11-26 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.PositiveSmallIntegerField(default=0)),
                ('age', models.PositiveSmallIntegerField(default=0)),
                ('address', models.PositiveSmallIntegerField(default=0)),
                ('famsize', models.PositiveSmallIntegerField(default=0)),
                ('Pstatus', models.PositiveSmallIntegerField(default=0)),
                ('Medu', models.PositiveSmallIntegerField(default=0)),
                ('Fedu', models.PositiveSmallIntegerField(default=0)),
                ('Mjob', models.PositiveSmallIntegerField(default=0)),
                ('Fjob', models.PositiveSmallIntegerField(default=0)),
                ('reason', models.PositiveSmallIntegerField(default=0)),
                ('guardian', models.PositiveSmallIntegerField(default=0)),
                ('traveltime', models.PositiveSmallIntegerField(default=0)),
                ('studytime', models.PositiveSmallIntegerField(default=0)),
                ('failures', models.PositiveSmallIntegerField(default=0)),
                ('schoolsup', models.PositiveSmallIntegerField(default=0)),
                ('famsup', models.PositiveSmallIntegerField(default=0)),
                ('paid', models.PositiveSmallIntegerField(default=0)),
                ('activities', models.PositiveSmallIntegerField(default=0)),
                ('nursery', models.PositiveSmallIntegerField(default=0)),
                ('higher', models.PositiveSmallIntegerField(default=0)),
                ('internet', models.PositiveSmallIntegerField(default=0)),
                ('romantic', models.PositiveSmallIntegerField(default=0)),
                ('famrel', models.PositiveSmallIntegerField(default=0)),
                ('freetime', models.PositiveSmallIntegerField(default=0)),
                ('goout', models.PositiveSmallIntegerField(default=0)),
                ('Dalc', models.PositiveSmallIntegerField(default=0)),
                ('Walc', models.PositiveSmallIntegerField(default=0)),
                ('health', models.PositiveSmallIntegerField(default=0)),
                ('absences', models.PositiveSmallIntegerField(default=0)),
                ('G1', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('G2', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('G3', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('G4', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('G5', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('G6', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('G7', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('Grade_8_Marks', models.PositiveSmallIntegerField(default=0)),
                ('Grade_9_Marks', models.PositiveSmallIntegerField(default=0)),
                ('Grade_10_Marks', models.PositiveSmallIntegerField(default=0)),
                ('Grade_11_Marks', models.PositiveSmallIntegerField(default=0)),
                ('Grade_12_Marks', models.PositiveSmallIntegerField(default=0)),
                ('name', models.CharField(default='Yash', max_length=50)),
                ('semester', models.PositiveSmallIntegerField(default=0)),
                ('course', models.PositiveSmallIntegerField(default=0)),
                ('student_categories', models.CharField(blank=True, default='weak', max_length=50, null=True)),
                ('cluster_group', models.PositiveSmallIntegerField(blank=True, default=3, null=True)),
            ],
        ),
    ]
