from django.contrib import admin

from .models import Patient, CoronaTest, CallPatient


class CoronaTestInline(admin.TabularInline):
    model = CoronaTest
    extra = 1


class CallPatientInline(admin.TabularInline):
    model = CallPatient
    extra = 1
    ordering = ['call_time']


class PatientAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal Information', {'fields': ['patient_first_name', 'patient_last_name', 'patient_id',
                                             'patient_date_of_birth']}),
        ('Hospitalization Data', {'fields': ['hospitalization_date']}),
    ]
    inlines = [CoronaTestInline, CallPatientInline]
    list_display = ('patient_last_name', 'patient_first_name', 'patient_id', 'is_in_risk_group')


admin.site.register(Patient, PatientAdmin)
