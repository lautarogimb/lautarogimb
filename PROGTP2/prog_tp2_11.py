men = int(input("Quiere el menú vegetariano o el común? 1: Vegetariano 2: Común: "))
if men == 1:
    ing = input("Qué ingrediente quiere?\n1: Pimientos \n2: Tofu\n")
    if ing == "1":
        ing = "Pimientos"
    else:
        ing = "Tofu"
elif men == 2:
    ing = input("Qué ingrediente quiere?\n1: Pepperoni \n2: Jamón\n3: Salmón\n")
    if ing == "1":
        ing = "Pepperoni"
    elif ing == "2":
        ing = "Jamón"
    else:
        ing = "Salmón"
if men == 1:
    print(f"Usted ha elegido el menú vegetariano y los ingredientes de su pizza son queso, tomate y {ing}")
if men == 2:
    print(f"Usted ha elegido el menú común y los ingredientes de su pizza son queso, tomate y {ing}")