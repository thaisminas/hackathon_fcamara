from django.contrib import admin
from .models import Donate, ItemType, ItemSelection, Grade, School, Student, ProfileType, DonationType, Profile

admin.site.register(Donate)
admin.site.register(ItemType)
admin.site.register(ItemSelection)
admin.site.register(Grade)
admin.site.register(School)
admin.site.register(Student)
admin.site.register(DonationType)
admin.site.register(Profile)
admin.site.register(ProfileType)