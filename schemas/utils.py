from faker import Faker
import csv
from time import sleep

fake = Faker()


def generate_rows(amount, args):
    rows = []
    rows.append(list(args))  # append column names

    for i in range(0, amount):
        row = []
        for argument in args:
            fake_word = getattr(fake, argument)()
            row.append(fake_word)
        rows.append(row)
    print(rows)
    return rows


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.schema.user_id, filename)
