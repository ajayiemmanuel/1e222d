# Generated by Django 5.0.2 on 2024-04-22 20:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0029_alter_transfer_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='transfer',
            old_name='date',
            new_name='purpose',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='pin',
        ),
        migrations.AddField(
            model_name='transfer',
            name='transferdate',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.CharField(max_length=200, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
