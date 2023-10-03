-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 03, 2023 at 08:09 AM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `geckoair`
--

-- --------------------------------------------------------

--
-- Table structure for table `airlines`
--

CREATE TABLE `airlines` (
  `airline_id` int(11) NOT NULL,
  `airline_name` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `airlines`
--

INSERT INTO `airlines` (`airline_id`, `airline_name`) VALUES
(1, 'Garuda Indonesia'),
(2, 'Lion Air'),
(3, 'Citilink'),
(4, 'ArabEmiratesAir'),
(5, 'Pku Air'),
(6, 'Prw Air'),
(7, 'Bengkalis Air'),
(8, 'Taiwan Air'),
(9, 'Vegas Air'),
(10, 'JHS Air Group');

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('eb38ff4ae370');

-- --------------------------------------------------------

--
-- Table structure for table `bookings`
--

CREATE TABLE `bookings` (
  `booking_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `flight_id` int(11) NOT NULL,
  `booking_date` datetime NOT NULL,
  `booking_status` varchar(20) NOT NULL,
  `cancel_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bookings`
--

INSERT INTO `bookings` (`booking_id`, `user_id`, `flight_id`, `booking_date`, `booking_status`, `cancel_date`) VALUES
(6, 2, 4, '2023-09-19 00:59:56', 'Unpaid', NULL),
(7, 8, 4, '2023-09-20 13:12:15', 'Cancelled', '2023-09-25 08:57:09'),
(8, 8, 6, '2023-09-20 14:06:15', 'Cancelled', '2023-09-25 15:16:25'),
(9, 8, 5, '2023-09-20 14:58:19', 'Unpaid', NULL),
(10, 8, 19, '2023-09-23 20:18:53', 'Refund', NULL),
(11, 8, 4, '2023-09-25 08:56:41', 'Refund', NULL),
(12, 8, 4, '2023-09-25 08:59:23', 'Refund', NULL),
(13, 8, 4, '2023-09-25 15:15:52', 'Refund', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `cities`
--

CREATE TABLE `cities` (
  `city_id` int(11) NOT NULL,
  `city_name` varchar(60) NOT NULL,
  `city_code` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cities`
--

INSERT INTO `cities` (`city_id`, `city_name`, `city_code`) VALUES
(1, 'Pekanbaru', 'PKU'),
(2, 'Perawang', 'PRW'),
(3, 'Jakarta', 'CGK'),
(4, 'Sentul', 'STL'),
(5, 'Bandung', 'BDO'),
(6, 'Bogor', 'BGR'),
(7, 'Yogyakarta', 'YGY'),
(8, 'Fukuoka', 'FUK'),
(9, 'Tianjin', 'TSN'),
(10, 'Fuzhou', 'FOK');

-- --------------------------------------------------------

--
-- Table structure for table `flights`
--

CREATE TABLE `flights` (
  `flight_id` int(11) NOT NULL,
  `flight_number` varchar(20) NOT NULL,
  `flight_date` date DEFAULT NULL,
  `route_id` int(11) NOT NULL,
  `flight_price` int(11) NOT NULL,
  `airline_id` int(11) NOT NULL,
  `seat_type_id` int(11) NOT NULL,
  `available_seats` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `flights`
--

INSERT INTO `flights` (`flight_id`, `flight_number`, `flight_date`, `route_id`, `flight_price`, `airline_id`, `seat_type_id`, `available_seats`) VALUES
(4, 'GA001', '2023-09-18', 1, 500000, 1, 1, 52),
(5, 'GA001', '2023-09-18', 1, 800000, 1, 2, 21),
(6, 'GA001', '2023-09-18', 1, 1000000, 1, 3, 11),
(7, 'LA001', '2023-09-18', 4, 900000, 2, 1, 30),
(8, 'LA001', '2023-09-18', 4, 1100000, 2, 2, 10),
(9, 'LA001', '2023-09-18', 4, 1800000, 2, 3, 6),
(10, 'LA002', '2023-09-18', 5, 1300000, 2, 1, 20),
(11, 'LA002', '2023-09-18', 5, 2800000, 2, 2, 10),
(12, 'LA002', '2023-09-18', 5, 5800000, 2, 3, 4),
(13, 'GA002', '2023-09-18', 8, 1800000, 1, 1, 30),
(14, 'GA002', '2023-09-18', 8, 4800000, 1, 2, 10),
(15, 'GA002', '2023-09-18', 8, 10800000, 1, 3, 4),
(16, 'JS001', '2023-09-18', 2, 1200000, 10, 1, 30),
(17, 'JS001', '2023-09-18', 2, 1800000, 10, 2, 10),
(18, 'JS001', '2023-09-18', 2, 4680000, 10, 3, 4),
(19, 'CL001', '2023-09-18', 3, 1280000, 3, 3, 2),
(20, 'CL001', '2023-09-18', 3, 800000, 3, 2, 10),
(21, 'CL001', '2023-09-18', 3, 400000, 3, 1, 60),
(22, 'BA001', '2023-09-18', 6, 400000, 7, 1, 60),
(23, 'BA001', '2023-09-18', 6, 800000, 7, 2, 30),
(24, 'BA001', '2023-09-18', 6, 1200000, 7, 3, 10),
(25, 'AE001', '2023-09-18', 7, 800000, 4, 1, 40),
(26, 'AE001', '2023-09-18', 7, 1200000, 4, 2, 20),
(27, 'AE001', '2023-09-18', 7, 5900000, 4, 3, 16),
(28, 'VG001', '2023-09-18', 9, 7400000, 9, 1, 30),
(29, 'VG001', '2023-09-18', 9, 12965000, 9, 2, 10),
(30, 'VG001', '2023-09-18', 9, 20125000, 9, 3, 5),
(36, 'GA003', '2023-09-18', 11, 1200000, 1, 1, 40),
(37, 'GA003', '2023-09-18', 11, 1985000, 1, 2, 10),
(38, 'GA003', '2023-09-18', 11, 2950000, 1, 3, 6);

-- --------------------------------------------------------

--
-- Table structure for table `payments`
--

CREATE TABLE `payments` (
  `payment_id` int(11) NOT NULL,
  `booking_id` int(11) NOT NULL,
  `payment_date` datetime NOT NULL,
  `paymentmethod` varchar(20) NOT NULL,
  `payment_status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `payments`
--

INSERT INTO `payments` (`payment_id`, `booking_id`, `payment_date`, `paymentmethod`, `payment_status`) VALUES
(41, 10, '2023-09-23 20:52:53', 'BCA', 'Paid'),
(42, 11, '2023-09-25 08:56:59', 'BCA', 'Paid'),
(43, 12, '2023-09-25 08:59:26', 'BCA', 'Paid'),
(44, 13, '2023-09-25 15:16:03', 'BCA', 'Paid');

--
-- Triggers `payments`
--
DELIMITER $$
CREATE TRIGGER `DecreaseSeat` AFTER INSERT ON `payments` FOR EACH ROW BEGIN
    DECLARE booking_flight_id INT;
    
    -- Find the flight_id associated with the booking_id from the payments table
    SELECT flight_id INTO booking_flight_id FROM bookings WHERE booking_id = NEW.booking_id;
    
    -- Update the available_seats in the flights table
    UPDATE flights
    SET available_seats = available_seats - 1
    WHERE flight_id = booking_flight_id;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `refund_payment`
--

CREATE TABLE `refund_payment` (
  `refund_id` int(11) NOT NULL,
  `payment_id` int(11) NOT NULL,
  `refund_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `refund_payment`
--

INSERT INTO `refund_payment` (`refund_id`, `payment_id`, `refund_date`) VALUES
(14, 41, '2023-09-23 20:53:29'),
(15, 42, '2023-09-25 08:57:18'),
(16, 43, '2023-09-25 08:59:41'),
(17, 44, '2023-09-25 15:16:29');

--
-- Triggers `refund_payment`
--
DELIMITER $$
CREATE TRIGGER `IncreaseSeat` AFTER INSERT ON `refund_payment` FOR EACH ROW BEGIN
    DECLARE payment_booking_id INT;
    DECLARE booking_flight_id INT;
    SELECT booking_id INTO payment_booking_id FROM payments WHERE payment_id = NEW.payment_id;
    SELECT flight_id INTO booking_flight_id FROM bookings WHERE booking_id = payment_booking_id;
    UPDATE flights
    SET available_seats = available_seats + 1
    WHERE flight_id = booking_flight_id;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `routes`
--

CREATE TABLE `routes` (
  `route_id` int(11) NOT NULL,
  `origin_city_id` int(11) NOT NULL,
  `destination_city_id` int(11) NOT NULL,
  `duration_hours` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `routes`
--

INSERT INTO `routes` (`route_id`, `origin_city_id`, `destination_city_id`, `duration_hours`) VALUES
(1, 1, 2, 200),
(2, 4, 2, 100),
(3, 5, 7, 150),
(4, 2, 9, 190),
(5, 3, 7, 690),
(6, 4, 5, 790),
(7, 2, 8, 800),
(8, 10, 3, 1000),
(9, 6, 8, 100),
(11, 7, 10, 420);

-- --------------------------------------------------------

--
-- Table structure for table `seat_types`
--

CREATE TABLE `seat_types` (
  `seat_type_id` int(11) NOT NULL,
  `seat_type_name` varchar(25) NOT NULL,
  `seat_type_price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `seat_types`
--

INSERT INTO `seat_types` (`seat_type_id`, `seat_type_name`, `seat_type_price`) VALUES
(1, 'Economy', 10),
(2, 'Business', 50),
(3, 'First', 90);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `date_of_birth` date NOT NULL,
  `name` varchar(25) NOT NULL,
  `phone_number` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `date_of_birth`, `name`, `phone_number`, `email`, `gender`, `password`) VALUES
(1, '2004-11-28', 'Jeff', '0811765971', 'ppti.jeffersontimotius@gmail.c', 'Male', '$2b$12$HyfPeYoXfbob6sbbdcBPIuGLetee5t/l82kXcnqhcbwdqmtcA1Jpa'),
(2, '2000-05-15', 'Alice', '0812345678', 'alice@example.com', 'Female', '$2b$12$ehQn13MkhanmSLydSo2szeWixV4ttmHsVQcJ5L/HL9MBwZc1LMWKy'),
(3, '1995-09-03', 'Michael', '0809876543', 'michael@example.com', 'Male', '$2b$12$Vh7tv/mSw4dZh/o4X00dqOGg9dPhpUwOqv8MJc8GIaCIKyagMXEUC'),
(4, '2001-07-22', 'Emily', '0854321098', 'emily@example.com', 'Female', '$2b$12$BvgRGGfIHu5mFb8QD5rM.eIsJILRlQj.oG2zpXxjrUzxvJzA9ImQy'),
(5, '1998-12-10', 'Daniel', '0810112233', 'daniel@example.com', 'Male', '$2b$12$iWAKALXapLYSnYr/OHefGedJVU96zj1LawONQj6ErymKhUIY46t8y'),
(6, '1993-04-17', 'Olivia', '0823456789', 'olivia@example.com', 'Female', '$2b$12$nnjcbSY8/.EO4gI/X6C4IO1RIBbtimPpc8rFmumk.NhzPCEwABlRS'),
(7, '1993-04-17', 'Olivia', '0823456789', 'olivia1@example.com', 'Female', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
(8, '2002-08-12', 'William', '0811223344', 'william@example.com', 'Male', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
(9, '1990-03-25', 'Sophia', '0876543210', 'sophia@example.com', 'Female', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
(10, '2003-01-08', 'James', '0856789012', 'james@example.com', 'Male', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
(11, '1997-06-19', 'Ava', '0812345678', 'ava@example.com', 'Female', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
(12, '1994-10-30', 'Benjamin', '0833333333', 'benjamin@example.com', 'Male', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
(13, '2005-02-14', 'Mia', '0898765432', 'mia@example.com', 'Female', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
(14, '1988-07-07', 'Liam', '0808080808', 'liam@example.com', 'Male', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
(15, '2000-12-02', 'Ella', '0865432109', 'ella@example.com', 'Female', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
(16, '1996-09-14', 'Ethan', '0878787878', 'ethan@example.com', 'Male', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
(17, '1991-05-07', 'Charlotte', '0819191919', 'charlotte@example.com', 'Female', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
(18, '2004-03-01', 'Henry', '0858585858', 'henry@example.com', 'Male', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
(19, '1999-11-11', 'Amelia', '0842424242', 'amelia@example.com', 'Female', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
(20, '1992-08-23', 'Noah', '0824242424', 'noah@example.com', 'Male', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
(21, '2002-06-06', 'Sofia', '0836363636', 'sofia@example.com', 'Female', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
(22, '1989-12-12', 'Emma', '0875757575', 'emma@example.com', 'Female', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
(23, '2003-09-09', 'Alexander', '0898989898', 'alexander@example.com', 'Male', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
(24, '1998-04-04', 'Mason', '0811111111', 'mason@example.com', 'Male', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
(25, '1995-02-02', 'Lily', '0859595959', 'lily@example.com', 'Female', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
(26, '2001-07-07', 'Daniel', '0849494949', 'daniel10@example.com', 'Male', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `airlines`
--
ALTER TABLE `airlines`
  ADD PRIMARY KEY (`airline_id`);

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `bookings`
--
ALTER TABLE `bookings`
  ADD PRIMARY KEY (`booking_id`),
  ADD KEY `flight_id` (`flight_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `cities`
--
ALTER TABLE `cities`
  ADD PRIMARY KEY (`city_id`);

--
-- Indexes for table `flights`
--
ALTER TABLE `flights`
  ADD PRIMARY KEY (`flight_id`),
  ADD KEY `airline_id` (`airline_id`),
  ADD KEY `route_id` (`route_id`),
  ADD KEY `seat_type_id` (`seat_type_id`);

--
-- Indexes for table `payments`
--
ALTER TABLE `payments`
  ADD PRIMARY KEY (`payment_id`),
  ADD UNIQUE KEY `booking_id` (`booking_id`);

--
-- Indexes for table `refund_payment`
--
ALTER TABLE `refund_payment`
  ADD PRIMARY KEY (`refund_id`),
  ADD UNIQUE KEY `payment_id` (`payment_id`);

--
-- Indexes for table `routes`
--
ALTER TABLE `routes`
  ADD PRIMARY KEY (`route_id`),
  ADD KEY `destination_city_id` (`destination_city_id`),
  ADD KEY `origin_city_id` (`origin_city_id`);

--
-- Indexes for table `seat_types`
--
ALTER TABLE `seat_types`
  ADD PRIMARY KEY (`seat_type_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `airlines`
--
ALTER TABLE `airlines`
  MODIFY `airline_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `bookings`
--
ALTER TABLE `bookings`
  MODIFY `booking_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `cities`
--
ALTER TABLE `cities`
  MODIFY `city_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `flights`
--
ALTER TABLE `flights`
  MODIFY `flight_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `payments`
--
ALTER TABLE `payments`
  MODIFY `payment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `refund_payment`
--
ALTER TABLE `refund_payment`
  MODIFY `refund_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `routes`
--
ALTER TABLE `routes`
  MODIFY `route_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `seat_types`
--
ALTER TABLE `seat_types`
  MODIFY `seat_type_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bookings`
--
ALTER TABLE `bookings`
  ADD CONSTRAINT `bookings_ibfk_1` FOREIGN KEY (`flight_id`) REFERENCES `flights` (`flight_id`),
  ADD CONSTRAINT `bookings_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);

--
-- Constraints for table `flights`
--
ALTER TABLE `flights`
  ADD CONSTRAINT `flights_ibfk_1` FOREIGN KEY (`airline_id`) REFERENCES `airlines` (`airline_id`),
  ADD CONSTRAINT `flights_ibfk_2` FOREIGN KEY (`route_id`) REFERENCES `routes` (`route_id`),
  ADD CONSTRAINT `flights_ibfk_3` FOREIGN KEY (`seat_type_id`) REFERENCES `seat_types` (`seat_type_id`);

--
-- Constraints for table `payments`
--
ALTER TABLE `payments`
  ADD CONSTRAINT `payments_ibfk_1` FOREIGN KEY (`booking_id`) REFERENCES `bookings` (`booking_id`);

--
-- Constraints for table `refund_payment`
--
ALTER TABLE `refund_payment`
  ADD CONSTRAINT `refund_payment_ibfk_1` FOREIGN KEY (`payment_id`) REFERENCES `payments` (`payment_id`);

--
-- Constraints for table `routes`
--
ALTER TABLE `routes`
  ADD CONSTRAINT `routes_ibfk_1` FOREIGN KEY (`destination_city_id`) REFERENCES `cities` (`city_id`),
  ADD CONSTRAINT `routes_ibfk_2` FOREIGN KEY (`origin_city_id`) REFERENCES `cities` (`city_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
