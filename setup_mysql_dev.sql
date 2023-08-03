-- prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS "hbnb_dev"@"localhost" IDENTIFIED BY "hbnb_dev_pwd";
--  los privilegios se aplicarán a todas las tablas y objetos dentro de la base de datos llamada "hbnb_dev_db"
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO "hbnb_dev"@"localhost";
GRANT SELECT ON performance_schema.* TO "hbnb_dev"@"localhost";