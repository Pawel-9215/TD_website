import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'ProToo.settings')
import django
django.setup()

import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_name = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_email = fakegen.email()

        user = User.objects.get_or_create(first_name = fake_name, last_name = fake_lname, email = fake_email)[0]


if __name__ == '__main__':
    print("Populating cript!")
    populate(20)
    print('Populating complete')