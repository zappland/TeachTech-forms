from django.forms import ModelForm
from django import forms
from .models import Certification
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, HTML, Field, Div
from crispy_forms.bootstrap import StrictButton

class CertForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['last_name','first_name','ssn','returning_or_new_hire','title_position','current_assignment','subject_grade','certification_status','nys_cert_area','cert_type','expiration_date','current_comment','comments_from_last_wksh','las','ats_w','cst','cst_subject','eas','ata']
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-offset-2 col-sm-2'
        self.helper.field_class = 'col-sm-8'
        self.helper.layout = Layout(
            'last_name','first_name','ssn','returning_or_new_hire','title_position','current_assignment','subject_grade','certification_status','nys_cert_area','cert_type','expiration_date','current_comment','comments_from_last_wksh','las','ats_w','cst','cst_subject','eas','ata',
        )
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'
        # self.helper.layout = Layout(

        #     Div('last_name', 'first_name', 'returning_or_new_hire'),
        #     Field('last_name', autocomplete='off'),
        #     Field('last_name', data_name="whatever"),
        #     Field('last_name', css_class="black-fields"),
        #     Field('last_name', css_id="custom_field_id"),
        #     Fieldset(
        #         'Tell us your favorite stuff {{ username }}',
        #         'like_website',
        #         'favorite_number',
        #         'favorite_color',
        #         'favorite_food',
        #         HTML("""
        #             <p>We use notes to get better, <strong>please help us {{ username }}</strong></p>
        #         """),
        #         'notes'
        #     ),
            # Submit('submit', 'Submit', css_class='button white'),
        # )



