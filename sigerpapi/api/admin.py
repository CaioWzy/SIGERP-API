from django.contrib import admin

from sigerpapi.api.models import Cliente, Funcionario, ClienteFuncionario, FuncionarioEscala, Ponto

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'fantasy_name', 'cnpj')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'enrolment', 'cpf', 'date_of_birth', 'email', 'admission_date')

@admin.register(ClienteFuncionario)
class ClienteFuncionarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'funcionario', 'start_date')

@admin.register(FuncionarioEscala)
class FuncionarioEscalaAdmin(admin.ModelAdmin):
    list_display = ('id', 'funcionario', 'weekday', 'marking_in', 'marking_out')

@admin.register(Ponto)
class PontoAdmin(admin.ModelAdmin):
    list_display = ('id', 'funcionario', 'date', 'marking_in', 'marking_out', 'justification')