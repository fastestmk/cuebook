from django.db import models

# Create your models here.
class OrderDetail(models.Model):
	client_name = models.CharField(max_length=50, blank=True, null=True)
	client_email = models.CharField(max_length=50, blank=True, null=True)
	client_address = models.CharField(max_length=250, blank=True, null=True)
	client_gst = models.CharField(max_length=50, blank=True, null=True)
	biller_name = models.CharField(max_length=50, blank=True, null=True)
	biller_email = models.CharField(max_length=50, blank=True, null=True)
	biller_address = models.CharField(max_length=250, blank=True, null=True)
	biller_gst = models.CharField(max_length=50, blank=True, null=True)
	service_name = models.CharField(max_length=50, blank=True, null=True)
	service_cost = models.FloatField(default=0.0)
	tax = models.FloatField(default=0.0)
	bank_account = models.IntegerField(blank=True, null=True)

	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)


class Invoice(models.Model):
	html_invoice = models.TextField()
	order_detail = models.ForeignKey(OrderDetail, on_delete=models.CASCADE)

	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)    
