from django.core.management import BaseCommand

from persons.models import Person


class Command(BaseCommand):
    help = 'Full DB'

    people = [
        {'name': 'Marilyn',
         'last_name': 'Monroe',
         'phone_number': '+380970000000',
         'address': 'Allen Street 22'
         },
        {'name': 'Abraham',
         'last_name': 'Lincoln',
         'phone_number': '+380970000001',
         'address': 'Cabrini Boulevard 9'
         },
        {'name': 'Winston',
         'last_name': 'Churchill',
         'phone_number': '+380972000000',
         'address': 'Fulton Street 136'
         },
        {'name': 'Bill',
         'last_name': 'Gates',
         'phone_number': '+380973200000',
         'address': 'Horatio Street 11'
         },
        {'name': 'Muhammad',
         'last_name': 'Ali',
         'phone_number': '+380973200001',
         'address': 'Lenox Avenue 7'
         },
        {'name': 'Charles',
         'last_name': 'Darwin',
         'phone_number': '+380933200001',
         'address': 'Nassau Street 27'
         },
        {'name': 'Muhammad',
         'last_name': 'Ali',
         'phone_number': '+380933200001',
         'address': 'Horatio Street 71'
         },
        {'name': 'Elvis',
         'last_name': 'Presley',
         'phone_number': '+380933200001',
         'address': 'Greene Street 13'
         },
        {'name': 'Albert',
         'last_name': 'Einstein',
         'phone_number': '+380933200001',
         'address': 'Morton Street 30'
         },
        {'name': 'Pablo',
         'last_name': 'Picasso',
         'phone_number': '+380933200001',
         'address': 'Nassau Street 4'
         },

    ]

    def handle(self, *args, **options):

        objs = [
            Person(
                name=item['name'],
                last_name=item['last_name'],
                phone_number=item['phone_number'],
                address=item['address'],
            )
            for item in self.people
        ]

        Person.objects.bulk_create(objs)

        self.stdout.write("successfully")
