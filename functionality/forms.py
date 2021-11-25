from django import forms
from django.contrib.auth.models import User
from functionality import models


class UserRegistrationForm(forms.Form):
	email = forms.EmailField(label='Email', label_suffix=':')
	password = forms.CharField(label='Password', label_suffix=':', widget=forms.PasswordInput)
	password2 = forms.CharField(label="Confirm password", label_suffix=":", widget=forms.PasswordInput)
	name = forms.CharField(label='Name', label_suffix=':')
	surname = forms.CharField(label='Surname', label_suffix=':')
	salary = forms.IntegerField(label='salary', required=False)
	phone = forms.CharField(label="Phone number", label_suffix=":")
	cname = forms.ModelChoiceField(label="Country",label_suffix=":", queryset=models.Country.objects.all())

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email).count()>0:
			raise forms.ValidationError('This email was already registered: {0}'.format(email))
		return email

	def clean(self):
		cleaned_data = super().clean()
		password = cleaned_data['password']
		password2 = cleaned_data['password2']
		if password != password2:
			raise forms.ValidationError('Passwords do not match!')

class DiseaseFilterForm(forms.Form):
	disease_code = forms.CharField(label="Disease Code", label_suffix=":", required=False)
	id_DiseaseType = forms.ModelChoiceField(label="Disease Type", label_suffix=":", queryset=models.DiseaseType.objects.all(), required=False)
	pathogen = forms.ChoiceField(label="Pathogen", label_suffix=":", choices=[(x,x) for x in models.Disease.objects.values_list('pathogen', flat=True).distinct()], required=False)
	order_by = forms.ChoiceField(choices=((None,''),('disease_code','Disease code'),('id_DiseaseType','Disease type'),('description','Description')), required=False)

	def clean_pathogen(self):
		return self.cleaned_data['pathogen']


class RecordFilterForm(forms.Form):
	disease_code = forms.ModelChoiceField(label="Disease Code", label_suffix=":",
										  queryset=models.Disease.objects.all().distinct(), required=False)
	cname = forms.ModelChoiceField(label="Country", label_suffix=":", queryset=models.Country.objects.all().distinct(), required=False)
	email = forms.ModelChoiceField(label="Added by", label_suffix=":",
									  queryset=models.PublicServant.objects.all().distinct(), required=False)

	order_by = forms.ChoiceField(choices=((None,''),('total_death','Total deaths'),('total_patients','Total patients'), ('cname','Country'),('email','Added by')), required=False)


class DiscoverFilterForm(forms.Form):
	disease_code = forms.ModelChoiceField(label="Disease Code", label_suffix=":",
										  queryset=models.Disease.objects.all().distinct(), required=False)
	cname = forms.ModelChoiceField(label="Country", label_suffix=":", queryset=models.Country.objects.all().distinct(), required=False)

	order_by = forms.ChoiceField(choices=((None,''),('cname','Country'),('disease_code','Disease code'),('first_enc_date','First encounter date')), required=False)


class DoctorFilterForm(forms.Form):
	id_DiseaseType = forms.ModelChoiceField(label="Specialization disease type", label_suffix=":",
										  queryset=models.DiseaseType.objects.all().distinct(), required=False)
	cname = forms.ModelChoiceField(label="Country", label_suffix=":", queryset=models.Country.objects.all().distinct(), required=False)

	# order_by = forms.ChoiceField(choices=((None,''),('cname','Country'),('email','Email')), required=False)



	# def is_valid(self):
	# 	answer = super().is_valid()
	# 	any_field = self.data['disease_code'] or self.data['cname'] or self.data['email']
	# 	return any_field or answer

# class SendSolutionForm(forms.Form):
# 	text = forms.CharField(label = 'Решение', label_suffix = ':', required = False, max_length = 1200, strip = True, widget = forms.Textarea)
# 	image_attached = forms.ImageField(label = 'Приложенная картинка', label_suffix = ':', required = False)
#
# 	def clean_image_attached(self):
# 		text = self.cleaned_data['text']
# 		image_attached = self.cleaned_data['image_attached']
# 		if not (text or image_attached):
# 			raise forms.ValidationError('Оба поля не могут быть пустыми')
# 		return image_attached
#
#
# class EvaluateForm(forms.Form):
# 	score = forms.IntegerField(label = 'Балл',label_suffix = ':')
# 	comment = forms.CharField(label='Комментарий',label_suffix=':', required = False, widget = forms.Textarea)
#
# 	def clean_score(self):
# 		score = self.cleaned_data['score']
# 		if score>7 or score<0:
# 			raise forms.ValidationError('Балл должен быть целым числом от 0 до 7')
# 		if int(score) != score :
# 			raise forms.ValidationError('Балл должен быть целым числом.')
# 		return score
#



			
