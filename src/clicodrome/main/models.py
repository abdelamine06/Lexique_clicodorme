from django.db import models

class FormeMot(models.Model):
    MotID = models.AutoField(null=False, primary_key=True)
    Mot = models.CharField(max_length=50, null=False)
    Affiche = models.CharField(max_length=100, null=False)
    Table = models.IntegerField(null=False)
    Infos = models.TextField(max_length=250,null=False)

    class Meta:
        verbose_name="Mots Formé"

class TableTransformation(models.Model):
    TransformationID = models.AutoField(null=False, primary_key=True)
    NumTab = models.IntegerField(null=False, db_index=True)
    Terminaison = models.CharField(max_length=10, null=True)
    Transformation = models.CharField(max_length=10, null=False)
    Infos = models.TextField(max_length=100, null=False)

class Mot(models.Model):
    Mot = models.CharField(max_length=50, null=False, db_index=True, primary_key=True)
    Affiche = models.CharField(max_length=100, null=False)
    Table = models.IntegerField(null=False)
    Cat = models.CharField(max_length=3, null=False)
    Infos = models.TextField(max_length=250,null=False)
