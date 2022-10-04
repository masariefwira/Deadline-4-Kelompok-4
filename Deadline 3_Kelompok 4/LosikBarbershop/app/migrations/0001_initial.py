# Generated by Django 4.0.2 on 2022-10-04 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='layanan',
            fields=[
                ('idlayanan', models.AutoField(primary_key=True, serialize=False)),
                ('jenislayanan', models.CharField(max_length=15)),
                ('hargalayanan', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='pelayan',
            fields=[
                ('idpelayan', models.AutoField(primary_key=True, serialize=False)),
                ('namapelayan', models.CharField(max_length=50)),
                ('notelp', models.IntegerField()),
                ('alamat', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='transaksi',
            fields=[
                ('idtransaksi', models.AutoField(primary_key=True, serialize=False)),
                ('namapelanggan', models.CharField(max_length=50)),
                ('tanggaltransaksi', models.DateField()),
                ('idpelayan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pelayan')),
            ],
        ),
        migrations.CreateModel(
            name='detaillayanan',
            fields=[
                ('iddetaillayanan', models.AutoField(primary_key=True, serialize=False)),
                ('idlayanan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.layanan')),
                ('idtransaksi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.transaksi')),
            ],
        ),
    ]
