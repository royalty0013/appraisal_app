from django.contrib import admin
from appraisal.models import Appraisal_Form, Appraisal_info, Appr_comment, Perf_improvement, Overall_rating, Accomplishment, Behavioral_competence
# Register your models here.

admin.site.site_header = "Performance Management Admin"
admin.site.index_title = "Performance Management Admin"
admin.site.site_title = "Performance Management Admin"

class AppraisalFormAdmin(admin.ModelAdmin):
	list_display = ['user', 'first_name', 'middle_name', 'last_name', 'staff_id', 'position', 'unit', 'directorate', 'designation', 'supervisor_name', 'area_office', 'region', 'goals_score', 'overall_score_sectA', 'total_score', 'appraisee_email', 'appraiser_email', 'reviewer_email']
	search_fields = ['user','staff_id', 'appraisee_email']
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
admin.site.register(Appraisal_Form, AppraisalFormAdmin)

class AppraisalInfoAdmin(admin.ModelAdmin):
	list_display = ['user', 'period_from', 'period_to', 'goal', 'actual_result', 'weight', 'appraisee_rating', 'appraiser_rating', 'score']
	search_fields = ['user__email']
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
admin.site.register(Appraisal_info, AppraisalInfoAdmin)

class ApprCommentAdmin(admin.ModelAdmin):
	list_display = ['user','first_name', 'last_name', 'staff_id', 'period_from','period_to', 'appraisee_comment', 'appraiser_comment', 'reviewer_comment']
	search_fields = ['user__email', 'staff_id']
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
admin.site.register(Appr_comment, ApprCommentAdmin)

class PerfImprovementAdmin(admin.ModelAdmin):
	list_display = ['user','period_from','period_to', 'key_strength', 'improvement_area', 'developmental_recommendation']
	search_fields = ['user__email', ]
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
admin.site.register(Perf_improvement, PerfImprovementAdmin)

class OverallRatingAdmin(admin.ModelAdmin):
	list_display = ['user','first_name', 'last_name', 'staff_id','period_from','period_to', 'section_A', 'section_B', 'total_score']
	search_fields = ['user__email', ]
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
admin.site.register(Overall_rating, OverallRatingAdmin)

class AccomplishmentAdmin(admin.ModelAdmin):
	list_display = ['user', 'period_from','period_to', 'accomplishment', 'strategic_focus', 'balanced_scorecard']
	search_fields = ['user__email']
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
admin.site.register(Accomplishment, AccomplishmentAdmin)

class BehavioralCompetenceAdmin(admin.ModelAdmin):
	list_display = ['user', 'first_name', 'last_name', 'staff_id','period_from','period_to', 'job_effectiveness', 'trust_and_integrity', 'supervision', 'dependability', 'collaboration', 'organizational_success', 'customer_orientation', 'leadership_drive', 'compliance_and_safety', 'diversity_and_respect', 'attendance', 'overall_score_sectB']
	search_fields = ['user__email']
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
admin.site.register(Behavioral_competence,BehavioralCompetenceAdmin)

