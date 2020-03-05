use db_clicodrome;

insert into main_mot (`Mot`,`Affiche`,`Cat`,`Table`,`Infos`) values ('manger','manger','v',5,'lemmes=[lemme1=manger],cat=v,lemme2=[test=test,test2=[test=test]],lemme3=test');
insert into main_mot (`Mot`,`Affiche`,`Cat`,`Table`,`Infos`) values ('content','content','adj',2,'lemmes=[lemme1=content],cat=adj,lemme2=test,lemme3=test');
insert into main_mot (`Mot`,`Affiche`,`Cat`,`Table`,`Infos`) values ('pomme','pomme','nc',1,'lemmes=[lemme1=pomme,lemme2=fruit,lemme3=aliment],cat=nc');
insert into main_mot (`Mot`,`Affiche`,`Cat`,`Table`,`Infos`) values ('poire','poire','nc',1,'lemmes=[lemme1=poire,lemme2=fruit,lemme3=aliment],cat=nc');
insert into main_mot (`Mot`,`Affiche`,`Cat`,`Table`,`Infos`) values ('carotte','carotte','nc',1,'lemmes=[lemme1=carotte,lemme2=légume,lemme3=aliment],cat=nc');

insert into main_tabletransformation (`NumTab`,`Terminaison`,`Transformation`,`Infos`) values (1,'','s','nb=pl');
insert into main_tabletransformation (`NumTab`,`Terminaison`,`Transformation`,`Infos`) values (2,'','e','genre=f');
insert into main_tabletransformation (`NumTab`,`Terminaison`,`Transformation`,`Infos`) values (2,'','s','nb=pl');
insert into main_tabletransformation (`NumTab`,`Terminaison`,`Transformation`,`Infos`) values (2,'','es','genre=f,nb=pl');
