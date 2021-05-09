from celery import shared_task
from schemas.models import Schema, SchemaColumn, Dataset
from schemas.utils import generate_rows
import csv
from io import StringIO
from django.core.files.base import ContentFile


@shared_task
def generate_dataset_task(dataset_id, row_amount):
    dataset_instance = Dataset.objects.get(id=dataset_id)
    schema_id = dataset_instance.schema_id
    print(schema_id)
    # # schema_instance = Schema.objects.get(id=schema_id)
    columns = SchemaColumn.objects.filter(
        schema_id=schema_id).values_list('type', flat=True)
    print(columns)

    # # generate rows
    row_list = generate_rows(int(row_amount), columns)

    csv_buffer = StringIO()
    csv_writer = csv.writer(csv_buffer)
    csv_writer.writerows(row_list)

    csv_file = ContentFile(csv_buffer.getvalue().encode('utf-8'))
    dataset_instance.file.save(f'dataset_{dataset_id}', csv_file)
