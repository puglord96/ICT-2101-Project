-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 02, 2020 at 05:42 PM
-- Server version: 10.3.16-MariaDB
-- PHP Version: 7.3.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
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

CREATE TABLE `assessment` (
  `AID` int(11) NOT NULL,
  `assessment_name` varchar(100) NOT NULL,
  `MID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `comment`
--

CREATE TABLE `comment` (
  `COID` int(7) NOT NULL,
  `comment` varchar(500) NOT NULL,
  `sender` int(7) NOT NULL,
  `receiver` int(7) NOT NULL,
  `CID` int(7) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `component`
--

CREATE TABLE `component` (
  `CID` int(7) NOT NULL,
  `description` varchar(500) NOT NULL,
  `type` varchar(100) NOT NULL,
  `AID` int(7) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `FID` int(11) NOT NULL,
  `FType` varchar(45) DEFAULT NULL,
  `FTitle` varchar(45) DEFAULT NULL,
  `FContent` varchar(255) DEFAULT NULL,
  `FSender` int(7) NOT NULL,
  `FReceiver` int(7) NOT NULL,
  `FMod_code` int(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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

CREATE TABLE `module` (
  `MID` int(11) NOT NULL,
  `mod_code` int(4) NOT NULL,
  `mod_name` varchar(50) NOT NULL,
  `UID` int(7) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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

CREATE TABLE `result` (
  `RID` int(7) NOT NULL,
  `UID` int(7) NOT NULL,
  `marks` int(7) NOT NULL,
  `CID` int(7) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `UID` int(7) NOT NULL,
  `name` varchar(100) NOT NULL,
  `isStudent` tinyint(1) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`UID`, `name`, `isStudent`, `email`) VALUES
(1001234, 'Tan Kok Leong', 0, '1001234@signaporetech.edu.sg'),
(1901000, 'John Lim Ko Pi', 1, '1901000@sit.singaporetech.edu.sg'),
(1901001, 'Thomas Lam Mi Lo', 1, '1901001@sit.singaporetech.edu.sg'),
(1901002, 'Ali Bin Abdul', 1, '1901002@sit.singaporetech.edu.sg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `assessment`
--
ALTER TABLE `assessment`
  ADD PRIMARY KEY (`AID`),
  ADD KEY `MID` (`MID`);

--
-- Indexes for table `comment`
--
ALTER TABLE `comment`
  ADD PRIMARY KEY (`COID`),
  ADD KEY `sender` (`sender`),
  ADD KEY `receiver` (`receiver`),
  ADD KEY `CID` (`CID`);

--
-- Indexes for table `component`
--
ALTER TABLE `component`
  ADD PRIMARY KEY (`CID`),
  ADD KEY `AID` (`AID`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`FID`);

--
-- Indexes for table `module`
--
ALTER TABLE `module`
  ADD PRIMARY KEY (`MID`),
  ADD KEY `UID` (`UID`);

--
-- Indexes for table `result`
--
ALTER TABLE `result`
  ADD PRIMARY KEY (`RID`),
  ADD KEY `CID` (`CID`),
  ADD KEY `UID` (`UID`),
  ADD KEY `CID_2` (`CID`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`UID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `assessment`
--
ALTER TABLE `assessment`
  MODIFY `AID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `comment`
--
ALTER TABLE `comment`
  MODIFY `COID` int(7) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `component`
--
ALTER TABLE `component`
  MODIFY `CID` int(7) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `FID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=112319;

--
-- AUTO_INCREMENT for table `module`
--
ALTER TABLE `module`
  MODIFY `MID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `result`
--
ALTER TABLE `result`
  MODIFY `RID` int(7) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `UID` int(7) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1901003;

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
