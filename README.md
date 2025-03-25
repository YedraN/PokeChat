# Pokémon Chatbot Web con SvelteKit y Flask

Este proyecto es una aplicación web que permite buscar información de Pokémon a través de la PokéAPI. Está desarrollado con un backend en Flask y un frontend en SvelteKit con TailwindCSS.

## Tecnologías utilizadas
- **Backend:** Flask (Python) con CORS habilitado
- **Frontend:** SvelteKit con TailwindCSS
- **API:** [PokéAPI](https://pokeapi.co/)

## Instalación y ejecución

### 1. Configurar el backend (Flask)
#### Requisitos previos
- Python instalado
- `pip` para instalar dependencias

#### Pasos
1. Clonar el repositorio y entrar en la carpeta del backend:
   ```bash
   git clone https://github.com/YedraN/PokeChat.git
   cd PokeChat/backend
   ```
2. Instalar las dependencias:
   ```bash
   pip install flask requests flask-cors
   ```
3. Ejecutar el servidor Flask:
   ```bash
   python app.py
   ```
4. El backend se ejecutará en `http://localhost:5000`

### 2. Configurar el frontend (SvelteKit)
#### Requisitos previos
- Node.js y npm instalados

#### Pasos
1. Entrar en la carpeta del frontend:
   ```bash
   cd ../frontend
   ```
2. Instalar las dependencias de SvelteKit:
   ```bash
   npm install
   ```
3. Ejecutar el frontend:
   ```bash
   npm run dev
   ```
4. Abrir el navegador en `http://localhost:5173`

## Uso de la aplicación
1. Introducir el número de Pokédex en el campo de búsqueda.
2. Presionar el botón "Buscar".
3. Se mostrará el nombre, la imagen y el tipo del Pokémon consultado.

## Personalización
Los estilos del frontend están basados en TailwindCSS con una escala de colores oscuros. Puedes modificar el diseño en `pokemon_fetch.svelte`.

## Mejoras futuras
- Agregar estadísticas de los Pokémon.
- Implementar búsqueda por nombre.
- Mejorar la interfaz con animaciones.

## Autor
Desarrollado por Juanjo Yedra.
