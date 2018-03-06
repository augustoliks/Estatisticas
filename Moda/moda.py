x = (1,2,3)
json = {}
aux = None
modas = []

for k in set(x):
    json[k] = x.count(k)

for k in json:
    if aux == None:
        aux = json[k]
    if json[k] > aux: 
        aux = json[k]

for k in json:
    print (json[k], " == ", aux)
    if json[k] == aux:
        modas.append(k)


if len(modas)==len(json):
        print ("Nao há moda")
modas

