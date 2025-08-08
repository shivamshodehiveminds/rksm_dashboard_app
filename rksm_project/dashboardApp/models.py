from . import models

class Student(models.Model):
    studentName = models.CharField(max_length=100)

    def __str__(self):
        return self.studentName


class Subject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Required on_delete
    name = models.CharField(max_length=200)
    mark = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.mark}"
