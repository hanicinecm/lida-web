# Generated by Django 3.2.8 on 2021-10-18 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('molecule', '0003_rename_resolving_html_isotopologue_resolving_vib_html'),
    ]

    operations = [
        migrations.AddField(
            model_name='isotopologue',
            name='resolving_el_html',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]
