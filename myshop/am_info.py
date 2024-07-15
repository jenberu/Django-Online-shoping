# myshop/am_info.py
from django.utils.translation.trans_real import LANG_INFO

def add_am_language_info():
    LANG_INFO['am'] = {
        'bidi': False,
        'code': 'am',
        'name': 'Amharic',
        'name_local': 'አማርኛ',
    }
