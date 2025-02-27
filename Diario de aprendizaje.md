## Resumen del aprendizaje sobre la API de Batman


### Métodos HTTP:
Aprendí las bases de cómo funcionan y se describen los métodos GET, POST, PUT y DELETE dentro de un Script generado en Python. Testeando la solicitud de PUT, entendí que para crear un campo extra en mi solicitud es necesario que este contemplado previamente en el código, ayudándome a entender el alcance que podría llegar a tener un tipo de prueba para esta solicitud. 

### Rutas y parámetros: 
Aprendí como las rutas (o endpoints) en Flask definen las URL a las que se puede hacer una solicitud, 
**@app.route()** define las rutas de nuestra API. Cada ruta está asociada a un método HTTP específico, como **GET, POST, PUT, DELETE**.
Por ejemplo, **/comics** para obtener todos los cómics o **/comics/<int:comic_id>** para acceder a un cómic específico por su ID. También la diferencia entre pasar un ID en la URL (**/comics/1**) y enviar datos en el cuerpo de la solicitud (body). Finalmente pude asimilar la diferencia entre endpoints, URL y parámetros opcionales.

### El uso de request y jsonify: 
El formato estándar para intercambiar datos en las APIs es JSON.  
**request.json** permite acceder al cuerpo de una solicitud HTTP en formato JSON. Se usa para obtener los datos enviados al servidor en solicitudes POST o PUT.
Ejemplo: **data = request.json** toma los datos JSON enviados en la solicitud y los convierte en un diccionario de Python.  
Después de manipular los datos, **jsonify()** convierte la respuesta de la API a formato JSON antes de enviarla a Postman. Esto garantiza que la respuesta siga el estándar JSON para que Postman pueda interpretarla correctamente.

### Variables de ruta:
Las variables de ruta son valores dinámicos en la URL, como <int:comic_id>, que permiten obtener información específica de la URL y usarla en el código.
En la ruta **/comics/<int:comic_id>**, **comic_id** es un parámetro que tomará el valor del número en la URL (como **/comics/2**), permitiendo al servidor saber qué cómic se está solicitando o actualizando.

### Errores desde el backend: 
Asociación directa entre código y request de los estados HTTP (200, 201, 400, 404, 500, etc.).
Puede analizar logs y mensajes de error directamente en la consola.
Prqueñas pruebas implementando mensajes de error más descriptivos. Por ejemplo: "El campo 'nombre' es obligatorio" en lugar de un simple "400 Bad Request".

---

#### Testing en Postman 

- **Pruebas manuales:** Comencé validando manualmente las respuestas en Postman, verificando códigos de estado y los datos devueltos. Cree un ambiente de pruebas, una collection y distintas carpetas para ordenar mis solicitudes. 

- **Pruebas automatizadas con scripts en Postman:** Exploré cómo automatizar pruebas utilizando scripts en JavaScript en la pestaña de Test. Una vez planteados mis casos de prueba y scripts corrí todos los test juntos de la collection creada para comparar resultados con las solicitudes realizadas previamente. 
