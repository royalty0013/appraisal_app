from django.contrib import admin
from goalsetting.models import Goal_Form, goal_info, Comment
# Register your models here.


admin.site.site_header = "Goal Setting Admin"
admin.site.index_title = "Goal Setting Admin"
admin.site.site_title = "Goal Setting Admin"

class GoalFormAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'middle_name', 'last_name', 'staff_id', 'position', 'unit', 'directorate', 'designation', 'supervisor_name', 'area_office', 'region', 'total', 'appraisee_email', 'appraiser_email', 'reviewer_email']
	search_fields = ['staff_id', 'appraisee_email']
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
admin.site.register(Goal_Form, GoalFormAdmin)

class GoalInfoAdmin(admin.ModelAdmin):
	list_display = ['user', 'period_from', 'period_to', 'objective', 'specific_task', 'KPI', 'Strategic_focus', 'Balanced_scorecard', 'weight', 'timeline']
	search_fields = ['user__email']
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
admin.site.register(goal_info, GoalInfoAdmin)

class CommentAdmin(admin.ModelAdmin):
	list_display = ['user','first_name', 'last_name', 'staff_id', 'period_from','period_to', 'appraisee_comment', 'appraiser_comment', 'reviewer_comment']
	search_fields = ['user__email', 'staff_id']
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
admin.site.register(Comment, CommentAdmin)


