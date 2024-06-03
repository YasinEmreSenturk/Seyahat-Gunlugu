-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1:3306
-- Üretim Zamanı: 27 Ara 2023, 14:03:11
-- Sunucu sürümü: 8.0.31
-- PHP Sürümü: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `seyahat`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `login`
--

DROP TABLE IF EXISTS `login`;
CREATE TABLE IF NOT EXISTS `login` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `u_password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Tablo döküm verisi `login`
--

INSERT INTO `login` (`id`, `username`, `u_password`) VALUES
(1, 'emr', '1'),
(2, 'emr', '1'),
(3, 'talha', '2'),
(4, 'sude', '123'),
(5, 'se', '1'),
(6, 'yas', '3'),
(7, 'ter', '1'),
(8, 'emir', '12'),
(9, 'yasın', '1'),
(10, 'tl', '1'),
(11, 'eko', '1'),
(12, 'oz', '12'),
(13, 'qw', 'wq'),
(14, 'qw', 'qw'),
(15, 'sd', 'AS'),
(16, 'aa', 'aa'),
(17, 'umut', '1'),
(18, 'sıla', '1'),
(19, 'ty', '2'),
(20, 'sondeme2', '1'),
(21, 'burak', '1'),
(22, 'turgay', '1');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `seyahat`
--

DROP TABLE IF EXISTS `seyahat`;
CREATE TABLE IF NOT EXISTS `seyahat` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `seyahat_ad` varchar(255) DEFAULT NULL,
  `ulke` varchar(255) DEFAULT NULL,
  `tarih` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=86 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Tablo döküm verisi `seyahat`
--

INSERT INTO `seyahat` (`id`, `user_id`, `seyahat_ad`, `ulke`, `tarih`) VALUES
(1, 1, 'abama', 'Türkiye', '2023-12-19'),
(43, 1, 'asdasd', 'İtalya', '0000-00-00'),
(44, 1, 'qewdas', 'ABD', '0000-00-00'),
(45, 1, 'ozan', 'İtalya', '2012-12-14'),
(46, 1, 'Gezi Tur', 'Fransa', '2022-02-04'),
(47, 1, 'selam', 'Fransa', '2015-04-07'),
(48, 1, 'LŞLŞL', 'Fransa', '0000-00-00'),
(49, 1, 'arif han deneme', 'Türkiye', '2012-12-12'),
(50, 1, 'deneme3', 'Almanya', '2014-12-12'),
(51, 1, 'seyahatım', 'Fransa', '0000-00-00'),
(52, 1, 'okul', 'İtalya', '2000-12-12'),
(53, 1, 'ok', 'İtalya', '2000-12-12'),
(54, 1, 'adsas', 'İngiltere', '0000-00-00'),
(55, 1, 'silmedeneme', 'Almanya', '0000-00-00'),
(56, 1, 'sadasddeneme', 'İngiltere', '0000-00-00'),
(57, 1, 'abama', 'İtalya', '0000-00-00'),
(58, 1, 'abama', 'İtalya', '0000-00-00'),
(59, 1, 'al', 'İtalya', '0000-00-00'),
(60, 1, 'asd', 'Fransa', '0000-00-00'),
(61, 1, 'saelam', 'Almanya', '0000-00-00'),
(62, 1, 'selam', 'İtalya', '0000-00-00'),
(41, 1, 'iş gezisi', 'Almanya', '2022-04-07'),
(42, 3, 'ambarasd', 'Almanya', '0000-00-00'),
(39, 1, 'adas', 'Fransa', '0000-00-00'),
(40, 1, 'asdas', 'Almanya', '0000-00-00'),
(63, 1, 'renkdeme', 'ABD', '1989-05-08'),
(64, 1, 'selamlar', 'Türkiye', '0000-00-00'),
(65, 1, 'sad', 'Fransa', '2022-12-12'),
(66, 17, 'iş ', 'Fransa', '2024-01-05'),
(67, 18, 'eskişehir', 'Türkiye', '2029-01-16'),
(68, 1, 'umayölölöl', 'İtalya', '2022-12-12'),
(69, 19, 'tytk', 'Fransa', '0000-00-00'),
(70, 1, 'sadas', 'Almanya', '0000-00-00'),
(71, 1, 'as', 'Fransa', '0000-00-00'),
(72, 1, 'silemdeneme', 'Fransa', '0000-00-00'),
(73, 1, 's', 'Türkiye', '0000-00-00'),
(74, 1, 's', 'Almanya', '0000-00-00'),
(75, 1, 'asda', 'ABD', '0000-00-00'),
(76, 1, 'sad', 'Almanya', '0000-00-00'),
(77, 1, 'koaskod', 'Fransa', '2012-12-10'),
(78, 1, 'asda', 'İtalya', '0000-00-00'),
(79, 1, 'emresentrssssssssss', 'Almanya', '0000-00-00'),
(80, 1, 'denemesonders', 'Fransa', '2022-12-01'),
(81, 21, 'iş ', 'İtalya', '2024-01-05'),
(82, 21, 'okul hayatı', 'İngiltere', '2024-01-05'),
(83, 1, 'şlmasdkmlasdkmlasdlkmafkmladskml', 'Fransa', '0000-00-00'),
(84, 22, 'kuşadası', 'İtalya', '2024-12-12'),
(85, 1, 'ykeleme', 'Fransa', '2022-12-12');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
