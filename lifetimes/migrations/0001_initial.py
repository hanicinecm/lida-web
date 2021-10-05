# Generated by Django 3.2.7 on 2021-10-05 15:36

from django.db import migrations, models
import django.db.models.deletion
import utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formula_str', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=64)),
                ('html', models.CharField(max_length=64)),
                ('charge', models.SmallIntegerField()),
                ('natoms', models.SmallIntegerField()),
            ],
            bases=(utils.models.BaseMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Isotopologue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso_formula_str', models.CharField(max_length=32)),
                ('iso_slug', models.CharField(max_length=32)),
                ('inchi_key', models.CharField(max_length=32)),
                ('dataset_name', models.CharField(max_length=16)),
                ('version', models.PositiveIntegerField()),
                ('html', models.CharField(max_length=64)),
                ('mass', models.FloatField()),
                ('formula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lifetimes.formula')),
            ],
            bases=(utils.models.BaseMixin, models.Model),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_str', models.CharField(max_length=64)),
                ('energy', models.FloatField()),
                ('state_html', models.CharField(max_length=64)),
                ('isotopologue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lifetimes.isotopologue')),
            ],
            bases=(utils.models.BaseMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Transition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lifetime', models.FloatField()),
                ('branching_ratio', models.FloatField()),
                ('final_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='final_state', to='lifetimes.state')),
                ('initial_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='initial_state', to='lifetimes.state')),
            ],
            bases=(utils.models.BaseMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Lifetime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lifetime', models.FloatField()),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lifetimes.state')),
            ],
            bases=(utils.models.BaseMixin, models.Model),
        ),
    ]
