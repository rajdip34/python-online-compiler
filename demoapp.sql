-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: demoapp
-- ------------------------------------------------------
-- Server version	5.7.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add index',7,'add_index'),(20,'Can change index',7,'change_index'),(21,'Can delete index',7,'delete_index'),(22,'Can add country',8,'add_country'),(23,'Can change country',8,'change_country'),(24,'Can delete country',8,'delete_country'),(25,'Can add calendar',9,'add_calendar'),(26,'Can change calendar',9,'change_calendar'),(27,'Can delete calendar',9,'delete_calendar'),(28,'Can add calendarholiday',10,'add_calendarholiday'),(29,'Can change calendarholiday',10,'change_calendarholiday'),(30,'Can delete calendarholiday',10,'delete_calendarholiday'),(31,'Can add currency',11,'add_currency'),(32,'Can change currency',11,'change_currency'),(33,'Can delete currency',11,'delete_currency');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$36000$EpbnwEmwKfvr$8/r+pXEtHcQQt5FEglxF45inGaxRpk1VOWZuo43W4DU=','2019-03-30 04:56:48.967933',1,'admin','','','azzu.25@gmail.com',1,1,'2019-03-30 04:53:50.578883');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `calendar`
--

DROP TABLE IF EXISTS `calendar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `calendar` (
  `Id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  `ModifyDateTime` datetime(6) NOT NULL,
  `ModifyUserid` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `calendar_ModifyUserid_3e3626a9_fk_auth_user_id` (`ModifyUserid`),
  CONSTRAINT `calendar_ModifyUserid_3e3626a9_fk_auth_user_id` FOREIGN KEY (`ModifyUserid`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `calendar`
--

LOCK TABLES `calendar` WRITE;
/*!40000 ALTER TABLE `calendar` DISABLE KEYS */;
INSERT INTO `calendar` VALUES (1,'Test','2019-03-30 08:29:14.309456',1);
/*!40000 ALTER TABLE `calendar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `calendarholiday`
--

DROP TABLE IF EXISTS `calendarholiday`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `calendarholiday` (
  `Id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  `HolidayDate` date NOT NULL,
  `ModifyDateTime` datetime(6) NOT NULL,
  `CalendarID` bigint(20) NOT NULL,
  `ModifyUserid` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `calendarholiday_CalendarID_HolidayDate_e6a3e29c_uniq` (`CalendarID`,`HolidayDate`),
  KEY `calendarholiday_ModifyUserid_30d6a2ea_fk_auth_user_id` (`ModifyUserid`),
  CONSTRAINT `calendarholiday_CalendarID_c49c59fb_fk_calendar_Id` FOREIGN KEY (`CalendarID`) REFERENCES `calendar` (`Id`),
  CONSTRAINT `calendarholiday_ModifyUserid_30d6a2ea_fk_auth_user_id` FOREIGN KEY (`ModifyUserid`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `calendarholiday`
--

LOCK TABLES `calendarholiday` WRITE;
/*!40000 ALTER TABLE `calendarholiday` DISABLE KEYS */;
/*!40000 ALTER TABLE `calendarholiday` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `country`
--

DROP TABLE IF EXISTS `country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `country` (
  `Id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `ModifyUserid` int(11) DEFAULT NULL,
  `ModifyDateTime` datetime(6) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `Fk_country_auth_user_de4577d` (`ModifyUserid`),
  CONSTRAINT `country_ibfk_1` FOREIGN KEY (`ModifyUserid`) REFERENCES `auth_user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `country`
--

LOCK TABLES `country` WRITE;
/*!40000 ALTER TABLE `country` DISABLE KEYS */;
INSERT INTO `country` VALUES (1,'United States',1,'2016-05-03 00:00:00.000000'),(2,'France',1,'2016-06-13 14:57:50.547000'),(3,'United Kingdom',1,'2016-06-13 14:57:50.610000'),(4,'Italy',1,'2016-06-13 14:57:50.610000'),(5,'Germany',1,'2016-06-13 14:57:50.630000'),(6,'Denmark',1,'2016-06-13 14:57:50.630000'),(7,'Spain',1,'2016-06-13 14:57:50.630000'),(8,'Switzerland',1,'2016-06-13 14:57:50.630000'),(9,'Netherlands',1,'2016-06-13 14:57:50.630000'),(10,'Sweden',1,'2016-06-13 14:57:50.633000'),(11,'Norway',1,'2016-06-13 14:57:50.633000'),(12,'Belgium',1,'2016-06-13 14:57:50.633000'),(13,'Russia',1,'2016-06-13 14:57:50.637000'),(14,'Turkey',1,'2016-06-13 14:57:50.637000'),(15,'Poland',1,'2016-06-13 14:57:50.637000'),(16,'Ireland',1,'2016-06-13 14:57:50.640000'),(17,'Austria',1,'2016-06-13 14:57:50.640000'),(18,'Czech Republic',1,'2016-06-13 14:57:50.660000'),(19,'Portugal',1,'2016-06-13 14:57:50.660000'),(20,'Hungary',1,'2016-06-13 14:57:50.660000'),(21,'Finland',1,'2016-06-13 14:57:50.660000'),(22,'Netherlands',1,'2016-06-13 14:57:50.660000'),(23,'Romania',1,'2016-06-13 14:57:50.660000'),(24,'Bulgaria',1,'2016-06-18 14:42:01.157000'),(25,'LUXEMBOURG',1,'2016-07-22 00:00:00.000000'),(27,'Greece',1,'2016-07-22 00:00:00.000000'),(28,'CROATIA',1,'2016-07-22 00:00:00.000000'),(29,'Canada',1,'2018-02-01 00:00:00.000000'),(30,'ISRAEL',1,'2018-02-01 00:00:00.000000'),(31,'Japan',1,'2018-05-19 00:00:00.000000');
/*!40000 ALTER TABLE `country` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `currency`
--

DROP TABLE IF EXISTS `currency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `currency` (
  `Id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Name` varchar(3) NOT NULL,
  `description` varchar(50) NOT NULL,
  `ModifyUserid` int(11) DEFAULT NULL,
  `ModifyDateTime` datetime(6) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `Fk_currency_auth_user_w3456` (`ModifyUserid`),
  CONSTRAINT `currency_ibfk_1` FOREIGN KEY (`ModifyUserid`) REFERENCES `auth_user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `currency`
--

LOCK TABLES `currency` WRITE;
/*!40000 ALTER TABLE `currency` DISABLE KEYS */;
INSERT INTO `currency` VALUES (1,'USD','US Dollar',1,'2016-05-02 00:00:00.000000'),(2,'GBP','Pounds',1,'2016-05-12 00:00:00.000000'),(3,'EUR','EUROS',1,'2016-06-13 15:15:34.957000'),(4,'DKK','Denmark',1,'2016-06-13 15:15:34.960000'),(5,'CHF','Switzerland',1,'2016-06-13 15:15:34.960000'),(6,'SEK','Sweden',1,'2016-06-13 15:15:34.960000'),(7,'NOK','Norway',1,'2016-06-13 15:15:34.960000'),(8,'RUB','Russia',1,'2016-06-13 15:15:34.960000'),(9,'TRY','Turkey',1,'2016-06-13 15:15:34.960000'),(10,'PLN','Poland',1,'2016-06-13 15:15:34.960000'),(11,'CZK','Czech Republic',1,'2016-06-13 15:15:34.963000'),(12,'HUF','Hungary',1,'2016-06-13 15:15:34.963000'),(13,'RON','Romania',1,'2016-06-13 15:15:34.963000'),(14,'HRK','HRK',1,'2016-06-26 00:00:00.000000'),(15,'JPY','JAPAN',1,'2018-01-31 00:00:00.000000'),(16,'BGN','BULGARIA',1,'2018-01-31 00:00:00.000000'),(17,'AUD','AUSTRALIA',1,'2018-01-31 00:00:00.000000'),(18,'BRL','BRAZIL',1,'2018-01-31 00:00:00.000000'),(19,'CAD','CANADA',1,'2018-01-31 00:00:00.000000'),(20,'CNY','CHINA',1,'2018-01-31 00:00:00.000000'),(21,'HKD','HONG KONG',1,'2018-01-31 00:00:00.000000'),(22,'IDR','INDONESIA',1,'2018-01-31 00:00:00.000000'),(23,'INR','BHUTAN',1,'2018-01-31 00:00:00.000000'),(24,'KRW','KOREA (THE REPUBLIC OF)',1,'2018-01-31 00:00:00.000000'),(25,'MXN','MEXICO',1,'2018-01-31 00:00:00.000000'),(26,'MYR','MALAYSIA',1,'2018-01-31 00:00:00.000000'),(27,'NZD','COOK ISLANDS (THE)',1,'2018-01-31 00:00:00.000000'),(28,'PHP','PHILIPPINES (THE)',1,'2018-01-31 00:00:00.000000'),(29,'SGD','SINGAPORE',1,'2018-01-31 00:00:00.000000'),(30,'THB','THAILAND',1,'2018-01-31 00:00:00.000000'),(31,'ZAR','LESOTHO',1,'2018-01-31 00:00:00.000000'),(32,'ILS','ISRAEL',1,'2018-01-31 00:00:00.000000'),(33,'CAD','Canadian Dollar',1,'2018-02-01 00:00:00.000000'),(34,'GBp','GBP Penny',1,'2018-02-01 00:00:00.000000');
/*!40000 ALTER TABLE `currency` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2019-03-30 08:29:14.460258','1','1-Test',1,'[{\"added\": {}}]',9,1),(2,'2019-03-30 08:30:06.474203','1','1-Test',1,'[{\"added\": {}}]',7,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(9,'calendar','calendar'),(10,'calendarholiday','calendarholiday'),(5,'contenttypes','contenttype'),(8,'country','country'),(11,'currency','currency'),(7,'index','index'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-03-30 04:49:17.853829'),(2,'auth','0001_initial','2019-03-30 04:49:36.201584'),(3,'admin','0001_initial','2019-03-30 04:49:39.578309'),(4,'admin','0002_logentry_remove_auto_add','2019-03-30 04:49:39.714035'),(5,'contenttypes','0002_remove_content_type_name','2019-03-30 04:49:41.863350'),(6,'auth','0002_alter_permission_name_max_length','2019-03-30 04:49:42.010075'),(7,'auth','0003_alter_user_email_max_length','2019-03-30 04:49:42.188255'),(8,'auth','0004_alter_user_username_opts','2019-03-30 04:49:42.241640'),(9,'auth','0005_alter_user_last_login_null','2019-03-30 04:49:42.979293'),(10,'auth','0006_require_contenttypes_0002','2019-03-30 04:49:43.023952'),(11,'auth','0007_alter_validators_add_error_messages','2019-03-30 04:49:43.077547'),(12,'auth','0008_alter_user_username_max_length','2019-03-30 04:49:43.224708'),(13,'sessions','0001_initial','2019-03-30 04:49:44.205027'),(14,'calendar','0001_initial','2019-03-30 04:51:56.000850'),(15,'calendarholiday','0001_initial','2019-03-30 04:52:06.988633'),(16,'country','0001_initial','2019-03-30 04:52:11.750815'),(17,'currency','0001_initial','2019-03-30 04:52:16.238060'),(18,'index','0001_initial','2019-03-30 04:52:32.414977');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('avea8327lblsum7x70i1n8ifm7rlni6g','YTEwZTUyNjcxZTQzZDU4ZjJkM2I0ZGJmOTU3YWQ1OGIwNzU1YTg1Yjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0ZjdlN2YyNDVhNWI4YzZjZTQ1YzljYzFmN2EzZDhmMjZlNjVmNTczIn0=','2019-04-13 04:56:49.283790');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index`
--

DROP TABLE IF EXISTS `index`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `index` (
  `Id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  `BloombergTicker` varchar(50) NOT NULL,
  `ReutersRic` varchar(50) NOT NULL,
  `BloombergID` varchar(50) NOT NULL,
  `ModifyDateTime` datetime(6) NOT NULL,
  `Active` int(11) DEFAULT NULL,
  `customindex` int(11) DEFAULT NULL,
  `customindexconfiguration` varchar(20000) DEFAULT NULL,
  `CurrencyId` bigint(20) NOT NULL,
  `ModifyUserid` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `index_CurrencyId_128079e4_fk_currency_Id` (`CurrencyId`),
  KEY `index_ModifyUserid_250972e9_fk_auth_user_id` (`ModifyUserid`),
  CONSTRAINT `index_CurrencyId_128079e4_fk_currency_Id` FOREIGN KEY (`CurrencyId`) REFERENCES `currency` (`Id`),
  CONSTRAINT `index_ModifyUserid_250972e9_fk_auth_user_id` FOREIGN KEY (`ModifyUserid`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index`
--

LOCK TABLES `index` WRITE;
/*!40000 ALTER TABLE `index` DISABLE KEYS */;
INSERT INTO `index` VALUES (1,'Test','t','t','2','2019-03-30 08:30:06.464738',1,1,'1',1,1);
/*!40000 ALTER TABLE `index` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-30 15:35:44
