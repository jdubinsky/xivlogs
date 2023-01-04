from django.core.management.base import BaseCommand

from analyzer.queries.abilities import find_abilities
from analyzer.services.abilities import bulk_create_abilities

class Command(BaseCommand):
    help = 'Fetches game abilities and saves them in the database.'

    def handle(self, *args, **kwargs):
        for ability_batch in find_abilities():
            bulk_create_abilities(ability_batch)
