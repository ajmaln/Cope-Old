from django.db import models
from django.utils import timezone

# Create your models here.


class EndUser(models.Model):
	'''
	Part of accessing register enlisting EndUser details.
	Inherited by Student and Employee Models.

	Contains common user specific details - name, card_number, gender,
	phone_number.
	'''

	gender_choices = (
		(u'F', u'Female'),
		(u'M', u'Male'),
		(u'U', u'Unspecified'),
	)

	name = models.CharField(max_length=50)
	card_number = models.CharField(max_length=50)
	gender = models.CharField(max_length=1, choices=gender_choices,)
	phone_number = models.CharField(max_length=15)

	def __str__(self):
		return self.name

class Student(EndUser):
	'''
	Student peculiar schema.
	comprises of details kin to student and book issue details.
	'''

	roll_number = models.CharField(max_length=20)
	branch = models.CharField(max_length=30)
	batch = models.CharField(max_length=4, default = timezone.now().year)
	semester = models.CharField(max_length=1)

	def __str__(self):
		return super(Student, self).__str__() + '| {}'.format(self.roll_number)

class Employee(EndUser):
	'''
	Employee or faculty peculiar schema.
	comprises of details kin to employee and book issue details.
	'''

	employee_id = models.CharField(max_length=25)
	joining_date = models.DateField()
	department = models.CharField(max_length=50)
	designation = models.CharField(max_length=50)

	def __str__(self):
		return u'%s | %s' %(self.name, self.employee_id)