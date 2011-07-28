import unittest

class Test(unittest.TestCase):
    def test_formata_joao_silva(self):
        nome = FormataNome().formatador("Joao Silva")
        self.assertEqual("SILVA, Joao",nome)
    
    def test_formata_maria_joao(self):
        nome = FormataNome().formatador("Maria Joao")
        self.assertEqual("JOAO, Maria", nome)

    def test_parse_nome_to_list(self):
        list = FormataNome().parse_nome_to_list("Joao Silva")
        self.assertEqual(['Joao', 'Silva'], list)
    
    def test_parse_com_espaco_nome_to_list(self):
        list = FormataNome().parse_nome_to_list("Joao  Silva")
        self.assertEqual(['Joao', 'Silva'], list)
    
    def test_formata_maria_joao_silva(self):
        nome = FormataNome().formatador("Maria Joao Silva")
        self.assertEqual("SILVA, Maria Joao", nome)    
    

class FormataNome: 
    def parse_nome_to_list(self, nome_composto):        
        lista_nomes_simples = nome_composto.split(" ")
        return [ nome_simples for nome_simples in lista_nomes_simples if (nome_simples != "") ]
        

    def formatador(self, nome):
        nome_list = self.parse_nome_to_list(nome)
        nome_invertido = nome_list[::-1]
        nome_invertido[0] = nome_invertido[0].upper() + ','
        return " ".join(nome_invertido)
#        return nome_invertido[0].upper() + ', ' + nome_invertido[1]
