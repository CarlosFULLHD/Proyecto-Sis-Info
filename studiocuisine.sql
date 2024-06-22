/*
 Navicat Premium Data Transfer

 Source Server         : entel
 Source Server Type    : MySQL
 Source Server Version : 50515
 Source Host           : localhost:3306
 Source Schema         : studiocuisine

 Target Server Type    : MySQL
 Target Server Version : 50515
 File Encoding         : 65001

 Date: 30/11/2022 19:28:14
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for carrito
-- ----------------------------
DROP TABLE IF EXISTS `carrito`;
CREATE TABLE `carrito`  (
  `Id_carrito` int(11) NOT NULL,
  `Producto` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `Cantidad` int(11) NULL DEFAULT NULL,
  `Precio` double NULL DEFAULT NULL,
  `dir_imagen` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`Id_carrito`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of carrito
-- ----------------------------

-- ----------------------------
-- Table structure for datosempresa
-- ----------------------------
DROP TABLE IF EXISTS `datosempresa`;
CREATE TABLE `datosempresa`  (
  `idDatosEmpresa` int(11) NOT NULL,
  `nombreEmpresa` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `nit` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `telefono` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `email` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `direccion` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `fechaFundacion` datetime NOT NULL,
  `estado` bit(1) NOT NULL,
  `fechaActualizacion` datetime NOT NULL,
  `empresa_idEmpresa` int(11) NOT NULL,
  PRIMARY KEY (`idDatosEmpresa`) USING BTREE,
  INDEX `datosEmpresa_empresa`(`empresa_idEmpresa`) USING BTREE,
  CONSTRAINT `datosEmpresa_empresa` FOREIGN KEY (`empresa_idEmpresa`) REFERENCES `empresa` (`idEmpresa`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of datosempresa
-- ----------------------------

-- ----------------------------
-- Table structure for datospersona
-- ----------------------------
DROP TABLE IF EXISTS `datospersona`;
CREATE TABLE `datospersona`  (
  `idDatosPersona` int(11) NOT NULL,
  `nombres` varchar(70) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `apellidoPaterno` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `apellidoMaterno` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `apellidoCasada` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `dni` int(11) NOT NULL,
  `genero_idGenero` int(11) NOT NULL,
  `celular` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `email` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `direccion` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `fechaNacimiento` datetime NOT NULL,
  `estado` bit(1) NOT NULL,
  `fechaActualizacion` datetime NOT NULL,
  `persona_idPersona` int(11) NOT NULL,
  PRIMARY KEY (`idDatosPersona`) USING BTREE,
  INDEX `datosPersona_genero`(`genero_idGenero`) USING BTREE,
  INDEX `datosPersona_persona`(`persona_idPersona`) USING BTREE,
  CONSTRAINT `datosPersona_genero` FOREIGN KEY (`genero_idGenero`) REFERENCES `genero` (`idGenero`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `datosPersona_persona` FOREIGN KEY (`persona_idPersona`) REFERENCES `persona` (`idPersona`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of datospersona
-- ----------------------------

-- ----------------------------
-- Table structure for datosproducto
-- ----------------------------
DROP TABLE IF EXISTS `datosproducto`;
CREATE TABLE `datosproducto`  (
  `idDatosProducto` int(11) NOT NULL,
  `nombre` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `descripcion` varchar(250) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `cantidadProduccionDiaria` int(11) NOT NULL,
  `frecuenciaProduccion` int(11) NOT NULL,
  `precio` double NOT NULL,
  `fechaModificacion` datetime NOT NULL,
  `producto_idProducto` int(11) NOT NULL,
  PRIMARY KEY (`idDatosProducto`) USING BTREE,
  INDEX `datosProducto_producto`(`producto_idProducto`) USING BTREE,
  CONSTRAINT `datosProducto_producto` FOREIGN KEY (`producto_idProducto`) REFERENCES `producto` (`idProducto`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of datosproducto
-- ----------------------------

-- ----------------------------
-- Table structure for datosrestaurante
-- ----------------------------
DROP TABLE IF EXISTS `datosrestaurante`;
CREATE TABLE `datosrestaurante`  (
  `idDatosRestaurante` int(11) NOT NULL,
  `Nombre` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `direccion` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `telefono` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `fechaFundacion` datetime NOT NULL,
  `email` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `restaurante_idRestaurante` int(11) NOT NULL,
  PRIMARY KEY (`idDatosRestaurante`) USING BTREE,
  INDEX `datosRestaurante_restaurante`(`restaurante_idRestaurante`) USING BTREE,
  CONSTRAINT `datosRestaurante_restaurante` FOREIGN KEY (`restaurante_idRestaurante`) REFERENCES `restaurante` (`idRestaurante`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of datosrestaurante
-- ----------------------------

-- ----------------------------
-- Table structure for datosusuario
-- ----------------------------
DROP TABLE IF EXISTS `datosusuario`;
CREATE TABLE `datosusuario`  (
  `idDatosUsuario` int(11) NOT NULL,
  `nombreUsuario` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `contrasenia` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `fechaCreacion` date NOT NULL,
  `estado` bit(1) NOT NULL,
  `usuario_idUsuario` int(11) NOT NULL,
  PRIMARY KEY (`idDatosUsuario`) USING BTREE,
  INDEX `datosUsuario_usuario`(`usuario_idUsuario`) USING BTREE,
  CONSTRAINT `datosUsuario_usuario` FOREIGN KEY (`usuario_idUsuario`) REFERENCES `usuario` (`idUsuario`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of datosusuario
-- ----------------------------
INSERT INTO `datosusuario` VALUES (1, 'Edna', 'gsjes', '2022-04-14', b'1', 1);
INSERT INTO `datosusuario` VALUES (2, 'Keith', 'jkpeb', '2022-01-12', b'1', 2);
INSERT INTO `datosusuario` VALUES (3, 'Charlotte', 'jDM1s', '2022-09-03', b'1', 3);
INSERT INTO `datosusuario` VALUES (4, 'Rhonda', '1vhge', '2022-07-16', b'0', 4);
INSERT INTO `datosusuario` VALUES (5, 'Marie', '5xqLe', '2022-08-01', b'0', 5);
INSERT INTO `datosusuario` VALUES (6, 'Todd', 'k20Y5', '2022-08-26', b'1', 6);
INSERT INTO `datosusuario` VALUES (7, 'Lois', 'tfUea', '2022-05-10', b'0', 7);
INSERT INTO `datosusuario` VALUES (8, 'Dawn', 'XhQhM', '2022-03-10', b'1', 8);
INSERT INTO `datosusuario` VALUES (9, 'Alice', 'UaQqu', '2022-06-02', b'0', 9);
INSERT INTO `datosusuario` VALUES (10, 'Gladys', 'dsWEB', '2022-07-19', b'1', 10);
INSERT INTO `datosusuario` VALUES (11, 'sdsada', '123', '2022-11-27', b'1', 11);
INSERT INTO `datosusuario` VALUES (12, 'Daniel', 'dan', '2022-11-27', b'1', 12);
INSERT INTO `datosusuario` VALUES (13, 'Eduardo', '221008', '2022-11-27', b'1', 13);
INSERT INTO `datosusuario` VALUES (14, 'Carlos', '123', '2022-11-27', b'1', 14);

-- ----------------------------
-- Table structure for desglosepedido
-- ----------------------------
DROP TABLE IF EXISTS `desglosepedido`;
CREATE TABLE `desglosepedido`  (
  `idDesglosePedido` int(11) NOT NULL,
  `producto_idProducto` int(11) NOT NULL,
  `pedido_idPedido` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `precioUnitarioProducto` double NOT NULL,
  PRIMARY KEY (`idDesglosePedido`) USING BTREE,
  INDEX `desglosePedido_pedido`(`pedido_idPedido`) USING BTREE,
  INDEX `desglosePedido_producto`(`producto_idProducto`) USING BTREE,
  CONSTRAINT `desglosePedido_pedido` FOREIGN KEY (`pedido_idPedido`) REFERENCES `pedido` (`idPedido`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `desglosePedido_producto` FOREIGN KEY (`producto_idProducto`) REFERENCES `producto` (`idProducto`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of desglosepedido
-- ----------------------------

-- ----------------------------
-- Table structure for empresa
-- ----------------------------
DROP TABLE IF EXISTS `empresa`;
CREATE TABLE `empresa`  (
  `idEmpresa` int(11) NOT NULL,
  `fechaCreacion` date NOT NULL,
  PRIMARY KEY (`idEmpresa`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of empresa
-- ----------------------------

-- ----------------------------
-- Table structure for genero
-- ----------------------------
DROP TABLE IF EXISTS `genero`;
CREATE TABLE `genero`  (
  `idGenero` int(11) NOT NULL,
  `tipoNombre` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`idGenero`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of genero
-- ----------------------------

-- ----------------------------
-- Table structure for inventario
-- ----------------------------
DROP TABLE IF EXISTS `inventario`;
CREATE TABLE `inventario`  (
  `idInventario` int(11) NOT NULL,
  `direccion` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`idInventario`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of inventario
-- ----------------------------

-- ----------------------------
-- Table structure for mediopago
-- ----------------------------
DROP TABLE IF EXISTS `mediopago`;
CREATE TABLE `mediopago`  (
  `idMedioPago` int(11) NOT NULL,
  `nombreTipo` varchar(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`idMedioPago`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of mediopago
-- ----------------------------

-- ----------------------------
-- Table structure for pago
-- ----------------------------
DROP TABLE IF EXISTS `pago`;
CREATE TABLE `pago`  (
  `idPago` int(11) NOT NULL,
  `medioPago_idMedioPago` int(11) NOT NULL,
  `pedido_idPedido` int(11) NOT NULL,
  PRIMARY KEY (`idPago`) USING BTREE,
  INDEX `pago_medioPago`(`medioPago_idMedioPago`) USING BTREE,
  INDEX `pago_pedido`(`pedido_idPedido`) USING BTREE,
  CONSTRAINT `pago_medioPago` FOREIGN KEY (`medioPago_idMedioPago`) REFERENCES `mediopago` (`idMedioPago`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `pago_pedido` FOREIGN KEY (`pedido_idPedido`) REFERENCES `pedido` (`idPedido`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of pago
-- ----------------------------

-- ----------------------------
-- Table structure for pedido
-- ----------------------------
DROP TABLE IF EXISTS `pedido`;
CREATE TABLE `pedido`  (
  `idPedido` int(11) NOT NULL,
  `costoTotal` int(11) NOT NULL,
  `fecha` datetime NOT NULL,
  `usuario_idUsuario` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `Cantidad` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`idPedido`) USING BTREE,
  INDEX `pedido_usuario`(`usuario_idUsuario`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of pedido
-- ----------------------------
INSERT INTO `pedido` VALUES (1, 187, '2022-07-02 06:00:02', 'Kathryn Tran', 5);
INSERT INTO `pedido` VALUES (2, 138, '2022-04-28 15:35:57', 'Grace Green', 4);
INSERT INTO `pedido` VALUES (3, 176, '2022-04-02 00:20:43', 'Ray Myers', 7);
INSERT INTO `pedido` VALUES (4, 167, '2022-10-20 02:31:21', 'Stanley Allen', 2);
INSERT INTO `pedido` VALUES (5, 179, '2022-11-04 20:45:24', 'Daniel Reynolds', 6);
INSERT INTO `pedido` VALUES (6, 66, '2022-04-28 04:18:01', 'Ralph Boyd', 8);
INSERT INTO `pedido` VALUES (7, 75, '2022-06-01 09:55:56', 'Alan Thompson', 4);
INSERT INTO `pedido` VALUES (8, 97, '2022-08-20 20:41:42', 'Dennis Gardner', 3);
INSERT INTO `pedido` VALUES (9, 125, '2022-04-22 15:36:06', 'Mark Ruiz', 2);
INSERT INTO `pedido` VALUES (10, 98, '2022-11-30 11:27:36', 'Ernest Fox', 5);

-- ----------------------------
-- Table structure for persona
-- ----------------------------
DROP TABLE IF EXISTS `persona`;
CREATE TABLE `persona`  (
  `idPersona` int(11) NOT NULL,
  `fechaCreacion` date NOT NULL,
  PRIMARY KEY (`idPersona`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of persona
-- ----------------------------

-- ----------------------------
-- Table structure for producto
-- ----------------------------
DROP TABLE IF EXISTS `producto`;
CREATE TABLE `producto`  (
  `idProducto` int(11) NOT NULL,
  `restaurante_idRestaurante` int(11) NOT NULL,
  PRIMARY KEY (`idProducto`) USING BTREE,
  INDEX `producto_restaurante`(`restaurante_idRestaurante`) USING BTREE,
  CONSTRAINT `producto_restaurante` FOREIGN KEY (`restaurante_idRestaurante`) REFERENCES `restaurante` (`idRestaurante`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of producto
-- ----------------------------

-- ----------------------------
-- Table structure for producto_inventario
-- ----------------------------
DROP TABLE IF EXISTS `producto_inventario`;
CREATE TABLE `producto_inventario`  (
  `idProducto_inventario` int(11) NOT NULL,
  `producto_idProducto` int(11) NOT NULL,
  `Inventario_idInventario` int(11) NOT NULL,
  PRIMARY KEY (`idProducto_inventario`) USING BTREE,
  INDEX `producto_inventario_Inventario`(`Inventario_idInventario`) USING BTREE,
  INDEX `producto_inventario_producto`(`producto_idProducto`) USING BTREE,
  CONSTRAINT `producto_inventario_Inventario` FOREIGN KEY (`Inventario_idInventario`) REFERENCES `inventario` (`idInventario`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `producto_inventario_producto` FOREIGN KEY (`producto_idProducto`) REFERENCES `producto` (`idProducto`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of producto_inventario
-- ----------------------------

-- ----------------------------
-- Table structure for restaurante
-- ----------------------------
DROP TABLE IF EXISTS `restaurante`;
CREATE TABLE `restaurante`  (
  `idRestaurante` int(11) NOT NULL,
  `fechaCreacion` date NOT NULL,
  PRIMARY KEY (`idRestaurante`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of restaurante
-- ----------------------------

-- ----------------------------
-- Table structure for tipocuenta
-- ----------------------------
DROP TABLE IF EXISTS `tipocuenta`;
CREATE TABLE `tipocuenta`  (
  `idTipoCuenta` int(11) NOT NULL,
  `nombreTipoCuenta` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`idTipoCuenta`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of tipocuenta
-- ----------------------------
INSERT INTO `tipocuenta` VALUES (1, 'Usuario');
INSERT INTO `tipocuenta` VALUES (2, 'Operador');
INSERT INTO `tipocuenta` VALUES (3, 'Admin');

-- ----------------------------
-- Table structure for usuario
-- ----------------------------
DROP TABLE IF EXISTS `usuario`;
CREATE TABLE `usuario`  (
  `idUsuario` int(11) NOT NULL,
  `tipoCuenta_idTipoCuenta` int(11) NOT NULL,
  `persona_idPersona` int(11) NULL DEFAULT NULL,
  `empresa_idEmpresa` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`idUsuario`) USING BTREE,
  INDEX `usuario_empresa`(`empresa_idEmpresa`) USING BTREE,
  INDEX `usuario_persona`(`persona_idPersona`) USING BTREE,
  INDEX `usuario_tipoCuenta`(`tipoCuenta_idTipoCuenta`) USING BTREE,
  CONSTRAINT `usuario_empresa` FOREIGN KEY (`empresa_idEmpresa`) REFERENCES `empresa` (`idEmpresa`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `usuario_persona` FOREIGN KEY (`persona_idPersona`) REFERENCES `persona` (`idPersona`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `usuario_tipoCuenta` FOREIGN KEY (`tipoCuenta_idTipoCuenta`) REFERENCES `tipocuenta` (`idTipoCuenta`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of usuario
-- ----------------------------
INSERT INTO `usuario` VALUES (1, 1, NULL, NULL);
INSERT INTO `usuario` VALUES (2, 2, NULL, NULL);
INSERT INTO `usuario` VALUES (3, 3, NULL, NULL);
INSERT INTO `usuario` VALUES (4, 1, NULL, NULL);
INSERT INTO `usuario` VALUES (5, 1, NULL, NULL);
INSERT INTO `usuario` VALUES (6, 2, NULL, NULL);
INSERT INTO `usuario` VALUES (7, 3, NULL, NULL);
INSERT INTO `usuario` VALUES (8, 1, NULL, NULL);
INSERT INTO `usuario` VALUES (9, 3, NULL, NULL);
INSERT INTO `usuario` VALUES (10, 1, NULL, NULL);
INSERT INTO `usuario` VALUES (11, 1, NULL, NULL);
INSERT INTO `usuario` VALUES (12, 1, NULL, NULL);
INSERT INTO `usuario` VALUES (13, 1, NULL, NULL);
INSERT INTO `usuario` VALUES (14, 1, NULL, NULL);

SET FOREIGN_KEY_CHECKS = 1;
