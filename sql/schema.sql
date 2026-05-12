create database job_tracker;
-- create user
create user 'sysadmin'@'localhost' identified by '******'; 
-- privilégios do usuário
grant all privileges on job_tracker.* to 'sysadmin'@'localhost';

