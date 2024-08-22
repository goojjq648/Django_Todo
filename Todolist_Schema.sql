
CREATE DATABASE IF NOT EXISTS `tododb`;
USE `tododb`;

CREATE TABLE IF NOT EXISTS `todolist` (
  `todo_id` int NOT NULL AUTO_INCREMENT,
  `completed` int NOT NULL DEFAULT '0',
  `todo` varchar(20) NOT NULL,
  `last_update` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`todo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
