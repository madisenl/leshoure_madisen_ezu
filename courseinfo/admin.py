from django.contrib import admin

from .models import Semester, Section, Course, Student, Registration, Period, Year, Instructor

admin.site.register(Semester)
admin.site.register(Section)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Registration)
admin.site.register(Period)
admin.site.register(Year)
admin.site.register(Instructor)

