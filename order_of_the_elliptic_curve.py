# Funkcja do dodawania dwóch punktów na krzywej eliptycznej
def add_points(point1, point2, a, b, p):
    # Obsługa punktów w nieskończoności
    if point1 == (float('inf'), float('inf')):
        return point2
    if point2 == (float('inf'), float('inf')):
        return point1
    
    # Współrzędne punktów
    x1, y1 = point1
    x2, y2 = point2
    
    # Sprawdzenie dla punktów o jednakowej współrzędnej x
    if x1 == x2 and y1 != y2:
        return (float('inf'), float('inf'))
    
    # Obliczenie nachylenia prostej
    if point1 == point2:
        s = (3 * x1 * x1 + a) * pow(2 * y1, -1, p) % p
    else:
        s = (y2 - y1) * pow(x2 - x1, -1, p) % p
    
    # Obliczenie współrzędnych punktu wynikowego
    x3 = (s * s - x1 - x2) % p
    y3 = (s * (x1 - x3) - y1) % p
    
    return (x3, y3)

# Funkcja do mnożenia punktu przez skalar
def scalar_multiply(point, scalar, a, b, p):
    result = (float('inf'), float('inf'))
    current = point
    
    while scalar > 0:
        print(f"Obliczanie {scalar}-krotności punktu {point}:")
        if scalar % 2 == 1:
            print(f"Dodawanie punktu {current} do wyniku")
            result = add_points(result, current, a, b, p)
        print(f"Mnożenie punktu {current} przez 2")
        current = add_points(current, current, a, b, p)
        scalar //= 2
    
    return result

# Główna funkcja programu
def main():
    # Parametry krzywej eliptycznej
    a = -1
    b = 8
    p = 23
    g = (14, 1)  # Punkt bazowy
    n = 1
    
    # Obliczenie i wypisanie punktów dla liczby od 1 do 20
    while n <= 20:
        print(f"\nObliczanie punktu {n}:")
        result = scalar_multiply(g, n, a, b, p)
        print(f"\nWynik: {result}")
        n += 1

if __name__ == "__main__":
    # Wypisanie postaci równania krzywej eliptycznej
    print("Postać równania krzywej eliptycznej: y^2 = x^3 - x + 8")
    # Wywołanie głównej funkcji programu
    main()
