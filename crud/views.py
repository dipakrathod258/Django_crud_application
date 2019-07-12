from django.shortcuts import render, redirect
from .models import Student
import json

def index(request):
	students = Student.objects.all()
	return render(request, "index.html", {'students':students})

def create_student(request):
	return render(request, "create.html")

def store_details(request):
	if request.method =="POST":
		hobbies = ','.join(request.POST.getlist("hobbies[]"))
		flag = request.POST.get("first_name") and request.POST.get("last_name") and request.POST.get("email") and request.POST.get("alternate_email") and request.POST.get("mobile") and request.POST.get("alternate_mobile") and request.POST.get("address") and request.POST.get("gender") and hobbies
		if flag:
			stud = Student()
			stud.first_name = request.POST.get("first_name")
			stud.last_name = request.POST.get("last_name")
			stud.email = request.POST.get("email")
			stud.alternate_email = request.POST.get("alternate_email")
			stud.mobile = request.POST.get("mobile")
			stud.alternate_mobile = request.POST.get("alternate_mobile")
			stud.address = request.POST.get("address")
			# stud.hobbies = request.POST.get("hobbies")
			stud.hobbies = hobbies
			# stud.gender = request.POST.get("gender")
			stud.gender = request.POST.get("gender")
			stud.save()
		else:
			return redirect("/home")
	return redirect("/home")
def edit(request, id):
	student = Student.objects.get(id=id)
	print("====student+++++")
	print(student.hobbies.split(","))
	student.hobbies = student.hobbies.split(",")
	print(vars(student))
	return render(request, "edit.html", {"student": student})

def update_details(request, id):
	if request.method =="POST":
		if request.POST.get("first_name") and request.POST.get("last_name") and request.POST.get("email"):
			stud = Student.objects.get(id=id)
			stud.first_name = request.POST.get("first_name")
			stud.last_name = request.POST.get("last_name")
			stud.email = request.POST.get("email")
			stud.save()
		else:
			return redirect("/home")
	return redirect("/home")

def destroy(request, id):
	stud = Student.objects.get(id=id)
	stud.delete()
	return redirect("/home")
