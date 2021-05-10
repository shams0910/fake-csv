from celery import shared_task
from schemas.models import Schema, SchemaColumn, Dataset
from schemas.utils import generate_rows, get_writer_params
import csv
from io import StringIO
from django.core.files.base import ContentFile


@shared_task
def generate_dataset_task(dataset_id, row_amount):
    dataset_instance = Dataset.objects.get(id=dataset_id)
    schema_id = dataset_instance.schema_id

    schema_instance = Schema.objects.get(id=schema_id)

    columns = SchemaColumn.objects.filter(
        schema_id=schema_id).values()

    # generate rows
    row_list = generate_rows(int(row_amount), columns)

    # writer options
    options = get_writer_params(schema_instance)

    csv_buffer = StringIO()
    csv_writer = csv.writer(csv_buffer, **options)
    csv_writer.writerows(row_list)

    csv_file = ContentFile(csv_buffer.getvalue().encode('utf-8'))
    dataset_instance.file.save(f'dataset_{dataset_id}.csv', csv_file)
