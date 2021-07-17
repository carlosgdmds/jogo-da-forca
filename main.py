import os
import verifica,tela
class Start():
	def __init__(self):
		estado = True
		while estado:
			tela.limpaTela()
			nome_desafiante = str(input("Digite o nome do desafiante "))
			nome_competidor = str(input("Digite o nome do competidor "))
			tela.limpaTela()
			self.palavra_chave = str(input("Digite a palavra chave "))
			try:
				self.palavra_chave = int(self.palavra_chave)
				estado = True
				print("O nome nao pode ser um numero")
			except:
				dicas = []
				for i in range(1,4):
					dicas.append(str(input("Digite a dica {} ".format(i))))
				estado = verifica.verificaDados(nome_desafiante, nome_competidor,self.palavra_chave ,dicas)

		tela.limpaTela()
		self.acertos = 0
		self.erros = 0
		self.sequencia_dica = 0

		#mostra texto em * 
		self.texto = []
		self.Primeirotexto = ""
		for i in range(len(self.palavra_chave)):
			self.texto.append("*")
			self.Primeirotexto = self.Primeirotexto + "*"

		print(self.Primeirotexto)

		self.letrasacertos = []
		self.quantidade = 0
		#roda programa ate o jogador ganhar ou perder
		while self.acertos < len(self.palavra_chave) and self.erros != 5:
			try:
				self.escolha = int(input("Jogar 1 | Dica 2 "))
			except:
				print("Opcao invalida")
			if self.escolha == 1:
				self.chute = str(input("Digite uma letra "))
				#verifica se acertou e a quantidades de vezes que a letra aparece na palavra chave
				acerto,self.quantidade = verifica.verificaLetra(self.chute,self.palavra_chave,self.quantidade)
				if acerto:
					if self.chute in self.letrasacertos:
						print('Essa letra ja foi usada')
					else:
						print('Acertou')
						self.acertos += self.quantidade
						self.letrasacertos.append(self.chute)
					self.quantidade = 0
				else:
					self.erros +=1
					print('erro: '+str(self.erros))
				print(tela.MostraPalavra(self.chute, self.palavra_chave,self.texto))

			elif self.sequencia_dica >=3:
				print("voce nao tem mais dicas")
				self.escolha = "1"

			elif self.escolha == 2:
				print(dicas[self.sequencia_dica])
				self.chute = str(input("Digite uma letra "))
				acerto,self.quantidade = verifica.verificaLetra(self.chute, self.palavra_chave,self.quantidade)
				if acerto:
					if self.chute in self.letrasacertos:
						print('Essa letra ja foi usada')
					else:
						print("Acertou")
						self.acertos += self.quantidade
						self.letrasacertos.append(self.chute)
					self.quantidade = 0
				else:
					self.erros +=1
					print("erro: "+str(self.erros))
				print(tela.MostraPalavra(self.chute, self.palavra_chave, self.texto))
				self.sequencia_dica +=1
			else:
				print('opção invalida')

		#verifica se jogador ganhou ou perdeu
		verifica.verificaVencedor(self.erros, self.acertos,self.palavra_chave,nome_desafiante,nome_competidor)
		tela.VerHistorico()

if __name__=="__main__":
	while True:
		Start()
		opcao = input("Clique em 1 para jogar novamente ou quaquer outro para sair ")
		if opcao != "1":
			break
