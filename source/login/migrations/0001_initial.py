# Generated by Django 4.0.dev20210331064157 on 2021-04-13 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.IntegerField(primary_key=True, serialize=False)),
                ('author_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookID', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=100)),
                ('isbn13', models.CharField(max_length=100)),
                ('average_rating', models.FloatField()),
                ('language_code', models.CharField(max_length=30)),
                ('num_pages', models.IntegerField()),
                ('ratings_count', models.IntegerField()),
                ('text_reviews_count', models.IntegerField()),
                ('publication_date', models.DateField(auto_now=True)),
                ('stocklevel', models.IntegerField()),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.author')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('passwd', models.CharField(max_length=100)),
                ('regdate', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('order_date', models.CharField(max_length=100)),
                ('order_status', models.CharField(max_length=100)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('permission_id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('publisher_id', models.IntegerField(primary_key=True, serialize=False)),
                ('publisher_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User_Category',
            fields=[
                ('category_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User_Permission',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('permission_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.permissions')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('passwd', models.CharField(max_length=130)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.user_category')),
            ],
        ),
        migrations.CreateModel(
            name='Usefulness_rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rater_customer_id', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('ratedate', models.DateTimeField(auto_now_add=True)),
                ('bookID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.book')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.customer')),
            ],
        ),
        migrations.CreateModel(
            name='TrustRecord',
            fields=[
                ('record_id', models.IntegerField(primary_key=True, serialize=False)),
                ('target_customer_id', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order_Details',
            fields=[
                ('detail_id', models.IntegerField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('purchase_price', models.FloatField()),
                ('discount', models.FloatField()),
                ('bookID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.book')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.order')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_timestamp', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField()),
                ('comment', models.CharField(max_length=250)),
                ('bookID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.book')),
                ('customer_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Book_movements',
            fields=[
                ('log_id', models.IntegerField(primary_key=True, serialize=False)),
                ('logdate', models.DateField(auto_now=True)),
                ('quantity', models.IntegerField()),
                ('bookID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.publisher'),
        ),
    ]
