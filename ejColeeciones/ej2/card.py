from typeguard import typechecked


@typechecked
class Card:
    def __init__(self, suit: str, number: int):
        self.__suit = suit
        self.__number = number

    def __repr__(self):
        return f"La carta es el {self.__number} de {self.__suit}"
