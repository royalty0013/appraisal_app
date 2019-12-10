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

from .models import *
# Create your views here.

# def index(request):
# 	context = {}
# 	return render(request, 'goalsetting/index.html', context)

# def appraisal_homepage(request):
#   	context = {}
#   	return render(request, 'appraisal/appraisal_page.html', context)

def success_page(request):
	return render(request, 'goalsetting/appraisee_success_page.html')

def appr_suc_page(request):
	return render(request, 'goalsetting/approval_success_page.html')

def final_suc_page(request):
	return render(request, 'goalsetting/success_page.html')

def login_process(request):
	context = {}
	username = request.POST['username']
	password = request.POST['password']

	if not username.endswith('@abujaelectricity.com'):
		username = username+'@abujaelectricity.com'
	# print(username)

	ldap_login = ldapLogin(username,password)
	if ldap_login == True:
		user = createOrGetUser(username)
		user.backend = 'django.contrib.auth.backends.ModelBackend'
		login(request,user)
		return HttpResponseRedirect(reverse('page'))

	else:
		context['error']="Invalid Username Or Password. Please make sure you are on AEDC network"
		return render(request, 'goalsetting/index.html', context)


# @login_required(login_url='/')
def goal_handler(request):
	context = {}
	context['appraisee_success'] = 'Goal setting form has been submitted for approval'
	if request.method == 'POST':
		goal_form_model = goal_form(request)
		period_model = goal_period(request)
		goal_info_model = get_goal_info(request)
		goal_comment_model = goal_comment(request)

		goal_form_model.save()
		period_model.save()
		goal_info.objects.bulk_create(goal_info_model)
		goal_comment_model.save()

		email = {}
		email['emp_applicant_name'] = goal_form_model.first_name + " " + goal_form_model.last_name
		email['emp_link'] = "{}/confirm/{}/{}/{}/".format(st.APP_BASE_URL, request.user.pk, request.POST['from'], request.POST['to'])
		email['subject_title'] = 'Goal Setting Form For your approval'
		email['emp_to'] = [request.POST['appraiser_email']]
		# email['cc'] = [request.POST['appraisee_email']]
		msg = '''
		<p> <strong> Dear Supervisor,  {applicant_name} </strong>has just completed the goal setting application. Please click here <a href= {link}> Link </a> to login and have a one-on-one discussion with the employee before you click the approve button. <p>
		
		<p style='color:red;'> Please copy this link <span style='color:blue; font-style:italic;'> {link} </i> </span> and paste in your browser if the link button is not working or clickable</p>

		Thank you!
		AEDC Goal Settting Project
		'''
		msg = msg.format(applicant_name=email['emp_applicant_name'], link=email['emp_link'])
		email['emp_msg'] = msg
		send_emp_email(email)
		return redirect('/success_page/')
		

	elif request.method == 'GET':
		return render(request, 'goalsetting/form_page.html')
		return render(request, 'appraisal/page.html')


def goal_form(request):
	f = Goal_Form(
		user=request.user,
		first_name = request.POST['firstname'],
		middle_name = request.POST['surname'],
		last_name = request.POST['lastname'],
		staff_id = request.POST['staffid'],
		position = request.POST['position'],
		unit = request.POST['unit'],
		directorate = request.POST['directorate'],
		designation = request.POST['designation'],
		supervisor_name = request.POST['supervisor_name'],
		area_office = request.POST['area_office'],
		region = request.POST['region'],
		total = request.POST['total'],
		appraisee_email = request.POST['appraisee_email'],
		appraiser_email = request.POST['appraiser_email'],
		reviewer_email = request.POST['reviewer_email'],
		# appraisee_comment=request.POST['appraisee_comment'],
		# appraiser_comment=request.POST['appraiser_comment'],
		# reviewer_comment=request.POST['reviewer_comment'],
	)
	return f

def goal_comment(request):
	c = Comment(
		user=request.user,
		first_name = request.POST['firstname'],
		last_name = request.POST['surname'],
		staff_id = request.POST['staffid'],
		period_from = request.POST['from'],
		period_to=request.POST['to'],
		appraisee_comment = request.POST['appraisee_comment']

		)
	return c

def goal_period(request):
	period = period_info(
		date_from=request.POST['from'], 
		date_to=request.POST['to'],
		)
	return period

def get_goal_info(request):
	goals = []
	objective = request.POST.getlist('objective')
	specific_task = request.POST.getlist('specific_task')
	achievement = request.POST.getlist('achievement')
	strat = request.POST.getlist('strat')
	bal = request.POST.getlist('bal')
	weight = request.POST.getlist('weight')
	timeline = request.POST.getlist('timeline')


	for i, val in enumerate(objective):
		i_goal = goal_info(
			user=request.user,
			period_from=request.POST['from'],
			period_to=request.POST['to'],
			objective=objective[i],
			specific_task=specific_task[i],
			KPI=achievement[i],
			Strategic_focus=strat[i],
		    Balanced_scorecard=bal[i],
			weight=weight[i],
			timeline=timeline[i],
			)
		goals.append(i_goal)
	return goals

def get_details(request, user, period_from, period_to):
	context = {}
	user = User(pk=user)
	goal_form = Goal_Form.objects.filter(user=user)[0]
	goals = goal_info.objects.filter(user=user, period_from=period_from, period_to=period_to)
	comments = Comment.objects.filter(user=user, period_from=period_from, period_to=period_to)[0]
	context['gen_info'] = goal_form
	context['period_from'] = period_from
	context['period_to'] = period_to
	context['goals'] = goals
	context['userid'] = user.id
	context['comments'] = comments
	# weight_sum = goals.aggregate(Sum('weight'))
	# context['weight'] = weight_sum['weight__sum']
	# if context['weight'] > 100:
	# 	err_msg = 'ooops!!! please limit to 100'
	# err_msg = err_msg
	# context['weight_err'] = err_msg
	context['link'] = "/approve/{}/{}/{}/".format(user.id, period_from, period_to)
	return render(request, 'goalsetting/approval_page.html', context)

def get_details_reviewer(request, user, period_from, period_to):
	context = {}
	user = User(pk=user)
	goal_form = Goal_Form.objects.filter(user=user)[0]
	goals = goal_info.objects.filter(user=user, period_from=period_from, period_to=period_to)
	comments = Comment.objects.filter(user=user, period_from=period_from, period_to=period_to)[0]
	context['gen_info'] = goal_form
	context['period_from'] = period_from
	context['period_to'] = period_to
	context['goals'] = goals
	context['userid'] = user.id
	context['comments'] = comments
	context['link'] = "/final_approval/{}/{}/{}/".format(user.id, period_from, period_to)
	return render(request, 'goalsetting/reviewer_page.html', context)

def get_details_form(request, user, period_from, period_to):
	context = {}
	user = User(pk=user)
	goal_form = Goal_Form.objects.filter(user=user)[0]
	goals = goal_info.objects.filter(user=user, period_from=period_from, period_to=period_to)
	comments = Comment.objects.filter(user=user, period_from=period_from, period_to=period_to)[0]
	context['gen_info'] = goal_form
	context['period_from'] = period_from
	context['period_to'] = period_to
	context['goals'] = goals
	context['userid'] = user.id
	context['comments'] = comments
	context['link'] = "/final_form/{}/{}/{}/".format(user.id, period_from, period_to)
	return render(request, 'goalsetting/data_page.html', context)

def approve(request, user, period_from, period_to):
	context={}
	context['approval_success_page'] = 'Goal setting form has been approved for final review'
	user = User(pk=user)
	appr = Approve(approver=user, user=user, period_from=period_from, period_to=period_to, approved=True)
	appr.save()
	email = {}
	goal_form_model = Goal_Form.objects.filter(user=user)[0]
	email['applicant_name'] = goal_form_model.first_name + " " + goal_form_model.last_name
	email['emp_applicant_name'] = goal_form_model.first_name + " " + goal_form_model.last_name
	email['link'] = "{}/review/{}/{}/{}/".format(st.APP_BASE_URL, user.pk, period_from, period_to)
	email['emp_link'] = "{}/final-form/{}/{}/{}/".format(st.APP_BASE_URL, user.pk, period_from, period_to)
	email['subject'] = 'Goal Setting Form For your Review'
	email['subject_title'] = 'Your Goal Setting Form has been updated'
	email['cc'] = [goal_form_model.appraiser_email]
	email['to'] = [goal_form_model.reviewer_email]
	email['emp_to'] = [goal_form_model.appraisee_email]
	msg = '''
	<p> <strong> Dear Sir/Ma, {applicant_name}'s </strong> goal setting application has been approved by the line manager, Please click here <a href= {link}> Link </a>to login and review. </p>

	<p style='color:red;'> Please copy this link <span style='color:blue; font-style:italic;'> {link} </i> </span> and paste in your browser if the link button is not working or clickable</p>
	Thank you!
	AEDC Goal Settting Project
	'''
	msg = msg.format(applicant_name=email['applicant_name'], link=email['link'])
	email['msg'] = msg

	appraisee_msg = '''
	 <strong> Dear {applicant_name}, </strong> 

	<p> your goal setting form has been approved by your line manager, Please click here <a href= {link}> Link </a>to view form </p>

	<p style='color:red;'> Please copy this link <span style='color:blue; font-style:italic;'> {link} </i> </span> and paste in your browser if the link button is not working or clickable</p>
	Thank you!
	AEDC Goal Settting Project
	'''
	appraisee_msg = appraisee_msg.format(applicant_name=email['emp_applicant_name'], link=email['emp_link'])
	email['emp_msg'] = appraisee_msg
	send_email(email)
	send_emp_email(email)

	return redirect('/approval_page/')

def final_approval(request, user, period_from, period_to):
	context={}
	context['success'] = 'Goal setting form is finally submitted'
	user = User(pk=user)
	appr = Approve(approver=user, user=user, period_from=period_from, period_to=period_to, approved=True)
	appr.save()
	email = {}
	goal_form_model = Goal_Form.objects.filter(user=user)[0]
	email['applicant_name'] = goal_form_model.first_name + " " + goal_form_model.last_name
	email['link'] = "{}/final-form/{}/{}/{}/".format(st.APP_BASE_URL, user.pk, period_from, period_to)
	email['subject'] = 'Goal Setting Submission has been Reviewed'
	email['cc'] = [goal_form_model.appraiser_email]
	email['to'] = [goal_form_model.appraisee_email]
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


