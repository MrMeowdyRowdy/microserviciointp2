from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Configuración de Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de la tabla rooms
class Room(db.Model):
    room_id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.Integer, nullable=False, unique=True)
    room_type = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)

# Inicialización de la base de datos
with app.app_context():
    db.create_all()

    # Insertar datos de prueba si no existen
    if not Room.query.first():
        sample_rooms = [
            Room(room_number=101, room_type="Single", status="available"),
            Room(room_number=102, room_type="Double", status="maintenance"),
            Room(room_number=201, room_type="Suite", status="available"),
        ]
        db.session.add_all(sample_rooms)
        db.session.commit()
        print("Datos de prueba insertados.")

# Endpoint para registrar una nueva habitación
@app.route('/rooms', methods=['POST'])
def register_room():
    data = request.json

    # Validar datos
    if not all(k in data for k in ("room_number", "room_type", "status")):
        return jsonify({"error": "Missing required fields"}), 400

    # Crear una nueva habitación
    new_room = Room(
        room_number=data['room_number'],
        room_type=data['room_type'],
        status=data['status']
    )
    db.session.add(new_room)
    db.session.commit()

    return jsonify({"message": "Room registered successfully", "room_id": new_room.room_id}), 201

# Endpoint para actualizar el estado de una habitación
@app.route('/rooms/<int:room_id>', methods=['PATCH'])
def update_room_status(room_id):
    data = request.json

    # Validar datos
    if "status" not in data:
        return jsonify({"error": "Missing 'status' field"}), 400

    # Buscar la habitación
    room = Room.query.get(room_id)
    if not room:
        return jsonify({"error": "Room not found"}), 404

    # Actualizar el estado
    room.status = data['status']
    db.session.commit()

    return jsonify({"message": "Room status updated successfully"})

# Ejecutar el servidor
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
