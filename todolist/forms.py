from django import forms

class TodoListForm(forms.Form):
    inputField = forms.CharField(max_length=45,
    widget=forms.TextInput(
        attrs={
            'class' : 'form-control mr-2 text-italic',
            'placeholder':'what todo e.g buy eggs',
            'aria-label':'Todo',
            'aria-describeby':'add-btn',
            'title': 'Type here'
            }
        )
    );
