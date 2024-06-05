import typing
import collections.abc

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class BPyML_BaseUI:
    """This is a mix-in class that defines a draw function
    which checks for draw_data
    """

    def draw(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...
