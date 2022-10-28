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
    result = None
    # Implementera koden nedan

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
    result = False
    # Här sker kontrollen
    # som eventuellt ställer om variabeln result
    # ...
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
    return result

# Test-exempel
y = np.array([[3], [2]])
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


u = np.array([1, 2, 3])
v = np.array([-2, 3, -4])
dot_product = np.dot(u, v)
print(dot_product) # Skriver ut -8