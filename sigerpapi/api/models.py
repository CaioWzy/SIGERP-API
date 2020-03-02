from django.db import models


class Cliente(models.Model):
    company_name = models.CharField(verbose_name="Razão Social", max_length=120)
    fantasy_name = models.CharField(verbose_name="Nome Fantasia", max_length=120)
    cnpj = models.CharField(verbose_name="CNPJ", max_length=14, unique=True)

    class Meta:
        db_table = "client"

    def __str__(self):
        return f"{self.fantasy_name} - CNPJ:  {self.cnpj}"


class Funcionario(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=255)
    enrolment = models.CharField(verbose_name="Matrícula", max_length=12)
    cpf = models.CharField(verbose_name="CPF", max_length=11, unique=True)
    date_of_birth = models.DateField(
        verbose_name="Data de Nascimento", null=True, blank=True
    )
    email = models.CharField(verbose_name="E-mail", max_length=120, unique=True)
    admission_date = models.DateField(
        verbose_name="Data de Admissão", null=True, blank=True
    )

    class Meta:
        db_table = "people"

    def __str__(self):
        return f"{self.name} - CNPJ:  {self.cpf}"


class ClienteFuncionario(models.Model):
    cliente = models.ForeignKey(
        Cliente, verbose_name="Cliente", on_delete=models.CASCADE, db_column="client_id"
    )
    funcionario = models.ForeignKey(
        Funcionario,
        verbose_name="Funcionário",
        on_delete=models.CASCADE,
        db_column="funcionario_id",
    )
    start_date = models.DateField(verbose_name="Início do Contrato")

    class Meta:
        db_table = "client_people"

    def __str__(self):
        return f"{self.cliente.fantasy_name} & {self.funcionario.name}"


class FuncionarioEscala(models.Model):
    funcionario = models.ForeignKey(
        Funcionario,
        verbose_name="Funcionário",
        on_delete=models.CASCADE,
        db_column="people_id",
    )
    weekday = models.PositiveIntegerField(verbose_name="Dia da Semana")
    marking_in = models.PositiveIntegerField(verbose_name="Entrada", null=True, blank=True)
    marking_out = models.PositiveIntegerField(verbose_name="Saída", null=True, blank=True)

    class Meta:
        db_table = "people_times"
        unique_together = ['funcionario', 'weekday']


    def __str__(self):
        return f"{self.funcionario.name} - Dia {self.weekday} das {self.marking_in} às {self.marking_out}"


class Ponto(models.Model):
    funcionario = models.ForeignKey(
        Funcionario,
        verbose_name="Funcionário",
        on_delete=models.CASCADE,
        db_column="people_id",
    )
    date = models.DateField(verbose_name="Dia")
    marking_in = models.PositiveIntegerField(
        verbose_name="Entrada", null=True, blank=True
    )
    marking_out = models.PositiveIntegerField(
        verbose_name="Saída", null=True, blank=True
    )
    justification = models.CharField(
        verbose_name="Justificativa", max_length=255, null=True, blank=True
    )

    class Meta:
        db_table = "time_register"
        unique_together = ['funcionario', 'date']

    def __str__(self):
        return f"{self.funcionario.name} - Dia {self.date}"
