Pokémon Chatbot Web con SvelteKit y Flask

Este proyecto es una aplicación web que permite buscar información de Pokémon a través de la PokéAPI. Está desarrollado con un backend en Flask y un frontend en SvelteKit con TailwindCSS.

Tecnologías utilizadas

Backend: Flask (Python) con CORS habilitado

Frontend: SvelteKit con TailwindCSS

API: PokéAPI

Instalación y ejecución

1. Configurar el backend (Flask)

Requisitos previos

Python 3 instalado

pip para instalar dependencias

Pasos

Clonar el repositorio y entrar en la carpeta del backend:

git clone https://github.com/tu-repo/pokemon-chatbot.git
cd pokemon-chatbot/backend

Instalar las dependencias:

pip install flask requests flask-cors

Ejecutar el servidor Flask:

python app.py

El backend se ejecutará en http://localhost:5000

2. Configurar el frontend (SvelteKit)

Requisitos previos

Node.js y npm instalados

Pasos

Entrar en la carpeta del frontend:

cd ../frontend

Instalar las dependencias de SvelteKit:

npm install

Ejecutar el frontend:

npm run dev

Abrir el navegador en http://localhost:5173

Uso de la aplicación

Introducir el número de Pokédex en el campo de búsqueda.

Presionar el botón "Buscar".

Se mostrará el nombre, la imagen y el tipo del Pokémon consultado.

Personalización

Los estilos del frontend están basados en TailwindCSS con una escala de colores oscuros. Puedes modificar el diseño en pokemon_fetch.svelte.

Mejoras futuras

Agregar estadísticas de los Pokémon.

Implementar búsqueda por nombre.

Mejorar la interfaz con animaciones.

Añadir soporte de voz para el chatbot.

Autor

Desarrollado por [Tu Nombre].