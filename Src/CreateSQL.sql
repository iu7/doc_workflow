CREATE TABLE IF NOT EXISTS `mydb`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(16) NOT NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(32) NOT NULL,
  `is_admin` INT NULL DEFAULT 0,
  `group` INT NULL,
  PRIMARY KEY (`id`));

CREATE TABLE IF NOT EXISTS `mydb`.`groups` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));


CREATE TABLE IF NOT EXISTS `mydb`.`user_to_groups` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NULL,
  `group_id` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_user_to_groups_1_idx` (`user_id` ASC),
  INDEX `fk_user_to_groups_2_idx` (`group_id` ASC),
  CONSTRAINT `fk_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_group`
    FOREIGN KEY (`group_id`)
    REFERENCES `mydb`.`groups` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


CREATE TABLE IF NOT EXISTS `mydb`.`documents` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `owner` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `path` VARCHAR(45) NULL,
  `public_date` DATETIME NULL,
  `status` TINYINT NULL,
  PRIMARY KEY (`id`));

CREATE TABLE IF NOT EXISTS `mydb`.`docs_versions` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `doc_id` INT NULL,
  `version` INT NULL,
  `change_date` DATETIME NULL,
  `change_person` INT NULL,
  `filename` VARCHAR(200) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_docs_versions_1_idx` (`doc_id` ASC),
  INDEX `fk_docs_versions_2_idx` (`change_person` ASC),
  CONSTRAINT `fk_docs_versions_1`
    FOREIGN KEY (`doc_id`)
    REFERENCES `mydb`.`documents` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_docs_versions_2`
    FOREIGN KEY (`change_person`)
    REFERENCES `mydb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS `mydb`.`docs_to_users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `doc_id` INT NULL,
  `user_id` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_docs_to_users_1_idx` (`doc_id` ASC),
  INDEX `fk_docs_to_users_2_idx` (`user_id` ASC),
  CONSTRAINT `fk_docs_to_users_1`
    FOREIGN KEY (`doc_id`)
    REFERENCES `mydb`.`documents` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_docs_to_users_2`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`users` (`id`)
    ON DELETE NO ACTION
   ON UPDATE NO ACTION) ;

CREATE TABLE IF NOT EXISTS `mydb`.`docs_to_groups` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `group_id` INT NULL,
  `doc_id` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_docs_to_groups_1_idx` (`doc_id` ASC),
  INDEX `fk_docs_to_groups_2_idx` (`group_id` ASC),
  CONSTRAINT `fk_docs_to_groups_1`
    FOREIGN KEY (`doc_id`)
    REFERENCES `mydb`.`documents` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_docs_to_groups_2`
    FOREIGN KEY (`group_id`)
    REFERENCES `mydb`.`groups` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


CREATE TABLE IF NOT EXISTS `mydb`.`comment` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NULL,
  `doc_id` INT NULL,
  `text` TEXT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comment_1_idx` (`doc_id` ASC),
  INDEX `fk_user_comment_idx` (`user_id` ASC),
  CONSTRAINT `fk_user_comment`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comment_1`
    FOREIGN KEY (`doc_id`)
    REFERENCES `mydb`.`documents` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

