CREATE DATABASE IF NOT EXISTS `nmap`;

USE nmap;

CREATE TABLE IF NOT EXISTS `hosts` (
		`id` int(11) NOT NULL AUTO_INCREMENT,
		`timeofscan` datetime NOT NULL,
		`ipaddress` varchar(15) NULL,
		`hostname` varchar(40) NULL,
		`osname` varchar(200) NULL,
		`accuracy` int(4) NULL,
		PRIMARY KEY (`id`)
	) ENGINE=MyISAM DEFAULT CHARSET=utf8;
	
	CREATE TABLE IF NOT EXISTS `ports` (
		`id` int(11) NOT NULL AUTO_INCREMENT,
		`timeofscan` datetime NOT NULL,
		`ipaddress` varchar(15) NULL,
		`protocol` varchar(20) NULL,
		`portid` int(10) NULL,
		`state` varchar(20) NULL,
		`reason` varchar(20) NULL,
		`reason_ttl` int(10) NULL,
		`servicename` varchar(20) NULL,
		PRIMARY KEY (`id`)
	) ENGINE=MyISAM DEFAULT CHARSET=utf8;
	
TRUNCATE `hosts`;
TRUNCATE `ports`;	