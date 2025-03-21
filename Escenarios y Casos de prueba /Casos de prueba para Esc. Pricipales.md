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
- **TC-API-007** Actualizar parámetro existente por ID de cómic
- **TC-API-008** Actualizar un cómic con ID no existente


**DELATE** - Eliminar cómic
- **TC-API- 009** Eliminar cómic existente
- **TC-API-010** Intentar eliminar cómic inexistente


[📄 Ver Responses JSON para:](https://github.com/agustinarav/GothamDatabaseAPI/blob/main/Escenarios%20y%20Casos%20de%20prueba%20/Responses)

-Obtener lista de cómics  
-Obtener un cómic por ID  
-Crear cómic con datos válidos  
-Actualizar cómic  
-Eliminar cómic  


--- 

| ID  TC-API-001 | **Título:** Obtener todos los cómics  |
| ------------- | ------------- |
| **Método HTTP**  | GET  |
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
| **Método HTTP**  | GET  |
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
| **Método HTTP**  | GET  |
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
| **Método HTTP**  | POST  |
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
| **Método HTTP**  | POST  |
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
| **Método HTTP**  | POST  |
| **Descripción** | Crear cómic con parámetros en el cuerpo que no estén permitidos en el código |
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

---

| ID TC-API-007 | **Título:** Actualizar un parámetro de un cómic existente por su ID |
| ------------- | ------------- |
| **Método HTTP**  | PUT  |
| **Descripción** | Actualizar un parámetro de un cómic utilizando solo los campos permitidos en el código. |
| **Precondiciones**  | **Descripción**  |
| 1 | La API debe estar en ejecución |
| 2|  Se debe elegir un parámetro existente (title, author, year)  |
| 3|  Se debe modificar la información de uno o varios parámetros (title, author, year)  |
| **Endpoint**  |  /comics/:id |
| **Headers**  | Content-Type: application/json, Content-Length:	141|
| **Curl**  | -  |
| **Body (JSON)**  | { "author": "Grant Morrison", "id": 3,"title": "Arkham Asylum: A Serious House on Serious Earth","year": 1988} |
| **Datos de entrada** | author: Grant Morrison, title: prueba1, year: 2000  |
| **Pasos** | **Descripción** |
| 1 | Enviar PUT /comics/3 con body y datos de actualización |
| 2 | Verificar que el código de respuesta sea 200 OK |
| 3 | Enviar GET /comics/3 para verificar si el cómic fue actualizado|
| **Respuesta esperada**  | 200 OK |
| **Respuesta obtenida**  | 200 OK |
| **Estado**  | **APROBADO** |

---

| ID TC-API-008 | **Título:** Actualizar un cómic con ID no existente |
| ------------- | ------------- |
| **Método HTTP**  | PUT  |
| **Descripción** | Actualizar un cómic con ID no existente |
| **Precondiciones**  | **Descripción**  |
| 1 | La API debe estar en ejecución |
| 2|  Se debe elegir un ID inexistente en la BDD para realizar la solicitud |
| **Endpoint**  |  /comics/:id |
| **Headers**  | Content-Type: application/json, Content-Length:	33|
| **Curl**  | -  |
| **Body (JSON)**  | { "author": "Grant Morrison", "id": 3,"title": "Arkham Asylum: A Serious House on Serious Earth","year": 1988} |
| **Request** | /comics/7 |
| **Datos de entrada** | author: Grant Morrison, id: 3,title:Arkham Asylum: A Serious House on Serious Earth,year: 1988 |
| **Pasos** | **Descripción** |
| 1 | Enviar PUT /comics/7 con body y datos de actualización |
| 2 | Verificar que el código de respuesta sea 404 NOT FOUND|
| 3 | Verificar que no se han realizado cambios en ningún comic con la solicitud|
| **Respuesta esperada**  | 404 NOT FOUND |
| **Respuesta obtenida**  | 404 NOT FOUND |
| **Estado**  | **APROBADO** |

---

| ID  TC-API-009 | **Título: Eliminar cómic existente **  |
| ------------- | ------------- |
| **Descripción** | Eliminar cómic existente de la BDD |
| **Precondiciones**  | **Descripción** |
| 1  | La API debe estar en ejecución |
| 2  | Debe haber cómics registrados |
| 3  | El ID del cómic debe formar parte de la lista de cómics en la BDD |
| **Endpoint**  |  /comics/:id  |
| **Método HTTP**  |  DELATE  |
| **Headers**  | Content-Type: application/json, Content-Length: 46  |
| **Curl**  |   |
| **Body (JSON)**  |  - |
| **Datos de entrada** | - |
| **Pasos** | **Descripción** |
| 1 | Enviar DELATE /comics/3 |
| 2 | Verificar que el código de respuesta sea 200 OK |
| 3 |  Validar que la respuesta para el cómic con ID 3 es "message": "Comic deleted successfully"|
| **Respuesta esperada**  | 200 OK  |
| **Respuesta obtenida**  |  200 OK   |
| **Estado**  | **APROBADO**   |

---

| ID  TC-API-010 | **Título: Intentar eliminar cómic inexistente**  |
| ------------- | ------------- |
| **Descripción** | Eliminar cómic con ID inexistente de la BDD |
| **Precondiciones**  | **Descripción** |
| 1  | La API debe estar en ejecución |
| 2  | Debe haber cómics registrados |
| 3  | El ID del cómic NO debe formar parte de la lista de cómics en la BDD |
| **Endpoint**  |  /comics/:id  |
| **Método HTTP**  |  DELATE  |
| **Headers**  | Content-Type: application/json, Content-Length: 46  |
| **Curl**  |   |
| **Body (JSON)**  |  - |
| **Datos de entrada** | - |
| **Pasos** | **Descripción** |
| 1 | Enviar DELATE /comics/3 |
| 2 | Verificar que el código de respuesta sea 404 NOT FOUND |
| 3 |  Validar que la respuesta para el cómic con ID 3 es "message": "error": "Comic not found"|
| **Respuesta esperada**  | 404 NOT FOUND  |
| **Respuesta obtenida**  |  404 NOT FOUND  |
| **Estado**  | **APROBADO**   |
