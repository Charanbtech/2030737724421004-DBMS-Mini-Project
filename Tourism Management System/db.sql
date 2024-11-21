CREATE DATABASE tourism_db;

USE tourism_db;

CREATE TABLE tourist_spots (
    spot_id INT AUTO_INCREMENT PRIMARY KEY,  -- Spot ID
    name VARCHAR(100) NOT NULL,              -- Spot Name
    location VARCHAR(100) NOT NULL,          -- Spot Location
    description TEXT NOT NULL                -- Spot Description
);

INSERT INTO tourist_spots (name, location, description)
VALUES 
('Eiffel Tower', 'Paris, France', 'An iconic wrought-iron lattice tower in Paris.'),
('Grand Canyon', 'Arizona, USA', 'A magnificent canyon with layered red rock formations.'),
('Great Wall of China', 'China', 'A historic wall stretching thousands of miles.'),
('Taj Mahal', 'Agra, India', 'A white marble mausoleum and UNESCO World Heritage Site.'),
('Sydney Opera House', 'Sydney, Australia', 'A world-famous performing arts center with unique architecture.');

SELECT * FROM tourist_spots;
