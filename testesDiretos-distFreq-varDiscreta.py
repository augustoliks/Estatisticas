import pandas as pd

numeros = [
	324,324,
	325,
	326,326,326,326,
	327,327,327,
	328,328,328,328,
	328,328,
	329,329,
	330,330
]

Xi = list(set(numeros))
fi = [ numeros.count(k) for k in set(numeros) ]

somatorio_fi = 0
for k in set(numeros):
    somatorio_fi += numeros.count(k)

fi.append(somatorio_fi)

fri = []
[ fri.append(fi[k]/somatorio_fi) for k in range(0, len(fi)-1 ) ]

aux = 0
Fi = []
for k in fi[:-1] :
    aux+=k
    Fi.append(aux)

Fri = []
[ Fri.append(Fi[k]/somatorio_fi) for k in range(0, len(Fi) ) ]

data = {
	'Xi': Xi,
	'fi': fi[:-1],
	'fri': fri,
	'Fi': Fi,
	'Fri': Fri
}

df = pd.DataFrame(data)
pd.DataFrame(df).to_csv('TabelaDistribuicaoFrequencia.csv')
