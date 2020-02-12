use db_clicodrome;

insert into main_mot (`Mot`,`Table`,`Infos`) values ('manger',5,'lemme=manger,cat=v,lemme2=test,lemme3=test');
insert into main_mot (`Mot`,`Table`,`Infos`) values ('content',2,'lemme=content,cat=adj,lemme2=test,lemme3=test');
insert into main_mot (`Mot`,`Table`,`Infos`) values ('pomme',1,'lemme=pomme,cat=nc,lemme2=fruit,lemme3=aliment');
insert into main_mot (`Mot`,`Table`,`Infos`) values ('poire',1,'lemme=poire,cat=nc,lemme2=fruit,lemme3=aliment');
insert into main_mot (`Mot`,`Table`,`Infos`) values ('carotte',1,'lemme=carotte,cat=nc,lemme2=legume,lemme3=aliment');

insert into main_tabletransformation (`NumTab`,`Terminaison`,`Transformation`,`Infos`) values (1,'*','s','nb=pl');
insert into main_tabletransformation (`NumTab`,`Terminaison`,`Transformation`,`Infos`) values (2,'*','e','genre=f');
insert into main_tabletransformation (`NumTab`,`Terminaison`,`Transformation`,`Infos`) values (2,'*','s','nb=pl');
insert into main_tabletransformation (`NumTab`,`Terminaison`,`Transformation`,`Infos`) values (2,'*','es','genre=f,nb=pl');
