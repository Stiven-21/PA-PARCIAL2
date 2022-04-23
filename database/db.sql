CREATE DATABASE IF NOT EXISTS `parcial2`;
USE `parcial2`;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DELETE FROM `archivos`;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DELETE FROM `usuarios`;