def Gerar(palavra_chave, desafiante, competidor, estado):
	arquivo = open('log.txt','a')
	if estado == 1:
		log = 'Palavra: '+palavra_chave+' -- Vencedor desafiante '+desafiante+' Perdedor competidor '+ competidor
	if estado == 2:
		log = 'Palavra: '+palavra_chave+' -- Vencedor competidor '+competidor+' Perdedor desafiante '+ desafiante
	arquivo.write(log+'\n')
	arquivo.close()
