import re

def normalize_phone(ph_number):
    ph_number = re.sub(r'[^0-9+]', '', ph_number)

    if not ph_number.startswith('+'):
        ph_number = '+38' + ph_number

    return ph_number
