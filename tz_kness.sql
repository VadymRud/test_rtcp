-- --------------------------------------------------------
-- Сервер:                       127.0.0.1
-- Версія сервера:               10.3.13-MariaDB-log - mariadb.org binary distribution
-- ОС сервера:                   Win64
-- HeidiSQL Версія:              10.2.0.5599
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for tz_kness
DROP DATABASE IF EXISTS `tz_kness`;
CREATE DATABASE IF NOT EXISTS `tz_kness` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
USE `tz_kness`;

-- Dumping structure for таблиця tz_kness.ai_desc
DROP TABLE IF EXISTS `ai_desc`;
CREATE TABLE IF NOT EXISTS `ai_desc` (
  `id` int(11),
  `id_RTU` int(11) DEFAULT NULL,
  `act_v` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `act_t` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `act_q` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  KEY `ai_desc_rtu_id_fk` (`id_RTU`),
  CONSTRAINT `ai_desc_rtu_id_fk` FOREIGN KEY (`id_RTU`) REFERENCES `rtu` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця tz_kness.bi_desc
DROP TABLE IF EXISTS `bi_desc`;
CREATE TABLE IF NOT EXISTS `bi_desc` (
  `id` int(11) DEFAULT NULL,
  `id_RTU` int(11) NOT NULL,
  `act_v` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `act_t` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `act_q` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_RTU`),
  CONSTRAINT `bi_desc_rtu_id_fk` FOREIGN KEY (`id_RTU`) REFERENCES `rtu` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця tz_kness.rtu
DROP TABLE IF EXISTS `rtu`;
CREATE TABLE IF NOT EXISTS `rtu` (
  `id` int(11) NOT NULL,
  `url` tinytext COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `time_upd_int` smallint(6) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Дані для експорту не вибрані

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
