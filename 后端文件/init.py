#set the database and the chart
#直接复制到Mysql中运行
create database work05 default  character set utf8mb4 collate utf8mb4_unicode_ci;

create table work05.users(
     `id` int not null auto_increment,
     `username`varchar(100)not null,
     `password` varchar(100)not null
     primary key(`id`),UNIQUE `unique_username`(`username`)
     engine=InnoDB default charset=utf8mb4 collate=utf8mb4_unicode_ci;
)

create user 'root'@'%'idenfied by '123456';
grant all priviledges on `work05`.*to `root`@'%';