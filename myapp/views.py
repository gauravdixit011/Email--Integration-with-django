from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Student
from django.core.mail import send_mail

# Create your views here.
def home(request):
    # new_student = Student(id="5", name="Akash")
    # new_student.save()
    # send_mail(
    #     "Welcome",
    #     "This is welcome message for creating successfull user",
    #     "swapsytesting@gmail.com",
    #     ["dgaurav300@gmail.com"],
    #     fail_silently=True,
    # )
    return HttpResponse("Home Page")

def email_form(request):
    return render(request, "send-email.html")
    
# post request for sending email
def send_email(request):
    if request.method == "POST":
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        from_email ="tcode837@gmail.com"
        recipient = [request.POST.get("recipient")]  

        send_mail(
            subject,
            message,
            from_email,
            recipient,
            fail_silently=False,
        )
        return HttpResponse("Email sent successfully!")
    else:
        return HttpResponse("Invalid request method.")
