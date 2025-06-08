from django import forms 

from .models import Instructors,AreaOfExpertise


class InstructorForm(forms.ModelForm):


    class Meta:

        model = Instructors

        exclude = ['profile', 'uuid', 'active_status', 'name']

        widgets={

            'image'    :   forms.FileInput(attrs={
                                                    'class' :   'form-control',
                                                    'required'  :   'required'
                                                }),
                                                
            'description' : forms.Textarea(attrs={
                                                    'class' :   'form-control',
                                                    'required'  :   'required',
                                                    'rows':'6',
                                                    'cols':'15'
                                                }),

            }
        

        area_of_expertise = forms.ModelChoiceField(queryset=AreaOfExpertise.objects.all(),widget=forms.Select(attrs={

                                                     'class' :   'form-control',
                                                     'required'  :   'required',

                                                }))