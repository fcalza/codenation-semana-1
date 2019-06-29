from decimal import Decimal
import calendar
import datetime


class CloudCost():
    def __init__(self, valorMensagem='0.00000040', valorExecucaoFuncoes='0.0000002',
                 valorTempoCorrente='0.0002080'):
        self.valorMensagem = Decimal(valorMensagem)
        self.valorExecucaoFuncoes = Decimal(valorExecucaoFuncoes)
        self.valorTempoCorrente = Decimal(valorTempoCorrente)


    def lambda_execution(self):
        quantidade = 50
        valores = {}
        valores['valorExecucaoDiaria'] = self.app_execution(quantidade)
        valores['valorExecucaoMensal'] = self.month(quantidade, 5)
        valores['valorExecucaoAnual'] = self.year(quantidade)
        # Não entendi o retorno desse cara. O teste só pede que seja um valor maior que zero...
        # A meu entender essa função está funcionando como uma controler para as demais funções
        return valores['valorExecucaoDiaria']


    def app_execution(self, execution_times):
        self.valida_execution_times(execution_times)
        valor = execution_times * self.valorMensagem
        valor += (execution_times * 2) * self.valorExecucaoFuncoes
        valor += (execution_times  * 3) * self.valorTempoCorrente
        return valor
        
            
    def month(self, execution_times, month_of_year):
        self.valida_quantidade_meses(month_of_year)
        valorDiario = self.app_execution(execution_times)
        dataAtual = (datetime.datetime.now())
        quantidadeDias = calendar.monthrange(dataAtual.year, month_of_year)[1]
        return valorDiario * quantidadeDias


    def year(self, execution_times):
        valorAnual = {}
        mes = 1
        while mes <= 12:
            valorAnual[mes] = self.month(execution_times, mes)
            mes += 1
        return valorAnual


    def valida_execution_times(self, execution_times):
        if execution_times < 0 and type(execution_times) == int:
            raise TypeError("Valor de execução deve ser inteiro e maior que 0")
        else: 
            return True
    

    def valida_quantidade_meses(self, mes):
        if mes < 0 or mes > 12:
            raise ValueError("Valor do mês deve ser entre 1 e 12")
        else: 
            return True




# /home/lipe/codenation/cloud-cost-python/test_submit.py:13: AssertionError: 4e-07 != 0.0012488
# /home/lipe/codenation/cloud-cost-python/test_submit.py:9: AssertionError: 4e-07 != 0.0006242
# /home/lipe/codenation/cloud-cost-python/test_submit.py:22: AssertionError: 1.24e-05 != 0.0387128
# /home/lipe/codenation/cloud-cost-python/test_submit.py:35: AssertionError: Lists differ: [1.24e-05, 1.12e-05, 1.24e-05, 1.2e-05, 1.[69 chars]e-05] != [0.0387128, 0.0349664, 0.0387128, 0.037464[81 chars]7128]