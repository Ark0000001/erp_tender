# Generated by Django 4.1.1 on 2022-09-18 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0003_alter_city_options_city_region'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='type_tender',
            options={'ordering': ['nomer'], 'verbose_name': 'Тип конкурса', 'verbose_name_plural': 'Тип конкурсов'},
        ),
        migrations.AddField(
            model_name='type_tender',
            name='nomer',
            field=models.IntegerField(max_length=10, null=True, verbose_name='Порядковый номер'),
        ),
    ]