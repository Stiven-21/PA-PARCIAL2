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
  `ruta` varchar(500) DEFAULT NULL,
  `accesso` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`id_archivo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla parcial2.archivos: ~0 rows (aproximadamente)
DELETE FROM `archivos`;
/*!40000 ALTER TABLE `archivos` DISABLE KEYS */;
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
	(2, 'James', '', 'sofreissaxeja-5176@yopmail.com', '83100ca686653af97f12ec4be588b4de535318ebe439051be1e98cc70b8604f525f4ee2dbeee60b22d9bf23cecfeeecf9f789ec99e3fe8482449e686fb9924ab', '7Kswh', 'F5BPK3QX4EQousLoaEyBe1gLOHKwEB6XZ465RK7kRDrJNkctG0jHGKwCYU5Q', '3cbqxzj1EkhDFPOWvFHXivNkvOGAZM7I25eLYoEMluZu6pGL1aazzc2vqkeH');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
