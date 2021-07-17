from django.db import models

# Service Areas - A, B, C
class ServiceArea(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True) 
    name = models.CharField(max_length=100) 
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

# Use Type - Residential, Industrial, Commercial, Institutional
class UseType(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True) 
    name = models.CharField(max_length=100) 
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

# Use Sub Type - Light Industrial, Manufacturing, Warehousing / General, Free Standing Discount Store, General Office, Hotel / Schools, Religious Facilities, Medical (Nursing Hm./Asstd Living), Medical (Clinic, Hospital)
class UseSubType(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True) 
    name = models.CharField(max_length=100) 
    usetypeid = models.ForeignKey(UseType, on_delete=models.CASCADE)
    parksandrecfee = models.DecimalField(decimal_places=2, max_digits=10)
    police = models.DecimalField(decimal_places=2, max_digits=10)
    fire = models.DecimalField(decimal_places=2, max_digits=10)
    streets = models.DecimalField(decimal_places=2, max_digits=10)
    totalfee = models.DecimalField(decimal_places=2, max_digits=10)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.name)

class Residential(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True) 
    minsize = models.DecimalField(decimal_places=2, max_digits=10)
    maxsize = models.DecimalField(decimal_places=2, max_digits=10)
    parksandrecfee = models.DecimalField(decimal_places=2, max_digits=10)
    police = models.DecimalField(decimal_places=2, max_digits=10)
    fire = models.DecimalField(decimal_places=2, max_digits=10)
    streets = models.DecimalField(decimal_places=2, max_digits=10)
    totalfee = models.DecimalField(decimal_places=2, max_digits=10)
    active = models.BooleanField(default=True)


class ServiceAreaCalculator(models.Model):
    service_area = models.ForeignKey(ServiceArea, on_delete=models.SET_NULL, blank=True, null=True)
    use_type = models.ForeignKey(UseType, on_delete=models.SET_NULL, blank=True, null=True)
    use_sub_type = models.ForeignKey(UseSubType, on_delete=models.SET_NULL, blank=True, null=True)
    square_feet = models.IntegerField(blank=True, null=True)
    units = models.IntegerField(blank=True, null=True)