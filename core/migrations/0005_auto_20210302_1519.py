# Generated by Django 3.1.7 on 2021-03-02 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210302_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='album',
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='core.artist'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='artist',
            field=models.CharField(max_length=280),
        ),
    ]