#TRABALHO 1 DE GRAFOS
#EXERCICIO: STORMSOFSWORDS
#PYTHON V 2.7.13
#UBUNTU 17.04
#ALUNOS: LEONARDO
#		 TATSU
#		 THIAGO KIRA
#ARQUIVO DE ENTRADA:
#		 stormofswords.csv
#		 para teste use o grafo teste.csv
#FUNCOES
#		 BFS
#		 CAMINHO BFS
#		 BIPARTIDO
#		 DFS (corrigido)
#		 STACK DFS


import Queue
import csv
import types

class Vertice:
	''' CLASSE VERTICE

		CLASSE PARA REPRESENTACAO DE VERTICES NO GRAFO

		ATRIBUTOS:
		nome: nome do vertice
		visitado: para aplicacao do BFS
		dist: distancia relativa a outro vertice
		pred: vertice predescessor
		adj: lista de nomes dos vertices adjacentes a este
		cor: indica a cor para verificar biparticao
		time: utilizado no dfs
		cc: componente conexo
		low: para verificar ponto de articulacao
	'''

	def __init__(self, n):
		''' METODO CONSTRUTOR DA CLASSE

			ARGS:
			n: nome dado ao vertice
		 '''
		self.cc = 0
		self.nome = n
		self.visitado = False
		self.dist = 0
		self.pred = None
		self.adj = []
		self.cor = 0
		self.time = 0
		self.low = 0

	def get_nome(self):
		''' METODO PARA PEGAR O NOME DO VERTICE

			RETURNS:
			retorna o nome do vertice
		'''
		return self.nome

	def get_visitado(self):
		''' METODO QUE VERIFICA SE O VERTICE JA FOI VISITADO

			RETURNS:
			true, se foi visitado
			false, caso contratio
	 	'''
		return (self.visitado)

	def set_visitado(self, b):
		''' METODO PARA SETAR VISITADO

			ARGS:
			b: variavel logica (True ou False)
		'''

		self.visitado = b

	def get_dist(self):
		''' METODO QUE RETORNA A DISTANCIA DO VERTICE

			RETURNS:
			retorna a distancia do vertice
		'''
		return (self.dist)

	def set_dist(self, d):
		''' METODO PARA SETAR A DISTANCIA

			ARGS:
			d: distancia relativa ao vertice
		'''
		self.dist = d

	def set_pred(self, v):
		''' METODO PARA SETAR O PREDESCESSOR DO VERTICE

			ARGS:
			v: e o vertice PREDESCESSOR
		'''
		self.pred = v

	def get_pred(self):
		''' METODO PARA RETORNAR O PREDESCESSOR
		'''
		return (self.pred)

	def add_adj(self, v):
		''' METODO PARA ADICIONAR DETERMINADO VERTICE A LISTA DE ADJACENTES

			ESTE METODO RECEBE UM VERTICE E O ADICIONA A LISTA DE VERTICES
			ADJACENTES

			ARGS:
			v: e o vertice predescessor
		'''
		self.adj.append(v)

	def get_adj(self):
		''' METODO PARA RETORNAR VERTICES ADJACENTES

			RETORNA UMA LISTA CONTENDO OS VERTICES ADJACENTES

			RETURNS
			devolve uma lista, com os vetices ADJACENTES
		'''
		return (self.adj)

	def get_cor(self):
		''' METODO PARA PEGAR COR DO VERTICE

			UTILIZA PARA VERIFICAR SE O GRAFO E BIPARTIDO

			RETURNS:
			0 BRANCO
			1 AZUL
			2 VERMELHO
		'''
		return (self.cor)

	def set_cor(self, c):
		''' METODO UTILIZADO PARA SETAR COR NO VERTICE

			UTILIZADO PARA VERIFICAR SE O GRAFO E BIPARTIDO

			ARGS:
			0 BRANCO
			1 AZUL
			2VERMELHO
		'''
		self.cor = c

	def set_low(self, l):
		''' METODO PARA SETAR LOW NO VERTICE

			ARGS:
			l: valor do low do VERTICE
		'''
		self.low = l

	def get_low(self):
		''' METODO PARA RETORNAR LOW DO VERTICE

			RETURNS:
			retorna o valor do low
		'''
		return (self.low)

	def set_time(self, t):
		''' METODO PARA SETAR TEMPO

			UTILIZADO NO DFS

			ARGS:
			t: tempo a ser setado
		'''
		self.time = t

	def get_time(self):
		''' METODO PARA PEGAR O TEMPO
		'''
		return (self.time)

	def get_cc(self):
		'''METODO PARA RETORNAR CC
		'''
		return self.cc

	def set_cc(self, c):
		''' METODO PARA SETAR CC
		'''
		self.cc = c

	def print_vertice(self):
		''' METODO PARA EXIBIR O VERTICE

			IMPRIME O VERTICE NA FORMA NOME: DISTANCIA
		'''

		print ('-> {}:' .format(self.nome))

	def print_bfs(self):
		''' METODO PARA IMPRIMIR INFORMACOES DO BFS
		'''
		print('V -> {} | D -> {} | P -> {}'.format(self.get_nome(),
		 									       self.get_dist(),
												   self.get_pred().get_nome()))

class Grafo:
	'''	CLASSE GRAFO

		CLASSE PARA REPRESENTACAO DOS GRAFOS
		ARMAZENA EM DICIONARIO

		ATRIBUTOS:
		vertex: lista com os vertices do Grafo
	'''
	def __init__(self):
		''' METODO CONSTRUTOR DA CLASSE

			O GRAFO E ESTRUTURADO NA FORMA DE DICIONARIO
			NO FORMATO {'NOME':'OBJETO'}

		'''
		self.cc = 0
		self.mystack = []
		self.tempo = 0
		self.vertex = {}
		with open ('teste.csv', 'rU') as input:
			spamreader = csv.reader(input)
			for row in spamreader:
				vaux1 = Vertice(row[0])
				vaux2 = Vertice(row[1])

				if (vaux1.get_nome() not in self.vertex.keys()):
					self.vertex[vaux1.get_nome()] = vaux1
				if (vaux2.get_nome() not in self.vertex.keys()):
					self.vertex[vaux2.get_nome()] = vaux2

				if (vaux2.get_nome() not in self.vertex[vaux1.get_nome()].get_adj()):
					self.vertex[vaux1.get_nome()].add_adj(vaux2.get_nome())
				if (vaux1.get_nome() not in self.vertex[vaux2.get_nome()].get_adj()):
					self.vertex[vaux2.get_nome()].add_adj(vaux1.get_nome())


	def print_grafo(self):
		''' METODO PARA IMPRIMIR GRAFO
		'''
		for k in self.vertex.keys():
			print('VERTICE ->')
			self.vertex[k].print_vertice()
			print('ADJACENTES ->')
			for i in self.vertex[k].get_adj():
				self.vertex[i].print_vertice()


	def init_grafo(self):
		''' METODO PARA INICIALIZAR GRAFO

			RESETA OS ATRIBUTOS DOS VERTICE DO GRAFO
		'''
		self.cc = 0
		self.mystack[:] = []
		self.tempo = 0
		for k in self.vertex.values():
			k.set_visitado(False)
			k.set_pred(None)
			k.set_dist(0)
			k.set_cor(0)
			k.set_time(0)
			k.set_low(0)

	def bfs(self, s):
		''' BREAD FIST SEARCH

			METODO PARA IMPLEMENTACAO DO BUSCA EM LARGURA

			ARGS:
			s: vertice raiz para o bfs
		'''
		self.init_grafo()
		myq = Queue.Queue()
		myq.put((s))
		while (not myq.empty()):
			v = myq.get()
			vaux1 = self.vertex[str(v)]
			for vaux2 in vaux1.get_adj():
				if (not self.vertex[vaux2].get_visitado()):
					self.vertex[vaux2].set_visitado(True)
					self.vertex[vaux2].set_dist(vaux1.get_dist()+1)
					self.vertex[vaux2].set_pred(vaux1)
					myq.put(str(vaux2))
			vaux1.set_visitado(True)

		for k in self.vertex.values():
			if (k.get_dist() > 0) :
				k.print_bfs()

	def caminho_bfs(self,s,v):

		''' IMPRIME O CAMINHO DO VERTICE ATE DETERMINADO DESTINO

			ARGS:
			s: e o vertice origem
			v: e o vertice destino
		'''

		if (s == v):
			print(self.vertex[s].get_nome())
		else:
			self.caminho_bfs(s, self.vertex[v].get_pred().get_nome())
			print(self.vertex[v].get_nome())

	def bipartido(self, s):

		''' VERIFICA SE O GRAFO E BIPARTIDO

			UTILIZA O CONCEITO DE QUE UM GRAFO BIPARTIDO NAO POSSUI CICLOS DE
			TAMANHO IMPAR

			ARGS:
			s: vertice raiz

			RETURNS:
			retorna True ou False
		'''
		self.init_grafo()
		self.vertex[s].set_visitado(True)
		myq = Queue.Queue()
		myq.put(s)
		while(not myq.empty()):
			v = myq.get()
			vaux1 = self.vertex[str(v)]
			for vaux2 in vaux1.get_adj():
				if (self.vertex[vaux2].get_cor() == 0):
					if (vaux1.get_cor() == 1):
						self.vertex[vaux2].set_cor(2)
					else:
						self.vertex[vaux2].set_cor(1)
					myq.put(vaux2)
				elif (vaux1.get_cor() == self.vertex[vaux2].get_cor()):
					return False
		return True

	def dfs(self, s):
		''' METODO DE BUSCA EM PROFUNDIDADE

			ALGORITMO DE BUSCA EM PROFUNDIDADE
			UTILIZA PILHA IMPLICITA (RECURSAO)


			ARGS:
			s: vertice raiz
		'''

		self.init_grafo()
		self.dfs_visit(self.vertex[s])

		#proposta de modificacao:
		#so para ajeitar a sequencia t.d, t.f
		#agora o vertice raiz tem t.d = 1
		#antigo codigo:
		#self.vertex[s].set_visitado(True)
		#for k in self.vertex[s].get_adj():
		#	if (not self.vertex[k].get_visitado()):
		#		self.dfs_visit(self.vertex[k])
		#fim

		for j in self.vertex.values():
			if (j.get_visitado()):
				print('N: {} | T.d: {}	| T.f: {} | P: {}'.format(j.get_nome(), j.get_dist(), j.get_time(), j.get_pred()))

	def dfs_visit(self,u):
		''' METODO DE BUSCA EM PROFUNDIDADE

			ALGORITMO DE BUSCA EM PROFUNDIDADE
			UTILIZA u.dist como u.d
			UTILIZA u.time como u.f

			ARGS:
			u: vertice raiz
		'''
		self.tempo += 1
		u.set_visitado(True)
		u.set_dist(self.tempo)
		for k in u.get_adj():
			if (not self.vertex[k].get_visitado()):
				(self.vertex[k]).set_pred(u.get_nome())
				self.dfs_visit(self.vertex[k])
		self.tempo += 1
		u.set_visitado(True)
		u.set_time(self.tempo)

	def stack_dfs(self, v):
		''' DFS USANDO STACK
			SO PARA TESTAR, AXO Q O PRIMEIRO DFS NAO FUNFA
			CORRECAO: FUNFA SIM
		'''

		self.init_grafo()
		self.mystack.append(v)
		while (self.mystack):
			u = self.mystack.pop()
			if (not self.vertex[u].get_visitado()):
				print(u)
				self.vertex[u].set_visitado(True)
				for k in self.vertex[u].get_adj():
					if (not self.vertex[k].get_visitado()):
						self.mystack.append(k)

		for j in self.vertex.values():
			if (j.get_visitado()):
				print('N: {} | T.d: {}	| T.f: {} | P: {}'.format(j.get_nome(), j.get_dist(), j.get_time(), j.get_pred()))


	def c_components(self):
		''' METODO PARA VERIFICAR OS COMPONENTES CONEXOS DO GRAFO

			RETURNS:
			retorna cc. o numero de componentes conexos
		'''
		self.init_grafo()
		for k in self.vertex.values():
			if (not k.get_visitado()):
				self.cc += 1
				self.c_visit(k)

		return self.cc

	def c_visit(self, c):
		''' DFS VISIT PARA CC

			ARGS:
			c: e o vertice visitado
		'''
		c.set_visitado(True)
		c.set_cc(self.cc)
		for k in c.get_adj():
			if (not self.vertex[k].get_visitado()):
				self.c_visit(self.vertex[k])

	def articulation_point(self, u):
		''' METODO PARA IDENTIFICAR PONTOS DE articulacao

			UTILIZA u.dist como u.d
			UTILIZA u.time como u.f

			ARGS:
			u: e o vertice visitado
		'''
		self.init_grafo()
		self.tempo += 1
		self.vertex[u].set_visitado(True)
		self.vertex[u].set_low(self.tempo)
		self.vertex[u].set_dist(self.tempo)
		for v in self.vertex[u].get_adj():
			if (not self.vertex[v].get_visitado()):
				self.vertex[v].set_pred(u)
				#self.articulation_point(v)
				if (self.vertex[u].get_pred() == None):
					if (len(self.vertex[u].get_adj()) > 2):
						print('Propriedade 1: u e raiz possui pelo menos 2 filhos')
						print('{} e articulacao'.format(self.vertex[u].get_nome()))
				else:
					self.vertex[u].set_low(min(self.vertex[u].get_low(),
											   self.vertex[v].get_low()))
					if (self.vertex[v].get_low() >= self.vertex[u].get_dist()):
						print('Propriedade 2: u possui descendente v com v.low >= u.d')
						print('{} e ponto de articulacao'.format(self.vertex[u].get_nome()))
			else:
				if (v != self.vertex[u].get_pred() and
					self.vertex[v].get_dist() < self.vertex[u].get_dist()):
					self.vertex[u].set_low(min(self.vertex[u].get_low,
					 						   self.vertex[v].get_dist()))

		self.tempo += 1
		self.vertex[u].set_time(self.tempo)


meugrafo = Grafo()
meugrafo.articulation_point('um')
#meugrafo.caminho_bfs('Aemon', 'Stannis')
#print(meugrafo.bipartido('Aemon'))
#meugrafo.stack_dfs('Aemon')
# meugrafo.dfs('um')
