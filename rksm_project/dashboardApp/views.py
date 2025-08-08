from django.shortcuts import render
from django.http import JsonResponse
from .models import Student

#git push -u origin shivam

# student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Required on_delete
#     name = models.CharField(max_length=200)
#     mark = models.IntegerField()


# def req(request):
#     if request.method=='POST':
#         student=request.POST.get('student')
#         name=request.POST.get('name')
#         marks=request.POST.get('marks')
        
#         if student and name and marks:
#             Student.objects.create(student=student,name=name,marks=marks)
#             return render(request,'forms.html')
#     return render(request, 'forms.html')

from django.shortcuts import render, redirect
from .models import Student  # Ensure Student model is imported

def req(request): 
    if request.method == 'POST':
        student = request.POST.get('student')
        name = request.POST.get('name')
        marks = request.POST.get('marks')

        if student and name and marks:
            try:
                marks = int(marks)  # Optional: Convert marks to int if your model expects it
                Student.objects.create(student=student, name=name, marks=marks)
                return redirect('form_success')  # Better to redirect after POST
            except ValueError:
                # Handle invalid integer conversion if needed
                pass

    return render(request, 'forms.html')
