from faker import Faker
import csv
from time import sleep

fake = Faker()


def mean(*args):
    return sum(args)/len(args)


def generate_rows(amount, column_dicts):
    column_names = [column['name'] for column in column_dicts]
    rows = []
    rows.append(column_names)  # append column names

    for i in range(0, amount):
        row = []
        for column in column_dicts:
            if column['type'] == 'text':
                if column['range_to'] and column['range_from']:
                    mean = mean(column['range_to'], column['range_from'])
                    fake_text = fake.paragraph(nb_sentences=mean)
                    row.append(fake_text)
                else:
                    fake_text = fake.paragraph()
                    row.append(fake_text)
            else:
                fake_word = getattr(fake, column['type'])()
                row.append(fake_word)
        rows.append(row)
    return rows


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.schema.user_id, filename)


def get_writer_params(schema_instance):
    options = {}
    options['quoting'] = csv.QUOTE_NONNUMERIC

    separator = schema_instance.column_separator
    if separator == 'comma':
        options['delimiter'] = ','
    elif separator == 'tab':
        options['delimiter'] = '\t'
    elif separator == 'pipe':
        options['delimiter'] = '|'

    string_character = schema_instance.string_character
    if string_character == 1:
        options['quotechar'] = '\''
    elif string_character == 2:
        options['quotechar'] = '"'
    elif string_character == 3:
        options['quoting'] = csv.QUOTE_MINIMAL

    return options
