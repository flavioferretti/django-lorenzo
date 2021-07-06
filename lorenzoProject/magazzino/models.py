from django.db import models  
class Magazzino(models.Model):  
	eid = models.CharField(max_length=20)  
	ename = models.CharField(max_length=100)  
	eefirm = models.CharField(max_length=100)  
	econtact = models.CharField(max_length=250)  
	class Meta:  
		db_table = "magazzino"  

