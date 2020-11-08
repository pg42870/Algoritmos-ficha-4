# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 16:49:28 2020

@author: joana
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
    seq : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    pass

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
    seq : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    pass

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
    pass

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
    pass

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
    pass

