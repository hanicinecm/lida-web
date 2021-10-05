from django.db import models


class BaseMixin:
    id = models.AutoField(primary_key=True)
    time_added = models.DateTimeField(auto_now_add=True)

    def str_to_repr(self, text):
        # noinspection PyUnresolvedReferences
        return f'{self.id}:{self.__name__}({text})'

    def __repr__(self):
        return self.str_to_repr(str(self))
