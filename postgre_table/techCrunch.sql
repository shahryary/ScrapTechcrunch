CREATE TABLE homePage(
   ID    serial primary key,
   title           character varying(256)    NOT NULL,
   author            character varying(128),
   postTime        character varying(32),
   postsByLink         character varying(256),
   postTags		character varying(128),
   postText		text,
   dlTimestamp		character varying(32)

);