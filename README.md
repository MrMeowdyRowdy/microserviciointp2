Para ejecutar esta aplicación realiza los siguientes comandos en la carpeta de la aplicación

docker build -t inventory-service .

docker run -d -p 5002:5002 --name inventory-container inventory-service

Pruebas
Registrar Habitación:

Endpoint: POST http://localhost:5002/rooms
Ejemplo de solicitud:
json
Copiar código
{
  "room_number": 301,
  "room_type": "Single",
  "status": "available"
}


Actualizar Estado de Habitación:

Endpoint: PATCH http://localhost:5002/rooms/{room_id}
Ejemplo de solicitud:
json
Copiar código
{
  "status": "maintenance"
}
