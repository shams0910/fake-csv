from django.db import models
from accounts.models import User
from .utils import user_directory_path

# Create your models here.


class Schema(models.Model):
    SEPARATOR_CHOICES = (
        ('comma', 'Comma (,)'),
        ('tab', 'Tab (\t)'),
        ('pipe', 'Pipe (|)')
    )

    STRING_CHARACTER_CHOICES = (
        (1, 'Single quote (\')'),
        (2, 'Double quote(")'),
        (3, 'No quotes')
    )

    name = models.CharField(max_length=50)
    column_separator = models.CharField(
        max_length=10, choices=SEPARATOR_CHOICES)
    string_character = models.PositiveIntegerField(
        choices=STRING_CHARACTER_CHOICES)
    modified_date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class SchemaColumn(models.Model):
    TYPE_CHOICES = (
        ('name', 'Full name'),
        ('job', 'Job'),
        ('email', 'Email'),
        ('address', 'Address'),
        ('phone_number', 'Phone number'),
        ('domain_name', 'Domain Name'),
        ('company', 'Company name'),
        ('text', 'Text')
    )
    name = models.CharField(max_length=30, verbose_name="Column name")
    type = models.CharField(choices=TYPE_CHOICES, max_length=20)
    range_to = models.IntegerField(null=True, verbose_name='To', blank=True)
    range_from = models.IntegerField(
        null=True, verbose_name='From', blank=True)
    order = models.IntegerField()
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, blank=True)


class Dataset(models.Model):
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to=user_directory_path)
