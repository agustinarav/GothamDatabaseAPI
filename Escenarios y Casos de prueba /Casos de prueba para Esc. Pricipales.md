## Índice para TC Esc. Principales

 
**GET** - Obtener Lista de cómics
- **TC-API-001**  Obtener todos los cómics  
- **TC-API-002**  Obtener cómic por ID 
- **TC-API-003**  Intentar obtener ID inexistente  

**POST** - Crear cómic
- **TC-API-004** Crear cómic con datos válidos  
- **TC-API-005** Crear cómic sin datos obligatorios

**PUT** - Actualizar cómic
- **TC-API-006** Actualizar existente
- **TC-API-007** Intentar actualizar uno que no existe

**DELATE** - Eliminar cómic
- **TC-API-010** Eliminar existente
- **TC-API-011** Intentar eliminar inexistente


[📄 Ver Responses](Responses.md)


--- 

| ID  TC-API-001 | **Título:** Obtener todos los cómics  |
| ------------- | ------------- |
| **Descripción** | Consulta para obtener la lista de cómics  |
| **Precondiciones**  | **Descripción** |
| 1  | La API debe estar en ejecución |
| 2  | Debe haber cómics registrados |
| **Endpoint**  |  /comics  |
| **Método HTTPP**  | GET  |
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
| **Estado**  |  Aprobado  |

---

| ID TC-API-002 | **Título:** Obtener cómic por ID  |
| ------------- | ------------- |
| **Descripción** | Consulta para obtener un cómic por su ID |
| **Precondiciones**  | **Descripción**  |
| 1 | La API debe estar en ejecución |
| 2| Debe haber cómics registrados |
| 3 | Debe haber un cómic registrado con el ID solicitado  |
| **Endpoint**  |  /comics/:id |
| **Método HTTPP**  | GET  |
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
| **Estado**  | Aprobado |

---

| ID TC-API-003 | **Título:** Intentar obtener ID inexistente  |
| ------------- | ------------- |
| **Descripción** | Consulta para obtener un cómic por un ID inexistente |
| **Precondiciones**  | **Descripción**  |
| 1 | La API debe estar en ejecución |
| 2| Debe haber cómics registrados |
| 3 | Se debe enviar un ID que no forme parte de la lista de cómics registrados  |
| **Endpoint**  |  /comics/:id |
| **Método HTTPP**  | GET  |
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
| **Estado**  | Aprobado |

