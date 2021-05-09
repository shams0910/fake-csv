from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import CreateSchemaForm, CreateSchemaColumnForm
from .models import Schema, SchemaColumn, Dataset
from schemas.tasks import generate_dataset_task


# Create your views here.

class SchemaListView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def get(self, request):
        schemas = Schema.objects.all()
        return render(request, 'schemas/schema_list.html', {'schemas': schemas})


class SchemaCreateView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def post(self, request):
        schema_form = CreateSchemaForm(request.POST)
        if schema_form.is_valid():
            schema_id = request.POST.get('schema_id', False)
            # saving schema
            schema = schema_form.save(commit=False)
            schema.user = request.user
            schema.save()

            column_form = CreateSchemaColumnForm()

            context = {
                # 'schema_form': schema_form,
                'submitted': True,
                'schema_id': schema.id,
                'column_form': column_form
            }

            return render(request, 'schemas/schema_create.html', context)
        else:
            return redirect('schemas:schema-list')

    def get(self, request):
        context = {
            'schema_form': CreateSchemaForm(),
            'column_form': CreateSchemaColumnForm()
        }
        return render(request, 'schemas/schema_create.html', context)


class SchemaDatasetsView(View):
    def get(self, request, id):
        datasets = Dataset.objects.filter(schema_id=id)
        return render(request, 'schemas/datasets.html', {'datasets': datasets, 'schema_id': id})


class SchemaDeleteView(View):
    def get(self, request, id):
        schema = get_object_or_404(Schema, pk=id)
        schema.delete()
        return redirect('schemas:schema-list')


class GenerateDataSetView(View):
    def post(self, request):
        # get params
        schema_id = request.POST.get('schema_id')
        row_amount = request.POST.get('row_amount')

        # create dataset instance
        dataset = Dataset.objects.create(schema_id=schema_id)

        # queue the task
        generate_dataset_task.delay(dataset.id, row_amount)

        return redirect(f'/schemas/schema-datasets/{schema_id}/')
