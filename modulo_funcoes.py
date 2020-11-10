"""
Created on Fri Nov  6 16:49:28 2020

@author: Joana Gabriel, Maria Couto, Teresa Coimbra
"""

#raise Exception(...)

#filehandle é um ficheiro que ja esta aberto nao temos de fazer open e assim
#é ler uma linha e fazer alguma coisa com ela e ja esta

FileHandle = open("demofile.txt","r")
def ler_seq(FileHandle):
    """
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

FH = open("variola.fasta","r")
def ler_FASTA_seq(file):
    """
    Parameters
    ----------
    FileHandle : _io.TextIOWrapper
        Um ficheiro fasta
    Returns
    -------
    seq:str 
        sequência contida num ficheiro fasta sem o cabeçalho
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
    """
    Parameters
    ----------
    seq : str
        sequência de DNA

    Returns
    -------
    seq2: str    
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
    """
    Parameters
    ----------
    seq : str
        Função que verifica se uma sequência de DNA é válida (devolve True ou False)
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
    """

    Parameters
    ----------
    seq : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    seq= seq.upper()
    dici = {}
    dici['A'] = seq.count('A')
    dici['C'] = seq.count('C')
    dici['G'] = seq.count('G')
    dici['T'] = seq.count('T')
    return dici

def reading_frames(seq):
    """
    

    Parameters
    ----------
    seq : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    if valida(seq):
       frames = []
       for i in range(3):
           frames.append(seq[i::])
       for i in range(3):
           frames.append(complemento_inverso(seq[i::]))
    return frames

def get_proteins(seq):
    """

    Parameters
    ----------
    seq : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    if valida(seq):
       frames = reading_frames(seq)
       proteins = []
       for f in frames:
           rna = transcricao(f)
           p = traducao(rna)
           proteins.append(p)
    return proteins

