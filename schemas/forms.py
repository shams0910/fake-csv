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
        fields = ['name', 'type', 'range_to', 'range_from', 'order', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['style'] = 'width:200px'
        self.fields['range_from'].widget.attrs.update({'style': 'width:100px'})
        self.fields['range_to'].widget.attrs.update({'style': 'width:100px'})
        self.fields['order'].widget.attrs.update(
            {'style': 'width:100px'})
        self.fields['type'].widget.attrs.update(
            {'onchange': 'atTypeChange(this)', 'onafterprint': 'atTypeChange(this)'})
        # self.fields['type'].widget.attrs.update(
        #     {'onbeforeprint': 'atTypeChange(this)'})
