--
-- Create model Rtu
--
CREATE TABLE `rtu` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `url` longtext NULL, `time_upd_int` smallint NOT NULL);
--
-- Create model BiDesc
--
CREATE TABLE `bi_desc` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `act_v` longtext NULL, `act_t` longtext NULL, `act_q` integer NULL, `id_RTU` integer NOT NULL);
--
-- Create model AiDesc
--
CREATE TABLE `ai_desc` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `act_v` longtext NULL, `act_t` longtext NULL, `act_q` longtext NULL, `id_RTU` integer NOT NULL);
ALTER TABLE `bi_desc` ADD CONSTRAINT `bi_desc_id_RTU_d914b7b2_fk_rtu_id` FOREIGN KEY (`id_RTU`) REFERENCES `rtu` (`id`);
ALTER TABLE `ai_desc` ADD CONSTRAINT `ai_desc_id_RTU_bc6c1172_fk_rtu_id` FOREIGN KEY (`id_RTU`) REFERENCES `rtu` (`id`);
