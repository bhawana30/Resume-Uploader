from django import forms
from .models import Resume
Gender_Choices = {
    ('Male','Male'),
    ('Female','Female')
}
job_city_locations={
    ('Delhi','Delhi'),
    ('Mumbai','Mumbai'),
    ('Bangalore','Bangalore'),
    ('Pune','Pune'),
    ('Noida','Noida')
}
class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=Gender_Choices,widget=forms.RadioSelect)
    job_city=forms.MultipleChoiceField(choices=job_city_locations,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=Resume
        fields=['name','dob','gender','locality','city',
                'pin','state','email','job_city','mobile','profile_image','my_file']
        labels ={'name':'Full Name','dob':'Date of Birth','pin':'Pin Code','mobile':'Mobile No.','email':'Email Id',
                 'job_city':'Preferred Job Location','profile_image':'Profile Image','my_file':'Document'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }