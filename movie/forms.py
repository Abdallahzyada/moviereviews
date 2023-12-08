from django.forms import ModelForm, Textarea
from .models import Review

class ReviewForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class':'form-control'})
        self.fields['watchAgain'].widget.attrs.update({'class':'form-chick-input'})
        
    class Meta:
    
        model = Review
        fields = ['text', 'watchAgain']
        labels = {'watchAgagin':('Watch Again')}
        widgets = {'text':Textarea(attrs={'rows':4}),}
    