
def escribir_el_nombre(*args, **kwargs):
    print("     inicio")
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)


escribir_el_nombre("Ludmila", primer_nombre="Luciano",
                   segundo_nombre="Cristian",
                   primer_apellido="Toneatti",
                   segundo_apellido="Gandolfo")
escribir_el_nombre(primer_nombre="Nehuen",
                   primer_apellido="Donozo",
                   segundo_apellido="Marquez")
escribir_el_nombre("Francisco", "Facundo", "Emiliano", primer_nombre="Celina",
                   segundo_nombre="Anahi",
                   primer_apellido="Guerra Diaz")
escribir_el_nombre("Raul", "Uva", "Antonio", "Pepe", "Yolanda", "Negra", primer_nombre="Eusebio",
                   primer_apellido="Quinteros")
