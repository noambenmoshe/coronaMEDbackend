import datetime

from django.db import models
from django.utils import timezone


class Patient(models.Model):
    patient_first_name = models.CharField(max_length=200, default="")
    patient_last_name = models.CharField(max_length=200, default="")
    patient_id = models.IntegerField(default=0)
    patient_date_of_birth = models.DateTimeField('date of birth')
    hospitalization_date = models.DateTimeField('date hospitalized')

    def __str__(self):
        id_p = str(self.patient_id)
        return id_p

    def is_in_risk_group(self):
        return int(timezone.now().year) - int(self.patient_date_of_birth.strftime('%Y')) >= 60

    def hospitalized_recently(self):
        return self.hospitalization_date >= timezone.now() - datetime.timedelta(days=1)

class CoronaTest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    corona_test_id = models.IntegerField(default=0)
    test_taken_date = models.DateTimeField('date test taken')
    TRUE = 'Positive'
    FALSE = 'Negative'
    NO_RESULT = 'NA'
    TEST_RESULTS_OPTIONS = [(TRUE, 'Positive'), (FALSE, 'Negative'), (NO_RESULT, 'NA')]
    test_result = models.CharField(max_length=8, choices=TEST_RESULTS_OPTIONS, default=NO_RESULT)

    def __str__(self):
        corona_id = str(self.corona_test_id)
        return corona_id


class CallPatient(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    call_time = models.DateTimeField('date and time called patient')
    TRUE = 'Positive'
    FALSE = 'Negative'
    CALL_OPTIONS = [(TRUE, 'Positive'), (FALSE, 'Negative')]
    call_status = models.CharField(max_length=8, choices=CALL_OPTIONS, default=FALSE)