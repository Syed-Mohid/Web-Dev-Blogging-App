from django import forms
from .models import Post, Category

#choices =[('General','General'),('Entertainment','Entertainment'),('Science','Science'),('Sport','Sports'),]

choices = Category.objects.all().values_list('name','name')

choice_list =[]

for item in choices:
    choice_list.append(item)

class  PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author','category','body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Title'}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
            'category': forms.Select(choices=choice_list , attrs={'class':'form-control','placeholder':'Select Category'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }

class  EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Title'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }