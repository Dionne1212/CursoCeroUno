encuestados = [['Femenino', 38, 2, "Nuevo Repueblo", "de 0 a 5,000", False],
               ['Femenino', 19, 0, "Contry La silla", "de 10,000 a 15,000", False],
               ['Masculino', 22, 1, "Fomerrey 22", "de 0 a 5,000", False],
               ['Masculino', 70, 3, "Valle Verde", "de 5,000 a 7,000", True],
               ['Femenino', 57, 4, "Centro", "de 7,000 a 10,000", False],
               ['Femenino', 44, 0, "Valle Alto", "de 30,000 a 50,000", False],
               ['Femenino', 20, 2, "Burócratas Municipales", "de 5,000 a 7,000", True],
               ['Masculino', 19, 0, "Buenos Aires", "de 10,000 a 13,000", True],
               ['Femenino', 12, 0, "Obrera", "de 5,000 a 7,000", True],
               ['Masculino', 32, 3, "Contry Sol", "de 10,000 a 15,000", False],
               ['Femenino', 87, 9, "Del Paseo", "de 15,000 a 20,000", True],
               ['Femenino', 25, 1, "Roma", "de 20,000 a 25,000", False],
               ['Masculino', 65, 3, "Estadio", "de 10,000 a 15,000", True], ]

# Dificultad normal:

# edad mayor a 20: no-joven
# edad menor a 20: joven
edad_del_usuario = 17
if edad_del_usuario > 20:
    print ("no joven")
else:
    print ("joven")


for x in encuestados:
    if x[1]>20:
        x.append("no joven")
    else:
        x.append("joven")
print(encuestados)           
