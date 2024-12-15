CREATE TABLE rooms (
    room_id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_number INTEGER NOT NULL UNIQUE,
    room_type TEXT NOT NULL,
    status TEXT NOT NULL
);

INSERT INTO rooms (room_number, room_type, status)
VALUES
(101, 'Single', 'available'),
(102, 'Double', 'maintenance'),
(201, 'Suite', 'available');
