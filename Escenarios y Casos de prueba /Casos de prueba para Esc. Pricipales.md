## Índice para TC Esc. Principales

 
**GET** - Obtener Lista de cómics
- **TC-API-001**  Obtener todos los cómics  
- **TC-API-002**  Obtener cómic por ID 
- **TC-API-003**  Intentar obtener ID inexistente  

**POST** - Crear cómic
- **TC-API-004** Crear cómic con datos válidos  
- **TC-API-005** Crear cómic con datos obligatorios vacíos
- **TC-API-006** Crear cómic con parámetros del cuerpo no incluídos en el código

**PUT** - Actualizar cómic
- **TC-API-** Actualizar existente
- **TC-API-** Intentar actualizar uno que no existe

**DELATE** - Eliminar cómic
- **TC-API-** Eliminar existente
- **TC-API-** Intentar eliminar inexistente


[📄 Ver Responses](https://github.com/agustinarav/GothamDatabaseAPI/blob/main/Escenarios%20y%20Casos%20de%20prueba%20/Responses)



--- 

| ID  TC-API-001 | **Título:** Obtener todos los cómics  |
| ------------- | ------------- |
| **Método HTTPP**  | GET  |
| **Descripción** | Consulta para obtener la lista de cómics  |
| **Precondiciones**  | **Descripción** |
| 1  | La API debe estar en ejecución |
| 2  | Debe haber cómics registrados |
| **Endpoint**  |  /comics  |
| **Headers**  | Content-Type: application/json, Content-Length: 405  |
| **Curl**  |   |
| **Body (JSON)**  | No requerido  |
| **Datos de entrada** | No requerido |
| **Pasos** | **Descripción** |
| 1 | Enviar GET /comics |
| 2 | Verificar que el código de respuesta sea 200 OK |
| 3 | Validar que los datos de los cómic en la BDD retornados sean correctos para: id, title, author, year|
| **Respuesta esperada**  | Código 200 OK, JSON |
| **Respuesta obtenida**  | 200 OK  |
| **Estado**  |  **APROBADO**  |

---

| ID TC-API-002 | **Título:** Obtener cómic por ID  |
| ------------- | ------------- |
| **Método HTTPP**  | GET  |
| **Descripción** | Consulta para obtener un cómic por su ID |
| **Precondiciones**  | **Descripción**  |
| 1 | La API debe estar en ejecución |
| 2| Debe haber cómics registrados |
| 3 | Debe haber un cómic registrado con el ID solicitado  |
| **Endpoint**  |  /comics/:id |
| **Headers**  | Content-Type: application/json, Content-Length:115 |
| **Curl**  | -  |
| **Body (JSON)**  | -  |
| **Datos de entrada** | ID: 1 |
| **Pasos** | **Descripción** |
| 1 | Enviar GET /comics/1 |
| 2 | Verificar que el código de respuesta sea 200 OK |
| 3 | Validar que los datos  del cómic con ID 1 en la BDD retornados sean correctos para: id, title, author, year|
| **Respuesta esperada**  | 200 OK  |
| **Respuesta obtenida**  | 200 OK |
| **Estado**  | **APROBADO** |

---

| ID TC-API-003 | **Título:** Intentar obtener ID inexistente  |
| ------------- | ------------- |
| **Método HTTPP**  | GET  |
| **Descripción** | Consulta para obtener un cómic por un ID inexistente |
| **Precondiciones**  | **Descripción**  |
| 1 | La API debe estar en ejecución |
| 2| Debe haber cómics registrados |
| 3 | Se debe enviar un ID que no forme parte de la lista de cómics registrados  |
| **Endpoint**  |  /comics/:id |
| **Headers**  | Content-Type: application/json, Content-Length:33 |
| **Curl**  | -  |
| **Body (JSON)**  | -  |
| **Datos de entrada** | ID: 5 |
| **Pasos** | **Descripción** |
| 1 | Enviar GET /comics/5 |
| 2 | Verificar que el código de respuesta sea 404 NOT FOUND |
| 3 | Validar que la respuesta para el cómic con ID 5 es {"error": "Comic not found"}|
| **Respuesta esperada**  | 404 NOT FOUND |
| **Respuesta obtenida**  | 404 NOT FOUND |
| **Estado**  | **APROBADO** |

---

| ID TC-API-004 | **Título:** Crear un nuevo cómic en la API  |
| ------------- | ------------- |
| **Método HTTPP**  | POST  |
| **Descripción** | Crear un nuevo cómic en la API |
| **Precondiciones**  | **Descripción**  |
| 1 | La API debe estar en ejecución |
| 2|  Cada campo enviado debe estar contemplado en el código (title, author, year,etc)  |
| **Endpoint**  |  /comics |
| **Headers**  | Content-Type: application/json, Content-Length:	145 |
| **Curl**  | -  |
| **Body (JSON)**  | {"title": "The Long Halloween","author": "Jeph Loeb","year": 1996}    |
| **Datos de entrada** | title: The Long Halloween, author: Jeph Loeb, year: 1996  |
| **Pasos** | **Descripción** |
| 1 | Enviar POST/comics con body |
| 2 | Verificar que el código de respuesta sea 201 CREATED |
| 3 | Validar el parámetro "message": "Comic added"|
| **Respuesta esperada**  | 201 CREATED |
| **Respuesta obtenida**  | 201 CREATED |
| **Estado**  | **APROBADO** |

---

| ID TC-API-005 | **Título:** Crear cómic con datos obligatorios vacíos  |
| ------------- | ------------- |
| **Método HTTPP**  | POST  |
| **Descripción** | Crear cómic con datos obligatorios vacíos |
| **Precondiciones**  | **Descripción**  |
| 1 | La API debe estar en ejecución |
| 2|  Cada campo debe estar contemplado en el código (title, author, year,etc)  |
| **Endpoint**  |  /comics |
| **Headers**  | Content-Type: text/html; charset=utf-8, Content-Length:188 |
| **Curl**  | -  |
| **Body (JSON)**  | {"title": "The Long Halloween","author": "Jeph Loeb","year":  }    |
| **Datos de entrada** | title: The Long Halloween, author: Jeph Loeb, year:   |
| **Pasos** | **Descripción** |
| 1 | Enviar POST/comics con body y campo year vacío |
| 2 | Verificar que el código de respuesta sea 400 BAD REQUEST |
| 3 | Verificar msj: Failed to decode JSON object: Expecting value: line 5 column 5 (char 90) |
| **Respuesta esperada**  | 400 BAD REQUEST |
| **Respuesta obtenida**  | 400 BAD REQUEST |
| **Estado**  | **APROBADO** |

---

| ID TC-API-006 | **Título:** Crear cómic con parámetros del cuerpo no incluídos en el código |
| ------------- | ------------- |
| **Método HTTPP**  | POST  |
| **Descripción** | Crear cómic con parámetros del cuerpo no incluídos en el código |
| **Precondiciones**  | **Descripción**  |
| 1 | La API debe estar en ejecución |
| 2|  Se debe sumar un campo NO contemplado en el código  |
| **Endpoint**  |  /comics |
| **Headers**  | Content-Type: application/json, Content-Length:	145 |
| **Curl**  | -  |
| **Body (JSON)**  | {"title": "The Long Halloween","author": "Jeph Loeb","year": 1996, "Prueba": 123  }    |
| **Datos de entrada** | title: The Long Halloween, author: Jeph Loeb, year: 1996, Prueba: 123   |
| **Pasos** | **Descripción** |
| 1 | Enviar POST/comics con body y campo adicional Prueba:123 |
| 2 | Verificar que el código de respuesta sea 400 BAD REQUEST |
| 3 | Verificar  "error": "Campos no permitidos: genre", al enviar un campo que no está permitido. |
| 4 | Verificar  si éste error está contemplado en el código. |
| **Respuesta esperada**  | 400 BAD REQUEST |
| **Respuesta obtenida**  | 201 CREATED |
| **Estado**  | **DESAPROBADO**|



