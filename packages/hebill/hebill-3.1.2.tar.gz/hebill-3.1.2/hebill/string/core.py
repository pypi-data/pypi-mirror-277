import secrets
import string
from ..digital.core import Digital


class String(str):
    def __new__(cls, characters):
        try:
            characters = str(characters)
        except (TypeError, ValueError) as e:
            raise ValueError(f"输入变量不能转化为字符串: {characters}") from e
        return str.__new__(cls, characters)

    @staticmethod
    def random(length: int = 16):
        if length <= 0:
            length = 16
        alphabet = string.ascii_letters + string.digits
        return ''.join(secrets.choice(alphabet) for _ in range(length))

    def contains(self, part: str):
        if not isinstance(part, str):
            raise ValueError("检查部分必须是字符串")
        return part in self

    def is_digitalizable(self):
        try:
            float(self.strip())
            return True
        except ValueError:
            return False

    def digitize(self) -> Digital:
        if self == '':
            return Digital(0)
        if not self.is_digitalizable():
            raise ValueError(f"字符不能转化为数浮点数: {self}")
        if '.' in self.strip():
            return Digital(float(self.strip()))
        return Digital(int(self.strip()))
