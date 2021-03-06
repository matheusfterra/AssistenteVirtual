-- MySQL Script generated by MySQL Workbench
-- Sun Mar 28 00:39:30 2021
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema assistente
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema assistente
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `assistente` DEFAULT CHARACTER SET utf8 ;
USE `assistente` ;

-- -----------------------------------------------------
-- Table `assistente`.`received_message_logs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `assistente`.`received_message_logs` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `userFrom` VARCHAR(45) NULL,
  `message` VARCHAR(500) NULL,
  `replied` TINYINT NULL DEFAULT 0,
  `registeredAt` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `receivedAt` TIMESTAMP NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `assistente`.`sent_message_logs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `assistente`.`sent_message_logs` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `userTo` VARCHAR(45) NULL,
  `message` VARCHAR(500) NULL,
  `isReply` TINYINT NULL,
  `received_message_logs_id` INT NULL,
  `registeredAt` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `sentAt` TIMESTAMP NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_sent_message_logs_received_message_logs_idx` (`received_message_logs_id` ASC) VISIBLE,
  CONSTRAINT `fk_sent_message_logs_received_message_logs`
    FOREIGN KEY (`received_message_logs_id`)
    REFERENCES `assistente`.`received_message_logs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
