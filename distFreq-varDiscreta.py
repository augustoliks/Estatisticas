import pandas as pd

class DistFrequencia():
	def __init__(self, dados, titulo, fonte):
		self.titulo = titulo
		self.fonte = fonte
		self.rol = dados
		self.Xi = self.make_Xi(self.rol)
		self.fi = self.make_fi(self.rol)
		self.somatorio_fi = self.make_sum_fi(self.fi, self.rol)
		self.fri = self.make_fri(self.fi, self.somatorio_fi)
		self.Fi = self.make_Fi(self.fi)
		self.Fri = self.make_Fri(self.Fi,self.somatorio_fi)
		self.make_dataframe()

	def make_Xi(self, dados):
		_aux = list(set(dados))
		_aux.sort()
		return _aux

	def make_fi(self, dados):
		return [ dados.count(k) for k in set(dados) ]

	def make_sum_fi(self, fi, dados):
		ak = 0
		for k in range(0, len(fi) ):
		    ak += fi[k]

		return ak

	def make_fri(self, fi, somatorio_fi):
		fri = []
		for k in range(0, len(fi) ):
			fri.append(self.fi[k]/somatorio_fi)

		return fri

	def make_Fi(self, fi):
		Fi = []
		aux = 0
		for k in fi :
		    aux+=k
		    Fi.append(aux)

		return Fi

	def make_Fri(self, Fi, somatorio_fi):
		Fri = []
		for k in range( 0, len(Fi) ):
			Fri.append(Fi[k] / somatorio_fi)

		return Fri

	def make_dataframe(self):

		data = {
			'Xi': self.Xi,
			'fi': self.fi,
			'fri': self.fri,
			'Fi': self.Fi,
			'Fri': self.Fri
		}

		df = pd.DataFrame(data, columns=['Xi','fi','fri', 'Fi', 'Fri'])
		pd.DataFrame(df).to_csv('TabelaDistribuicaoFrequencia.csv')
		print ("\t", self.titulo, "\n", df, "\nFonte: ", self.fonte)

if __name__ == '__main__':
	numeros = [
		0,
		324,324,
		325,
		326,326,326,326,
		327,327,327,
		328,328,328,328,
		328,328,
		329,329,
		330,330,
		0,1000,1,
		0,330
	]
