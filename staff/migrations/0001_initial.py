# Generated by Django 3.1.4 on 2021-06-01 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AccountStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
                ('time', models.DateTimeField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullAddress', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BookDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('font', models.IntegerField()),
                ('paperSize', models.CharField(max_length=100)),
                ('colorFont', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BookStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartType', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ClothingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credits', models.IntegerField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fullname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saleOff', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.address')),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additionalFee', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('fullname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.fullname')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateShip', models.DateTimeField(max_length=100)),
                ('receiveDate', models.DateTimeField(max_length=100)),
                ('bill', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='staff.bill')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='staff.account')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.address')),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='staff.user')),
                ('company', models.CharField(max_length=100)),
            ],
            bases=('staff.user',),
        ),
        migrations.CreateModel(
            name='Cash',
            fields=[
                ('payment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='staff.payment')),
                ('amount', models.CharField(max_length=100)),
            ],
            bases=('staff.payment',),
        ),
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='staff.product')),
                ('material', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
            ],
            bases=('staff.product',),
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('payment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='staff.payment')),
                ('creditNumber', models.BigIntegerField()),
            ],
            bases=('staff.payment',),
        ),
        migrations.CreateModel(
            name='DomesticShip',
            fields=[
                ('shipment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='staff.shipment')),
                ('distance', models.BigIntegerField()),
                ('district', models.CharField(max_length=100)),
            ],
            bases=('staff.shipment',),
        ),
        migrations.CreateModel(
            name='Electronic',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='staff.product')),
                ('desc', models.CharField(max_length=100)),
            ],
            bases=('staff.product',),
        ),
        migrations.CreateModel(
            name='GlobalShip',
            fields=[
                ('shipment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='staff.shipment')),
                ('country', models.CharField(max_length=100)),
                ('typeDelivery', models.CharField(max_length=100)),
            ],
            bases=('staff.shipment',),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='staff.person')),
                ('workAddress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.address')),
            ],
            bases=('staff.person',),
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='staff.address')),
            ],
        ),
        migrations.CreateModel(
            name='ShipmentStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
                ('shipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.shipment')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.product')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.storage')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatusLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderStatus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.orderstatus')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saleOff', models.FloatField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.customer')),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='staff.payment')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('shipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.shipment')),
            ],
        ),
        migrations.CreateModel(
            name='ItemInCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.cart')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.order')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='productInStock',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='staff.productinstock'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.item')),
            ],
        ),
        migrations.CreateModel(
            name='BookGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookDescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.bookdescription')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.genre')),
            ],
        ),
        migrations.AddField(
            model_name='bookdescription',
            name='bookStatus',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='staff.bookstatus'),
        ),
        migrations.AddField(
            model_name='bill',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.order'),
        ),
        migrations.AddField(
            model_name='account',
            name='accountStatus',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='staff.accountstatus'),
        ),
        migrations.AddField(
            model_name='account',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.person'),
        ),
        migrations.CreateModel(
            name='Appliance',
            fields=[
                ('electronic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='staff.electronic')),
                ('width', models.CharField(max_length=100)),
                ('height', models.FloatField()),
                ('length', models.FloatField()),
                ('type', models.CharField(max_length=100)),
            ],
            bases=('staff.electronic',),
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('electronic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='staff.electronic')),
                ('dimension', models.FloatField()),
                ('type', models.CharField(max_length=100)),
            ],
            bases=('staff.electronic',),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='staff.product')),
                ('bookDescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.bookdescription')),
            ],
            bases=('staff.product',),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='staff.person')),
                ('organization', models.CharField(max_length=100)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.book')),
            ],
            bases=('staff.person',),
        ),
        migrations.CreateModel(
            name='StorageStaff',
            fields=[
                ('staff_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='staff.staff')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.storage')),
            ],
            bases=('staff.staff',),
        ),
    ]
