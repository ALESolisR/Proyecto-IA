#crea entorno virtual
C:\Users\XCPC\Desktop\pasantia\semana0_alejandro_solis>python -m venv env

#activar entorno virtual
C:\Users\XCPC\Desktop\pasantia\semana0_alejandro_solis>.\env\Scripts\activate

#instala librerias necesarias
(env) C:\Users\XCPC\Desktop\pasantia\semana0_alejandro_solis>pip install fastapi uvicorn requests python-dotenv ollama
Collecting fastapi

(env) C:\Users\XCPC\Desktop\pasantia\semana0_alejandro_solis>curl http://localhost:11434
Ollama is running

(env) C:\Users\XCPC\Desktop\pasantia\semana0_alejandro_solis>ollama run deepseek-r1

#ejecutar el servidor puerto 8000
PS C:\Users\XCPC\Desktop\pasantia\semana0_alejandro_solis> uvicorn app.main:app --reload

*******************************************************************************************************************
# DESCRIPCION DE TECNOLOGIAS UTILIZADAS
    Este proyecto utiliza herramientas y tecnologias coo Python y FastApi para crear una API de manera eficiente para crear un backend que va a interactuar con un modelo de IA, para el cual se usa ollama para manejar el modelo de IA deepseek-r1.

    tambien se utiliza Postman para poder realizar pruebas mediante solicitudes HTTP como: get y post a la API.

    Python 3.13
    Descripción: Python es un lenguaje de programación versátil y muy utilizado en el desarrollo de aplicaciones de inteligencia artificial. La versión 3.13 incluye mejoras en la eficiencia y nuevas características.

    Ollama
    Descripción: Ollama es una herramienta diseñada para gestionar y ejecutar modelos de inteligencia artificial de manera simplificada. Permite interactuar fácilmente con modelos pre-entrenados.

    Modelo deepseek-r1
    Descripción: Este modelo está optimizado para tareas específicas de procesamiento de lenguaje natural. Es ideal para empezar a trabajar con modelos de IA sin complicaciones.

    Postman
    Descripción: Postman es una herramienta fundamental para probar APIs. Permite enviar solicitudes HTTP y analizar respuestas de una manera intuitiva.

    Librerías Necesarias
   
    Descripción de Librerías:
    • FastAPI: Framework para construir APIs de alta eficiencia.
    • Uvicorn: Servidor ASGI para ejecutar tu aplicación FastAPI.
    • Requests: Librería para realizar solicitudes HTTP.
    • Python-dotenv: Permite trabajar con archivos .env para gestionar variables de entorno.
    • Ollama: Herramienta para ejecutar modelos de IA localmente.

# COMO CONFIGURAR Y EJECUTAR ESTE PROYECTO

# paso 1 iniciar el emtorno virtual o crearlo
python -m venv env
.\env\Scripts\activate

# paso 2 instalar las librerias, las mismas estaran enlazadas al entorno virtual creado y no de manera general, solo se realiza una vez
pip install fastapi uvicorn requests python-dotenv ollama

Descripción de Librerías:
•
FastAPI: Framework para construir APIs de alta eficiencia.
•
Uvicorn: Servidor ASGI para ejecutar tu aplicación FastAPI.
•
Requests: Librería para realizar solicitudes HTTP.
•
Python-dotenv: Permite trabajar con archivos .env para gestionar variables de entorno.
•
Ollama: Herramienta para ejecutar modelos de IA localmente.

# ollama se ejecuta en segundo plano, en cmd se puede comprobar se esta running, sino activarlo con: ollama run deepseek-r1

# paso 3 iniciar la aplicacion para poder ejecutar la api con: uvicorn app.main:app --reload

# iniciar postman y hacer pruebas

# INVESTIGACION Y APRENDIZAJE

1 ¿Qué es Ollama?
    Este programa te permite instalar modelos de inteligencia artificial en tu ordenador y usarlos de forma local sin conectarte a Internet. Se trata de un cliente de modelos de inteligencia artificial, por lo que es la base sobre la que luego instalar una IA que quieras utilizar.

2 ¿Qué es FastAPI?
    FastAPI es un framework web de Python que permite crear APIs de forma rápida y sencilla. Es uno de los frameworks de Python más rápidos y se considera una herramienta ideal para el backend de aplicaciones web.

3 ¿Qué es el modelo deepseek-r1?
    DeepSeek R1 es un modelo de inteligencia artificial (IA) de código abierto que resuelve problemas complejos, toma decisiones y razona. Fue desarrollado por la empresa china DeepSeek

4 Uso de peticiones con stream=True
    Las peticiones con streaming son solicitudes de larga duración que permiten enviar datos y recibir resultados en tiempo real. Se utilizan en aplicaciones web y móviles para proporcionar información actualizada a los usuarios

5 ¿Cómo garantizar la escalabilidad de una API que consume modelos de IA pesados?
    La escalabilidad es la capacidad de una API para manejar cantidades crecientes de tráfico y solicitudes sin comprometer el rendimiento, la confiabilidad o la funcionalidad. Es un factor crucial para cualquier API que tenga como objetivo servir a una base de usuarios grande y diversa, admitir múltiples plataformas y dispositivos, y adaptarse a las necesidades cambiantes del negocio y las demandas del mercado. En este artículo, aprenderá algunas de las mejores prácticas para garantizar la escalabilidad de la API, como el diseño para la flexibilidad, la implementación del almacenamiento en caché, la aplicación de límites de velocidad, la supervisión y las pruebas, y el aprovechamiento de los servicios en la nube.
    * diseno y flexibilidad
    * almacenamiento en cache
    * limitacion de velocidad
    * supervision y pruebas
    * aprovechar servicios en la nube

    Referencia: https://es.linkedin.com/advice/1/what-best-practices-ensuring-api-scalability-skills-programming?lang=es

6 ¿Qué parámetros de Ollama (ej: num_ctx, temperature) afectan el rendimiento/calidad de respuestas?
    Para mejorar la calidad de las respuestas, se puede experimentar principalmente con parametros como: temperature, num_ctx, top_p, y top_k.

    Para mejorar el rendimiento, se debe considerar el tamaño del modelo, la cuantización, el uso de GPU, se pueden ajustar parametros como: num_ctx según los recursos. Las variables de entorno del servidor también son importantes para optimizar el manejo de múltiples solicitudes.

7 ¿Qué estrategias usar para balancear carga entre múltiples instancias de Ollama?
    Para balancear carga en Ollama:

    Estrategias: Usa Round Robin (simple), Least Connections (mejor distribución), Least Response Time (basado en rendimiento), IP Hash (sesiones del cliente), o balanceo basado en Peso (para instancias con diferente capacidad).

    Implementación: Necesitas un balanceador de carga como Nginx, HAProxy, Traefik o servicios en la nube. En Kubernetes, usa Ingress.

    Importante: Configura verificaciones de salud para evitar enviar tráfico a instancias fallidas. Considera la persistencia de sesión y el escalado automático. Monitorea el rendimiento.

8 ¿Qué patrones de diseño (ej: CQRS, Singleton) son útiles para integrar modelos de IA en backend?

    Para integrar modelos de IA en backend, usa patrones como:

    CQRS: Separa lectura (inferencia) de escritura (entrenamiento) para escalar y optimizar cada parte.

    Microservicios: Aísla la IA en un servicio independiente para escalabilidad y mantenimiento.

    EDA: Comunicación por eventos para desacoplamiento y procesamiento asíncrono.

    Caching: Guarda resultados de inferencia para mejorar la velocidad.

    Procesamiento Asíncrono: Usa colas para tareas de inferencia largas.

    Adapter/Strategy: Facilita el uso de diferentes modelos con interfaces consistentes.