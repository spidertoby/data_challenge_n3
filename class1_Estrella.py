class Estrella:
    def __init__(self, nombre, masa, radio, temperatura, distancia, movimiento_propio):
        """
        Inicializa una instancia de la clase Estrella con los atributos especificados.

        Parámetros:
        nombre (str): El nombre de la estrella.
        masa (float): La masa de la estrella en kilogramos.
        radio (float): El radio de la estrella en metros.
        temperatura (float): La temperatura efectiva de la estrella en Kelvin.
        distancia (float): La distancia de la estrella a la Tierra en parsecs.
        movimiento_propio (float): El movimiento propio de la estrella en segundos de arco por año.

        ---------------
        CLASS Luminosidad_total

        Calcula la luminosidad total de la estrella.

        Returns:
        float: La luminosidad total de la estrella en vatios.
        -------------------
        ATRIBUTOS DE LA CLASE ESTRELLA
    
        ---------------
        CLASS Luminosidad_secuencia_principal
        Calcula la luminosidad de la secuencia principal de la estrella, comparada con el Sol.

        Returns:
        float: La luminosidad de la estrella en términos de la luminosidad del Sol.

        -------------------
        CLASS Radio_schwarzschild
        Calcula y devuelve el radio de Schwarzschild de la estrella.

        Returns:
        float: El radio de Schwarzschild de la estrella en kilómetros.

        -------------------
        CLASS Clasificacion_espectral
        Clasifica la estrella entregada de acuerdo a la Clasificacion Espectral, la cual separa
        las estrellas de acuerdo a su temperatura:

        	Temperatura	              Color
        O	30.000 - 60.000 K	Estrellas azules
        B	10.000 - 30.000 K	Estrellas azules-blancas
        A	7.500 - 10.000 K	Estrellas blancas
        F	6.000 - 7.500 K	    Estrellas amarillas-blancas
        G	5.000 - 6.000 K  	Estrellas amarillas (como el Sol)
        K	3.500 - 5.000K	    Estrellas amarillas-naranjas
        M	< 3.500 K	        Estrellas rojas

        Returns:
        Clasificacion espectral para la estrella entregada.
        """
        self.nombre = nombre
        self._masa = masa
        self._radio = radio
        self._temperatura = temperatura
        self._distancia = distancia
        self._movimiento_propio = movimiento_propio

    def luminosidad_total(self):
        return 4 * np.pi * self._radio ** 2 * self._temperatura


    def luminosidad_secuencia_principal(self):
        L_sun = 3.828e26  # Luminosidad del Sol en vatios
        M_sun = 1.9884e30  # Masa del Sol en kilogramos
        return L_sun * (self._masa / M_sun) ** 3.5

    
    def radio_schwarzschild(self):
        c = 300_000  # Velocidad de la luz en km/s
        G = 6.67e-11  # Constante gravitatoria universal
        return (2 * G * self._masa) / (c ** 2)  # km
    



    def clasificacion_espectral(self):
        if self._temperatura > 41000:
            return "Clase O"
        elif 9500 <= self._temperatura <= 41000:
            return "Clase B"
        elif 7240 <= self._temperatura < 9500:
            return "Clase A"
        elif 5920 <= self._temperatura < 7240:
            return "Clase F"
        elif 5300 <= self._temperatura < 5920:
            return "Clase G"
        elif 3850 <= self._temperatura < 5300:
            return "Clase K"
        else:
            return "Clase M"
        




#!/usr/bin/env python
# coding: utf-8

# In[11]:
