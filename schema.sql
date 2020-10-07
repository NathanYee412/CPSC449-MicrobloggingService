drop table if exists user;
create table user (
  user_id integer primary key autoincrement,
  username text not null,
  email text not null,
  pw_hash text not null
);

drop table if exists follower;
create table follower (
  followeeID integer,
  followerID integer
);

drop table if exists timeline;
create table timeline (
  message_id integer primary key autoincrement,
  author_id integer not null,
  text text not null,
  pub_date integer
);
