create table if not exists
vehicle (
    id integer primary key autoincrement,
    passenger_spots unsigned tinyint not null default 3
);

create table if not exists
person (
    id integer primary key autoincrement,
    name varchar(50) not null,
    car vecicle
);
