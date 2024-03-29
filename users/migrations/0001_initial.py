# Generated by Django 3.2.14 on 2022-10-21 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import webcampicture.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FlipcartImageVerify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_image', models.ImageField(upload_to='flipcart_images', verbose_name='Image slot')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AmazonImageVerify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_image', models.ImageField(upload_to='amazon_images', verbose_name='Image slot')),
                ('picture', webcampicture.fields.WebcamPictureField(blank=True, upload_to='amazon_images', verbose_name='Picture')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
