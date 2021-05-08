from django import forms
from .models import Schema, SchemaColumn


class CreateSchemaForm(forms.ModelForm):
    class Meta:
        model = Schema
        fields = ['id', 'name', 'column_separator', 'string_character']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['style'] = 'display:block;width:500px'


class CreateSchemaColumnForm(forms.ModelForm):
    class Meta:
        model = SchemaColumn
        fields = '__all__'
