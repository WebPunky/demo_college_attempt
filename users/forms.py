from django.contrib.auth.forms import UserCreationForm

from .models import Users

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Users
        fields = ("first_name", "last_name", "username", "email", "phone")

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for name in self.fields:
            self.fields[name].required = True
