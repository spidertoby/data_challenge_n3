#!/usr/bin/env python
# coding: utf-8

# In[10]:


class SistemaJerarquico:
    """
    Inicializa una instancia de la clase SistemaJerarquico con las estrellas proporcionadas.

    Parámetros:
    estrellas (list): Una lista de objetos de la clase Estrella que componen el sistema jerárquico.

    -------------------------
    estrellas_ordenadas_por_masa
    Devuelve la lista de estrellas ordenadas por masa estelar.

    Retorna:
    list: Una lista de objetos de la clase Estrella ordenados por masa estelar.

    -----------------------------
    nombres_con_letras_del_alfabeto
    Imprime los nombres de las estrellas seguidos de letras del alfabeto.

    Esta función imprime los nombres de las estrellas seguidos de letras del alfabeto en orden alfabético,
    asignando una letra diferente a cada estrella en la lista.
    
    """
    def __init__(self, estrellas):
        """
        Inicializa una instancia de la clase SistemaEstelar con una lista de estrellas.

        Parámetros:
        estrellas (list): Una lista de objetos de la clase Estrella que representan las estrellas en el sistema estelar.
        """
        self.estrellas = estrellas

    def estrellas_ordenadas_por_masa(self):
        """
        Devuelve la lista de estrellas ordenadas por su masa.

        Retorna:
        list: Una lista de objetos de la clase Estrella ordenados por su masa.
        """
        return sorted(self.estrellas, key=lambda estrella: estrella.masa)

    def nombres_con_letras_del_alfabeto(self):
        """
        Imprime los nombres de las estrellas con letras del alfabeto.
        Cada nombre se imprime seguido de una letra del alfabeto en orden.
        """
        alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        nombres = [estrella.nombre for estrella in self.estrellas]
        for i, nombre in enumerate(nombres):
            print(f"{nombre}{alfabeto[i]}")

