def get_list_display(model):
    return [field.name for field in model._meta.fields]
