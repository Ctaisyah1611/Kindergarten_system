-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 16, 2024 at 06:35 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kindergarten_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `Stu_Id` int(7) NOT NULL,
  `Stu_Name` varchar(30) NOT NULL,
  `Birth_Year` int(4) NOT NULL,
  `Stu_Gender` varchar(6) NOT NULL,
  `Current_Year` int(4) NOT NULL,
  `Stu_Age` int(3) NOT NULL,
  `Stu_Class` varchar(30) NOT NULL,
  `Parent_Name` varchar(30) NOT NULL,
  `Contact_Num` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`Stu_Id`, `Stu_Name`, `Birth_Year`, `Stu_Gender`, `Current_Year`, `Stu_Age`, `Stu_Class`, `Parent_Name`, `Contact_Num`) VALUES
(20232810, 'QISTINA RAISYA AKMAL ', 2018, 'Female', 2024, 6, 'Class Alpha', 'AKMAL BIN JAMAL', '0146075536'),
(20237432, 'NUR MELISSA BINTI ZIZAN', 2018, 'Female', 2024, 6, 'Class Beta', 'ZIZAN BIN RAHIM ', '0133676674'),
(20234557, 'NUR AMERNA BINTI FAUZI', 2018, 'Female', 2024, 6, 'Class Charlie', 'IZATI BINTI ZAMRI', '0114413004'),
(20235481, 'SYED AHMAD BIN SYED ZAKI', 2019, 'Male', 2024, 5, 'Class Alpha', 'ASYIKIN BINTI ZAHAR ', '0136613731'),
(20236451, 'AMNA MEDINA BINTI HARIZ ', 2019, 'Female', 2024, 5, 'Class Beta', 'NINA BINTI ARIF ', '0122244171'),
(20231054, 'MUHAMMAD ALIF BIN HARIZ ', 2019, 'Male', 2024, 5, 'Class Charlie', 'NINA BINTI ALIF ', '0122244171'),
(20238148, 'AIN AMIRAH BINTI ALI ', 2020, 'Female', 2024, 4, 'Class Alpha', 'ALI BIN ALIF ', '0115061430'),
(20235264, 'AMIR BADRISHAH BIN ABU ', 2020, 'Male', 2024, 4, 'Class Beta', 'ABU BIN ARIFIN ', '0126670053'),
(20236112, 'AIDA ELYANA BINTI ZAIDI', 2020, 'Female', 2024, 4, 'Class Charlie', 'AZIZAH BINTI KAMAL', '0115543111');

-- --------------------------------------------------------

--
-- Table structure for table `subject_registration`
--

CREATE TABLE `subject_registration` (
  `student_id` int(11) NOT NULL,
  `student_name` text NOT NULL,
  `student_age` int(11) NOT NULL,
  `subject` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `subject_registration`
--

INSERT INTO `subject_registration` (`student_id`, `student_name`, `student_age`, `subject`) VALUES
(20232810, 'QISTINA RAISYA AKMAL', 6, 'SCIENCE'),
(20235264, 'AMIR BADRISYAH BIN ABU', 4, 'MATHEMATICS'),
(20236451, 'AMNA MEDINA BINTI HARIZ', 5, 'WRITING');

-- --------------------------------------------------------

--
-- Table structure for table `teacher_calculator`
--

CREATE TABLE `teacher_calculator` (
  `number_of_subject` int(11) NOT NULL,
  `monthly_teaching_day` int(11) NOT NULL,
  `gross_salary` int(11) NOT NULL,
  `kwsp_contributions` float NOT NULL,
  `socso` float NOT NULL,
  `income_tax` float NOT NULL,
  `other_pay` int(11) NOT NULL,
  `net_salary` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `teacher_calculator`
--

INSERT INTO `teacher_calculator` (`number_of_subject`, `monthly_teaching_day`, `gross_salary`, `kwsp_contributions`, `socso`, `income_tax`, `other_pay`, `net_salary`) VALUES
(1, 3, 300, 2, 3, 2, 20, 257),
(3, 20, 6000, 5, 5, 4, 500, 4696),
(3, 20, 6000, 11, 1.75, 30, 0, 5957),
(3, 9, 2700, 23, 2.3, 3.2, 300, 2372);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
