from django.db import models


class ExamScore(models.Model):

    allSubject = (
        ("คณิตสาสตร์", "คณิตสาสตร์"),
        ("ฟิสิกส์", "ฟิสิกส์"),
        ("ชีววิทยา", "ชีววิทยา"),
        ("อังกฤษ", "อังกฤษ"),
        ("ศิลปะ", "ศิลปะ"),
        ("สังคม", "สังคม"),
    )

    subject = models.CharField(max_length=200, choices=allSubject, default="math")
    student_name = models.CharField(max_length=200)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.student_name
