-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 25 Des 2024 pada 13.32
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gameverse_store`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `karyawan`
--

CREATE TABLE `karyawan` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `position` varchar(50) NOT NULL,
  `salary` int(11) NOT NULL,
  `hire_date` date NOT NULL,
  `contact_number` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `karyawan`
--

INSERT INTO `karyawan` (`id`, `name`, `position`, `salary`, `hire_date`, `contact_number`) VALUES
(1, 'ryan', 'Kasir', 4000000, '2023-01-15', '081234567890'),
(2, 'anggino', 'Manajer', 8000000, '2022-06-01', '082345678901'),
(3, 'fais', 'Staf Penjualan', 5000000, '2024-02-01', '085678901234'),
(4, 'hardi', 'Staf Gudang', 3500000, '2023-03-10', '083456789012');

-- --------------------------------------------------------

--
-- Struktur dari tabel `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `price` int(11) NOT NULL,
  `stock` int(11) NOT NULL,
  `image_path` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `products`
--

INSERT INTO `products` (`id`, `name`, `price`, `stock`, `image_path`) VALUES
(60, 'Cyberpunk 2077', 750000, 4, NULL),
(61, 'The Witcher 3', 350000, 14, NULL),
(62, 'Elden Ring', 800000, 20, NULL),
(63, 'God of War', 600000, 12, NULL),
(64, 'Hogwarts Legacy', 650000, 18, NULL),
(65, 'FIFA 24', 700000, 25, NULL),
(66, 'Assassin\'s Creed Mirage', 750000, 29, NULL),
(67, 'Call of Duty: Modern Warfare 2', 850000, 22, NULL),
(68, 'Spider-Man 2', 900000, 5, NULL),
(69, 'Red Dead Redemption 2', 400000, 14, NULL),
(70, 'GTA V', 500000, 30, NULL),
(71, 'Valorant', 0, 100, NULL),
(72, 'League of Legends', 0, 100, NULL),
(73, 'Overwatch 2', 450000, 50, NULL),
(74, 'Starfield', 950000, 15, NULL),
(75, 'Baldur\'s Gate 3', 850000, 20, NULL),
(76, 'Diablo IV', 900000, 10, NULL),
(77, 'Far Cry 6', 700000, 23, NULL),
(78, 'Mortal Kombat 11', 550000, 34, NULL),
(79, 'Apex Legends', 0, 100, NULL),
(80, 'PUBG', 400000, 40, NULL),
(81, 'Fortnite', 0, 100, NULL),
(82, 'Minecraft', 300000, 50, NULL),
(83, 'Roblox', 0, 75, NULL),
(84, 'Among Us', 60000, 70, NULL),
(85, 'Hades', 300000, 40, NULL),
(86, 'Hollow Knight', 150000, 60, NULL),
(87, 'Celeste', 200000, 53, NULL),
(88, 'Stardew Valley', 120000, 79, NULL),
(89, 'The Sims 4', 250000, 35, NULL),
(90, 'Planet Zoo', 350000, 25, NULL),
(91, 'Cities: Skylines', 300000, 30, NULL),
(92, 'Forza Horizon 5', 950000, 14, NULL),
(93, 'Gran Turismo 7', 850000, 20, NULL),
(94, 'Doom Eternal', 600000, 15, NULL),
(95, 'Death Stranding', 750000, 12, NULL),
(96, 'Resident Evil 4 Remake', 850000, 19, NULL),
(97, 'Silent Hill 2 Remake', 900000, 8, NULL),
(98, 'Metal Gear Solid V', 450000, 25, NULL),
(99, 'Final Fantasy XVI', 950000, 9, NULL),
(100, 'Pokemon Scarlet', 700000, 20, NULL),
(101, 'Animal Crossing: New Horizons', 600000, 15, NULL),
(102, 'Super Smash Bros. Ultimate', 750000, 18, NULL),
(103, 'The Legend of Zelda: Tears of the Kingdom', 850000, 10, NULL),
(104, 'Mario Kart 8 Deluxe', 650000, 30, NULL),
(105, 'Splatoon 3', 750000, 20, NULL),
(106, 'Metroid Prime Remastered', 650000, 25, NULL),
(107, 'Fire Emblem: Three Houses', 700000, 10, NULL),
(108, 'Bayonetta 3', 850000, 14, NULL),
(109, 'Xenoblade Chronicles 3', 800000, 20, NULL);

-- --------------------------------------------------------

--
-- Struktur dari tabel `sales`
--

CREATE TABLE `sales` (
  `id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `total_price` int(11) NOT NULL,
  `sale_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `sales`
--

INSERT INTO `sales` (`id`, `product_id`, `quantity`, `total_price`, `sale_date`, `created_at`) VALUES
(27, 83, 25, 0, '2024-12-16 12:25:16', '2024-12-17 12:51:27'),
(28, 60, 1, 750000, '2024-12-16 15:24:56', '2024-12-17 12:51:27'),
(29, 60, 4, 3000000, '2024-12-16 17:55:21', '2024-12-17 12:51:27'),
(30, 68, 3, 2700000, '2024-12-17 12:35:08', '2024-12-17 12:51:27'),
(31, 107, 2, 1400000, '2024-12-17 14:17:30', '2024-12-17 14:17:30'),
(32, 94, 1, 600000, '2024-12-17 14:18:20', '2024-12-17 14:18:20'),
(33, 94, 1, 600000, '2024-12-17 14:19:52', '2024-12-17 14:19:52'),
(34, 94, 1, 600000, '2024-12-17 15:10:28', '2024-12-17 15:10:28'),
(35, 108, 1, 850000, '2024-12-17 18:33:24', '2024-12-17 18:33:24'),
(36, 60, 1, 750000, '2024-12-17 18:34:46', '2024-12-17 18:34:46'),
(37, 108, 1, 850000, '2024-12-17 18:37:36', '2024-12-17 18:37:36'),
(38, 108, 1, 850000, '2024-12-17 18:54:48', '2024-12-17 18:54:48'),
(39, 108, 1, 850000, '2024-12-17 18:55:03', '2024-12-17 18:55:03'),
(40, 61, 1, 350000, '2024-12-17 18:59:42', '2024-12-17 18:59:42'),
(41, 78, 1, 550000, '2024-12-17 19:08:07', '2024-12-17 19:08:07'),
(42, 92, 1, 950000, '2024-12-17 19:11:41', '2024-12-17 19:11:41'),
(43, 77, 1, 700000, '2024-12-17 19:13:32', '2024-12-17 19:13:32'),
(44, 87, 2, 400000, '2024-12-17 19:17:16', '2024-12-17 19:17:16'),
(45, 99, 1, 950000, '2024-12-18 19:59:38', '2024-12-18 19:59:38'),
(46, 88, 1, 120000, '2024-12-18 20:02:19', '2024-12-18 20:02:19'),
(47, 96, 1, 850000, '2024-12-18 20:35:12', '2024-12-18 20:35:12'),
(48, 66, 1, 750000, '2024-12-18 20:35:29', '2024-12-18 20:35:29'),
(49, 97, 2, 1800000, '2024-12-19 07:17:33', '2024-12-19 07:17:33'),
(50, 77, 1, 700000, '2024-12-19 08:21:22', '2024-12-19 08:21:22');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `karyawan`
--
ALTER TABLE `karyawan`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `sales`
--
ALTER TABLE `sales`
  ADD PRIMARY KEY (`id`),
  ADD KEY `product_id` (`product_id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `karyawan`
--
ALTER TABLE `karyawan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `products`
--
ALTER TABLE `products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=114;

--
-- AUTO_INCREMENT untuk tabel `sales`
--
ALTER TABLE `sales`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `sales`
--
ALTER TABLE `sales`
  ADD CONSTRAINT `sales_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
