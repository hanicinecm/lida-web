# Generated by Django 3.2.7 on 2021-10-06 12:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lifetimes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transition',
            name='lifetime',
        ),
        migrations.AddField(
            model_name='state',
            name='lifetime',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transition',
            name='d_energy',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transition',
            name='partial_lifetime',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='formula',
            name='natoms',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='isotopologue',
            name='formula',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lifetimes.formula'),
        ),
        migrations.AlterField(
            model_name='transition',
            name='branching_ratio',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)]),
        ),
        migrations.AlterField(
            model_name='transition',
            name='final_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transition_to', to='lifetimes.state'),
        ),
        migrations.AlterField(
            model_name='transition',
            name='initial_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transition_from', to='lifetimes.state'),
        ),
        migrations.DeleteModel(
            name='Lifetime',
        ),
    ]
