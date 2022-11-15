create database Telebot;
use Telebot;

create table logins
(
	id int primary key auto_increment,
    user varchar(30),
    password varchar(30)
);

insert logins (user, password)
values ("user", "12345");

create table message_chat_id
(
    id bigint primary key,
    autorization_check boolean
); 