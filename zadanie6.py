def suma_dzielnikow(n):
    suma=[]
    for i in range(1,n):
        if n%i==0:
            suma.append(i)
    return suma

print(suma_dzielnikow(6))