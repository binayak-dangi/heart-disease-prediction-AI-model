from django.db import models


class RegisterDetail(models.Model):
    username = models.CharField(max_length=150, unique=True)
    full_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    weight = models.FloatField()


class HeartInfo(models.Model):
    Customer_id = models.OneToOneField(RegisterDetail, on_delete=models.CASCADE, primary_key=True)
    Age = models.IntegerField(blank=True, null=True)
    Gender = models.CharField(max_length=6, blank=True, null=True)
    Cp = models.IntegerField(blank=True, null=True)
    Trestbps = models.IntegerField(blank=True, null=True)
    Chol = models.IntegerField(blank=True, null=True)
    Fbs = models.IntegerField(blank=True, null=True)
    Restecg = models.IntegerField(blank=True, null=True)
    Mhra = models.IntegerField(blank=True, null=True)
    Exang = models.IntegerField(blank=True, null=True)
    Oldpeak = models.FloatField(blank=True, null=True)
    Slope = models.IntegerField(blank=True, null=True)
    Ca = models.IntegerField(blank=True, null=True)
    Thal = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"HeartInfo for {self.Customer_id.Username}"

