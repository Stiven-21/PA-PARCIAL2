-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         5.7.33 - MySQL Community Server (GPL)
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para parcial2
CREATE DATABASE IF NOT EXISTS `parcial2` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `parcial2`;

-- Volcando estructura para tabla parcial2.archivos
CREATE TABLE IF NOT EXISTS `archivos` (
  `id_archivo` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_usuario` bigint(20) DEFAULT NULL,
  `nombre_archivo` varchar(255) DEFAULT NULL,
  `ruta_archivo` varchar(500) DEFAULT NULL,
  `ruta_vista` varchar(500) DEFAULT NULL,
  `type` varchar(500) DEFAULT NULL,
  `size` varchar(20) DEFAULT NULL,
  `accesso` varchar(3) DEFAULT NULL,
  `url_share` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_archivo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla parcial2.archivos: ~0 rows (aproximadamente)
DELETE FROM `archivos`;
/*!40000 ALTER TABLE `archivos` DISABLE KEYS */;
INSERT INTO `archivos` (`id_archivo`, `id_usuario`, `nombre_archivo`, `ruta_archivo`, `ruta_vista`, `type`, `size`, `accesso`, `url_share`) VALUES
	(1, 1, 'prueba prueba prueba  1', 'prueba-prueba-prueba--1-2022-04-16-21-50-6-186419.mp3', './static/images/types/no-image.jpg', 'mp3', '3.7 MB', 'on', '7y3vvQQ0aCeUaurK27t2arhDDHQU20xGx1hchFcB9DG9XNJSDuDgMRAhWMYkdbXbmajbflU1FdF7JtAOOSfji5hjbP'),
	(2, 1, 'prueba prueba prueba  1 ', 'prueba-prueba-prueba--1--2022-04-16-21-50-20-570441.exe', './static/images/types/ejecutable.png', 'exe', '4.9 MB', 'on', '7GJFt9g8BgnXUYYwLHARi5lCp1k1ZB19Xg3j5uvdebTepW6ev5DjQ4MCF5RRuFunEM7qeuq8Rd16jYPdJsfNPKf7oR'),
	(3, 1, 'prueba prueba prueba  1 ', 'prueba-prueba-prueba--1--2022-04-16-21-50-36-314450.png', './static/images_server/prueba-prueba-prueba--1--2022-04-16-21-50-36-314450.png', 'png', '1.4 MB', 'off', 'x0ugCW9v1p4C7phsmXZInWjRVhPg2kYClep544Whl3JsL73WoHfXGj0bHcjPxmyam5phPYGxVUphQcuRQ1qG8eokCj');
/*!40000 ALTER TABLE `archivos` ENABLE KEYS */;

-- Volcando estructura para tabla parcial2.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id_usuario` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre_usuario` varchar(50) DEFAULT NULL,
  `apellido_usuario` varchar(255) DEFAULT NULL,
  `user` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `validate` varchar(5) DEFAULT NULL,
  `url_val_mail` varchar(100) DEFAULT NULL,
  `url_pass` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla parcial2.usuarios: ~0 rows (aproximadamente)
DELETE FROM `usuarios`;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` (`id_usuario`, `nombre_usuario`, `apellido_usuario`, `user`, `password`, `validate`, `url_val_mail`, `url_pass`) VALUES
	(1, 'James', 'Cordoba', 'zujuroquemma-2730@yopmail.com', 'df548fa419918be525b32cd27570a925e1311b480cc329067d3940639cf3eaa584727efd2fd2fa5c3d9443835dc0bcb0f74eb06a669565d1d47ea0ad202888c5', 'true', '', ''),
	(2, 'James', '', 'sofreissaxeja-5176@yopmail.com', 'df548fa419918be525b32cd27570a925e1311b480cc329067d3940639cf3eaa584727efd2fd2fa5c3d9443835dc0bcb0f74eb06a669565d1d47ea0ad202888c5', 'true', '', '');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
