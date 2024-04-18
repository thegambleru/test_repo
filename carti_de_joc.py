carti = range(1,14)
simboluri = ["Pica","Inima","Trefla","Romb"]
pachet = []
for carte in carti:
    for simbol in simboluri: 
        pachet.append(f"{carte} de {simbol}")

print(pachet)
