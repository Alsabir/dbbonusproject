from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .models import MyUser
#from .models import Problem, Solution, TypeOfProblem, Evaluation, ProfileData
#admin.site.register(User, UserAdmin)



class DiseaseInline(admin.TabularInline):
    model = Disease


class CountryInline(admin.TabularInline):
    model = Country

class RecordInline(admin.TabularInline):
    model = Record

class MyUserInline(admin.TabularInline):
    model = MyUser

class DoctorInline(admin.TabularInline):
    model = Doctor

class PublicServantInline(admin.TabularInline):
    model = PublicServant

class SpecializeInline(admin.TabularInline):
    model = Specialize

class DiscoverInline(admin.TabularInline):
    model = Discover


class DiseaseTypeInline(admin.TabularInline):
    model = DiseaseType

class RecordInline(admin.TabularInline):
    model = Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ("id","disease_code","cname","email","total_death","total_patients")


@admin.register(DiseaseType)
class DiseaseTypeAdmin(admin.ModelAdmin):
    list_display = ("id","description")
    inlines = (DiseaseInline,)

@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('disease_code','pathogen','description')
    #inlines = (DiseaseTypeInline,)


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    exclude = []
    inlines = (DoctorInline, PublicServantInline)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    exclude = []
    inlines = (SpecializeInline,)


@admin.register(PublicServant)
class PublicServantAdmin(admin.ModelAdmin):
    exclude = []
    inlines = (RecordInline,)


@admin.register(Discover)
class DiscoverAdmin(admin.ModelAdmin):
    exclude = []
    #inlines = (SpecializeInline,)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('cname','population')
    inlines = (DiscoverInline, RecordInline, MyUserInline)






#
# class SolutionInline(admin.TabularInline):
#     model = Solution
#     extra = 0
#
# class EvaluationInline(admin.TabularInline):
#     model = Evaluation
#     extra = 0
#
# @admin.register(Problem)
# class ProblemAdmin(admin.ModelAdmin):
#     list_display = ('title','description','image_attached')
#     inlines = [SolutionInline]
#
#
#
# @admin.register(Solution)
# class SolutionAdmin(admin.ModelAdmin):
# 	exclude = []
# 	inlines = [EvaluationInline]
#
# @admin.register(ProfileData)
# class ProfileDataAdmin(admin.ModelAdmin):
# 	exclude = []
#
#
# @admin.register(Evaluation)
# class EvaluationAdmin(admin.ModelAdmin):
#     exclude = []
#
#


