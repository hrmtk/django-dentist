from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {})


def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message_subject = request.POST['message-subject']
		message = request.POST['message']

		# send an email
		# send_mail(
		# 	message_subject, # subject
		# 	message, # message
		# 	message_email, # from email
		# 	['da@example.com'], # to email
		# )

		return render(request, 'contact.html', {'message_name': message_name})

	else:
		return render(request, 'contact.html', {})


def about(request):
	return render(request, 'about.html', {})


def appointment(request):
	if request.method == "POST":
		your_service = request.POST['your-service']
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_date = request.POST['your-date']
		your_time = request.POST['your-time']
		
		# send an appointment
		appointment = 'Name: ' + your_name + '\nService: ' + your_service
		
		# send_mail(
		# 	'Appointment request', # subject
		# 	appointment, # message
		# 	your_email, # from email
		# 	['da@example.com'], # to email
		# )
		
		return render(request, 'appointment.html', {

			'your_service': your_service,
			'your_name': your_name,
			'your_phone': your_phone,
			'your_email': your_email,
			'your_date': your_date,
			'your_time': your_time

		})

	else:
		return render(request, 'appointment.html', {})


def price(request):
	return render(request, 'price.html', {})


def service(request):
	return render(request, 'service.html', {})


def team(request):
	return render(request, 'team.html', {})


def testimonial(request):
	return render(request, 'testimonial.html', {})