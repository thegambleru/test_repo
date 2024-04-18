import random

# 1. alegem cuv din lista
# 2. sectionam cuv
# 3. blind spot holder litere
# 4. validam literele
# 4.5. Vizibilitate User litere deja alese
# 5. nr max incercari(4)
# 6. rezulat

random_words = [
    "apple", "banana", "carrot", "dog", "elephant", "fish", "guitar", "hat", "icecream", "jacket",
    "kangaroo", "lamp", "monkey", "notebook", "orange", "penguin", "quilt", "rabbit", "snake", "tiger",
    "umbrella", "violin", "watermelon", "xylophone", "yogurt", "zebra", "airplane", "book", "cat", "duck",
    "eggplant", "frog", "globe", "helicopter", "igloo", "jellyfish", "kite", "lemon", "mango", "ninja",
    "octopus", "piano", "quokka", "rose", "squirrel", "tulip", "unicorn", "volcano", "walrus", "xylophone",
    "yacht", "zeppelin", "astronaut", "bee", "caterpillar", "dolphin", "earring", "firetruck", "giraffe",
    "hamburger", "iguanodon", "jigsaw", "kangaroo", "lighthouse", "moon", "narwhal", "ostrich", "penguin",
    "quail", "raccoon", "seahorse", "turtle", "umbrella", "vampire", "whale", "xylophone", "yeti", "zebra",
    "acorn", "butterfly", "cactus", "dragon", "elephant", "flamingo", "gazelle", "hedgehog", "iceberg",
    "jackal", "koala", "llama", "mushroom", "narwhal", "owl", "peacock", "quokka", "rattlesnake", "sunflower",
    "toucan", "unicorn", "volcano", "whale", "x-ray", "yak", "zeppelin"
]

# get rendom word from list 

# defragmentare cuvant 

# create blind spot holder

# user alege litere if correct then blind spot holder -> liera aleasa -> dispaly / overite blindspot -> daca nu muiepestatuie - 1 incercare + incearca din nou pana cand #5.

# 5. daca nr actual incercari << nr max incercari  si cuvant descoperit = succes, ifelse negri in 1800



# watermelon

# w a t e r m e l o n 

# _ _ _ _ _ _ _ _ _ _ 

# N = corect -> _ _ _ _ _ _ _ _ _ N 

# Q = incorect -> _ _ _ _ _ _ _ _ _ N -> nr incercari ramse 3
 
# A = corect -> _ A _ _ _ _ _ _ _ N 



# get random word from list + defragementare 

# imp blindspot cover 
 
# lasa-l sa aleaga pana cand nrIncercari = 0 

random_word = random.choice(random_words)

cuvant = []
for litera in random_word:
    cuvant.append(litera)

nrIncercari= 4
cuvantBlind=[]
cuvantTemp = cuvant.copy()
for litera in cuvant:
    cuvantBlind.append('_')

print (cuvantBlind)



while nrIncercari > 0:
    print('Alege Litera')
    literaAleasa=input()
    if literaAleasa in cuvant:
        print(f'Ai ghicit {literaAleasa}')
        for litera in cuvant:
            if litera == literaAleasa:
                cuvantBlind[cuvantTemp.index(litera)] = litera
                cuvantTemp[cuvant.index(litera)] = 99
    else:
        nrIncercari -= 1
        if nrIncercari == 0:
            print(cuvant)
            break
    if cuvantBlind == cuvant:
        print('Ai Castigat!')
        break
                
    print(f'cuvantul este: {cuvantBlind}')            
    print(f'Mai ai {nrIncercari} incercari')


