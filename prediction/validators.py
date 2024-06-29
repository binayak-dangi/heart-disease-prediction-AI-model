import re
from django.core.exceptions import ValidationError

def validate_full_name(value):
    if not re.match(r'^[a-zA-Z\s]+$', value):
        raise ValidationError('Full name should contain only letters.')

def validate_phone_number(value):
    if not re.match(r'^\d+$', value):
        raise ValidationError('Phone number should contain only digits.')
