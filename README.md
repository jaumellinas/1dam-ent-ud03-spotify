# Spotify (Python)
![Captura de la aplicación](https://i.ibb.co/20T90s7x/Captura-de-pantalla-2025-03-08-a-las-18-36-38.png)
Este proyecto pretende ser una biblioteca de canciones que almacena datos como su ID, su título, su artista, su duración y su link de YouTube para su posterior reproducción. 

Hecho por Jaume Llinàs, Andrés Urriola y Alex Bascuñana, alumnos de 1º de DAM de Sant Josep Obrer para la asignatura de Entornos de desarrollo, dónde hemos estado trasteando con plantillas de Jinja y bases de datos SQLite. 

## Endpoints
Esta app funciona con los siguientes endpoints: 

 - **/** (GET) -- página principal. Muestra todas las canciones.
 - **/canciones/add** (GET y POST) -- formulario para añadir canciones a la base de datos.
	 - El endpoint contiene un pequeño rewrite para adaptar los links de YouTube que se le introducen al método "embed", necesario para luego poder reproducir las canciones correctamente.
- **/canciones/get** (GET y POST) -- formulario para buscar canciones por ID.
- **/canciones/delete/\<int:cancion_id\>** (POST) -- permite eliminar X canción por su ID.
- **/canciones/edit/\<int:cancion_id\>** (POST) -- permite editar X canción por su ID.
- **/play/\<int:cancion_id\>** (GET) -- permite reproducir X canción por su ID.

## Demo
La app (con ciertos ajustes adaptados a Vercel) está disponible para probarla [en este link](https://spotify-python.vercel.app).
