class Model:

    def __init__(self) -> None:
        self.previous_value: str = ''
        self.value: str = ''
        self.operator: str = ''

    def calculate(self, caption):
        if caption == 'C':
            self.previous_value = ''
            self.value = ''
            self.operator = ''
        elif caption == '+/-' and self.value:
            self.value = (
                self.value[1:] if self.value[0] == '-' else f'-{self.value}')
        elif caption == '%' and self.value:
            value = (
                float(self.value) if '.' in self.value else int(self.value))
            self.value = str(value / 100)
        elif (caption == '=' and
              self.previous_value and
              self.operator and self.value):
            value = str(self._evaluate())
            self.value = value[0:-2] if value[-2:] == '.0' else value
            self.operator = caption
        elif caption == '.' and caption not in self.value:
            self.value += caption
        elif isinstance(caption, int) and self.operator == '=':
            self.value = str(caption)
            self.operator = ''
        elif isinstance(caption, int):
            self.value += str(caption)
        elif self.value:
            self.operator = caption
            self.previous_value = self.value
            self.value = ''
        return self.value

    def _evaluate(self):
        return eval(self.previous_value + self.operator + self.value)
