-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 27, 2020 at 03:23 AM
-- Server version: 5.7.31
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `2101project`
--

-- --------------------------------------------------------

--
-- Table structure for table `assessment`
--

DROP TABLE IF EXISTS `assessment`;
CREATE TABLE IF NOT EXISTS `assessment` (
  `AID` int(11) NOT NULL AUTO_INCREMENT,
  `assessment_name` varchar(100) NOT NULL,
  `MID` int(11) NOT NULL,
  PRIMARY KEY (`AID`),
  KEY `MID` (`MID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
CREATE TABLE IF NOT EXISTS `comment` (
  `COID` int(7) NOT NULL AUTO_INCREMENT,
  `comment` varchar(500) NOT NULL,
  `sender` int(7) NOT NULL,
  `receiver` int(7) NOT NULL,
  `CID` int(7) DEFAULT NULL,
  PRIMARY KEY (`COID`),
  KEY `sender` (`sender`),
  KEY `receiver` (`receiver`),
  KEY `CID` (`CID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `component`
--

DROP TABLE IF EXISTS `component`;
CREATE TABLE IF NOT EXISTS `component` (
  `CID` int(7) NOT NULL AUTO_INCREMENT,
  `description` varchar(500) NOT NULL,
  `type` varchar(100) NOT NULL,
  `AID` int(7) NOT NULL,
  PRIMARY KEY (`CID`),
  KEY `AID` (`AID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `module`
--

DROP TABLE IF EXISTS `module`;
CREATE TABLE IF NOT EXISTS `module` (
  `MID` int(11) NOT NULL AUTO_INCREMENT,
  `mod_name` varchar(50) NOT NULL,
  `UID` int(7) NOT NULL,
  PRIMARY KEY (`MID`),
  KEY `UID` (`UID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `result`
--

DROP TABLE IF EXISTS `result`;
CREATE TABLE IF NOT EXISTS `result` (
  `RID` int(7) NOT NULL AUTO_INCREMENT,
  `UID` int(7) NOT NULL,
  `marks` int(7) NOT NULL,
  `CID` int(7) NOT NULL,
  PRIMARY KEY (`RID`),
  KEY `CID` (`CID`),
  KEY `UID` (`UID`),
  KEY `CID_2` (`CID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `UID` int(7) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `isStudent` tinyint(1) NOT NULL,
  PRIMARY KEY (`UID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `assessment`
--
ALTER TABLE `assessment`
  ADD CONSTRAINT `assessment_ibfk_1` FOREIGN KEY (`MID`) REFERENCES `module` (`MID`);

--
-- Constraints for table `comment`
--
ALTER TABLE `comment`
  ADD CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`CID`) REFERENCES `component` (`CID`),
  ADD CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`receiver`) REFERENCES `user` (`UID`),
  ADD CONSTRAINT `comment_ibfk_3` FOREIGN KEY (`sender`) REFERENCES `user` (`UID`);

--
-- Constraints for table `component`
--
ALTER TABLE `component`
  ADD CONSTRAINT `component_ibfk_1` FOREIGN KEY (`AID`) REFERENCES `assessment` (`AID`);

--
-- Constraints for table `module`
--
ALTER TABLE `module`
  ADD CONSTRAINT `module_ibfk_1` FOREIGN KEY (`UID`) REFERENCES `user` (`UID`);

--
-- Constraints for table `result`
--
ALTER TABLE `result`
  ADD CONSTRAINT `result_ibfk_1` FOREIGN KEY (`CID`) REFERENCES `component` (`CID`),
  ADD CONSTRAINT `result_ibfk_2` FOREIGN KEY (`UID`) REFERENCES `user` (`UID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
