from django.db import models
from accounts.models import User


# Create your models here.

class Schema(models.Model):
    SEPARATOR_CHOICES = (
        ('comma', 'Comma (,)'),
        ('semicolon', 'Semicolon (;)'),
        ('tab', 'Tab (\\t)'),
        ('space', 'Space ( )'),
        ('pipe', 'Pipe (|)')
    )

    STRING_CHARACTER_CHOICES = (
        (1, 'Single quote (\')'),
        (2, 'Double quote(")')
    )

    name = models.CharField(max_length=50)
    column_separator = models.CharField(
        max_length=10, choices=SEPARATOR_CHOICES)
    string_character = models.PositiveIntegerField(
        choices=STRING_CHARACTER_CHOICES)
    modified_date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_modified(self):
        return self.modified_date


class SchemaColumn(models.Model):
    TYPE_CHOICES = (
        ('name', 'Full name'),
        ('job', 'Job'),
        ('email', 'Email'),
        ('domain', 'Domain name'),
        ('phone', 'Phone number'),
        ('company', 'Company name'),
        ('text', 'Text')
    )
    name = models.CharField(max_length=30, verbose_name="Column name")
    type = models.CharField(choices=TYPE_CHOICES, max_length=20)
    range_to = models.IntegerField(null=True, verbose_name='To')
    range_from = models.IntegerField(null=True, verbose_name='From')
    order = models.IntegerField()
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, blank=True)


class Dataset(models.Model):
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    file = models.FileField()
