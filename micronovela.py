respuesta = int(input("Te acabas de despertar, queres: (1) tomar agua o (2) seguir durmiendo? "))
if respuesta == 1 :
    print("""Te levantaste de la cama, bajaste a la cocina y buscaste un vaso de agua.
             Volviste a subir, el sueño te gano y nuevamente fuiste a dormir, sin despertar hasta la noche.
             Al despertar comiste algo y luego tuviste una noche normal.""")
elif respuesta == 2:
    respuesta = input("""Decidiste seguir durmiendo, te despertaste poco despues por un ruido en la ventana.
                               Quieres ir a ver el ruido? (s/n) """)
    if respuesta == "s":
        respuesta = input(""" Un pequeño ave golpeo contra tu ventana quedando mal herida, se nota una lastimadura en su alas.
                                    Abres la ventana y dejas entrar al pobre amiguito? (s/n) """)
        if respuesta == "s":
            respueta = input(""" Abres la ventana, una brisa toca tu cara suavemente mientras estiras los brazos para agarrar al ave.
                                       Mientras la agarras ves como un gato se acerca con rapidez, tiras al ave hacia tu habitacion cerrando la ventana bruscamente.
                                       Quien sabe que le podria haber pasado a la pobre ave si no abrias.""")
        elif respuesta == "n":
            print("""Continuas durmiendo dejando al pobre ave afuera.
                     Cuando vuelves a despertarte el ave ya no esta, solo un rastro rojo...""")
    elif respuesta == "n":
        respuesta = input(""" Ignoras el ruido intentando volver a dormir, poco tiempo despues escuchas suaves pisadas en tu techo.
                              Parece que un gato esta caminando hacia tu ventana, olvidas el ruido e ignoras al gato, te das vuelta y vuelves a dormir.
                              Cuando vuelves a despertar miras tu ventana notando un par de plumas pequeñas y un rastro rojo...""")
