from decimal import Decimal
import calendar
import datetime

class CloudCost():

    def __init__(self):
        self.valor_execucao = 0.0000002
        self.valor_por_tempo_corrente = 0.0002080
        self.tempo_corrente_segundos = 3.0
        self.valor_execution_time = 0.00000040


    def lambda_execution(self):
        return  (self.valor_por_tempo_corrente * self.tempo_corrente_segundos) + self.valor_execucao


    def app_execution(self, execution_times):
        self.valida_execution_times(execution_times)
        return ((self.lambda_execution() * 2.0) + self.valor_execution_time) * execution_times
        
            
    def month(self, execution_times, month_of_year):
        self.valida_quantidade_meses(month_of_year)
        self.valida_execution_times(execution_times)
        data_atual = (datetime.datetime.now())
        quantidade_dias = calendar.monthrange(data_atual.year, int(month_of_year))[1]
        valor_app = self.app_execution(execution_times)
        valor_mes = (valor_app * quantidade_dias)
        return valor_mes


    def year(self, execution_times):
        self.valida_execution_times(execution_times)
        valor_anual = []
        mes = 1
        while mes <= 12:
            valor_anual.append(self.month(execution_times, mes))
            mes += 1
        return valor_anual


    def valida_execution_times(self, execution_times):
        if int(execution_times) < 0:
            raise ValueError("Valor de execução deve ser inteiro e maior que 0")
        else: 
            return True
    

    def valida_quantidade_meses(self, mes):
        mes = int(mes)
        if mes < 0 or mes > 12:
            raise ValueError("Valor do mês deve ser entre 1 e 12")
        else: 
            return True
