from django.db import models

# Create your models here.
from django.utils.translation import gettext as _

class Sighting(models.Model):
    LONGITUDE = models.FloatField(
            help_text=_('Longitude of the sight'),)

    LATITUDE = models.FloatField(
            help_text=_('Latitude of the sight'),)

    SQUIRREL_ID= models.CharField(
         max_length=100,
         help_text=_('Unique Sighting ID of the squirrel'),
         primary_key= True,a
         default='123ABC',
         unique=True
         )

    AM='AM'
    PM='PM'
    shift = ((AM,'AM'),(PM,'PM'))
    SHIFT = models.CharField(
            max_length = 100,
            choices = shift,
            help_text = _('Whether sighting happens in the morning or late afternoon'),
            blank = True
            )
    DATE = models.DateField(
            help_text = _('Date of the sighting')
            )
    ADULT='Adult'
    JUVENILE = 'Juvenile'
    age_choice = ((ADULT,'Adult'), (JUVENILE,'Juvenile'))

    AGE = models.CharField(
            max_length=50,
            choices = age_choice,
            help_text=_('Age Category of the Squirrel'),
            blank = True,
            )
    GREY= 'Grey'
    CINNAMON= 'Cinnamon'
    BLACK = 'Black'
    color_choice = ((GREY,'Grey'),(CINNAMON, 'Cinnamon'),(BLACK,'Black'))
    FUR_COLOR = models.CharField(
            max_length=50,
            blank=True,
            choices= color_choice,
            help_text=_('Fur Color of the Squirrel'),
            )

    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'
    location_choice = ((GROUND_PLANE,'Ground Plane'), (ABOVE_GROUND, 'Above Ground'))
    LOCATION = models.CharField(
            help_text=_('Location where squirrel is found'),
            max_length=200,
            choices = location_choice,
            blank = True,
            )
    SPECIFIC_LOCATION = models.CharField(
            help_text=_('Any additional notes regarding location'),
            max_length=200,
            blank=True,
         )
    RUNNING = models.BooleanField(
            help_text=_('Running'),
            default = False,
            )
    CHASING = models.BooleanField(
            help_text=_('Chasing'),
            default = False,
            )
    CLIMBING= models.BooleanField(
            help_text=_('Climbing'),
            default = False,
            )
    EATING= models.BooleanField(
            help_text=_('Eating'),
            default = False,
            )
    FORAGING= models.BooleanField(
            help_text=_('Foraging'),
            default = False,
            )
    OTHER_ACTIVITIES= models.CharField(
            help_text=_('Other Activities Noted'),
            max_length=300,
            blank=True,
           )
    KUKS= models.BooleanField(
            help_text=_('Kuks'),
            default = False,
            )
    QUAAS= models.BooleanField(
            help_text=_('Quaas'),
            default = False,
            )
    MOANS= models.BooleanField(
            help_text=_('Moans'),
            default = False,
            )
    TAIL_FLAGS = models.BooleanField(
            help_text=_('Tail Flags'),
            default = False,
            )
    TAIL_TWITCH= models.BooleanField(
            help_text=_('Tail Twitches'),
            default = False,
            )
    APPROACHES = models.BooleanField(
            help_text=_('Approaches humans'),
            default = False,
            )
    RUNS_FROM= models.BooleanField(
            help_text=_('Runs away from humans'),
            default = False,
            )
