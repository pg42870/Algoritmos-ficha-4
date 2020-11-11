"""
Created on Fri Nov  6 16:49:28 2020

@author: Joana Gabriel, Maria Couto, Teresa Coimbra
"""


#raise Exception(...)

#filehandle é um ficheiro que ja esta aberto nao temos de fazer open e assim
#é ler uma linha e fazer alguma coisa com ela e ja esta

filename = input('Nome do ficheiro: ')
filename_F = input('Nome do ficheiro fasta: ')

FileHandle = open(filename,"r")
def ler_seq(FileHandle):
    """ Funcao que devolve a 
    Parameters
    ----------
    FileHandle : _io.TextIOWrapper
        Um ficheiro .txt aberto que contém uma sequência de DNA por linha

    Returns
    -------
    
    seq : str
        Sequência de DNA que está contida numa linha   

    """
    seq = FileHandle.readline()
    return seq

print(ler_seq(FileHandle))
FileHandle.close()

import re

FH = open(filename_F,"r")
def ler_FASTA_seq(file):
    """Função que devolve uma sequência contida num ficheiro FASTA
    
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
    """ Função que devolve o complemento inverso de uma sequência de DNA
    fornecida

    Parameters
    ----------
    seq : str
        Sequência de DNA

    Returns
    -------
    seq2 : str    
        Complemento inverso de uma sequência de DNA (seq)
    """
    assert len(seq)!= 0,  'Sequência vazia'
    assert valida(seq), "Sequencia de DNA invalida"
    seq2 = seq[::-1].lower().replace('a','T').replace('c','G').replace('g','C').replace('t','A')
    return seq2

def transcricao(seq):
    """

    Parameters
    ----------
    seq : str
        Sequência de DNA

    Returns
    -------
         Transcrição de uma sequência de DNA em RNA

    """
    assert valida(seq), "Sequencia de DNA invalida"
    seq = seq.replace("T","U")
    return seq

def traducao(seq):
    """

    Parameters
    ----------
    seq : str
        Sequência de DNA

    Returns
    -------
        Tradução de uma sequência de DNA

    """
    seq = seq.upper()
    codoes = re.findall('...',seq)
    aas = ''
    gencode = {'ATA':'I', 'ATC':'I', 'ATT':'I', 
    'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 
    'ACT':'T','AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
    for i in codoes:
        aas += gencode[i]
    return(aas)

def valida(seq):
    """ Função que verifica se a sequência de DNA é válida (devolve True or False)
    
    Parameters
    ----------
    seq : str
        Sequência de DNA que queremos saber se é vélida
        
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
    """Função que recebe uma sequência de DNA e faz a contagem das suas bases

    Parameters
    ----------
    seq : str
        Sequência de DNA da qual queremos contar as bases

    Returns
    -------
    dici : dict
         Dicionario que conta como chave as bases azotadas da sequência de DNA
         e para cada chave apresenta o valor da contagem dessa base
    """
    
    assert valida(seq), "Sequencia de DNA invalida"
    seq= seq.upper()
    dici = {}
    dici['A'] = seq.count('A')
    dici['C'] = seq.count('C')
    dici['G'] = seq.count('G')
    dici['T'] = seq.count('T')
    return dici

def reading_frames(seq):
    """Função que devolve uma lista com as 3 reading frames da sequência
    de DNA fornecida, bem como as 3 do seu complemento inverso

    Parameters
    ----------
    seq : str
        Sequência de DNA da qual queremos saber as reading frames

    Returns
    -------
    frames : list of str
        As 3 reading frames da sequencia fornecida e as 3
        do seu complemento inverso
    """
    
    assert valida(seq), "Sequencia de DNA invalida"
    frames = []
    for i in range(3):
        frames.append(traducao(seq[i::]))
    for i in range(3):
        frames.append(traducao(complemento_inverso(seq[i::])))
    return frames


def get_proteins(seq):
    """Função que devolve a lista ordenada das proteinas resultantes da traducao 
    da sequência de DNA fornecida
    
    Parameters
    ----------
    seq : str
        Sequência de DNA da qual queremos saber as proteinas resultantes

    Returns
    -------
    proteins: list of str
        Proteinas resultantes da traduçãoo da sequência de DNA, ordenadas por 
        tamanho e dentro do mesmo tamanho por ordem alfabética
    """
    
    assert valida(seq), "Sequencia de DNA invalida"
    frames = reading_frames(seq)
    proteins = []
    for f in frames:
        p = re.findall('M.*?_',f)
        for i in p:
            proteins.append(i)
    proteins = list(set(proteins))
    proteins.sort()
    proteins = sorted(proteins, key=len, reverse = True)
    return proteins
