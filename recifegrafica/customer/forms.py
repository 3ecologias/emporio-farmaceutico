# -*- coding: utf-8 -*-

from oscar.apps.customer.forms import EmailUserCreationForm as CoreUserCreationForm
from oscar.apps.customer.forms import UserForm as CoreUserForm
from oscar.core.compat import (get_user_model, existing_user_fields)
from oscar.core.loading import get_profile_class
from django import forms
# from localflavor.br.forms import BRCNPJField, BRCPFField
from django.utils.translation import ugettext_lazy as _
User = get_user_model()

class EmailUserCreationForm(CoreUserCreationForm):

    PERSONA_CHOICES = (('fs','Física'),('jr', 'Jurídica'))

    persona = forms.CharField(label=_('Personalidade'), required=True,widget=forms.Select(choices=PERSONA_CHOICES))
    cnpj = forms.CharField(label=_('CNPJ'), required=False)
    cpf = forms.CharField(label=_('CPF'), required=False)
    class Meta:
        model = User
        fields = ('email','persona', 'cnpj', 'cpf')

class UserForm(CoreUserForm):
    class Meta:
        model = User
        fields = existing_user_fields(['first_name', 'last_name', 'email', 'cpf' , 'cnpj'])

Profile = get_profile_class()

if Profile:  # noqa (too complex (12))
    class UserAndProfileForm(forms.ModelForm):

        def __init__(self, user, *args, **kwargs):
            try:
                instance = Profile.objects.get(user=user)
            except Profile.DoesNotExist:
                # User has no profile, try a blank one
                instance = Profile(user=user)
            kwargs['instance'] = instance

            super(UserAndProfileForm, self).__init__(*args, **kwargs)

            # Get profile field names to help with ordering later
            profile_field_names = list(self.fields.keys())

            # Get user field names (we look for core user fields first)
            core_field_names = set([f.name for f in User._meta.fields])
            user_field_names = ['email']
            for field_name in ('first_name', 'last_name'):
                if field_name in core_field_names:
                    user_field_names.append(field_name)
            user_field_names.extend(User._meta.additional_fields)

            # Store user fields so we know what to save later
            self.user_field_names = user_field_names

            # Add additional user form fields
            additional_fields = forms.fields_for_model(
                User, fields=user_field_names)
            self.fields.update(additional_fields)
            # Ensure email is required and initialised correctly
            self.fields['email'].required = True

            # Set initial values
            for field_name in user_field_names:
                self.fields[field_name].initial = getattr(user, field_name)

            # Ensure order of fields is email, user fields then profile fields
            self.fields.keyOrder = user_field_names + profile_field_names

        class Meta:
            model = Profile
            exclude = ('user',)

        def clean_email(self):
            email = normalise_email(self.cleaned_data['email'])

            users_with_email = User._default_manager.filter(
                email__iexact=email).exclude(id=self.instance.user.id)
            if users_with_email.exists():
                raise ValidationError(
                    _("A user with this email address already exists"))
            return email

        def save(self, *args, **kwargs):
            user = self.instance.user

            # Save user also
            for field_name in self.user_field_names:
                setattr(user, field_name, self.cleaned_data[field_name])
            user.save()

            return super(ProfileForm, self).save(*args, **kwargs)

        ProfileForm = UserAndProfileForm
else:
        ProfileForm = UserForm
