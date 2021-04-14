import csv
from datetime import datetime

from django.core.management import BaseCommand
from squirrel.models import Sighting
class Command(BaseCommand):
            
        def add_arguments(self,parser):
            parser.add_argument('path', type=str)

        def handle(self, *args, **kwargs):
            Sighting.objects.all().delete()
            path = kwargs['path']
            counter = 0
            with open(path, 'rt') as f:
                unique = set()
                reader = csv.reader(f, dialect='excel')
                next(reader,None)
                for column in reader:
                    counter += 1

                    if column[2] in unique:
                        continue
                    unique.add(column[2])
                    sights = Sighting.objects.create(
                            LONGITUDE=column[0],
                            LATITUDE=column[1],
                            SQUIRREL_ID=column[2],
                            SHIFT=column[4],
                            DATE=datetime.strptime(column[5], '%m%d%Y'),
                            AGE=column[7],
                            FUR_COLOR=column[8],
                            LOCATION=column[12],
                            SPECIFIC_LOCATION=column[14],
                            RUNNING=(column[15]=='true'),
                            CHASING=(column[16]=='true'),
                            CLIMBING=(column[17]=='true'),
                            EATING=(column[18]=='true'),
                            FORAGING=(column[19]=='true'),
                            OTHER_ACTIVITIES=column[20],
                            KUKS=(column[21]=='true'),
                            QUAAS=(column[22]=='true'),
                            MOANS=(column[23]=='true'),
                            TAIL_FLAGS=(column[24]=='true'),
                            TAIL_TWITCH=(column[25]=='true'),
                            APPROACHES=(column[26]=='true'),
                            RUNS_FROM=(column[28]=='true'))
                    sights.save()

