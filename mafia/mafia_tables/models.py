# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class BusinessType(models.Model):
    type = models.CharField(max_length=45, blank=True, null=True)
    profit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'business_type'

    def __str__(self):
        return self.type


class District(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'district'

    def __str__(self):
        return self.name

class MissionTypes(models.Model):
    type = models.CharField(db_column='Type', max_length=45, blank=True, null=True)  # Field name made lowercase.
    region_of_responsibility = models.ForeignKey('RegionOfResponsibility', on_delete=models.CASCADE, db_column='Region_of_responsibility_id')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'mission_types'
        unique_together = (('id', 'region_of_responsibility'),)

    def __str__(self):
        return self.type


class Person(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    post_types = models.ForeignKey('PostTypes', on_delete=models.CASCADE, db_column='Post_types_id')  # Field name made lowercase.
    personToObey = models.ForeignKey('self', on_delete=models.CASCADE, db_column='Person_id', blank=True, null=True)  # Field name made lowercase.
    date_of_birth = models.DateField(db_column='Date of Birth', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    region_of_responsibility = models.ForeignKey('RegionOfResponsibility', on_delete=models.CASCADE, db_column='Region_of_responsibility_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'person'

    def __str__(self):
        return self.name


class PersonHasTasks(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, db_column='Person_id')  # Field name made lowercase.
    tasks = models.ForeignKey('Tasks', on_delete=models.CASCADE, db_column='Tasks_id')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'person_has_tasks'
        unique_together = (('person', 'tasks'),)

    def __str__(self):
        return 'Task for ' + self.person.name

class PostTypes(models.Model):
    post = models.CharField(db_column='Post', max_length=45, blank=True, null=True)  # Field name made lowercase.
    profit = models.IntegerField(db_column='Profit', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'post_types'

    def __str__(self):
        return self.post


class RegionOfResponsibility(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    business = models.ForeignKey(BusinessType, on_delete=models.CASCADE, db_column='Business_id')  # Field name made lowercase.
    district = models.ForeignKey(District, on_delete=models.CASCADE, db_column='District_id')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'region_of_responsibility'
        unique_together = (('id', 'business', 'district'),)

    def __str__(self):
        return self.name


class Tasks(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    profit = models.IntegerField(db_column='Profit', blank=True, null=True)  # Field name made lowercase.
    start_time = models.DateTimeField(db_column='Start_time', blank=True, null=True)  # Field name made lowercase.
    end_time = models.DateTimeField(db_column='End_time', blank=True, null=True)  # Field name made lowercase.
    real_end_time = models.DateTimeField(db_column='Real_end_time', blank=True, null=True)  # Field name made lowercase.
    mission_types = models.ForeignKey(MissionTypes, on_delete=models.CASCADE, db_column='Mission_types_id')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tasks'
        unique_together = (('id', 'mission_types'),)

    def __str__(self):
        return self.name
