create table dmca (
  id serial primary key,
  copy_link int references copy_site(id),
  copyright int references actress(id),
  created_at text,
  dmca_date text
)
