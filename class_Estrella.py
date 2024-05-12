#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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
