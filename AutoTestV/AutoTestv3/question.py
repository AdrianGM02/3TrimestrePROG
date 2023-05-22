from typeguard import typechecked


class No_has_escrito_enunciado(ValueError):
    def __init__(self, mensaje):
        self.__mensaje = mensaje
        super().__init__(mensaje)


class No_hay_opciones(ValueError):
    def __init__(self, mensaje):
        self.__mensaje = mensaje
        super.__init__(mensaje)


class Options_Error(Exception):
    def __init__(self, mensaje):
        self.__mensaje = mensaje
        super().__init__(mensaje)


class BaseScore_Error(Exception):
    def __init__(self, mensaje):
        self.__mensaje = mensaje
        super().__init__(mensaje)


@typechecked
class Question:
    def __init__(self, name_question: str, statement: str, choices: list[tuple[str, float]], points: float = 1.0):
        self.__check(name_question, statement, choices, points)
        self.__name = name_question
        self.__statement = statement
        self.__choices = choices
        self.__points = points

    @staticmethod
    def __check(name, statement, choices, points: float = 1):
        if name == "" or statement == "":
            raise No_has_escrito_enunciado("No has indicado el nombre de las cuestion o de el enunciado")
        if len(choices) == 0:
            raise No_hay_opciones("No se han indicado opciones")
        list_points_of_options = [choice[1] for choice in choices]
        if points not in list_points_of_options:
            raise Options_Error("No hay ninguna opción que tenga la puntuacion máxima")
        if points < 0:
            raise BaseScore_Error("La base no puede ser negativo")

    def get_score(self, chosen_option: int):
        self.__check_if_option_is_correct(chosen_option)
        score_option = self.__choices[chosen_option - 1][1]
        return score_option

    def __check_if_option_is_correct(self, chosen_option: int):
        if chosen_option > len(self.__choices):
            raise Options_Error("Esta opción no existe en esta pregunta")

    @property
    def name_question(self):
        return self.__name

    @property
    def statement(self):
        return self.__statement

    @property
    def choice(self):
        return self.__choices

    @property
    def points(self):
        return self.__points
