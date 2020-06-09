create table copy_link(
id  serial not null,
domain text,
link text,
embedlink text,
actress text,
status text default 'exist'
update_date text,
primary key(id)
);
