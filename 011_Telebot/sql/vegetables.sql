-- create database Vegetables;
use Vegetables;

-- create table logins
-- (
-- 	id int primary key auto_increment,
--     user varchar(30),
--     password varchar(30)
-- );

-- insert logins (user, password)
-- values ("user", "12345");

-- create table message_chat_id
-- (
--     id bigint primary key,
--     autorization_check boolean
-- );

create table vegetables
(
    id int primary key auto_increment,
    name varchar(30),
    cost varchar(30)
);