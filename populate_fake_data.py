import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

from django.utils import timezone

import django
django.setup()

from faker import Faker
import random
from first_app.models import Topic, WebPage, AccessRecord

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):

        # Create topic
        top = add_topic()

        # Create fake data
        fake_url = fakegen.url()
        fake_date = fakegen.date_time(tzinfo=timezone.utc)
        fake_name = fakegen.company()

        # Create webpage
        w = WebPage.objects.get_or_create(topic=top, web_name=fake_name, url_address=fake_url)[0]
        a = AccessRecord.objects.get_or_create(name=w, date_accessed=fake_date)[0]

if __name__ == '__main__':
    print("Populating data")
    populate(20)
    print("Done populating data!")

