#!/usr/bin/env python
# coding: utf-8

# In[13]:


class SistemaPlanetario:
    """
    Sistema Planetario
    Un sistema planetario contiene una lista de planetas y proporciona métodos para operar con ellos.

    Atributos:
    planetas (list): La lista de planetas en el sistema planetario.

    Métodos:
    __init__(planetas): Inicializa una instancia de la clase SistemaPlanetario con la lista de planetas proporcionada.
    numero_planetas(): Devuelve el número de planetas en el sistema planetario.
    planetas_ordenados_por_radio(): Devuelve la lista de planetas ordenada por su radio semi-mayor de la órbita 'a'.
    """
    def __init__(self, planetas):
        """
        Inicializa una instancia de la clase SistemaPlanetario con la lista de planetas proporcionada.

        Parámetros:
        planetas (list): La lista de planetas en el sistema planetario.
        """
        self.planetas = planetas

    def numero_planetas(self):
        """
        Devuelve el número de planetas en el sistema planetario.

        Retorna:
        int: El número de planetas en el sistema planetario.
        """
        return len(self.planetas)

    def planetas_ordenados_por_radio(self):
        """
        Devuelve la lista de planetas ordenada por su radio semi-mayor de la órbita 'a'.

        Retorna:
        list: La lista de planetas ordenada por su radio semi-mayor de la órbita 'a'.
        """
        return sorted(self.planetas, key=lambda planeta: planeta.a)


