# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ap(models.Model):

    ap_idx = models.AutoField(db_column='AP_idx', primary_key=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='TIME', blank=True, null=True)  # Field name made lowercase.
    x_coord = models.CharField(db_column='X_coord', max_length=45)  # Field name made lowercase.
    y_coord = models.CharField(db_column='Y_coord', max_length=45)  # Field name made lowercase.
    z_coord = models.CharField(db_column='Z_coord', max_length=45)  # Field name made lowercase.
    azimuth = models.CharField(db_column='Azimuth', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ap'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False

        db_table = 'auth_group'



class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)



class AuthPermission(models.Model):
    name = models.CharField(max_length=255)

    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)

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
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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


class ProjectPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField()
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_post'


class Result(models.Model):
    result_idx = models.IntegerField(primary_key=True)
    rmse = models.CharField(db_column='RMSE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mae = models.CharField(db_column='MAE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "result"


# class User(models.Model):
#     name = models.CharField(max_length=45, blank=True, null=True)
#     id = models.CharField(primary_key=True, max_length=45)
#     password = models.CharField(max_length=45, blank=True, null=True)
#     e_mail = models.CharField(
#         db_column="e-mail", max_length=45, blank=True, null=True
#     )  # Field renamed to remove unsuitable characters.

#     class Meta:
#         managed = False
#         db_table = "user"


class UserExperiment(models.Model):
    user_id = models.CharField(
        db_column="User_ID", primary_key=True, max_length=45
    )  # Field name made lowercase.
    ap_idx = models.ForeignKey(
        Ap, models.DO_NOTHING, db_column="AP_idx", unique=True
    )  # Field name made lowercase.
    result_idx = models.ForeignKey(
        Result, models.DO_NOTHING, db_column="Result_idx"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "user_experiment"



    class Meta:
        managed = False
        db_table = 'user_experiment'
