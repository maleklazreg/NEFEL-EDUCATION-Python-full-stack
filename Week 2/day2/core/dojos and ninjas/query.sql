SELECT * FROM dojos_and_ninjas_schema.dojos;
SELECT * FROM dojos_and_ninjas_schema.ninjas;
insert into dojos (name) values ("pablo");
insert into dojos (name) values ("cee");
insert into dojos (name) values ("asab rocky");

delete from dojos where name = "pablo";
delete from dojos where name = "cee";
delete from dojos where name = "asab rocky";

insert into ninjas (first_name, last_name, age, dojo_id) values ("malek", "lazreg","18",1);
insert into ninjas (first_name, last_name, age, dojo_id) values ("taha", "tito","27",1);
insert into ninjas (first_name, last_name, age, dojo_id) values ("taha", "tito","27",1);

insert into ninjas (first_name, last_name, age, dojo_id) values ("ilisen", "alii","12",2);
insert into ninjas (first_name, last_name, age, dojo_id) values ("rocky", "tito","45",2);
insert into ninjas (first_name, last_name, age, dojo_id) values ("rdderr", "tito","90",2);

insert into ninjas (first_name, last_name, age, dojo_id) values ("mo", "mo","11",3);
insert into ninjas (first_name, last_name, age, dojo_id) values ("popo", "titi","22",3);
insert into ninjas (first_name, last_name, age, dojo_id) values ("gargar", "toto","69",3);


select * from ninjas where dojo_id = 1;

select * from ninjas where dojo_id = 3;

select dojos.* from dojos join ninjas on dojos.id = ninjas.dojo_id order by ninjas.id desc limit 1;

select ninjas.* ,dojos.name as dojo_name from ninjas join dojos on ninjas.dojo_id = dojos.id where ninjas.id = 6;

