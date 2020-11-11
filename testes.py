# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 19:53:45 2020

@author: Joana Gabriel, Maria Couto, Teresa Coimbra
"""
import unittest

class Testes(unittest.TestCase):
    
    def testar_ler_seq(self):
        # testes 
        pass
    
    def testar_ler_FASTA(self):
        # testes2
        pass
    
    def testar_complemento(self):
        self.assertTrue(complemento_inverso(''), 'Sequência vazia')
        self.assertTrue(complemento_inverso('atg').isupper())
        self.assertEqual(complemento_inverso('CAgatgattt'), 'AAATCATCTG')
    
if __name__ == '__main__':
    unittest.main()
















