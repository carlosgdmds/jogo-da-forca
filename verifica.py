import historico
from time import sleep
def verificaDados(nome_desafiante, nome_competidor, palavra_chave,dicas):
	estado = True
	if len(nome_desafiante) > 0 and len(nome_competidor) >0 and len(palavra_chave) > 0:
		for dica in dicas:
			if len(dica) > 0:
				estado = False
			else:
				estado = True
	else:
		print("Alguma informacao é invalida")
		sleep(2)
	return estado

def verificaLetra(chute, palavra_chave,quantidade):
	if chute in palavra_chave:
		acerto = True
	else:
		acerto = False

	for letra in palavra_chave:
		if chute == letra:
			quantidade +=1
	return acerto,quantidade

def verificaVencedor(erros,acertos,palavra_chave, desafiante, competidor):
	if erros == 5:
		print("Voce perdeu fim de jogo")
		estado = 1
		historico.Gerar(palavra_chave, desafiante, competidor, estado)
	if acertos == len(palavra_chave):
		print("Voce ganhou")
		estado = 2
		historico.Gerar(palavra_chave, desafiante, competidor, estado)
