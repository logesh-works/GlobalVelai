from django.db import models
import uuid

GENDER_CHOICES  = [('M','Male'),('F','Female'),('O','Others')]
EXPREIENCE_COICES = [("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),("6","6"),("7","7"),('8',"8"),('9','9'),("10+","10+")]
SALARY_EXPECTATION = [("4L","4L"),("5L","5L"),("6L+","6L+")]

class CountryList(models.Model):
    country_name = models.CharField("Country Name",max_length=255,default=None)
class StateList(models.Model):
    state_name = models.CharField("State Name",max_length=255,default=None)
class DegreeList(models.Model):
    degree_name = models.CharField("Degree Name",max_length=255,default=None)
class SkillList(models.Model):
    skill_name =  models.CharField("Skill Name",max_length=255,default=None)
class FieldsList(models.Model):
    field_name =  models.CharField("Field Name",max_length=255,default=None)

class Applicant(models.Model):
    uuid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    is_active = models.BooleanField(default=True)
    is_suspended = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=50,choices=GENDER_CHOICES)
    phone_number = models.BigIntegerField()
    email = models.EmailField(unique=False)
    address = models.TextField()
    city = models.CharField(max_length=255)
    state = models.ForeignKey(StateList, on_delete=models.DO_NOTHING)
    pincode = models.IntegerField()
    country = models.ForeignKey(CountryList, on_delete=models.DO_NOTHING)

class EducationDetails(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    degree = models.ForeignKey(DegreeList,on_delete=models.DO_NOTHING)
    year_of_passing = models.IntegerField()
    school = models.CharField(max_length=255)

class CertificationDetails(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    certificate_name = models.CharField(max_length=255)
    year_of_certification = models.IntegerField()

class PreferenceDetails(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    country = models.ForeignKey(CountryList, on_delete=models.DO_NOTHING)
    industry = models.ManyToManyField(FieldsList)
    position = models.CharField(max_length=255)
    available_from = models.DateField()
    has_passport = models.BooleanField(default=False)
    salary_expectation = models.CharField(max_length=230,choices=SALARY_EXPECTATION)

class WorkDetails(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    skill = models.ManyToManyField(SkillList)
    years_of_experience = models.CharField(max_length=50,choices=EXPREIENCE_COICES)

class EmploymentHistory(models.Model):
    job_title = models.CharField(max_length=255)
    employer = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state =models.ForeignKey(StateList, on_delete=models.DO_NOTHING)
    country = models.ForeignKey(CountryList, on_delete=models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

class AwardsDetails(models.Model):
    award_name = models.CharField(max_length=255)
    awarded_organisation = models.CharField(max_length=255)

class CompanyProfile(models.Model):
    uuid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    company_name = models.CharField(max_length=255)
    phone_number = models.BigIntegerField()
    email = models.EmailField(unique=True)
    address = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pincode = models.IntegerField()
    country = models.CharField(max_length=255)
    industry_type = models.ForeignKey(FieldsList,on_delete=models.DO_NOTHING)
    website = models.URLField(blank=True, null=True)

class JobPostings(models.Model):
    is_suspended = models.BooleanField(default=False)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    required_skill = models.ManyToManyField(SkillList)
    vacancies = models.IntegerField()
    posted_on = models.DateField(auto_now_add=True)
    is_fulfilled = models.BooleanField(default=False)


