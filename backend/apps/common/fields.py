from django.db.models import ForeignKey, CASCADE


class CustomForeignKey(ForeignKey):
    """
    Override ForeignKey in order to set `on_delete=CASCADE` by default.
    """

    def __init__(self, *args, **kwargs):
        kwargs['on_delete'] = kwargs.get('on_delete', CASCADE)

        super().__init__(*args, **kwargs)
