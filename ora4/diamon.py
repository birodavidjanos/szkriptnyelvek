def draw_diamond(height):
    # Ellenőrizzük, hogy a magasság páratlan-e
    if height % 2 == 0:
        print("Hiba: A magasság csak páratlan szám lehet!")
        return
    
    # Felső háromszög kirajzolása
    for i in range(1, height + 1, 2):
        print(("*" * i).center(height))
    
    # Alsó háromszög kirajzolása
    for i in range(height - 2, 0, -2):
        print(("*" * i).center(height))

# Példa használatra
draw_diamond(3)
draw_diamond(7)
draw_diamond(4)  # Hibaüzenetet fog adni