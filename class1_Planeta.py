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

        
        -------------------
        CLASS densidad_y_flotabilidad
        Calcula la densidad del planeta y verifica si flotaría en el agua de la Tierra.
        
        Returns:
        str: Un mensaje indicando si el planeta flotaría o no en el agua de la Tierra.


        -------------------
        CLASS superficie_habitable
        Asigna al planeta la cualidad de si tiene una superficie
        habitable o no, esto de acuerdo a su temperatura y su distancia
        con la estrella.

        Returns:
        str: Un mensaje indicando si el planeta flotaría o no en el agua de la Tierra.
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


    def densidad_y_flotabilidad(self):

        densidad_agua_tierra = 1000  # Densidad del agua de la Tierra en kg/m^3

        # Calcula el volumen del planeta
        volumen = (4 / 3) * np.pi * self._radio ** 3

        # Calcula la densidad del planeta
        densidad_planeta = self._masa_planetaria / volumen

        # Verifica si el planeta flotaría en el agua de la Tierra
        if densidad_planeta < densidad_agua_tierra:
            mensaje = f"El planeta flotaría en el agua de la Tierra."
        else:
            mensaje = f"El planeta no flotaría en el agua de la Tierra."

        return mensaje
    
    def superficie_habitable(self):
        temperatura_habitabilidad = (273.15, 373.15)  # Rango de temperatura habitable en grados Kelvin
        distancia_habitabilidad = (0.75, 1.5)  # Rango de distancia habitable en UA

        temperatura = self._temperatura
        distancia = self._a #Distancia desde el planeta a la estrella

        if temperatura_habitabilidad[0] <= temperatura <= temperatura_habitabilidad[1]:
            if distancia_habitabilidad[0] <= distancia <= distancia_habitabilidad[1]:
                return "El planeta si tiene una superficie habitable"
    
        if temperatura_habitabilidad[0] <= temperatura <= temperatura_habitabilidad[1]:
            if distancia_habitabilidad[0] <= distancia <= distancia_habitabilidad[1]:
                return "El planeta no tiene una superficie habitable"

    




