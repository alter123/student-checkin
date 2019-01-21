
from django.db import models
from django.utils import timezone


branches = (
    ('INFT', 'Information Tech.'),
    ('CMPN', 'Computer Science'),
    ('ETRX', 'Electronics'),
    ('EXTC', 'Electronics & Tele.'),
    ('BIOM', 'Biomedical'),
    ('MMS', 'Management Studies'),
)


class Attendee( models.Model ):

    name = models.CharField( max_length=50, blank=False )
    roll_no = models.CharField( max_length=15, blank=True )
    branch = models.CharField( max_length=15, choices=branches )
    checkin = models.BooleanField( default=False )
    seat_no = models.CharField( max_length=15, blank=True, null=True )
    checkin_time = models.DateTimeField( blank=True, null=True )
    email = models.EmailField( max_length=50, null=True, blank=True )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Attendees'


class Document( models.Model ):

    name = models.CharField( max_length=15, blank=False )
    branch = models.CharField( max_length=15, choices=branches, blank=False )
    document = models.FileField( upload_to='' )
    uploaded_at = models.DateTimeField( default=timezone.now )

    def __str__(self):
        return self.title


class Slots( models.Model ):
    """ This Model stores slot setting and uses singleton model """

    slot_1 = models.CharField( max_length=15, choices=branches, blank=True, default=None, null=True )
    slot_2 = models.CharField( max_length=15, choices=branches, blank=True, default=None, null=True )
    slot_3 = models.CharField( max_length=15, choices=branches, blank=True, default=None, null=True )
    slot_4 = models.CharField( max_length=15, choices=branches, blank=True, default=None, null=True )
    slot_5 = models.CharField( max_length=15, choices=branches, blank=True, default=None, null=True )
    slot_6 = models.CharField( max_length=15, choices=branches, blank=True, default=None, null=True )
    slot_7 = models.CharField( max_length=15, choices=branches, blank=True, default=None, null=True )
    slot_8 = models.CharField( max_length=15, choices=branches, blank=True, default=None, null=True )
    slot_9 = models.CharField( max_length=15, choices=branches, blank=True, default=None, null=True )

    total_seats_1 = models.IntegerField( default=0, blank=True )
    total_seats_2 = models.IntegerField( default=0, blank=True )
    total_seats_3 = models.IntegerField( default=0, blank=True )

    filled_seats_1 = models.IntegerField( default=0, blank=True )
    filled_seats_2 = models.IntegerField( default=0, blank=True )
    filled_seats_3 = models.IntegerField( default=0, blank=True )

    update_choice = models.IntegerField( default=0, blank=False )

    reserved = models.IntegerField( default=0, blank=True )