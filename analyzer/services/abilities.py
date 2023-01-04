from django.db.utils import IntegrityError
from analyzer.models import Ability
from typing import List

def bulk_create_abilities(abilities, ignore_conflicts=True):
    ability_models = [
        Ability(
            ability_id=ability.id,
            name=ability.name,
            description=ability.description,
        ) for ability in abilities
    ]

    Ability.objects.bulk_create(ability_models, ignore_conflicts=ignore_conflicts)
