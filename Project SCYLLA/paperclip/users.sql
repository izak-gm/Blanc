use scylla;
create table users(username varchar(50) primary key,lastName text not null,
phoneNumber bigint,
email text ,
nationalID smallint not null unique,joined_date date,
nextofkin text null);


alter table users add location text;
drop table users;
