from django.db import models
from django.contrib.auth.models import User

# Create your models here.
POSITION = (
	('AEDC3-General Manager', 'AEDC3-General Manager'),
	('AEDC4-Senior Manager', 'AEDC4-Senior Manager'),
	('AEDC5-Manager', 'AEDC5-Manager'),
	('AEDC6-Assistant Manager', 'AEDC6-Assistant Manager'),
	('AEDC7-Senior Officer', 'AEDC7-Senior Officer'),
	('AEDC8-Function Officer 1', 'AEDC8-Function Officer 1'),
	('AEDC-9-Function Officer 2', 'AEDC-9-Function Officer 2'),
	('AEDC-10-Support Officer', 'AEDC-10-Support Officer'),
	)

UNIT = (
	('AEDC Change', 'AEDC Change'),
	('Billing', 'Billing'),
	('Fraud Billing', 'Fraud Billing'),
	('Debt Management', 'Debt Management'),
	('Technical Services', 'Technical Services'),
	('Commercial Services', 'Commercial Services'),
	('MAP', 'MAP'),
	('SPM', 'SPM'),
	('Projects', 'Projects'),
	('Protocol', 'Protocol'),
	('Human Resources and Industrial Relations', 'Human Resources and Industrial Relations'),
	('Business Corporate Risk', 'Business Corporate Risk'),
	('Commercial Performance Management', 'Commercial Performance Management'),
	('Communications Facilities and Infrastructure', 'Communications Facilities and Infrastructure'),
	('Company Secretariat', 'Company Secretariat'),
	('Compliance Audit', 'Compliance Audit'),
	('Contract and Documentation', 'Contract and Documentation'),
	('Corporate Communications', 'Corporate Communications'),
	('Corporate Finance and Corporate Development', 'Corporate Finance and Corporate Development'),
	('Customer Care Services', 'Customer Care Services'),
	('Cyber Security and BCP', 'Cyber Security and BCP'),
	('Dispute Resolution', 'Dispute Resolution'),
	('Environmental and Social', 'Environmental and Social'),
	('Financial Operations', 'Financial Operations'),
	('Fleet Management and Logistics', 'Fleet Management and Logistics'),
	('GIS and Communications', 'GIS and Communications'),
	('Health and Safety', 'Health and Safety'),
	('Human Resources and Administration', 'Human Resources and Administration'),
	('IT Audit', 'IT Audit'),
	('Key/Debt Account', 'Key/Debt Account'),
	('Legal Advisory', 'Legal Advisory'),
	('Legal Services', 'Legal Services'),
	('Management Office', 'Management Office'),
	('Network Deployment', 'Network Deployment'),
	('Network Surveillance', 'Network Surveillance'),
	('Network Operations', 'Network Operations'),
	('Operations and Maintenance', 'Operations and Maintenance'),
	('Operations Audit', 'Operations Audit'),
	('Operations Control', 'Operations Control'),
	('Protection, Control and Communications', 'Protection, Control and Communications'),
	('Quality Assurance', 'Quality Assurance'),
	('Facility', 'Facility'),
	('Regulatory and Government Relations', 'Regulatory and Government Relations'),
	('Revenue Protection', 'Revenue Protection'),
	('Security Services', 'Security Services'),
	('Shared Services', 'Shared Services'),
	('Strategic PMO Office', 'Strategic PMO Office'),
	('Strategic and Corporate Planning', 'Strategic and Corporate Planning'),
	('Supply Chain (Procurement)', 'Supply Chain (Procurement)'),
	('Treasury and Financial Risk Management', 'Treasury and Financial Risk Management'),
	('User Support and Application Management', 'User Support and Application Management'),
	('Vending', 'Vending'),
	('ICT Infrastructure and Platform', ' ICT Infrastructure and Platform'),
	)

DIRECTORATE =(
	('Change Management and PMO', 'Change Management and PMO'),
	('Projects', 'Projects'),
	('Corporate Services', 'Corporate Services'),
	('Operations', 'Operations'),
	('Financial Services', 'Financial Services'),
	('Information Communication and Technology', 'Information Communication and Technology'),
	('Internal Audit', 'Internal Audit'),
	('Legal Services and Company Secretariat', 'Legal Services and Company Secretariat'),
	('Risk and Compliance', 'Risk and Compliance'),
	)

AREA_OFFICE =(
	('Gwagwalada', 'Gwagwalada'),
	('Jabi', 'Jabi'),
	('Kuje', 'Kuje'),
	('Apo', 'Apo'),
	('Lugbe', 'Lugbe'),
	('Lokogoma', 'Lokogoma'),
	('Asokoro', 'Asokoro'),
	('Garki', 'Garki'),
	('Jikwoyi', 'Jikwoyi'),
	('Karu', 'Karu'),
	('Maitama', 'Maitama'),
	('Head Office', 'Head Office'),
	('Wuse', 'Wuse'),
	('Bwari', 'Bwari'),
	('Gwarinpa', 'Gwarinpa'),
	('Katampe', 'Katampe'),
	('Kubwa', 'Kubwa'),
	('Mpape', 'Mpape'),
	('Life Camp', 'Life Camp'),
	('Bida', 'Bida'),
	('Bosso', 'Bosso'),
	('Kotangora', 'Kotangora'),
	('Minna', 'Minna'),
	('Suleja', 'Suleja'),
	('Zuma', 'Zuma'),
	('Idah', 'Idah'),
	('Kabba', 'Kabba'),
	('Lokoja', 'Lokoja'),
	('Okene', 'Okene'),
	('Ado', 'Ado'),
	('Akwanga', 'Akwanga'),
	('Keffi', 'Keffi'),
	('Lafia', 'Lafia'),
	('Mararaba', 'Mararaba'),
	)

REGION = (
	('FCT Central', 'FCT Central'),
	('FCT North', 'FCT North'),
	('FCT South', 'FCT South'),
	('FCT West', 'FCT West'),
	('FCT East', 'FCT East'),
	('Head Office', 'Head Office'),
	('Kogi', 'Kogi'),
	('Niger', 'Niger'),
	('Nassarawa', 'Nassarawa'),
	)

STRATEGIC_FOCUS = (
		('Reduce ATC&C Loss','Reduce ATC&C Loss'),
		('Achieve Financial Viability','Achieve Financial Viability'),
		('Create a Customer Centric Organization','Create a Customer Centric Organization'),
		('Effective Regulatory & Stakeholders Engagement', 'Effective Regulatory & Stakeholders Engagement'),
		('Improve HSE Practices','Improve HSE Practices'),
		('Implement Prudent Asset Management Practices', 'Implement Prudent Asset Management Practices'),
		('Deploy Fit for Purpose ICT Business Solutions', 'Deploy Fit for Purpose ICT Business Solutions'),
		('Create a High Performance Culture','Create a High Performance Culture'),
		('Compliance with Reengineered Business Processes','Compliance with Reengineered Business Processes'),
		)
E = 4
M = 3
PM = 2
DM = 1

RATING_CHOICES =(
	(E, 'E'),
	(M, 'M'),
	(PM, 'PM'),
	(DM, 'DM'),
	)

class Appraisal_Form(models.Model):
	user=models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	first_name = models.CharField(max_length=50, null=True)
	middle_name = models.CharField(max_length=50, null=True)
	last_name = models.CharField(max_length=50, null=True)
	staff_id =  models.CharField(max_length=10, null=True)
	position = models.CharField(max_length=30, choices=POSITION, null=True)
	unit = models.CharField(max_length=100, choices=UNIT, null=True)
	directorate = models.CharField(max_length=100, choices=DIRECTORATE, null=True)
	designation = models.CharField(max_length=100, null=True)
	supervisor_name = models.CharField(max_length=100, null=True)
	area_office = models.CharField(max_length=30, choices=AREA_OFFICE, null=True)
	region = models.CharField(max_length=30, choices=REGION, null=True)
	goals_score = models.FloatField(default=0.0)
	overall_score_sectA = models.FloatField(default=0.0)
	total_score = models.FloatField(default=0.0)
	appraisee_email = models.EmailField(null=True)
	appraiser_email = models.EmailField(null=True)
	reviewer_email = models.EmailField(null=True)

	class meta:
		verbose_name = "Appraisal form"
		verbose_name_plural = "Appraisal forms"

	def __str__(self):
		return self.first_name

class Appr_period_info(models.Model):
	date_from = models.CharField(max_length=50)
	date_to = models.CharField(max_length=50)
	

	def __str__(self):
		return self.date_from

class Behavioral_competence(models.Model):
	user=models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	period_from=models.CharField(max_length=50, null=True)
	period_to=models.CharField(max_length=50, null=True)
	first_name = models.CharField(max_length=50, null=True)
	last_name = models.CharField(max_length=50, null=True)
	staff_id =  models.CharField(max_length=10, null=True)
	job_effectiveness = models.IntegerField(default=0)
	trust_and_integrity = models.IntegerField(default=0)
	supervision = models.IntegerField(default=0)
	dependability = models.IntegerField(default=0)
	collaboration = models.IntegerField(default=0)
	organizational_success = models.IntegerField(default=0)
	customer_orientation = models.IntegerField(default=0)
	leadership_drive = models.IntegerField(default=0)
	compliance_and_safety = models.IntegerField(default=0)
	diversity_and_respect = models.IntegerField(default=0)
	attendance = models.IntegerField(default=0)
	# point_scored = models.IntegerField(default=0)
	overall_score_sectB = models.FloatField(default=0.0)

	class meta:
		verbose_name = "Behavioral Competence"
		verbose_name_plural = "Behavioral_Competences"

class Appraisal_info(models.Model):
	user=models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	period_from=models.CharField(max_length=50, null=True)
	period_to=models.CharField(max_length=50, null=True)
	goal = models.TextField(max_length=300)
	actual_result =models.TextField(max_length=300)
	weight = models.IntegerField(default=0)
	appraisee_rating = models.CharField(max_length=10, choices=RATING_CHOICES)
	appraiser_rating = models.CharField(max_length=10, choices=RATING_CHOICES)
	# average = models.FloatField(default=0.0)
	score = models.FloatField(default=0.0)

	class meta:
		verbose_name = "goal score"
		verbose_name_plural = "goal scores"

class Accomplishment(models.Model):
	user=models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	period_from = models.CharField(max_length=50, null=True)
	period_to = models.CharField(max_length=50, null=True)
	accomplishment = models.CharField(max_length=300, null=True)
	strategic_focus = models.CharField(max_length=300, null=True)
	balanced_scorecard = models.CharField(max_length=300, null=True)

	class meta:
		verbose_name = "accomplishment"
		verbose_name_plural = "accomplishments"

class Overall_rating(models.Model):
	user=models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	period_from = models.CharField(max_length=50, null=True)
	period_to = models.CharField(max_length=50, null=True)
	first_name = models.CharField(max_length=50, null=True)
	last_name = models.CharField(max_length=50, null=True)
	staff_id =  models.CharField(max_length=10, null=True)
	section_A = models.FloatField(default=0.0)
	section_B = models.FloatField(default=0.0)
	total_score = models.FloatField(default=0.0)

	class meta:
		verbose_name = "section_A"
		verbose_name_plural = "section_As"
 
class Perf_improvement(models.Model):
	user=models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	period_from = models.CharField(max_length=50, null=True)
	period_to = models.CharField(max_length=50, null=True)
	key_strength = models.CharField(max_length=300, null=True)
	improvement_area = models.CharField(max_length=300, null=True)
	developmental_recommendation = models.CharField(max_length=300, null=True)

	class meta:
		verbose_name = "key strength"
		verbose_name_plural = "key strengths"

class Appr_comment(models.Model):
	user=models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	first_name = models.CharField(max_length=50, null=True)
	last_name = models.CharField(max_length=50, null=True)
	staff_id =  models.CharField(max_length=10, null=True)
	period_from=models.CharField(max_length=50, null=True)
	period_to=models.CharField(max_length=50, null=True)
	appraisee_comment = models.TextField(max_length=300, null=True, blank=True)
	appraiser_comment = models.TextField(max_length=300, null=True, blank=True)
	reviewer_comment = models. TextField(max_length=300, null=True, blank=True)

	class meta:
		verbose_name = 'Appraisal comment'
		verbose_name_plural = 'Appraisal comments'

class Appr_approve(models.Model):
	approver=models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	user=models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="appr_owner")
	period_from=models.CharField(max_length=50, null=True)
	period_to=models.CharField(max_length=50, null=True)
	approved = models.BooleanField(default=False)