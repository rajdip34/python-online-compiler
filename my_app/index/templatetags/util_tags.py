from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def get_num_key_item(dictionary, key):
    return dictionary.get(int(key))