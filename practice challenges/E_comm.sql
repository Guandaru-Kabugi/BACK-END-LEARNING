
CREATE DATABASE IF NOT EXISTS E_Commerce;

USE E_Commerce;
DROP TABLE IF EXISTS Products;
CREATE TABLE IF NOT EXISTS Products(ProductID INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(100) NOT NULL, Price DECIMAL(10,2) NOT NULL, Quantity INT NOT NULL, Unit ENUM('grams', 'liters') NOT NULL CHECK (Unit IN ('grams', 'liters')), Total DECIMAL(10,2) AS (Price * Quantity) STORED);