import re
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from goalsetting.utils import ldapLogin, createOrGetUser
from django.urls import reverse
from django.http import HttpResponse
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.conf import settings as st

from appraisal.models import *
# Create your views here.

def appr_success_page(request):
	return render(request, 'appraisal/appr_success_page.html')

def appraiser_suc_page(request):
	return render(request, 'appraisal/appraiser_success_page.html')

def reviewer_suc_page(request):
	return render(request, 'appraisal/reviewer_success_page.html')

def page(request):
	return render(request, 'appraisal/page.html')


def appr_form(request):
	f = Appraisal_Form(
		user=request.user,
		first_name = request.POST['firstname'],
		middle_name = request.POST['middlename'],
		last_name = request.POST['lastname'],
		staff_id = request.POST['staffid'],
		position = request.POST['position'],
		unit = request.POST['unit'],
		directorate = request.POST['directorate'],
		designation = request.POST['designation'],
		supervisor_name = request.POST['supervisor_name'],
		area_office = request.POST['area_office'],
		region = request.POST['region'],
		goals_score = request.POST['goals_score'],
		overall_score_sectA = request.POST['overall_score_sectA'],
		# total_score= request.POST['total_score'],
		appraisee_email = request.POST['appraisee_email'],
		appraiser_email = request.POST['appraiser_email'],
		reviewer_email = request.POST['reviewer_email'],
	)
	return f

def appr_comment(request):
	c = Appr_comment(
		user=request.user,
		first_name = request.POST['firstname'],
		last_name = request.POST['middlename'],
		staff_id = request.POST['staffid'],
		period_from = request.POST['from'],
		period_to=request.POST['to'],
		appraisee_comment = request.POST['appraisee_comment']

		)
	return c

def appr_period(request):
	period = Appr_period_info(
		date_from=request.POST['from'], 
		date_to=request.POST['to'],
		)
	return period

def behavior_comp(request):
	behavior = Behavioral_competence(
		user=request.user,
		period_from = request.POST['from'],
		period_to=request.POST['to'],
		job_effectiveness=request.POST['job'],
		trust_and_integrity =request.POST['trust'],
		supervision =request.POST['supervision'],
		dependability =request.POST['dependability'],
		collaboration =request.POST['collaboration'],
		organizational_success =request.POST['org_success'],
		customer_orientation =request.POST['orientation'],
		leadership_drive =request.POST['leadership'],
		compliance_and_safety =request.POST['compliance'],
		diversity_and_respect =request.POST['diversity'],
		attendance =request.POST['attendance'],
		# point_scored =request.POST['goals_total_scoreA'],
		overall_score_sectB =request.POST['overall_score_sectB'],
		)
	return behavior

def overall_rating(request):
	rating = Overall_rating(
		user=request.user,
		period_from = request.POST['from'],
		period_to=request.POST['to'],
		section_A=request.POST['overall_score_sectA'],
		section_B=request.POST['overall_score_sectB'],
		total_score=request.POST['total_score'],
		)
	return rating

def get_appr_info(request):
	appraisals = []
	goal = request.POST.getlist('goal')
	actual_result = request.POST.getlist('actual_result')
	weight = request.POST.getlist('weight')
	rating = request.POST.getlist('rating')
	score = request.POST.getlist('score')

	for i, val in enumerate(goal):
		i_appraisal = Appraisal_info(
			user=request.user,
			period_from=request.POST['from'],
			period_to=request.POST['to'],
			goal=goal[i],
			actual_result=actual_result[i],
			weight=weight[i],
			rating=rating[i],
		    score=score[i],
			)
		appraisals.append(i_appraisal)
	return appraisals

def get_accomplish_info(request):
	accomplishs = []
	accomplishment = request.POST.getlist('accomplishment')
	business_impact = request.POST.getlist('business_impact')

	for i, val in enumerate(accomplishment):
		i_accomplish = Accomplishment(
			user=request.user,
			period_from=request.POST['from'],
			period_to=request.POST['to'],
			accomplishment=accomplishment[i],
			business_impact=business_impact[i],
			)
		accomplishs.append(i_accomplish)
	return accomplishs

def get_performance_info(request):
	perfs = []
	key_strength = request.POST.getlist('key_strength')
	improvement_area = request.POST.getlist('improvement_area')
	developmental_recommendation = request.POST.getlist('developmental_recommendation')

	for i, val in enumerate(key_strength):
		i_perf = Perf_improvement(
			user=request.user,
			period_from=request.POST['from'],
			period_to=request.POST['to'],
			key_strength=key_strength[i],
			improvement_area=improvement_area[i],
			developmental_recommendation=developmental_recommendation[i],
			)
		perfs.append(i_perf)
	return perfs

def appr_handler(request):
	context = {}
	context['appraisee_success'] = 'Appraisal form has been submitted for approval'
	if request.method == 'POST':
		appr_form_model = appr_form(request)
		appr_period_model = appr_period(request)
		appr_info_model = get_appr_info(request)
		behavior_comp_model = behavior_comp(request)
		overall_rating_model = overall_rating(request)
		appr_accomplish_model = get_accomplish_info(request)
		appr_performace_model = get_performance_info(request)
		overall_rating_model = overall_rating(request)
		appr_comment_model = appr_comment(request)


		appr_form_model.save()
		appr_period_model.save()
		Appraisal_info.objects.bulk_create(appr_info_model)
		behavior_comp_model.save()
		overall_rating_model.save()
		Accomplishment.objects.bulk_create(appr_accomplish_model)
		Perf_improvement.objects.bulk_create(appr_performace_model)
		appr_comment_model.save()

		email = {}
		email['emp_applicant_name'] = appr_form_model.first_name + " " + appr_form_model.last_name
		email['emp_link'] = "{}/appr_confirm/{}/{}/{}/".format(st.APP_BASE_URL, request.user.pk, request.POST['from'], request.POST['to'])
		email['subject_title'] = 'Appraisal Form For your approval'
		email['emp_to'] = [request.POST['appraiser_email']]
		# email['cc'] = [request.POST['appraisee_email']]
		msg = '''
		<p> <strong> Dear Supervisor,  {applicant_name} </strong>has just submitted his appraisal form. Please click here <a href= {link}> Link </a> to login and have a one-on-one discussion with the employee before you click the approve button. <p>
		
		<p style='color:red;'> Please copy this link <span style='color:blue; font-style:italic;'> {link} </i> </span> and paste in your browser if the link button is not working or clickable</p>

		Thank you!
		AEDC Goal Settting Project
		'''
		msg = msg.format(applicant_name=email['emp_applicant_name'], link=email['emp_link'])
		email['emp_msg'] = msg
		send_emp_email(email)
		return redirect('/appr_success_page/')
		

	elif request.method == 'GET':
		return render(request, 'appraisal/appraisal_page.html')


def get_appr_details(request, user, period_from, period_to):
	context = {}
	user = User(pk=user)
	appr_form = Appraisal_Form.objects.filter(user=user)[0]
	goals = Appraisal_info.objects.filter(user=user, period_from=period_from, period_to=period_to)
	perfs = Perf_improvement.objects.filter(user=user, period_from=period_from, period_to=period_to)
	accomplishs = Accomplishment.objects.filter(user=user, period_from=period_from, period_to=period_to)
	appr_comments = Appr_comment.objects.filter(user=user, period_from=period_from, period_to=period_to)[0]
	behavior = Behavioral_competence.objects.filter(user=user, period_from=period_from, period_to=period_to)[0]
	rating = Overall_rating.objects.filter(user=user, period_from=period_from, period_to=period_to)[0]
	context['gen_info'] = appr_form
	context['period_from'] = period_from
	context['period_to'] = period_to
	context['goals'] = goals
	context['perfs'] = perfs
	context['accomplishs'] = accomplishs
	context['behavior'] = behavior
	context['rating'] = rating
	context['userid'] = user.id
	context['comment'] = appr_comments
	context['link'] = "/appr_approve/{}/{}/{}/".format(user.id, period_from, period_to)
	return render(request, 'appraisal/appr_approval_page.html', context)

def get_appr_details_reviewer(request, user, period_from, period_to):
	context = {}
	user = User(pk=user)
	appr_form = Appraisal_Form.objects.filter(user=user)[0]
	goals = Appraisal_info.objects.filter(user=user, period_from=period_from, period_to=period_to)
	perfs = Perf_improvement.objects.filter(user=user, period_from=period_from, period_to=period_to)
	accomplishs = Accomplishment.objects.filter(user=user, period_from=period_from, period_to=period_to)
	appr_comments = Appr_comment.objects.filter(user=user, period_from=period_from, period_to=period_to)[0]
	behavior = Behavioral_competence.objects.filter(user=user, period_from=period_from, period_to=period_to)[0]
	rating = Overall_rating.objects.filter(user=user, period_from=period_from, period_to=period_to)[0]
	context['gen_info'] = appr_form
	context['period_from'] = period_from
	context['period_to'] = period_to
	context['goals'] = goals
	context['perfs'] = perfs
	context['accomplishs'] = accomplishs
	context['behavior'] = behavior
	context['rating'] = rating
	context['userid'] = user.id
	context['comment'] = appr_comments
	context['link'] = "/appr_approve/{}/{}/{}/".format(user.id, period_from, period_to)
	return render(request, 'appraisal/appr_reviewer_page.html', context)

def get_appr_details_form(request, user, period_from, period_to):
	context = {}
	user = User(pk=user)
	appr_form = Appraisal_Form.objects.filter(user=user)[0]
	goals = Appraisal_info.objects.filter(user=user, period_from=period_from, period_to=period_to)
	perfs = Perf_improvement.objects.filter(user=user, period_from=period_from, period_to=period_to)
	accomplishs = Accomplishment.objects.filter(user=user, period_from=period_from, period_to=period_to)
	appr_comments = Appr_comment.objects.filter(user=user, period_from=period_from, period_to=period_to)[0]
	behavior = Behavioral_competence.objects.filter(user=user, period_from=period_from, period_to=period_to)[0]
	rating = Overall_rating.objects.filter(user=user, period_from=period_from, period_to=period_to)[0]
	context['gen_info'] = appr_form
	context['period_from'] = period_from
	context['period_to'] = period_to
	context['goals'] = goals
	context['perf'] = perfs
	context['accomplishs'] = accomplishs
	context['behavior'] = behavior
	context['rating'] = rating
	context['userid'] = user.id
	context['comment'] = appr_comments
	context['link'] = "/appr_final-form/{}/{}/{}/".format(user.id, period_from, period_to)
	return render(request, 'appraisal/appr_data_page.html', context)

def appr_approve(request, user, period_from, period_to):
	context={}
	context['approval_success_page'] = 'Appraisal form has been approved for final review'
	user = User(pk=user)
	appr = Appr_approve(approver=user, user=user, period_from=period_from, period_to=period_to, approved=True)
	appr.save()
	email = {}
	appr_form_model = Appraisal_Form.objects.filter(user=user)[0]
	email['applicant_name'] = appr_form_model.first_name + " " + appr_form_model.last_name
	email['emp_applicant_name'] = appr_form_model.first_name + " " + appr_form_model.last_name
	email['link'] = "{}/appr_review/{}/{}/{}/".format(st.APP_BASE_URL, user.pk, period_from, period_to)
	email['emp_link'] = "{}/appr_final-form/{}/{}/{}/".format(st.APP_BASE_URL, user.pk, period_from, period_to)
	email['subject'] = 'Appraisal Form For your Review'
	email['subject_title'] = 'Your Appraisal Form has been updated'
	email['cc'] = [appr_form_model.appraiser_email]
	email['to'] = [appr_form_model.reviewer_email]
	email['emp_to'] = [appr_form_model.appraisee_email]
	msg = '''
	<p> <strong> Dear Sir/Ma, {applicant_name}'s </strong> Appraisal application has been approved by the line manager, Please click here <a href= {link}> Link </a>to login and review. </p>

	<p style='color:red;'> Please copy this link <span style='color:blue; font-style:italic;'> {link} </i> </span> and paste in your browser if the link button is not working or clickable</p>
	Thank you!
	AEDC Goal Settting Project
	'''
	msg = msg.format(applicant_name=email['applicant_name'], link=email['link'])
	email['msg'] = msg

	appraisee_msg = '''
	 <strong> Dear {applicant_name}, </strong> 

	<p> your appraisal form has been approved by your line manager, Please click here <a href= {link}> Link </a>to view form </p>

	<p style='color:red;'> Please copy this link <span style='color:blue; font-style:italic;'> {link} </i> </span> and paste in your browser if the link button is not working or clickable</p>
	Thank you!
	AEDC Goal Settting Project
	'''
	appraisee_msg = appraisee_msg.format(applicant_name=email['emp_applicant_name'], link=email['emp_link'])
	email['emp_msg'] = appraisee_msg
	send_email(email)
	send_emp_email(email)

	return redirect('/approval_page/')

def appr_final_approval(request, user, period_from, period_to):
	context={}
	context['success'] = 'Appraisal form is finally submitted'
	user = User(pk=user)
	appr = Appr_approve(approver=user, user=user, period_from=period_from, period_to=period_to, approved=True)
	appr.save()
	email = {}
	appr_form_model = Appraisal_Form.objects.filter(user=user)[0]
	email['applicant_name'] = appr_form_model.first_name + " " + appr_form_model.last_name
	email['link'] = "{}/appr_final-form/{}/{}/{}/".format(st.APP_BASE_URL, user.pk, period_from, period_to)
	email['subject'] = 'Appraisal Submission has been Reviewed'
	email['cc'] = [appr_form_model.appraiser_email]
	email['to'] = [appr_form_model.appraisee_email]
	msg = '''
	<strong> Dear {applicant_name},</strong>
	
	<p>Your goal setting form has been submitted, Please click here <a href={link}> Link </a> to view form </p>

	For further information as regards your goal setting please contact the HR department.
	Best Of Luck!!!

	<p style='color:red;'> Please copy this link <span style='color:blue; font-style:italic;'> {link} </i> </span> and paste in your browser if the link button is not working or clickable</p>

	AEDC Goal Settting Project
	'''
	msg = msg.format(applicant_name=email['applicant_name'], link=email['link'])
	email['msg'] = msg
	send_email(email)

	return redirect('/approved_submission/')

def update_rec(request, pk):
	user = User.objects.get(pk=pk)
	keys = request.POST.getlist('key')
	for key in keys:
		print(key)		
		upt_goal = goal_info.objects.get(pk=int(key))
		upt_goal.objective = request.POST["objective*{}".format(key)]
		upt_goal.specific_task = request.POST["specific_task*{}".format(key)]
		upt_goal.KPI = request.POST["achievement*{}".format(key)]
		upt_goal.Strategic_focus = request.POST["strat*{}".format(key)]
		upt_goal.Balanced_scorecard = request.POST["bal*{}".format(key)] 
		upt_goal.weight = request.POST["weight*{}".format(key)]
		upt_goal.timeline = request.POST["timeline*{}".format(key)]

		upt_goal.save()
	comments = Comment.objects.filter(user=user, period_from=request.POST['period_from'], period_to=request.POST['period_to'])[0]
	comments.appraiser_comment = request.POST['appraiser_comment']
	comments.save()

	return HttpResponseRedirect("/confirm/{}/{}/{}/".format(pk,request.POST['period_from'],request.POST['period_to']))

def update_rec2(request, pk):
	user = User.objects.get(pk=pk)
	keys = request.POST.getlist('key')
	for key in keys:		
		upt_goal = goal_info.objects.get(pk=int(key))
		upt_goal.objective = request.POST["objective*{}".format(key)]
		upt_goal.specific_task = request.POST["specific_task*{}".format(key)]
		upt_goal.KPI = request.POST["achievement*{}".format(key)]
		upt_goal.Strategic_focus = request.POST["strat*{}".format(key)]
		upt_goal.Balanced_scorecard = request.POST["bal*{}".format(key)]
		upt_goal.weight = request.POST["weight*{}".format(key)]
		upt_goal.timeline = request.POST["timeline*{}".format(key)]

		upt_goal.save()
	comments = Comment.objects.filter(user=user, period_from=request.POST['period_from'], period_to=request.POST['period_to'])[0]
	comments.reviewer_comment = request.POST['reviewer_comment']
	comments.save()

	return HttpResponseRedirect("/review/{}/{}/{}/".format(pk,request.POST['period_from'],request.POST['period_to']))

def send_email(details):
    applicant_name = details['applicant_name']
    link = details['link']
    subject = details['subject']
    sender = 'software.notice@abujaelectricity.com'
    send_to = details['to']
    cc = details['cc']
    msg = details['msg']

    # print(cc, send_to)
    html_content = msg
    
    email = EmailMultiAlternatives(subject=subject, body=msg, from_email=sender, to=send_to, cc=cc)
    email.attach_alternative(html_content, "text/html")
    email.send()
    return HttpResponse('Email Sent successfully')

def send_emp_email(details):
    applicant_name = details['emp_applicant_name']
    link = details['emp_link']
    subject = details['subject_title']
    sender = 'software.notice@abujaelectricity.com'
    send_to = details['emp_to']
    emp_msg = details['emp_msg']

    html_content = emp_msg
    
    email = EmailMultiAlternatives(subject=subject, body=emp_msg, from_email=sender, to=send_to)
    email.attach_alternative(html_content, "text/html")
    email.send()
    return HttpResponse('Email Sent successfully')

def logOut(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))


