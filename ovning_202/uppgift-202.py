import numpy as np

def dot_product(vec_1, vec_2):
    '''
    Parametrar:
        vec_1: en vektor av typen ndarray
        vec_2: en vektor av typen ndarray
    Returvärde:
        Om vektorerna går att multiplicera skalärt:
            Skalärprodukten
        Om vektorerna inte går att multiplicera skalärt:
            None
    Övrigt: Denna funktion bygger inte på NumPy:s implementering
    av skalärprodukt.
    '''
    
    # Implementera koden nedan
    result = 0
    if len(vec_1) == len(vec_2):
        for i in range(len(vec_1)):
            result += vec_1[i]*vec_2[i]
    else:
        result = None

    return result

def is_orthogonal(koord_axlar):
    '''
    Parameter:
        koord_axlar: en matris av typen ndarray som
        definierar de båda koordinat-axlarnas riktning i kolonnerna
    Returvärde:
        Om ortogonala axlar: True
        Om ej ortogonala axlar: False
    '''
    # Här sker kontrollen
    # som eventuellt ställer om variabeln result
    # ...

    if koord_axlar[0][0] == koord_axlar[1][1] and koord_axlar[0][1] == - koord_axlar[1][0]:
        result = True
    else:
        result = False
    
    return result

def calc_proj(vektor, koord_axlar):
    '''
    Parametrar:
        vektor: en vektor med två komponenter av typen ndarray
        koord_axlar: en matris av typen ndarray som definierar
        de båda koordinat-axlarnas riktning i kolonnerna
    Returvärde:
        En matris av typen ndarray som innehåller projektionen
        på respektive koordinataxel i kolonnerna
    '''
    result = np.zeros([2, 2])
    # Här sker själva beräkningen som lagrar
    # resultatet i variabeln result
    # ...

    täljare = dot_product(vektor, koord_axlar[0])
    nämnare = dot_product(koord_axlar[0], koord_axlar[0])

    y11 = täljare/nämnare*koord_axlar[0][0]
    y12 = täljare/nämnare*koord_axlar[0][1]
    y21 = vektor[0]-y11
    y22 = vektor[1]-y12

    rad1 = np.array([y11,y21])
    rad2 = np.array([y12,y22])

    result = np.array([rad1.T, rad2.T])

    return result




# Test-exempel
y = np.array([3, 2])
u1 = np.array([4, 1])
u2 = np.array([-1, 4])
u = np.array([u1.T, u2.T])
# Kontrollera hur y och u skrivs ut
# INNAN du börjar skriva funktionerna



### Ändra inget under denna rad
if is_orthogonal(u):
    proj = calc_proj(y, u)
    print(proj.round(2))
    # För en fungerande funktion och givna
    # data enligt räkneexemplet så skrivs ut:
    # [[3.29, -0.29],
    # [0.82, 1.18]]

    print("Längden på ovanstående projektionsvektorer:")
    norm_u1 = round(np.linalg.norm(proj[:, 0]), 2)
    norm_u2 = round(np.linalg.norm(proj[:, 1]), 2)
    print(f"||u1|| = {norm_u1}")  # Blir 3.4
    print(f"||u2|| = {norm_u2}")  # Blir 1.21
else:
    print("Angivna koordinataxlar är inte ortogonala.")
