from django.forms import ModelForm
from. models import Task
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        #self.fields['name'].widget.attrs['class'] = 'form-control'
        #self.fields['field2'].widget.attrs['readonly'] = True