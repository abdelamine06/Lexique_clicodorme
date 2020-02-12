use db_clicodrome;

insert into main_mot (`Mot`,`Table`,`Infos`) values ('manger',5,'[lemme=manger,cat=v]');
insert into main_mot (`Mot`,`Table`,`Infos`) values ('content',2,'[lemme=content,cat=adj]');
insert into main_mot (`Mot`,`Table`,`Infos`) values ('pomme',1,'[lemme=manger,cat=nc]');

insert into main_tabletransformation (`NumTab`,`Terminaison`,`Transformation`,`Infos`) values (1,'*','s','[nb=pl]');
insert into main_tabletransformation (`NumTab`,`Terminaison`,`Transformation`,`Infos`) values (2,'*','e','[genre=f]');
insert into main_tabletransformation (`NumTab`,`Terminaison`,`Transformation`,`Infos`) values (2,'*','s','[nb=pl]');
insert into main_tabletransformation (`NumTab`,`Terminaison`,`Transformation`,`Infos`) values (2,'*','es','[genre=f,nb=pl]');
