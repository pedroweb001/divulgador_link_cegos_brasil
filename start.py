import pyperclip as pedroian
import random
import requests

 #encoding: utf-8
#Atenção:
#Para tudo funcionar corretamente, execute esse comando no seu cmd com o python fechado:
#pip install pyperclip
#E pronto. Agora pode executar o script normalmente.

def menu():
	print("Olá! Seja bem-vindo!")
	pega_titulo()

def pega_titulo():
	titulo_padrao = input("Digite ou cole o título da série/filme: Obs.: Use shift+insert para colar o conteúdo da área de transferência:")
	while (titulo_padrao == "	"):
		titulo_padrao = input("Erro. Esse campo não pode ficar vazio! \n Digite ou cole o título da série/filme: Obs.: Use shift+insert para colar o conteúdo da área de transferência:")
	while (titulo_padrao == ""):
		titulo_padrao = input("Erro. Esse campo não pode ficar vazio! \n Digite ou cole o título da série/filme: Obs.: Use shift+insert para colar o conteúdo da área de transferência:")
	converte_titulo(titulo_padrao)

def converte_titulo(titulo):
	titulo_novo = titulo.split(";")
	conteudo_area_transferencia = titulo_novo[0]+ "."
	pega_link(conteudo_area_transferencia)

def pega_link(titulo):
	novo_link = ""
	conteudo_link = input("Agora por favor, digite o link que direciona para esse título:")
	while (conteudo_link == ""):
		conteudo_link = input("Erro. Esse campo não pode ficar vazio! \n Por favor, digite o link que direciona para o título:")
	while (conteudo_link == "	"):
		conteudo_link = input("Erro. Esse campo não pode ficar vazio! \n Por favor, digite o link que direciona para o título:")
	verifica_link = ""
	if (verifica_link not in conteudo_link):
		novo_link = conteudo_link
	else:
		n = conteudo_link.split("")
		novo_link = n[0]
	mistura_e_copia(titulo, novo_link)

def mistura_e_copia(titulo, link):
	with open("mensagens.txt", "r") as arquivo:
		leia_arquivo = arquivo.read()
		linhas = list(map(str, leia_arquivo.split('\n')))
		mensagem_sorteada = random.choice(linhas)
	m = "Confira nesse link:";
	print(mensagem_sorteada)
	print()
	print(titulo)
	print()
	print(m)
	print()
	print(link)
	tudo_certo1 = mensagem_sorteada + "\n" + titulo + "\n" +m + "\n" + link
	pedroian.copy(tudo_certo1)
	print("Conteúdo copiado para área de transferência com sucesso!")
	verifica_sair()

def verifica_sair():
	res = input("Você deseja copiar mais conteúdos para área de transferência?")
	while (res != "n" and res != "s"):
		res = input("Você deseja copiar mais conteúdos para área de transferência?")
	if(res == "s"):
		pega_titulo()
	else:
		if(res == "n"):
			exit()

menu()