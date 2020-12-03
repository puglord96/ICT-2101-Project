-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 03, 2020 at 02:27 PM
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
CREATE DATABASE IF NOT EXISTS `2101project` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `2101project`;

-- --------------------------------------------------------

--
-- Table structure for table `assessment`
--

DROP TABLE IF EXISTS `assessment`;
CREATE TABLE IF NOT EXISTS `assessment` (
  `AID` int(11) NOT NULL AUTO_INCREMENT,
  `assessment_name` varchar(100) NOT NULL,
  `MID` int(11) NOT NULL,
  `type` varchar(100) NOT NULL,
  `weight` float NOT NULL,
  PRIMARY KEY (`AID`),
  KEY `MID` (`MID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `assessment`
--

INSERT INTO `assessment` (`AID`, `assessment_name`, `MID`, `type`, `weight`) VALUES
(1, 'Milestone 1', 1, 'Project', 20),
(2, 'Milestone 2', 1, 'Project', 20),
(3, 'Milestone 3', 1, 'Project', 30),
(4, 'Milestone 4', 1, 'Project', 30),
(5, 'Project 1', 2, 'Project', 50),
(6, 'Project 2', 2, 'Project', 50);

-- --------------------------------------------------------

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
CREATE TABLE IF NOT EXISTS `comment` (
  `COID` int(11) NOT NULL AUTO_INCREMENT,
  `comment` varchar(500) NOT NULL,
  `sender` int(11) NOT NULL,
  `receiver` int(11) NOT NULL,
  `CID` int(11) DEFAULT NULL,
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
  `CID` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(500) NOT NULL,
  `AID` int(11) NOT NULL,
  `weight` float NOT NULL,
  PRIMARY KEY (`CID`),
  KEY `AID` (`AID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `component`
--

INSERT INTO `component` (`CID`, `description`, `AID`, `weight`) VALUES
(1, 'Report', 1, 30),
(2, 'Code', 1, 50),
(3, 'Feedback', 1, 20);

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
CREATE TABLE IF NOT EXISTS `feedback` (
  `FID` int(11) NOT NULL,
  `FType` varchar(45) DEFAULT NULL,
  `FTitle` varchar(45) DEFAULT NULL,
  `FContent` varchar(255) DEFAULT NULL,
  `FSender` int(11) DEFAULT NULL,
  `FReceiver` int(11) DEFAULT NULL,
  `FMod_code` int(4) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`FID`, `FType`, `FTitle`, `FContent`, `FSender`, `FReceiver`, `FMod_code`) VALUES
(1, 'General', 'Good Job', 'Good job on your work', 1001234, 1901000, 1001),
(2, 'Summative', 'Test', 'Test', 1001234, 1901000, 1001),
(3, 'Summative', 'Very Good', 'TTEEESSTT', 1001234, 1901001, 1002),
(4, 'Summative', 'Summative Test', 'Test', 1001234, 1901003, 9999);

-- --------------------------------------------------------

--
-- Table structure for table `module`
--

DROP TABLE IF EXISTS `module`;
CREATE TABLE IF NOT EXISTS `module` (
  `MID` int(11) NOT NULL AUTO_INCREMENT,
  `mod_code` int(11) NOT NULL,
  `mod_name` varchar(50) NOT NULL,
  `UID` int(11) NOT NULL,
  PRIMARY KEY (`MID`),
  KEY `UID` (`UID`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `module`
--

INSERT INTO `module` (`MID`, `mod_code`, `mod_name`, `UID`) VALUES
(1, 1001, 'Introduction to ICT', 1901000),
(2, 1002, 'Programming Fundamentals', 1901000),
(3, 1003, 'Computer Organisation and Architecture', 1901000),
(4, 1004, 'Web Systems and Technologies', 1901000),
(5, 1005, 'Mathematics and Staitstics for ICT', 1901000),
(6, 1006, 'ICT in Organisations', 1901000),
(7, 1007, 'Operating Systems', 1901000),
(8, 1008, 'Data Structures and Algorithms', 1901000),
(9, 1009, 'Object-Oriented Programming', 1901000),
(10, 1010, 'Computer Networks', 1901000),
(11, 1001, 'Introduction to ICT', 1001234),
(12, 1002, 'Programming Fundamentals', 1001234),
(13, 1003, 'Computer Organisation and Architecture', 1001234),
(14, 1001, 'Introduction to ICT', 1901001),
(15, 1002, 'Programming Fundamentals', 1901001),
(16, 1003, 'Computer Organisation and Architecture', 1001234);

-- --------------------------------------------------------

--
-- Table structure for table `result`
--

DROP TABLE IF EXISTS `result`;
CREATE TABLE IF NOT EXISTS `result` (
  `RID` int(11) NOT NULL AUTO_INCREMENT,
  `UID` int(11) NOT NULL,
  `marks` int(11) NOT NULL,
  `CID` int(11) NOT NULL,
  PRIMARY KEY (`RID`),
  KEY `CID` (`CID`),
  KEY `UID` (`UID`),
  KEY `CID_2` (`CID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `result`
--

INSERT INTO `result` (`RID`, `UID`, `marks`, `CID`) VALUES
(1, 1901000, 40, 1),
(2, 1901000, 50, 2),
(3, 1901000, 50, 3);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `UID` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `isStudent` tinyint(1) NOT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`UID`)
) ENGINE=InnoDB AUTO_INCREMENT=1901003 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`UID`, `name`, `isStudent`, `email`) VALUES
(1001234, 'Tan Kok Leong', 0, '1001234@signaporetech.edu.sg'),
(1901000, 'John Lim Ko Pi', 1, '1901000@sit.singaporetech.edu.sg'),
(1901001, 'Thomas Lam Mi Lo', 1, '1901001@sit.singaporetech.edu.sg'),
(1901002, 'Ali Bin Abdul', 1, '1901002@sit.singaporetech.edu.sg');

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
