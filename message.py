import inspect


def get_field_name(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]


class Field:
    separator = "="

    def __init__(self, field_name: str, value: float):
        self.field_name = field_name[0]
        self.value = value

    def to_string(self) -> str:
        string = self.field_name + Field.separator + str(self.value)
        return string

    @staticmethod
    def parse(string: str):
        res = string.split(Field.separator)
        return Field(res[0], float(res[1]))


class Message:
    separator = ";"

    def __init__(self, message: str = ""):
        self.message = message
        self.fields = []
        if message != "":
            self.fields = self.parse()


    def get_specific_field(self, var_name):
        needed_field = None
        for i, field in enumerate(self.fields):
            if field.field_name == var_name:
                needed_field = field
                return needed_field
        if needed_field == None:
            raise Exception("Искомое поле не найдено. Процедура аутентификации провалена")

    def add_field(self, field: Field):
        self.fields.append(field)

    def parse(self):
        self.fields.clear()

        full_mes_res = self.message.split(Message.separator)
        if len(full_mes_res) > 0:
            for i, str_field in enumerate(full_mes_res):
                field = Field.parse(str_field)
                self.fields.append(field)
        return self.fields

    def to_string(self):
        message = ""
        if len(self.fields) > 0:
            for i, field in enumerate(self.fields):
                message += field.to_string()
                if i + 1 > len(self.fields) - 1:
                    return message
                else:
                    message += Message.separator
