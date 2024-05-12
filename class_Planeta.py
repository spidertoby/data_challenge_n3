#!/usr/bin/env python
# coding: utf-8

# In[11]:


class Planeta:
    def __init__(self, estrella_anfitriona, masa_planetaria, radio, a, inclinacion, excentricidad, argumento_periastron):
        """
        Inicializa una instancia de la clase Planeta con los atributos especificados.

        Parámetros:
        estrella_anfitriona (Estrella): La estrella anfitriona alrededor de la cual orbita el planeta.
        masa_planetaria (float): La masa del planeta en kilogramos.
        radio (float): El radio del planeta en metros.
        a (float): El semieje mayor de la órbita del planeta en metros.
        inclinacion (float): La inclinación orbital del planeta en grados.
        excentricidad (float): La excentricidad orbital del planeta.
        argumento_periastron (float): El argumento del periastron del planeta en grados.

        ---------------
        ATRIBUTOS DE LA CLASE PLANETA

        ---------------
        CLASS periodo_rotacion_kepleriana
        Calcula y devuelve el período de rotación kepleriana del planeta.

        Parámetros:
        G (float): La constante gravitacional en unidades adecuadas.

        Returns:
        float: El período de rotación kepleriana del planeta en segundos.
        """
        self._estrella_anfitriona = estrella_anfitriona
        self._masa_planetaria = masa_planetaria
        self._radio = radio
        self._a = a
        self._inclinacion = inclinacion
        self._excentricidad = excentricidad
        self._argumento_periastron = argumento_periastron

    def periodo_rotacion_kepleriana(self, G):
        T = 2 * np.pi * np.sqrt((self._a ** 3) / (G * self._estrella_anfitriona._masa))
        return T
    