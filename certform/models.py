from django.db import models
from django.urls import reverse

class Certification(models.Model):
    id = models.AutoField(primary_key = True)
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    ssn = models.CharField(max_length=200)
    returning_or_new_hire = models.CharField(max_length=200)
    title_position = models.CharField(max_length=200)
    current_assignment = models.CharField(max_length=200)
    subject_grade = models.CharField(max_length=200, null=True)
    certification_status = models.CharField(max_length=200)
    nys_cert_area = models.CharField(max_length=200, null=True)
    cert_type = models.CharField(max_length=200, null=True)
    expiration_date = models.CharField(max_length=200, null=True)
    current_comment = models.CharField(max_length=200, null=True)
    comments_from_last_wksh = models.CharField(max_length=200, null=True)
    las = models.CharField(max_length=200, null=True)
    ats_w = models.CharField(max_length=200, null=True)
    cst = models.CharField(max_length=200, null=True)
    cst_subject = models.CharField(max_length=200, null=True)
    eas = models.CharField(max_length=200, null=True)
    ata = models.CharField(max_length=200, null=True)



    def __str__(self):
        return "certification" + str(self.id)
    

    def get_absolute_url(self):
        return reverse('record_edit', kwargs={'pk': self.pk})