"""
Created on Fri Nov  6 16:49:28 2020

@author: Joana Gabriel, Maria Couto, Teresa Coimbra
"""

import re
#Constantes - Mensagem de erro
seq_inv = "Sequencia de DNA invalida"
fich_vaz = "Ficheiro vazio"

def ler_seq(FileHandle):
    """ Funcao que devolve a sequencia contida numa linha do ficheiro
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
    assert seq != '', fich_vaz
    seq= seq.upper()
    return seq



def ler_FASTA_seq(file):
    """Função que devolve a primeira sequência contida num ficheiro FASTA
    Se o ficheiro apresentar mais do que uma sequência, devolve apenas a primeira
    
    Parameters
    ----------
    FileHandle : _io.TextIOWrapper
        Um ficheiro FASTA
        
    Returns
    -------
    seq : str 
        Primeira sequência contida num ficheiro FASTA, sem o cabeçalho
    """
    
    linhas = file.readlines()
    assert linhas != [], fich_vaz
    
    seq = ''
    
    a = ''.join(linhas)
    header = re.findall('>.+[\n]',a) # para obter a lista dos cabeçalhos
   
    for l in linhas:
        if l == header[0]:
            continue
        elif l not in header:
            seq+=l.replace('\n','')
        elif l in header:
            break
    return seq    




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
    
    if valida(seq):
        seq2 = seq[::-1].lower().replace('a','T').replace('c','G').replace('g','C').replace('t','A')
    else:
        raise Exception(seq_inv)
    return seq2

def transcricao(seq):
    """Função que faz a transcrição de uma sequência de DNA

    Parameters
    ----------
    seq : str
        Sequência de DNA

    Returns
    -------
    rna : str
        Transcrição de uma sequência de DNA em RNA
    """
    
    if valida(seq):
        rna = seq.upper().replace("T","U")
    else:
        raise Exception(seq_inv)
    return rna

def traducao(seq):
    """Função que faz a tradução de uma sequência de DNA

    Parameters
    ----------
    seq : str
        Sequência de DNA

    Returns
    -------
    aas : str
        Sequência de aminoácidos resultante da tradução da sequência de DNA
    """
    
    if valida(seq):
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
    else:
        raise Exception(seq_inv)
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
    if (len(seq)==true_seq) and (len(seq) > 0):
        return True
    else:
        return False

def contar_bases(seq):
    """Função que recebe uma sequência de DNA, RNA ou aminoacidos e faz
    a contagem das suas bases

    Parameters
    ----------
    seq : str
        Sequência de DNA, RNA ou aminoacidos da qual queremos contar as bases

    Returns
    -------
    dici : dict[str,int]
         Dicionário que conta como chave as bases da sequência
         e para cada chave apresenta o valor da contagem dessa base
    """
    
    if seq.isalpha():
        seq= seq.upper()
        dici = {}
        for letra in seq:
            if letra not in dici:
                dici[letra] = 0
            dici[letra] += 1
    else:
        raise Exception(seq_inv)
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
    
    if valida(seq):
        frames = []
        for i in range(3):
            frames.append(traducao(seq[i::]))
        com_inv = complemento_inverso(seq)
        for i in range(3):
            frames.append(traducao(com_inv[i::]))
    else:
        raise Exception(seq_inv)
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
    
    if valida(seq):
        frames = reading_frames(seq)
        proteins = []
        for f in frames:
            p = re.findall('M.*?_',f)
            for i in p:
                proteins.append(i)
        proteins = list(set(proteins))
        proteins.sort()
        proteins = sorted(proteins, key=len, reverse = True)
    else:
        raise Exception(seq_inv)
    return proteins
