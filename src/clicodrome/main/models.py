from django.db import models

class FormeMot(models.Model):
    MotID = models.AutoField(null=False, primary_key=True)
    Mot = models.CharField(max_length=50, null=False)
    Infos = models.TextField(max_length=250,null=False)

    class Meta:
        verbose_name="Mots Formé"

class TableTransformation(models.Model):
    TransformationID = models.AutoField(null=False, primary_key=True)
    NumTab = models.IntegerField(null=False)
    Terminaison = models.CharField(max_length=10, null=True)
    Transformation = models.CharField(max_length=10, null=False)
    Infos = models.TextField(max_length=100, null=False)

class Mot(models.Model):
    MotID = models.AutoField(null=False, primary_key=True)
    Mot = models.CharField(max_length=50, null=False)
    Table = models.IntegerField(null=False)
    Infos = models.TextField(max_length=250,null=False)

class Utilisateur(models.Model):
    UtilID = models.AutoField(null=False, primary_key=True)
    Nom = models.CharField(max_length=50, null=False)
    Prenom = models.CharField(max_length=50, null=False)
    MdP = models.CharField(max_length=50, null=False)
    Droit = models.IntegerField(default=0)
