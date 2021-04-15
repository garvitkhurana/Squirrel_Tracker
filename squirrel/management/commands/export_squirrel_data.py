from django.core.management.base import BaseCommand
from squirrel.models import Sighting
import csv

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        d = {} 
        sights = Sighting.objects.all()
        with open(options['csv_file'], "w") as f:
            for s in sights:
                d['Longitude'] = s.LONGITUDE
                d['Latitude'] = s.LATITUDE
                d['Unique Squirrel ID'] = s.SQUIRREL_ID
                d['Shift'] = s.SHIFT
                d['Date'] = s.DATE
                d['Age'] = s.AGE
                d['Primary Fur Color'] = s.FUR_COLOR
                d['Location'] = s.LOCATION
                d['Specific Location'] = s.SPECIFIC_LOCATION
                d['Running'] = s.RUNNING
                d['Chasing'] = s.CHASING
                d['Climbing'] = s.CLIMBING
                d['Eating'] = s.EATING
                d['Foraging'] = s.FORAGING
                d['Other Activities'] = s.OTHER_ACTIVITIES
                d['Kuks'] = s.KUKS
                d['Quaas'] = s.QUAAS
                d['Moans'] = s.MOANS
                d['Tail Flags'] = s.TAIL_FLAGS
                d['Tail Twitches'] = s.TAIL_TWITCH
                d['Approaches'] = s.APPROACHES
                d['Runs from'] = s.RUNS_FROM
                writer = csv.DictWriter(f, delimiter = ",", fieldnames=d.keys())
                writer.writeheader()
                writer.writerow(d)
