# Gestor de Enlaces (Link Shortener)

Este es un proyecto de un gestor de enlaces (link shortener) que permite a los usuarios acortar URLs largas y obtener enlaces cortos personalizados.

## Funcionalidades Principales

*   **Generar Enlaces Cortos:** Los usuarios pueden introducir una URL larga y obtener una URL corta correspondiente.
*   **Enlaces Personalizados (Opcional):** Los usuarios pueden personalizar la parte final de la URL corta (opcional).
*   **Redirección:** Al acceder a una URL corta, el usuario es redirigido a la URL original.

## Tecnologías Utilizadas

*   **Frontend:**
    *   HTML5
    *   CSS3
    *   JavaScript
*   **Backend:**
    *   Python 3.10+
    *   Flask
    *   Flask-CORS
    *   SQLite3

## Estructura del Proyecto
shorter-url-saas/
├── .venv/ # Entorno virtual
├── backend/ # Carpeta para el backend
│ ├── app.py # Script principal de Flask
│ ├── requirements.txt # Dependencias del backend
│ ├── schema.sql # Script SQL de la base de datos
│ └── links.db # Base de datos SQLite
├── frontend/ # Carpeta para el frontend
│ ├── index.html # Archivo principal del frontend
│ ├── script.js # Código JavaScript
│ └── style.css # Estilos CSS
├── README.md # Documentación del proyecto
└── .gitignore # Archivo para ignorar archivos en git


## Configuración y Ejecución

### Configuración del Entorno

1.  **Clona el repositorio:**
    ```bash
    git clone <URL_del_repositorio>
    cd <nombre_del_repositorio>
    ```
2.  **Crea un entorno virtual:**
    ```bash
    python -m venv .venv
    ```
3.  **Activa el entorno virtual:**
    *   **Windows:**
        ```bash
        .\.venv\Scripts\activate
        ```
    *   **macOS/Linux:**
        ```bash
        source .venv/bin/activate
        ```
4.  **Instala las dependencias del backend:**
    ```bash
    cd backend
    pip install -r requirements.txt
    ```

### Ejecución del Proyecto

1.  **Ejecuta el backend (API):**
    ```bash
    cd backend
    python app.py
    ```
    El backend se iniciará en `http://127.0.0.1:5000/`

2.  **Abre el frontend (interfaz de usuario) en un navegador:**
    *   Abre el archivo `index.html` que se encuentra en la carpeta `frontend` directamente en tu navegador.
   *   O Utiliza un servidor web (como `python -m http.server`) en la carpeta `frontend`.
   *    Y accede a tu página desde el navegador.

### Despliegue

#### Frontend
* Utiliza GitHub Pages, Vercel o Netlify para desplegar tu frontend.

#### Backend
* Utiliza Railway o Heroku para desplegar tu backend.

## Próximas Funcionalidades

*   Implementar un sistema de autenticación para los usuarios.
*   Añadir estadísticas de clics para cada enlace.
*   Implementar la posibilidad de eliminar los enlaces.
*   Mejorar la gestión de errores.
*   Mejorar la interfaz de usuario.

## Créditos

*   Este proyecto ha sido creado por \[Tu Nombre].

## Licencia

*   Este proyecto no está bajo ninguna licencia. Puedes utilizar este código siempre que des crédito.