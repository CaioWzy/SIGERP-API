from random import randint

from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from sigerpapi.api.models import Funcionario
from random import randint


class Command(BaseCommand):
    help = 'Popula a tabela de funcionários com dados aleatórios'

    def add_arguments(self, parser):
        parser.add_argument('quantidade', type=int)

    def handle(self, *args, **options):
        fake = Faker(['pt-BR'])

        for i in range(0, options['quantidade']):
            Faker.seed(i)
            Funcionario.objects.create(
                name=fake.name(),
                enrolment=randint(1000000, 9999999),
                cpf=fake.cpf().replace('-', '').replace('/', ''),
                date_of_birth=fake.date(),
                email=fake.email(),
                admission_date=fake.date(),
            ).save()
