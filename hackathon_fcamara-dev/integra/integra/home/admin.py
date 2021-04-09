from django.contrib import admin
from .models import Donate, Item, StudentList, ItemSelection, Grade, School, Student, ProfileType, DonationType, Profile

admin.site.register(Donate)
admin.site.register(Item)
admin.site.register(ItemSelection)
admin.site.register(Grade)
admin.site.register(School)
admin.site.register(Student)
admin.site.register(DonationType)
admin.site.register(Profile)
admin.site.register(ProfileType)
admin.site.register(StudentList)