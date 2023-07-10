# Generated by Django 4.1.3 on 2022-11-29 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AmazonProductData",
            fields=[
                ("also_bought", models.TextField(blank=True, null=True)),
                ("also_viewed", models.TextField(blank=True, null=True)),
                (
                    "asin",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("bought_together", models.TextField(blank=True, null=True)),
                ("brand", models.TextField(blank=True, null=True)),
                ("buy_after_viewing", models.TextField(blank=True, null=True)),
                ("categories", models.TextField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("imurl", models.TextField(blank=True, db_column="imUrl", null=True)),
                ("price", models.FloatField(blank=True, null=True)),
                ("title", models.TextField(blank=True, null=True)),
                ("sale_category", models.TextField(blank=True, null=True)),
                ("sale_rank", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "amazon_product_data",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AsinCategory",
            fields=[
                (
                    "asin",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("category1", models.TextField(blank=True, null=True)),
                ("category2", models.TextField(blank=True, null=True)),
                ("category3", models.TextField(blank=True, null=True)),
                ("category4", models.TextField(blank=True, null=True)),
                ("category5", models.TextField(blank=True, null=True)),
                ("category6", models.TextField(blank=True, null=True)),
                ("category7", models.TextField(blank=True, null=True)),
                ("category8", models.TextField(blank=True, null=True)),
                ("category9", models.TextField(blank=True, null=True)),
                ("category10", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "asin_category",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="CreditCard",
            fields=[
                (
                    "credit_card_id",
                    models.CharField(max_length=225, primary_key=True, serialize=False),
                ),
                ("firstname", models.CharField(max_length=255)),
                ("lastname", models.CharField(blank=True, max_length=255, null=True)),
                ("security_code", models.CharField(max_length=255)),
                ("money", models.IntegerField()),
            ],
            options={
                "db_table": "Credit_card",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Dealer",
            fields=[
                (
                    "first_name",
                    models.CharField(db_column="First_name", max_length=255),
                ),
                ("last_name", models.CharField(db_column="Last_name", max_length=255)),
                (
                    "email",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("username", models.CharField(max_length=255)),
                ("password", models.CharField(max_length=255)),
                ("brand", models.CharField(max_length=255)),
                ("id_number", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "Dealer",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                ("record_id", models.AutoField(primary_key=True, serialize=False)),
                ("quantity", models.IntegerField()),
                (
                    "paidorunpaid",
                    models.IntegerField(db_column="PaidOrUnpaid", default=False),
                ),
            ],
            options={
                "db_table": "Order",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Temp1",
            fields=[
                ("temp1_id", models.AutoField(primary_key=True, serialize=False)),
                ("category1", models.TextField(blank=True, null=True)),
                ("category1_count", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "temp1",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Temp2",
            fields=[
                ("temp2_id", models.AutoField(primary_key=True, serialize=False)),
                ("category1", models.TextField(blank=True, null=True)),
                ("category2", models.TextField(blank=True, null=True)),
                ("my_count", models.BigIntegerField()),
            ],
            options={
                "db_table": "temp2",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Temp3",
            fields=[
                ("temp3_id", models.AutoField(primary_key=True, serialize=False)),
                ("category1", models.TextField(blank=True, null=True)),
                ("category2", models.TextField(blank=True, null=True)),
                ("category3", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "temp3",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "first_name",
                    models.CharField(db_column="First_name", max_length=255),
                ),
                ("last_name", models.CharField(db_column="Last_name", max_length=255)),
                ("email", models.CharField(max_length=255)),
                (
                    "username",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("password", models.CharField(max_length=255)),
                (
                    "user_address",
                    models.CharField(db_column="User_address", max_length=255),
                ),
                (
                    "user_phone_number",
                    models.CharField(db_column="User_phone_number", max_length=255),
                ),
            ],
            options={
                "db_table": "User",
                "managed": True,
            },
        ),
    ]