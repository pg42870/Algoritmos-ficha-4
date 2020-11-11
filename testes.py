# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 19:53:45 2020

@author: Joana Gabriel, Maria Couto, Teresa Coimbra
"""
import unittest
from modulo_funcoes import ler_seq, ler_FASTA_seq, complemento_inverso, transcricao, traducao, valida, contar_bases, reading_frames, get_proteins


class Testes(unittest.TestCase):
    
    def testar_ler_seq(self):
        FileHandle = open('BRCA.txt',"r") 
        self.assertEqual(ler_seq(FileHandle), 'ATTTAATTACAAGTCTTCAGAATGCCAGAGATATACAGGAT')
        FileHandle.close()
    
    
    def testar_ler_FASTA(self):
        FileHandle = open('Homo_sapiens_BRCA.fasta',"r")
        self.assertEqual(ler_FASTA_seq(FileHandle),'ATTTAATTACAAGTCTTCAGAATGCCAGAGATATACAGGATATGCGAATTAAGAAGAAACAAAGGCAACGCGTCTTTCCACAGCCAGGCAGTCTGTATCTTGCAAAAACATCCACTCTGCCTCGAATCTCTCTGAAAGCAGCAGTAGGAGGCCAAGTTCCCTCTGCGTGTTCTCATAAACAG')
        FileHandle.close()
        
    
    def testar_complemento(self):
        self.assertRaises(Exception, complemento_inverso, '')
        self.assertRaises(Exception, complemento_inverso, 'HSIDN')
        self.assertRaises(Exception, complemento_inverso, 'hyeod')
        self.assertRaises(Exception, complemento_inverso, 'ATGCTX')
        self.assertRaises(Exception, complemento_inverso, 'AUGCUA')
        self.assertRaises(Exception, complemento_inverso, '15485')
        self.assertTrue(complemento_inverso('atg').isupper())
        self.assertEqual(complemento_inverso('CAgatgattt'), 'AAATCATCTG')
    
    def testar_transcricao(self):
        self.assertRaises(Exception, transcricao, '')
        self.assertRaises(Exception, transcricao, 'HSIDN')
        self.assertRaises(Exception, transcricao, 'hyeod')
        self.assertRaises(Exception, transcricao, 'ATGCTX')
        self.assertRaises(Exception, transcricao, 'AUGCUA')
        self.assertRaises(Exception, transcricao, '15485')
        self.assertTrue(transcricao('atg'), 'AUG')
        self.assertEqual(transcricao('CAgatgattt'), 'CAGAUGAUUU')
        self.assertEqual(transcricao('ATG'), 'AUG')
        self.assertEqual(transcricao('ACCAGAGCGG'), 'ACCAGAGCGG')
        self.assertEqual(transcricao('ATTTAATTACAAGTCTTCAGAATGCCAGAGATATACAGGATCTAACCA'), 'AUUUAAUUACAAGUCUUCAGAAUGCCAGAGAUAUACAGGAUCUAACCA')
        self.assertEqual(transcricao('TTTTTTTT'), 'UUUUUUUU') 
    
                         
    def testar_traducao(self):
        self.assertRaises(Exception, traducao, '')
        self.assertRaises(Exception, traducao, 'HSIDN')
        self.assertRaises(Exception, traducao, 'hyeod')
        self.assertRaises(Exception, traducao, 'ATGCTX')
        self.assertRaises(Exception, traducao, 'AUGCUA')
        self.assertRaises(Exception, traducao, '15485')
        self.assertTrue(traducao('atg').isupper())
        self.assertEqual(traducao('ATG'), 'M')
        self.assertEqual(traducao('ATTTAATTACAAGTCTTCAGAATGCCAGAGATATACAGGATCTAACCA'), 'I_LQVFRMPEIYRI_P')
         
            
    def testar_sequenciavalida(self):
        self.assertFalse(valida(''))
        self.assertFalse(valida('HSIDN'))
        self.assertFalse(valida('hyeod'))
        self.assertFalse(valida('ATGCTX'))
        self.assertFalse(valida('AUGCUA'))
        self.assertFalse(valida('15485'))
        self.assertTrue(valida('ATGC'))
        self.assertTrue(valida('atgc'))
        self.assertTrue(valida('AtGc'))
        self.assertTrue(valida('AATGGCTAGT'))
        self.assertTrue(valida('ATTTAATTACAAGTCTTCAGAATGCCAGAGATATACAGGATCTAACCA'))
        
 
    def testar_contar_bases(self):
        self.assertRaises(Exception, contar_bases, '')
        self.assertRaises(Exception, contar_bases, 'HSIDN')
        self.assertRaises(Exception, contar_bases, 'hyeod')
        self.assertRaises(Exception, contar_bases, 'ATGCTX')
        self.assertRaises(Exception, contar_bases, 'AUGCUA')
        self.assertRaises(Exception, contar_bases, '15485')
        self.assertEqual(contar_bases('ATGC'), {'A':1, 'T':1, 'C':1, 'G':1})
        self.assertEqual(contar_bases('atgc'), {'A':1, 'T':1, 'C':1, 'G':1})
        self.assertEqual(contar_bases('AtGc'), {'A':1, 'T':1, 'C':1, 'G':1})
        self.assertEqual(contar_bases('AATGGCTAGT'), {'A':3, 'T':3, 'C':1, 'G':3})
        self.assertEqual(contar_bases('AATTTTAATA'), {'A':5, 'T':5, 'C':0, 'G':0})
    
    def testar_reading_frames(self):
        self.assertRaises(Exception, reading_frames, '')
        self.assertRaises(Exception, reading_frames, 'HSIDN')
        self.assertRaises(Exception, reading_frames, 'hyeod')
        self.assertRaises(Exception, reading_frames, 'ATGCTX')
        self.assertRaises(Exception, reading_frames, 'AUGCUA')
        self.assertRaises(Exception, contar_bases, '15485')
        self.assertEqual(reading_frames('ATTTAATTACAAGTCTTCAGAATGCCAGAGATATACAGGATCTAACCA'), ['I_LQVFRMPEIYRI_P', 'FNYKSSECQRYTGSN', 'LITSLQNARDIQDLT','WLDPVYLWHSEDL_LN','G_ILYISGILKTCN_', 'VRSCISLAF_RLVIK' ])
        self.assertEqual(reading_frames('ATGTTGGGCATGATCAAGAACTCGCTGTTCGGAAGCGTAGAGACGTGCCTTGGCAGGTCCTA'), ['MLGMIKNSLFGSVETCLGRS', 'CWA_SRTRCSEA_RRALAGP', 'VGHDQELAVRKRRDVPWQVL', '_DLPRHVSTLPNSEFLIMPN', '_DLPRHVSTLPNSEFLIMPN', '_DLPRHVSTLPNSEFLIMPN'])                                                                  
                                                                                                                                                                              
    def testar_get_proteins(self):
        self.assertRaises(Exception, get_proteins, '')
        self.assertRaises(Exception, get_proteins, 'HSIDN')
        self.assertRaises(Exception, get_proteins, 'hyeod')
        self.assertRaises(Exception, get_proteins, 'ATGCTX')
        self.assertRaises(Exception, get_proteins, 'AUGCUA')
        self.assertRaises(Exception, get_proteins, 'ATGGCTCGTACGGAA')
        self.assertRaises(Exception, contar_bases, '15485') 
        self.assertEqual(get_proteins('ATTTAATTACAAGTCTTCAGAATGCCAGAGATATACAGGATCTAACCA'), ['MPEIYRI_'])
        self.assertEqual(get_proteins('ATGTTGGGAGAAGTGACAGATAAGACAGTCGCTCTCTGCAGAAGAAATTAAAAGTCTGGTTCCGGATTCCAAACCAATTTCAAAGCGACCCACCAGCTCCCAGTGACAAAAGCGTTAAGATTGAGGAACGGGAAGGCATCACTGTCTATTCCATGCAGTTTGGTGGTTATGCCAAGGAAGCAGACTACGTAGCACAAGCCACCCGTCTGCGTGCTGCCCTGGAGGGCACAGCCACCTACCGGGGGGACATCTACTTCTGCACGGGTTATGACCCTCCCATGAAGCCCTACGGACGGCGCAATGAGATCTGGCTGTTGAAGACATGA', ['MQFGGYAKEADYVAQATRLRAALEGTATYRGDIYFCTGYDPPMKPYGRRNEIWLLKT_', 'MLGEVTDKTVALCRRN_', 'MPRKQTT_', 'MRSGC_', 'MTLP_']))
    

    
if __name__ == '__main__':
   unittest.main()
















