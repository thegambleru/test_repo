carti = list(range(1,14))
simboluri = ["Pica","Inima","Trefla","Romb"]

for carte in carti:
    for simbol in simboluri:
        print(f'{carte} of {simbol}'.ljust(13), end='')

print()

