# Clases Astrofísicas

Este repositorio contiene clases Python para modelar objetos astrofísicos como estrellas, planetas y sistemas planetarios. Estas clases son útiles para realizar cálculos y simulaciones relacionadas con la astronomía y la astrofísica.

## Clase Estrella

La clase `Estrella` modela una estrella y proporciona métodos para calcular propiedades como luminosidad, radio de Schwarzschild y clasificación espectral.

### Atributos:

- `nombre` (str): El nombre de la estrella.
- `masa` (float): La masa de la estrella en kilogramos.
- `radio` (float): El radio de la estrella en metros.
- `temperatura` (float): La temperatura efectiva de la estrella en Kelvin.
- `distancia` (float): La distancia de la estrella a la Tierra en parsecs.
- `movimiento_propio` (float): El movimiento propio de la estrella en segundos de arco por año.

### Métodos:

- `luminosidad_total()`: Calcula la luminosidad total de la estrella en vatios.
- `luminosidad_secuencia_principal()`: Calcula la luminosidad de la secuencia principal de la estrella, comparada con el Sol.
- `radio_schwarzschild()`: Calcula y devuelve el radio de Schwarzschild de la estrella.
- `clasificacion_espectral()`: Clasifica la estrella de acuerdo a la Clasificación Espectral.

### Clasificación Espectral:

La clasificación espectral separa las estrellas de acuerdo a su temperatura:

| Clase | Temperatura (K) | Color             |
|-------|------------------|-------------------|
| O     | 30,000 - 60,000  | Estrellas azules  |
| B     | 10,000 - 30,000  | Estrellas azules-blancas |
| A     | 7,500 - 10,000   | Estrellas blancas |
| F     | 6,000 - 7,500    | Estrellas amarillas-blancas |
| G     | 5,000 - 6,000    | Estrellas amarillas (como el Sol) |
| K     | 3,500 - 5,000    | Estrellas amarillas-naranjas |
| M     | < 3,500          | Estrellas rojas    |

## Clase Planeta

La clase `Planeta` modela un planeta y proporciona métodos para calcular propiedades como el período de rotación kepleriana y la densidad.

### Atributos:

- `estrella_anfitriona` (Estrella): La estrella anfitriona alrededor de la cual orbita el planeta.
- `masa_planetaria` (float): La masa del planeta en kilogramos.
- `radio` (float): El radio del planeta en metros.
- `a` (float): El semieje mayor de la órbita del planeta en metros.
- `inclinacion` (float): La inclinación orbital del planeta en grados.
- `excentricidad` (float): La excentricidad orbital del planeta.
- `argumento_periastron` (float): El argumento del periastron del planeta en grados.

### Métodos:

- `periodo_rotacion_kepleriana(G)`: Calcula el período de rotación kepleriana del planeta.
- `densidad_y_flotabilidad()`: Calcula la densidad del planeta y verifica si flotaría en el agua de la Tierra.
- `superficie_habitable()`: Determina si el planeta tiene una superficie habitable en función de su temperatura y distancia a su estrella.

## Clase PlanetaExoplanetario

La clase `PlanetaExoplanetario` hereda de la clase `Planeta` y agrega métodos para determinar el método de descubrimiento y si el planeta es similar a Tatooine.

### Atributos:

- `estrella_anfitriona` (Estrella): La estrella anfitriona alrededor de la cual orbita el planeta exoplanetario.
- `masa_planetaria` (float): La masa del planeta exoplanetario en kilogramos.
- `radio` (float): El radio del planeta exoplanetario en metros.
- `a` (float): El semieje mayor de la órbita del planeta exoplanetario en metros.
- `inclinacion` (float): La inclinación orbital del planeta exoplanetario en grados.
- `excentricidad` (float): La excentricidad orbital del planeta exoplanetario.
- `argumento_periastron` (float): El argumento del periastron del planeta exoplanetario en grados.

### Métodos:

- `periodo_rotacion_kepleriana(G)`: Calcula el período de rotación kepleriana del planeta exoplanetario.
- `densidad_y_flotabilidad()`: Calcula la densidad del planeta exoplanetario y verifica si flotaría en el agua de la Tierra.
- `superficie_habitable()`: Determina si el planeta exoplanetario tiene una superficie habitable en función de su temperatura y distancia a su estrella.
- `metodo_descubrimiento(metodo)`: Determina el método de primer descubrimiento del planeta exoplanetario, ya sea por "imagen directa", "velocidad radial" o "tránsito".
- `tatooine()`: Determina si el planeta exoplanetario es similar a Tatooine, es decir, si orbita alrededor de una estrella binaria.

## Clase SistemaJerarquico

La clase `SistemaJerarquico` modela un sistema de estrellas jerárquico y proporciona métodos para operar con ellas, como ordenarlas por masa y asignarles letras del alfabeto.

### Atributos:

- `estrellas` (list): Una lista de objetos de la clase Estrella que componen el sistema jerárquico.

### Métodos:

- `estrellas_ordenadas_por_masa()`: Devuelve la lista de estrellas ordenadas por su masa estelar.
- `nombres_con_letras_del_alfabeto()`: Imprime los nombres de las estrellas seguidos de letras del alfabeto.

## Clase SistemaPlanetario

La clase `SistemaPlanetario` modela un sistema planetario y proporciona métodos para operar con los planetas en él, como contar el número de planetas y ordenarlos por su radio semi-mayor de la órbita.

### Atributos:

- `planetas` (list): Una lista de objetos de la clase Planeta que componen el sistema planetario.

### Métodos:

- `numero_planetas()`: Devuelve el número de planetas en el sistema planetario.
- `planetas_ordenados_por_radio()`: Devuelve la lista de planetas ordenada por su radio semi-mayor de la órbita 'a'.


