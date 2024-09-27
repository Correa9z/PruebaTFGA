CREATE DATABASE pruebaT;

USE DATABASE pruebaT;


CREATE TABLE departamentos(
    id int AUTO_INCREMENT,
    nombre varchar(100) UNIQUE,
    PRIMARY KEY(id),
);

CREATE TABLE empleados(
    id int AUTO_INCREMENT,
    nombre varchar(100),
    identificacion varchar(100) UNIQUE,
    departamento_id int,
    PRIMARY KEY(id),
    FOREIGN KEY(departamento_id) REFERENCES(departamentos(id))  
);

CREATE TABLE proyectos(    
    id int AUTO_INCREMENT,
    nombre varchar(100) UNIQUE,
    empleado_id int,
    PRIMARY KEY(id),
    FOREIGN KEY(departamento_id) REFERENCES(departamentos(id))  
);