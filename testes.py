# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 19:53:45 2020

@author: Joana Gabriel, Maria Couto, Teresa Coimbra
"""
import unittest

class Testes(unittest.TestCase):
    
    def testar_ler_seq(self):
        self.asssertEqual('BRCA.txt', 'ATTTAATTACAAGTCTTCAGAATGCCAGAGATATACAGGAT')
    
    def testar_ler_FASTA(self):
        self.assertEqual(ler_FASTA_seq('empty.fasta'), 'Ficheiro vazio')
        self.assertEqual(ler_FASTA_seq('Homo_sapiens_BRCA.fasta'),'ATTTAATTACAAGTCTTCAGAATGCCAGAGATATACAGGATATGCGAATTAAGAAGAAACAAAGGCAACGCGTCTTTCCACAGCCAGGCAGTCTGTATCTTGCAAAAACATCCACTCTGCCTCGAATCTCTCTGAAAGCAGCAGTAGGAGGCCAAGTTCCCTCTGCGTGTTCTCATAAACAG')
    
    def testar_complemento(self):
        self.assertTrue(complemento_inverso(''), 'Sequência vazia')
        self.assertTrue(complemento_inverso('atg').isupper())
        self.assertEqual(complemento_inverso('CAgatgattt'), 'AAATCATCTG')
    
    def testar_transcricão(self):
         self.assertTrue(transcricao(''), 'Sequência vazia')
         self.assertTrue(transcricao('atg').isupper().replace('T', 'U'))
         self.assertEqual(transcricao('CAgatgattt'), 'GUCUACUAAA')
         self.assertEqual(transcricao('ATG'), 'AUG')
    
    def testar_traducão(self):
         self.assertTrue(traducao(''), 'Sequência vazia')
         self.assertTrue(traducão('atg').isupper())
         self.assertEqual(tradução('ATG'), 'M')
         
            
    def testar_sequenciavalida(self):
        self.assertTrue(sequenciavalida(''), 'Sequência vazia')
        self.assertTrue(seq.count('A')+seq.count('T')+seq.count('C')+seq.count('G'))
        
        
        
    
if __name__ == '__main__':
    unittest.main()
















