from django.db import models

class Certification(models.Model):
    id = models.AutoField(primary_key = True)
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    ssn = models.CharField(max_length=200)
    returning_or_new_hire = models.CharField(max_length=200)
    title_position = models.CharField(max_length=200)
    current_assignment = models.CharField(max_length=200)
    subject_grade = models.CharField(max_length=200)
    certification_status = models.CharField(max_length=200)
    nys_cert_area = models.CharField(max_length=200)
    cert_type = models.CharField(max_length=200)
    expiration_date = models.CharField(max_length=200)
    current_comment = models.CharField(max_length=200)
    comments_from_last_wksh = models.CharField(max_length=200)
    las = models.CharField(max_length=200)
    ats_w = models.CharField(max_length=200)
    cst = models.CharField(max_length=200)
    cst_subject = models.CharField(max_length=200)
    eas = models.CharField(max_length=200)
    ata = models.CharField(max_length=200)



    def __str__(self):
        return "certification" + str(self.id)