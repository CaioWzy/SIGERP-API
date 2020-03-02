from random import randint

from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from sigerpapi.api.models import Cliente


class Command(BaseCommand):
    help = 'Popula a tabela de clientes com dados aleatórios'

    def add_arguments(self, parser):
        parser.add_argument('quantidade', type=int)

    def handle(self, *args, **options):
        fake = Faker(['pt-BR'])

        for i in range(0, options['quantidade']):
            Faker.seed(i)
            Cliente.objects.create(
                company_name=f"{fake.company()}",
                fantasy_name = fake.company(),
                cnpj = fake.cnpj().replace('-', '').replace('/', '')
            ).save()
