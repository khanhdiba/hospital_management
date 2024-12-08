# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class AdmittedTo(models.Model):
    patientid = models.OneToOneField('Patient', models.CASCADE, db_column='patientID', primary_key=True)  # Field name made lowercase. The composite primary key (patientID, roomID) found, that is not supported. The first column is selected.
    roomid = models.ForeignKey('Room', models.CASCADE, db_column='roomID')  # Field name made lowercase.
    admitteddate = models.DateField(db_column='admittedDate', blank=True, null=True)  # Field name made lowercase.
    dischargeddate = models.DateField(db_column='dischargedDate', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.roomid)
    
    class Meta:
        managed = False
        db_table = 'admitted_to'
        unique_together = (('patientid', 'roomid'),)


class Appointment(models.Model):
    appointmentid = models.IntegerField(db_column='appointmentID', primary_key=True)  # Field name made lowercase.
    patientid = models.ForeignKey('Patient', models.CASCADE, db_column='patientID', blank=True, null=True)  # Field name made lowercase.
    doctorid = models.ForeignKey('Doctor', models.CASCADE, db_column='doctorID', blank=True, null=True)  # Field name made lowercase.
    appointmentdate = models.DateField(db_column='appointmentDate', blank=True, null=True)  # Field name made lowercase.
    appointmenttime = models.TimeField(db_column='appointmentTime', blank=True, null=True)  # Field name made lowercase.
    

    class Meta:
        managed = False
        db_table = 'appointment'


class Assists(models.Model):
    nurseid = models.OneToOneField('Nurse', models.CASCADE, db_column='nurseID', primary_key=True)  # Field name made lowercase. The composite primary key (nurseID, treatmentID) found, that is not supported. The first column is selected.
    treatmentid = models.ForeignKey('Treatment', models.CASCADE, db_column='treatmentID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'assists'
        unique_together = (('nurseid', 'treatmentid'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.CASCADE)
    permission = models.ForeignKey('AuthPermission', models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.CASCADE)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.CASCADE)
    group = models.ForeignKey(AuthGroup, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.CASCADE)
    permission = models.ForeignKey(AuthPermission, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bank(models.Model):
    bankid = models.CharField(db_column='bankID', primary_key=True, max_length=3)  # Field name made lowercase.
    bankname = models.CharField(db_column='bankName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paid = models.ForeignKey('PaymentApproach', models.CASCADE, db_column='PAID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bank'


class Bill(models.Model):
    billid = models.IntegerField(db_column='billID', primary_key=True)  # Field name made lowercase.
    patientid = models.ForeignKey('Patient', models.CASCADE, db_column='patientID')  # Field name made lowercase.
    amount = models.PositiveIntegerField(blank=True, null=True)
    createddate = models.DateField(db_column='createdDate', blank=True, null=True)  # Field name made lowercase.
    paymentstatus = models.IntegerField(db_column='paymentStatus', blank=True, null=True)  # Field name made lowercase.
    paid = models.ForeignKey('PaymentApproach', models.CASCADE, db_column='PAID', blank=True, null=True)  # Field name made lowercase.
    paiddate = models.DateField(db_column='paidDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bill'


class Cash(models.Model):
    cashierid = models.CharField(db_column='cashierID', primary_key=True, max_length=3)  # Field name made lowercase.
    cashiername = models.CharField(db_column='cashierName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paid = models.ForeignKey('PaymentApproach', models.CASCADE, db_column='PAID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cash'


class Department(models.Model):
    departmentid = models.CharField(db_column='departmentID', primary_key=True, max_length=2)  # Field name made lowercase.
    departmentname = models.CharField(db_column='departmentName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.departmentname)
    
    class Meta:
        managed = False
        db_table = 'department'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Doctor(models.Model):
    doctorid = models.OneToOneField('MedicalStaff', models.CASCADE, db_column='doctorID', primary_key=True)  # Field name made lowercase.
    license = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self):
        return str(self.doctorid)
    
    class Meta:
        managed = False
        db_table = 'doctor'


class Ewallet(models.Model):
    ewalletid = models.CharField(db_column='ewalletID', primary_key=True, max_length=3)  # Field name made lowercase.
    ewalletname = models.CharField(db_column='ewalletName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paid = models.ForeignKey('PaymentApproach', models.CASCADE, db_column='PAID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ewallet'


class Manages(models.Model):
    departmentid = models.OneToOneField(Department, models.CASCADE, db_column='departmentID', primary_key=True)  # Field name made lowercase.
    doctorid = models.OneToOneField(Doctor, models.CASCADE, db_column='doctorID')  # Field name made lowercase.
    startdate = models.DateField(db_column='startDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'manages'


class MedicalRecord(models.Model):
    recordid = models.IntegerField(db_column='recordID')  # Field name made lowercase.
    patientid = models.OneToOneField('Patient', models.CASCADE, db_column='patientID', primary_key=True)  # Field name made lowercase. The composite primary key (patientID, recordID) found, that is not supported. The first column is selected.
    recorddate = models.DateField(db_column='recordDate', blank=True, null=True)  # Field name made lowercase.
    treatmentid = models.ForeignKey('Treatment', models.CASCADE, db_column='treatmentID')  # Field name made lowercase.
    diagnosis = models.CharField(max_length=1000, blank=True, null=True)
    testresult = models.CharField(db_column='testResult', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medical_record'
        unique_together = (('patientid', 'recordid'),)


class MedicalStaff(models.Model):
    staffid = models.CharField(db_column='staffID', primary_key=True, max_length=7)  # Field name made lowercase.
    staffssn = models.CharField(db_column='staffSSN', unique=True, max_length=10)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=20)  # Field name made lowercase.
    midname = models.CharField(db_column='midName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    staffdob = models.DateField(db_column='staffDoB', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(max_length=1, blank=True, null=True)
    phonenumber = models.CharField(db_column='phoneNumber', max_length=10, blank=True, null=True)  # Field name made lowercase.
    salary = models.PositiveIntegerField(blank=True, null=True)
    departmentid = models.ForeignKey(Department, models.CASCADE, db_column='departmentID', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.staffid
    
    def fullname(self):
        return f'{self.firstname} {self.midname} {self.lastname}'
    
    # def __str__(self):
    #     return str(self.departmentid)
    
    class Meta:
        managed = False
        db_table = 'medical_staff'


class Medicine(models.Model):
    medicineid = models.CharField(db_column='medicineID', primary_key=True, max_length=11)  # Field name made lowercase.
    medicinename = models.CharField(db_column='medicineName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(max_length=1000, blank=True, null=True)
    pharmacyid = models.ForeignKey('Pharmacy', models.CASCADE, db_column='pharmacyID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medicine'


class Nurse(models.Model):
    nurseid = models.OneToOneField(MedicalStaff, models.CASCADE, db_column='nurseID', primary_key=True)  # Field name made lowercase.
    yearexperience = models.IntegerField(db_column='yearExperience', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.nurseid)
    class Meta:
        managed = False
        db_table = 'nurse'


class Patient(models.Model):
    patientid = models.CharField(db_column='patientID', primary_key=True, max_length=7)  # Field name made lowercase.
    patientssn = models.CharField(db_column='patientSSN', unique=True, max_length=10)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=20)  # Field name made lowercase.
    midname = models.CharField(db_column='midName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    patientdob = models.DateField(db_column='patientDoB', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(max_length=1, blank=True, null=True)
    phonenumber = models.CharField(db_column='phoneNumber', max_length=10, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.patientid)
    
    def get_name(self):
        return f'{self.firstname} {self.midname} {self.lastname}'
    
    def get_address(self):
        return f'{self.street} {self.district} {self.city}'
    class Meta:
        managed = False
        db_table = 'patient'


class PatientsFamily(models.Model):
    familyid = models.IntegerField(db_column='familyID')  # Field name made lowercase.
    patientid = models.OneToOneField(Patient, models.CASCADE, db_column='patientID', primary_key=True)  # Field name made lowercase. The composite primary key (patientID, familyID) found, that is not supported. The first column is selected.
    relationship = models.CharField(max_length=50, blank=True, null=True)
    phonenumber = models.CharField(db_column='phoneNumber', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patients_family'
        unique_together = (('patientid', 'familyid'),)


class PaymentApproach(models.Model):
    paid = models.CharField(db_column='PAID', primary_key=True, max_length=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payment_approach'


class Performs(models.Model):
    doctorid = models.OneToOneField(Doctor, models.CASCADE, db_column='doctorID', primary_key=True)  # Field name made lowercase. The composite primary key (doctorID, treatmentID) found, that is not supported. The first column is selected.
    treatmentid = models.ForeignKey('Treatment', models.CASCADE, db_column='treatmentID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'performs'
        unique_together = (('doctorid', 'treatmentid'),)


class Pharmacy(models.Model):
    pharmacyid = models.CharField(db_column='pharmacyID', primary_key=True, max_length=2)  # Field name made lowercase.
    pharmacyname = models.CharField(db_column='pharmacyName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pharmacy'


class Prescribes(models.Model):
    medicineid = models.ForeignKey(Medicine, models.CASCADE, db_column='medicineID')  # Field name made lowercase.
    patientid = models.OneToOneField(Patient, models.CASCADE, db_column='patientID', primary_key=True)  # Field name made lowercase. The composite primary key (patientID, medicineID, doctorID) found, that is not supported. The first column is selected.
    doctorid = models.ForeignKey(Doctor, models.CASCADE, db_column='doctorID')  # Field name made lowercase.
    prescribesdate = models.DateField(db_column='prescribesDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prescribes'
        unique_together = (('patientid', 'medicineid', 'doctorid'),)


class Room(models.Model):
    roomid = models.CharField(db_column='roomID', primary_key=True, max_length=3)  # Field name made lowercase.
    capacity = models.IntegerField(blank=True, null=True)
    roomtype = models.CharField(db_column='roomType', max_length=20, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.roomid)
    class Meta:
        managed = False
        db_table = 'room'


class Specialization(models.Model):
    doctorid = models.OneToOneField(Doctor, models.CASCADE, db_column='doctorID', primary_key=True)  # Field name made lowercase. The composite primary key (doctorID, aSpecialization) found, that is not supported. The first column is selected.
    aspecialization = models.CharField(db_column='aSpecialization', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'specialization'
        unique_together = (('doctorid', 'aspecialization'),)


class TakesCare(models.Model):
    nurseid = models.OneToOneField(Nurse, models.CASCADE, db_column='nurseID', primary_key=True)  # Field name made lowercase. The composite primary key (nurseID, roomID) found, that is not supported. The first column is selected.
    roomid = models.ForeignKey(Room, models.CASCADE, db_column='roomID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'takes_care'
        unique_together = (('nurseid', 'roomid'),)


class Treatment(models.Model):
    treatmentid = models.IntegerField(db_column='treatmentID', primary_key=True)  # Field name made lowercase.
    patientid = models.ForeignKey(Patient, models.CASCADE, db_column='patientID')  # Field name made lowercase.
    treatmentdate = models.DateField(db_column='treatmentDate', blank=True, null=True)  # Field name made lowercase.
    treatmentprocedure = models.CharField(db_column='treatmentProcedure', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    
    class Meta:
        managed = False
        db_table = 'treatment'


################################################################
###                         VIEW                             ###
################################################################

class PatientView(models.Model):
    patientID = models.IntegerField(primary_key=True)  # Assuming patientID is the primary key
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    contact = models.CharField(max_length=255)
    # Add other fields from the Patient table based on your schema

    class Meta:
        managed = False  # Don't let Django manage the view
        db_table = 'Patient_View'  # Name of the MySQL view


class PatientsFamilyView(models.Model):
    familyID = models.IntegerField(primary_key=True)  # Assuming familyID is the primary key
    patientID = models.IntegerField()
    family_member_name = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    # Add other fields from the Patients_Family table based on your schema

    class Meta:
        managed = False  # Don't let Django manage the view
        db_table = 'Patients_Family_View'  # Name of the MySQL view

class AppointmentView(models.Model):
    appointmentID = models.IntegerField(primary_key=True)  # Assuming appointmentID is the primary key
    patientID = models.IntegerField()
    appointment_date = models.DateTimeField()
    doctor_name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    # Add other fields from the Appointment table based on your schema

    class Meta:
        managed = False  # Don't let Django manage the view
        db_table = 'Appointment_View'  # Name of the MySQL view

class MedicalRecordView(models.Model):
    recordID = models.IntegerField(primary_key=True)  # Assuming recordID is the primary key
    patientID = models.IntegerField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    doctor_name = models.CharField(max_length=255)
    # Add other fields from the Medical_Record table based on your schema

    class Meta:
        managed = False  # Don't let Django manage the view
        db_table = 'Medical_Record_View'  # Name of the MySQL view

class PrescribesView(models.Model):
    prescriptionID = models.IntegerField(primary_key=True)  # Assuming prescriptionID is the primary key
    patientID = models.IntegerField()
    medication_name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)
    doctor_name = models.CharField(max_length=255)
    # Add other fields from the Prescribes table based on your schema

    class Meta:
        managed = False  # Don't let Django manage the view
        db_table = 'Prescribes_View'  # Name of the MySQL view

class BillView(models.Model):
    billID = models.IntegerField(primary_key=True)  # Assuming billID is the primary key
    patientID = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=255)
    bill_date = models.DateTimeField()
    # Add other fields from the Bill table based on your schema

    class Meta:
        managed = False  # Don't let Django manage the view
        db_table = 'Bill_View'  # Name of the MySQL view