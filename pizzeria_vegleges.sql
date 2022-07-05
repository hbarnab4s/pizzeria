-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Gép: 127.0.0.1
-- Létrehozás ideje: 2021. Nov 28. 16:31
-- Kiszolgáló verziója: 10.4.18-MariaDB
-- PHP verzió: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Adatbázis: `pizzeria`
--

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `futar`
--

CREATE TABLE `futar` (
  `futar_id` int(11) NOT NULL,
  `futar_nev` varchar(128) NOT NULL,
  `futar_jarmu` varchar(128) NOT NULL,
  `futar_ertekeles` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- A tábla adatainak kiíratása `futar`
--

INSERT INTO `futar` (`futar_id`, `futar_nev`, `futar_jarmu`, `futar_ertekeles`) VALUES
(1111, 'Asztalos János', 'Robogó', 2),
(1112, 'Katona András', 'Autó', 3),
(1114, 'Király Dóra', 'Robogó', 5),
(1115, 'Antal Béla', 'Autó', 4),
(1120, 'Jáki Benjámin', 'Robogó', 2),
(1122, 'Kovács András', 'Kerékpár', 4),
(1123, 'Buza Balázs', 'Kerékpár', 5),
(1125, 'Juhász Béla', 'Autó', 4),
(1126, 'Kővári Dániel', 'Kerékpár', 3),
(1127, 'Haiter Dominik', 'Autó', 2),
(5454, 'Kissfalvi Andor', 'Kerékpár', 2),
(5474, 'Arató Károly', 'Kerékpár', 4),
(6541, 'Asztalos János', 'Autó', 5);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `pizza`
--

CREATE TABLE `pizza` (
  `pizza_id` int(11) NOT NULL,
  `pizza_nev` varchar(128) NOT NULL,
  `pizza_ar` int(11) NOT NULL,
  `pizza_meret` int(11) NOT NULL,
  `vegetarianus` varchar(128) NOT NULL,
  `hozzavalok` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- A tábla adatainak kiíratása `pizza`
--

INSERT INTO `pizza` (`pizza_id`, `pizza_nev`, `pizza_ar`, `pizza_meret`, `vegetarianus`, `hozzavalok`) VALUES
(0, 'Négysajtos pizza', 1990, 28, 'igen', 'paradicsomos alap, mozzarella sajt, karaván sajt, camembert sajt, eidami sajt'),
(1, 'BBQ pizza', 1740, 28, 'nem', 'barbecue alap, tarja, hagyma, sajt'),
(2, 'Belga pizza', 1760, 28, 'nem', 'sajtkrémes alap, szalámi, sajt, kukorica'),
(3, 'Gyümölcsös pizza', 1740, 28, 'nem', 'paradicsomos alap, sonka, ananász, sajt'),
(4, 'Húsimádó pizza', 1790, 28, 'nem', 'húsmártásos alap, kolbász, bacon, sajt'),
(5, 'Magyaros pizza', 1740, 28, 'nem', 'paradicsomos alap, sajt, sonka, hagyma, bacon'),
(6, 'Modenani pizza', 1890, 28, 'nem', 'tejfölös alap, sonka, sajt, kukorica, hagyma'),
(7, 'Nápoly pizza', 1990, 28, 'nem', 'paradicsomos alap, csirkehús, hagyma, marinált paprika, mozzarella sajt'),
(8, 'Olympic pizza', 1740, 32, 'nem', 'tzaziki alap, csirkehús, olívia, mozzarella sajt'),
(9, 'Sonka-kukorica pizza', 1840, 28, 'nem', 'paradicsomos alap, sonka, kukorica, sajt'),
(10, 'Sonkás-gombás pizza', 1870, 28, 'nem', 'paradicsomos alap, sonka, gomba, sajt'),
(11, 'Speedy pizza', 1750, 28, 'nem', 'paradicsomos alap, sonka, szalámi, oregánó'),
(12, 'Szögedi pizza', 1740, 28, 'nem', 'paradicsomos alap, kolbász, paprika, hagyma, bacon'),
(13, 'Alexandra pizza', 1860, 28, 'nem', 'paradicsomos alap, sonka, kukorica, sajt, ananász'),
(14, 'Americano pizza', 1690, 28, 'nem', 'paradicsomos alap, csirkehús, mozzarella, bacon'),
(15, 'Calzone pizza', 1940, 28, 'nem', 'sajtkrémes alap, fűszeres csirkehús, mozzarella, bacon'),
(16, 'Don Donato pizza', 2690, 32, 'nem', 'fokhagymás-tejfölös alap, kukorica, tarja, bacon, sajt'),
(17, 'Margaretha pizza', 1890, 32, 'igen', 'paradicsomos alap, sajt, paradicsom'),
(18, 'Tarjás pizza', 1940, 32, 'nem', 'paradicsomos alap, tarja, mozzarella, sajt'),
(19, 'Vegetáriánus pizza', 2090, 32, 'igen', 'paradicsomos alap, gomba, paprika, hagyma, zöld olivabogyó, mozzarella sajt'),
(20, '2x2 évszak pizza', 1850, 32, 'nem', 'paradicsomos alap, gomba, kukorica, bacon, sonka, mozzarella sajt'),
(21, 'Bolognai pizza', 1990, 32, 'nem', 'paradicsomos alap, bolognai ragu, hagyma, mozzarella sajt'),
(22, 'Shon-Goo-Kun pizza', 2200, 32, 'nem', 'paradicsomos alap, sonka, gomba, kukorica, mozzarella sajt'),
(23, 'Carbonara pizza', 2591, 32, 'nem', 'tejfölös - fokhagymás alap, tojás, parmezán sajt, mozzarella sajt, carbonara ragu'),
(1111, 'Bud Spencer kedvence pizza', 3650, 32, 'nem', 'paradicsomos alap, bab, hagyma, bacon szalonna, sajt');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `rendeles`
--

CREATE TABLE `rendeles` (
  `rendeles_id` int(11) NOT NULL,
  `email` varchar(128) NOT NULL,
  `pizza_nev` varchar(128) NOT NULL,
  `rendeles_ev` int(11) NOT NULL,
  `rendeles_honap` varchar(128) NOT NULL,
  `rendeles_nap` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- A tábla adatainak kiíratása `rendeles`
--

INSERT INTO `rendeles` (`rendeles_id`, `email`, `pizza_nev`, `rendeles_ev`, `rendeles_honap`, `rendeles_nap`) VALUES
(0, 'hitesbarnus@gmail.com', 'Négysajtos pizza', 2019, 'Február', 4),
(1, 'hitesbeni@gmail.com', 'Bud Spencer kedvence pizza', 2020, 'Április', 3),
(2, 'hitesbarnus@gmail.com', 'BBQ pizza', 2019, 'Május', 8),
(4, 'bandi@gmail.com', 'Olympic pizza', 2018, 'Február', 18),
(5, 'konczbern@citromail.hu', 'Alexandra pizza', 2021, 'Február', 4),
(6, 'benwolf@gmail.com', 'Gyümölcsös pizza', 2018, 'Február', 7),
(7, 'feketekrisz@gmail.com', 'Négysajtos pizza', 2021, 'Július', 3),
(8, 'osig@gmail.com', 'Olympic pizza', 2020, 'Február', 26),
(9, 'harmlev@freemail.com', 'Sonkás-gombás pizza', 2019, 'Május', 14),
(10, 'hitesbeni@gmail.com', 'Négysajtos pizza', 2021, 'Július', 11),
(11, 'aranyospali@gmail.com', 'Nápoly pizza', 2021, 'Április', 7),
(12, 'hitesbarnus@gmail.com', 'Alexandra pizza', 2020, 'Június', 9),
(13, 'hites.gabor@gmail.com', 'Margaretha pizza', 2021, 'Szeptember', 9),
(14, 'harkalykincses@citromail.hu', 'Gyümölcsös pizza', 2020, 'Május', 19),
(29, 'hitesbarnus@gmail.com', 'Négysajtos pizza', 2020, 'Január', 3),
(55, 'hitesbeni@gmail.com', 'Americano pizza', 2020, 'Május', 15),
(56, 'jani.jani@citromail.hu', 'Négysajtos pizza', 2019, 'Január', 23),
(57, 'hatlabaskata@gmail.com', 'Négysajtos pizza', 2018, 'Január', 11),
(58, 'andrastoth@gmail.com', 'Shon-Goo-Kun pizza', 2019, 'Szeptember', 21),
(59, 'kanyaandi@freemail.hu', 'Vegetáriánus pizza', 2020, 'Szeptember', 24),
(60, 'adamgungl@gmail.com', 'Speedy pizza', 2021, 'Október', 20),
(61, 'horvathpeter@freemail.hu', 'Vegetáriánus pizza', 2021, 'November', 18),
(62, 'hitesbarnus@gmail.com', 'Gyümölcsös pizza', 2020, 'Április', 5),
(63, 'makkosambrus@gmail.com', 'Négysajtos pizza', 2021, 'November', 27),
(64, 'hitesbeni@gmail.com', 'Olympic pizza', 2020, 'Május', 10),
(65, 'hitesv@gmail.com', 'Margaretha pizza', 2021, 'November', 28),
(66, 'godeimre@gmail.com', 'Négysajtos pizza', 2019, 'Március', 9),
(67, 'tothbalint@gmail.com', 'Nápoly pizza', 2021, 'Április', 10),
(68, 'osig@gmail.com', 'Shon-Goo-Kun pizza', 2021, 'November', 21);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `szakacs`
--

CREATE TABLE `szakacs` (
  `szakacs_id` int(11) NOT NULL,
  `szakacs_nev` varchar(128) NOT NULL,
  `szakacs_fizetes` int(16) NOT NULL,
  `szakacs_ertekeles` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- A tábla adatainak kiíratása `szakacs`
--

INSERT INTO `szakacs` (`szakacs_id`, `szakacs_nev`, `szakacs_fizetes`, `szakacs_ertekeles`) VALUES
(2346, 'Kun Attila', 415690, 3),
(2347, 'Nemkreatív Béla', 199874, 4),
(2348, 'Karácsonyi Attila', 289700, 4),
(2349, 'Takács Dorka', 339478, 5),
(2350, 'Csurdi Donát', 239500, 4),
(2352, 'Szabó Dániel', 245870, 4),
(2355, 'Mucsi Erika', 323400, 5),
(5427, 'Halas János', 327956, 4),
(7854, 'Kovács Béla', 114235, 3),
(9876, 'Angyalföldi Béla', 191213, 3);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `szallitas`
--

CREATE TABLE `szallitas` (
  `szallitas_id` int(11) NOT NULL,
  `pizza_id` int(11) NOT NULL,
  `futar_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- A tábla adatainak kiíratása `szallitas`
--

INSERT INTO `szallitas` (`szallitas_id`, `pizza_id`, `futar_id`) VALUES
(0, 1, 1111),
(1, 0, 6541),
(2, 3, 1112),
(3, 17, 1115),
(4, 13, 5454),
(5, 2, 1114),
(6, 6, 6541),
(7, 3, 1113),
(8, 0, 1111),
(9, 1111, 1127),
(10, 22, 1126);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `ugyfel`
--

CREATE TABLE `ugyfel` (
  `email` varchar(128) NOT NULL,
  `nev` varchar(128) NOT NULL,
  `telefonszam` varchar(128) NOT NULL,
  `varos` varchar(128) NOT NULL,
  `utca` varchar(128) NOT NULL,
  `hazszam` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- A tábla adatainak kiíratása `ugyfel`
--

INSERT INTO `ugyfel` (`email`, `nev`, `telefonszam`, `varos`, `utca`, `hazszam`) VALUES
('adamgungl@gmail.com', 'Gungl Ádám', '+36204715962', 'Budapest', 'Heves utca', '48'),
('andrastoth@gmail.com', 'Tóth András', '+36208975643', 'Szeged', 'Körtöltés utca', '33'),
('angyal.janos@freemail.hu', 'Angyal János Béla', '+36201698721', 'Balatonszemes', 'Diós utca', '3'),
('aranyospali@gmail.com', 'Aranyos Pál', '+36308945623', 'Budapest', 'Pál utca', '16'),
('bandi@gmail.com', 'Antal András', '+36201369874', 'Szeged', 'Péncél köz', '3'),
('benwolf@gmail.com', 'Farkas Bence', '+36207415629', 'Veszprém', 'Ibolya utca', '19'),
('feketekrisz@gmail.com', 'Fekete Krisztián', '+36309994545', 'Szeged', 'Ács utca', '14'),
('fogasfeco11@gmail.com', 'Fogas Ferenc', '+30508826414', 'Szeged', 'Eper utca', '1'),
('godeimre@gmail.com', 'Göde Imre', '+36205876632', 'Szeged', 'Lengyel utca', '8'),
('hangyaldavid@gmail.com', 'Hangyál Dávid', '+36205478923', 'Szeged', 'Szent László utca', '18'),
('harkalykincses@citromail.hu', 'Harkály Kincses', '+36507845621', 'Szeged', 'Boldogasszony sugárút', '36'),
('harmlev@freemail.com', 'Harmatos Levente', '+36204523987', 'Székesfehérvár', 'Mikes Kelemen utca', '9'),
('hatlabaskata@gmail.com', 'Hatlábas Kata', '+36228975624', 'Székesfehérvár', 'Zrínyi utca', '13'),
('henczeszter@gmail.com', 'Hencz Eszter', '+36307718954', 'Szeged', 'Tölgyfa utca', '11'),
('hites.gabor@gmail.com', 'Hites Gábor', '+36309612012', 'Zichyújfalu', 'Ady Endre utca', '2'),
('hitesbarnus@gmail.com', 'Hites Barnabás', '+36308251447', 'Szeged', 'Pécskai utca', '8'),
('hitesbeni@gmail.com', 'Hites Benjamin', '+36202262019', 'Szeged', 'Sólyom utca', '8 2/1'),
('hitesv@gmail.com', 'Hitesné Forstner Valéria', '+36205697450', 'Zichyújfalu', 'Ady Endre utca', '2'),
('horvathpeter@freemail.hu', 'Horváth Péter', '+36221456978', 'Szeged', 'Boldogasszony sugárút', '139'),
('jani.jani@citromail.hu', 'Jani János', '+368974512', 'Székesfehérvár', 'Prohászka Ottokár utca', '81 3/2'),
('jozsaanasztazia@gmail.com', 'Józsa Anasztázia', '+36509635454', 'Szeged', 'Bor utca', '1'),
('kanyaandi@freemail.hu', 'Kánya Andrea', '+36307458932', 'Szeged', 'Zászló utca', '28'),
('kelemenkatalin@gmail.com', 'Kelemen Katalin', '+36205542299', 'Szeged', 'Levél utca', '4'),
('konczbern@citromail.hu', 'Koncz Bernadett', '+36309856314', 'Szeged', 'Sőtér István köz', '9'),
('koosgabor@gmail.com', 'Koós Gábor', '+36508896541', 'Szeged', 'Holló utca', '9'),
('kovacskristof@gmail.com', 'Kovács Kristóf', '+36307774466', 'Szeged', 'Baktói utca', '16'),
('lazarborci@gmail.com', 'Lázár Bíborka', '++36507746612', 'Székesfehérvár', 'Tóvárosi lakónegyed', '34 4/2'),
('makkosambrus@gmail.com', 'Makkos Ambrus', '+36309875648', 'Fót', 'Táncsis Mihály utca', '14'),
('makkosmarcellilles@gmail.com', 'Makkos Marcell Illés', '+36508452266', 'Szeged', 'Alma utca', '12'),
('markuseszter@gmail.com', 'Márkus Eszter', '+36508845656', 'Szeged', 'Népdal utca', '3'),
('molnarbalint@gmail.com', 'Molnár Bálint', '+36208856652', 'Szeged', 'Közép fasor', '21'),
('osig@gmail.com', 'Osváth Gergely', '+36504783322', 'Szeged', 'Csuka utca', '10'),
('palkovicsaba@gmail.com', 'Palkovics Csaba', '+36309963354', 'Szeged', 'Szilva utca', '19'),
('rajkijanos@gmail.com', 'Rajki János', '+36309997486', 'Szeged', 'Pázsit utca', '2'),
('ridegjudit@gmail.com', 'Rideg Judit', '+36504446633', 'Szeged', 'Alma utca', '23'),
('rozsbotond@gmail.com', 'Rozs Botond', '+36508541296', 'Szeged', 'Bodzafa utca', '3'),
('spaniczisti@citromail.hu', 'Spánicz István', '+36208894433', 'Szeged', 'Körte utca', '19'),
('szabotimi@gmail.com', 'Szabó Eszter Tímea', '+36208885566', 'Szeged', 'Sárközi utca', '7'),
('szakalbianka@gamil.com', 'Szakál Bianka', '+36504719825', 'Szeged', 'Árvíz utca', '7'),
('szarkaendere@gmail.com', 'Szarka Endre', '+36308745653', 'Szeged', 'Margaréta utca', '18'),
('szucsdave@gmail.com', 'Szücs Dávid', '+36508741253', 'Szeged', 'Kukorica utca', '8'),
('tekerilles@gmail.com', 'Teker Illés', '+36305556633', 'Szeged', 'Csuka utca', '6'),
('tothbalint@gmail.com', 'Tóth Bálint', '+36307896655', 'Székesfehérvár', 'Kossuth Lajos utca', '62'),
('vidagabor@gmail.com', 'Vida Gábor', '+36209976413', 'Szeged', 'Gém utca', '11'),
('zsamolyandi@gmail.com', 'Zsámoly Andrea', '+36205419832', 'Debrecen', 'Szent Anna utca', '26');

--
-- Indexek a kiírt táblákhoz
--

--
-- A tábla indexei `futar`
--
ALTER TABLE `futar`
  ADD PRIMARY KEY (`futar_id`);

--
-- A tábla indexei `pizza`
--
ALTER TABLE `pizza`
  ADD PRIMARY KEY (`pizza_id`);

--
-- A tábla indexei `rendeles`
--
ALTER TABLE `rendeles`
  ADD PRIMARY KEY (`rendeles_id`),
  ADD KEY `email` (`email`),
  ADD KEY `pizza_nev` (`pizza_nev`);

--
-- A tábla indexei `szakacs`
--
ALTER TABLE `szakacs`
  ADD PRIMARY KEY (`szakacs_id`);

--
-- A tábla indexei `szallitas`
--
ALTER TABLE `szallitas`
  ADD PRIMARY KEY (`szallitas_id`),
  ADD KEY `pizza_id` (`pizza_id`),
  ADD KEY `futar_id` (`futar_id`);

--
-- A tábla indexei `ugyfel`
--
ALTER TABLE `ugyfel`
  ADD PRIMARY KEY (`email`);

--
-- Megkötések a kiírt táblákhoz
--

--
-- Megkötések a táblához `rendeles`
--
ALTER TABLE `rendeles`
  ADD CONSTRAINT `rendeles_ibfk_1` FOREIGN KEY (`email`) REFERENCES `ugyfel` (`email`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
