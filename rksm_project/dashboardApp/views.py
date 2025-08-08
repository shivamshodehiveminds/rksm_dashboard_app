from django.shortcuts import render
from django.http import JsonResponse
from .models import Student

#git push -u origin shivam

def req(request):
    if request.method=='POST':
        studentName=request.POST.get('studentName')
        marks=request.POST.get('marks')
        subject=request.POST.get('subject')
        if studentName and marks and subject:
            Student.objects.create(studentName=studentName,marks=marks,subject=subject)
            return render(request,'thankyou.html')
    return render(request, 'forms.html')