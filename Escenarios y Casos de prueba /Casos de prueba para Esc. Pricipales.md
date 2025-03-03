## Índice para TC Esc. Principales

| **Título** | **GET** |
| ------------- | ------------- |
| **TC-API-001** | Obtener cómics  |
| **TC-API-002** | Obtener cómic por ID |
| **TC-API-003**  | Intentar obtener ID inexistente  |

---

| ID  | TC-API-001 |
| ------------- | ------------- |
| **Título** | Obtener cómics  |
| **Descripción** | Consulta para obtener la lista de cómics  |
| **Precondiciones**  | La API debe estar en ejecución y debe haber cómics registrados |
| **Endpoint**  |  /comics  |
| **Método HTTPP**  | GET  |
| **Headers**  |   |
| **Curl**  |   |
| **Body (JSON)**  | -  |
| **Datos de entrada** | -|
| **Pasos** | **Descripción** |
| 1 | Enviar GET /comics/1 |
| 2 | Verificar que el código de respuesta sea 200 OK |
| 3 | Validar que los datos de los cómic en la BDD retornados sean correctos para: id, title, author, year|
| **Respuesta esperada**  | Código 200 OK, JSON |
| **Respuesta obtenida**  |  |
| **Estado**  |   |

