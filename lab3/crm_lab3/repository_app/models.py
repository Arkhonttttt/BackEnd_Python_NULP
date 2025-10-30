# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccuralType(models.Model):
    accural_type_id = models.AutoField(primary_key=True)
    accural_type_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'accural_type'

class Bonus(models.Model):
    bonus_type_id = models.AutoField(primary_key=True)
    bonus_type_name = models.CharField(max_length=100)
    bonus_percentage = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bonus'


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    number_of_workers = models.IntegerField()
    monthly_budget = models.IntegerField()
    department_chief = models.OneToOneField('Employee', models.DO_NOTHING, related_name='chief_of_department')

    class Meta:
        managed = False
        db_table = 'department'


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    gender = models.CharField(max_length=1)
    birth_date = models.DateField()
    phone_number = models.IntegerField(unique=True)
    email = models.CharField(max_length=45)
    bank_account = models.IntegerField()
    department = models.ForeignKey(Department, models.DO_NOTHING)
    position = models.ForeignKey('Position', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'employee'


class OtherAccurals(models.Model):
    employee = models.OneToOneField(Employee, models.DO_NOTHING, primary_key=True)
    bonus_type = models.ForeignKey(Bonus, models.DO_NOTHING, blank=True, null=True)
    total_sum = models.FloatField()
    accural_type = models.ForeignKey(AccuralType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'other_accurals'


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_date = models.DateTimeField()
    sum = models.FloatField()
    employee = models.OneToOneField(Employee, models.DO_NOTHING)
    accural_type = models.ForeignKey(AccuralType, models.DO_NOTHING)
    payment_type = models.ForeignKey('PaymentType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payment'


class PaymentType(models.Model):
    payment_type_id = models.AutoField(primary_key=True)
    payment_type_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'payment_type'


class Position(models.Model):
    position_id = models.AutoField(primary_key=True)
    base_monthly_wage = models.FloatField()
    position_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'position'


class Wage(models.Model):
    employee = models.OneToOneField(Employee, models.DO_NOTHING, primary_key=True)
    bonus_type = models.ForeignKey(Bonus, models.DO_NOTHING, blank=True, null=True)
    other_accurals = models.IntegerField()
    total_sum = models.FloatField()
    accural_type = models.ForeignKey(AccuralType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wage'
