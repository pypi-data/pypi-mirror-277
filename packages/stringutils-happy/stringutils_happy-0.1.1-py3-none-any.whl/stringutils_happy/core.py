# stringutils/core.py

def to_snake_case(s):
    import re
    s = re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
    return s

def to_camel_case(s):
    s = ''.join(word.capitalize() or '_' for word in s.split('_'))
    return s[0].lower() + s[1:]

def remove_special_characters(s):
    import re
    return re.sub(r'[^A-Za-z0-9 ]+', '', s)

def normalize_whitespace(s):
    import re
    return ' '.join(s.split())
