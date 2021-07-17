from sys import platform
from os import system

def limpaTela():
    if "linux" in platform:
        system('clear')
    else:
        system('cls')

def VerHistorico():
	arquivo = open('log.txt','r')
	for linha in arquivo:
		print(linha.strip())

def MostraPalavra(chute,palavra,texto):
	contador = 0
	for letra in palavra:
		if chute == letra:
			texto[contador] =letra
		contador +=1
	novo_texto = ""
	for letra in texto:
		novo_texto = novo_texto + letra
	return novo_texto
