def slice_simple():
    texto = "Awesome"
    texto=texto.lower()
    print (texto[:3]) 
    print(texto[int(len(texto)/2)-1 :int(len(texto)/2) +2 ])
    print(texto[:4]+texto[len(texto)-3:])
