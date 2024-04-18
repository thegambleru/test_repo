def functie(element):

    print(f"Element is {element}")

def mai_mare_decat_5(element):
    if element > 5:
        return "da"
    elif element == 5:
        return "egal cu 5"
    return "nu"

a = mai_mare_decat_5(5)

print(a)

def numere_mai_mari_decat_5(element):
    for el in element:
        if el > 5:
            print(el)

b = [12,5,22,37,3,2,5,4,3]

print(b.index(37))

dict = {
    "a": "test",
    "B": 25
}

print(dict["a"])