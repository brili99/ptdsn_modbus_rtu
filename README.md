# Mod Bus RTU PTDSN
listening directly data from modbus rtu PLC then log it

menggunakan image 2022-01-28-raspios-buster-armhf atau raspi versi buster

#tata cara instalasi
```sh
sudo apt update
sudo apt install apache2 php mariadb-server php7.3-mysql
sudo mysql_secure_installation
sudo chmod -R 777 /var/www/html
cd /var/www/html
rm index.html
wget https://files.phpmyadmin.net/phpMyAdmin/5.1.3/phpMyAdmin-5.1.3-all-languages.zip
unzip phpMyAdmin-5.1.3-all-languages.zip
rm phpMyAdmin-5.1.3-all-languages.zip
```

#inisialisasi database mysql
```sql
CREATE USER 'ptdsn_admin'@'localhost' IDENTIFIED BY 'bismillah';
GRANT ALL PRIVILEGES ON *.* TO 'ptdsn_admin'@'localhost';

CREATE DATABASE ptdsn;
USE ptdsn;

CREATE TABLE `status`(
    `vid` INT PRIMARY KEY AUTO_INCREMENT,
    `updated` TIMESTAMP,
    `nama` VARCHAR(200) NOT NULL,
    `nilai` FLOAT NOT NULL
);

CREATE TABLE `log` (
`lid` INT PRIMARY KEY AUTO_INCREMENT,
`created` TIMESTAMP,
`nama` VARCHAR(200) NOT NULL,
`nilai` FLOAT NOT NULL
);

INSERT INTO `status` (nama, nilai) VALUES 
('1','1'),
('2','1'),
('3','1'),
('4','1'),
('5','1'),
('6','1'),
('7','1'),
('8','1');
```
