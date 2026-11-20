
from django import forms
from myapp.models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = "__all__"

    def clean_ename(self):
        ename = self.cleaned_data["ename"]

        if not ename.replace(" ", "").isalpha():
            raise forms.ValidationError(
                "Full name should contain letters only."
            )

        return ename

    def clean_econtact(self):
        econtact = self.cleaned_data["econtact"]

        if not econtact.isdigit():
            raise forms.ValidationError(
                "Contact should contain digits only."
            )

        return econtact
