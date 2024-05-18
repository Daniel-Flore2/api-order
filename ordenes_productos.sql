-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-05-2024 a las 05:54:39
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `api_gateway`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ordenes_productos`
--

CREATE TABLE `ordenes_productos` (
  `orden_id` int(11) DEFAULT NULL,
  `producto_id` int(11) DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ordenes_productos`
--

INSERT INTO `ordenes_productos` (`orden_id`, `producto_id`, `precio`, `cantidad`) VALUES
(1, 1, '100.00', 2);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `ordenes_productos`
--
ALTER TABLE `ordenes_productos`
  ADD KEY `Orden_Id` (`orden_id`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `ordenes_productos`
--
ALTER TABLE `ordenes_productos`
  ADD CONSTRAINT `ordenes_productos_ibfk_1` FOREIGN KEY (`Orden_Id`) REFERENCES `ordenes` (`Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
