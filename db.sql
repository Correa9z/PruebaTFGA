-- Creación de la base de datos
CREATE DATABASE pruebaT;

-- Referencia/uso de la base de datos
USE pruebaT;

-- Creación de la tabla departamentos
CREATE TABLE departamentos(
    id INT AUTO_INCREMENT,
    nombre VARCHAR(100) UNIQUE,
    PRIMARY KEY(id)
);

-- Creación de la tabla empleados
CREATE TABLE empleados(
    id INT AUTO_INCREMENT,
    nombre VARCHAR(100),
    identificacion VARCHAR(100) UNIQUE,
    departamento_id INT,
    PRIMARY KEY(id),
    FOREIGN KEY(departamento_id) REFERENCES departamentos(id)  
);

-- Creación de la tabla proyectos
CREATE TABLE proyectos(    
    id INT AUTO_INCREMENT,
    nombre VARCHAR(100) UNIQUE,
    empleado_id INT,
    PRIMARY KEY(id),
    FOREIGN KEY(empleado_id) REFERENCES empleados(id)  
);