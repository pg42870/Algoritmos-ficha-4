"""
Created on Fri Nov  6 16:49:28 2020

@author: Joana Gabriel, Maria Couto, Teresa Coimbra
"""


#raise Exception(...)

#filehandle é um ficheiro que ja esta aberto nao temos de fazer open e assim
#é ler uma linha e fazer alguma coisa com ela e ja esta

filename = input('Nome do ficheiro: ')
filenanme_F = input('Nome do ficheiro fasta: ')

FileHandle = open(filename,"r")
def ler_seq(FileHandle):
    """ Funcao que devolve a 
    Parameters
    ----------
    FileHandle : _io.TextIOWrapper
        Um ficheiro .txt aberto que contem uma sequencia de DNA por linha

    Returns
    -------
    
    seq : str
        sequencia de DNA que esta contida numa linha   

    """
    seq = FileHandle.readline()
    return seq

print(ler_seq(FileHandle))
FileHandle.close()

import re

FH = open(filename_F,"r")
def ler_FASTA_seq(file):
    """Funcao que devolve uma sequencia contida num ficheiro FASTA
    
    Parameters
    ----------
    FileHandle : _io.TextIOWrapper
        Um ficheiro FASTA
        
    Returns
    -------
    seq : str 
        Sequência contida num ficheiro FASTA sem o cabeçalho
    """
    
    linhas = FH.readlines()
    seq = ''
    
    a = ''.join(linhas)
    header = re.findall('>.+[\n]',a) # para obter o cabeçalho
    header=''.join(header)
    
    for l in linhas:
        if l != header:
            seq+=l.replace('\n','')
    return seq

print(ler_FASTA_seq(FH))
FH.close()

def complemento_inverso(seq):
    """ Funcao que devolve o complemento inverso de uma sequencia de DNA
    fornecida

    Parameters
    ----------
    seq : str
        sequência de DNA

    Returns
    -------
    seq2 : str    
        complemento inverso de uma sequência de DNA (seq)
    """
    
    seq2 = seq[::-1].lower().replace('a','T').replace('c','G').replace('g','C').replace('t','A')
    return seq2

def transcricao(seq):
    """

    Parameters
    ----------
    seq : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    pass

def traducao(seq):
    """

    Parameters
    ----------
    seq : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    pass

def valida(seq):
    """ Funcao que verifica se a sequencia de DNA e valida (devolve True or False)
    
    Parameters
    ----------
    seq : str
        Sequência de DNA que queremos saber se e valida
        
    Returns
    -------
    boolean(True/False)
    """
    
    seq = seq.upper()
    true_seq = seq.count('A')+seq.count('T')+seq.count('C')+seq.count('G')
    if len(seq)==true_seq:
        return True
    else:
        return False

def contar_bases(seq):
    """Funcao que recebe uma sequencia de DNA e faz a contagem das suas bases

    Parameters
    ----------
    seq : str
        Sequencia de DNA da qual queremos contar as bases

    Returns
    -------
    dici : dict
         Dicionario que contem como chave as bases azotadas da sequencia de DNA
         e para cada chave apresenta o valor da contagem dessa base
    """
    if valida(seq):
        seq= seq.upper()
        dici = {}
        dici['A'] = seq.count('A')
        dici['C'] = seq.count('C')
        dici['G'] = seq.count('G')
        dici['T'] = seq.count('T')
    return dici

def reading_frames(seq):
    """Funcao que devolve uma lista com as 3 reading frames da sequencia
    de DNA fornecida, bem como as 3 do seu complemento inverso

    Parameters
    ----------
    seq : str
        Sequencia de DNA da qual queremos saber as reading frames

    Returns
    -------
    frames : list of str
        As 3 reading frames da sequencia fornecida e as 3
        do seu complemento inverso
    """
    
    if valida(seq):
       frames = []
       for i in range(3):
           frames.append(seq[i::])
       for i in range(3):
           frames.append(complemento_inverso(seq[i::]))
    return frames


def get_proteins(seq):
    """Funcao que devolve a lista ordenada das proteinas resultantes da traducao 
    da sequencia de DNA fornecida
    
    Parameters
    ----------
    seq : str
        Sequencia de DNA da qual queremos saber as proteinas resultantes

    Returns
    -------
    proteins: list of str
        Proteinas resultantes da traducao da sequencia de DNA, ordenadas por 
        tamanho e dentro do mesmo tamanho por ordem alfabetica
    """
    
    if valida(seq):
        frames = reading_frames(seq)
        proteins = []
        for f in frames:
            p = traducao(f)
            p = re.findall('M.*?_',p)
            for i in p:
                proteins.append(i)
        proteins = set(proteins)
        proteins = list(proteins)
        proteins.sort()
        proteins = sorted(proteins, key=len, reverse = True)
    return proteins

import unittest

class Testes(unittest.TestCase):
    
    def testar_ler_seq(self):
        # testes 
        pass
    
    def testar_ler_FASTA(self):
        # testes2
        pass
    
    def testar_complemento(self):
        self.assertTrue(complemento_inverso('atg').isupper())
        self.assertEqual(complemento_inverso('CAgatgattt'), 'AAATCATCTG')
    
if __name__ == '__main__':
    unittest.main()

