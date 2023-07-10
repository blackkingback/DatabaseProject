from django.db import models

# Create your models here.


class Dealer(models.Model):
    first_name = models.CharField(db_column='First_name', max_length=255)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_name', max_length=255)  # Field name made lowercase.
    email = models.CharField(primary_key=True, max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Dealer'
        unique_together = (('email', 'id_number'),)


class User(models.Model):
    first_name = models.CharField(db_column='First_name', max_length=255)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_name', max_length=255)  # Field name made lowercase.
    email = models.CharField(max_length=255)
    username = models.CharField(primary_key=True, max_length=255)
    password = models.CharField(max_length=255)
    user_address = models.CharField(db_column='User_address',max_length=255)
    user_phone_number = models.CharField(db_column='User_phone_number', max_length=255)

    class Meta:
        managed = True
        db_table = 'User'

class AmazonProductData(models.Model):
    also_bought = models.TextField(blank=True, null=True)
    also_viewed = models.TextField(blank=True, null=True)
    asin = models.CharField(primary_key=True, max_length=255)
    bought_together = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    buy_after_viewing = models.TextField(blank=True, null=True)
    categories = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    imurl = models.TextField(db_column='imUrl', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    sale_category = models.TextField(blank=True, null=True)
    sale_rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amazon_product_data'

class AsinCategory(models.Model):
    asin = models.CharField(primary_key=True, max_length=255)
    category1 = models.TextField(blank=True, null=True)
    category2 = models.TextField(blank=True, null=True)
    category3 = models.TextField(blank=True, null=True)
    category4 = models.TextField(blank=True, null=True)
    category5 = models.TextField(blank=True, null=True)
    category6 = models.TextField(blank=True, null=True)
    category7 = models.TextField(blank=True, null=True)
    category8 = models.TextField(blank=True, null=True)
    category9 = models.TextField(blank=True, null=True)
    category10 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asin_category'

class Order(models.Model):
    record_id = models.AutoField(primary_key=True)
    asin = models.ForeignKey('AmazonProductData', models.DO_NOTHING, db_column='asin')
    username = models.ForeignKey('User', models.DO_NOTHING, db_column='username')
    quantity = models.IntegerField()
    paidorunpaid = models.IntegerField(db_column='PaidOrUnpaid',default=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Order'

class CreditCard(models.Model):
    credit_card_id = models.CharField(primary_key=True, max_length=225)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    security_code = models.CharField(max_length=255)
    money = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Credit_card'
        unique_together = (('credit_card_id', 'security_code'),)

class Temp1(models.Model):
    temp1_id = models.AutoField(primary_key=True)
    category1 = models.TextField(blank=True, null=True)
    category1_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp1'


class Temp2(models.Model):
    temp2_id = models.AutoField(primary_key=True)
    category1 = models.TextField(blank=True, null=True)
    category2 = models.TextField(blank=True, null=True)
    my_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'temp2'


class Temp3(models.Model):
    temp3_id = models.AutoField(primary_key=True)
    category1 = models.TextField(blank=True, null=True)
    category2 = models.TextField(blank=True, null=True)
    category3 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp3'
