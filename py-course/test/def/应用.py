import random
import string

ALL_CHARS = string.digits + string.ascii_letters

def generate_code(code_len: int = 6) -> str:
    """生成指定长度的验证码
    :param code_len: 验证码的长度(默认4个字符)
    """
    return ''.join(random.choices(ALL_CHARS, k=code_len))

code = generate_code(4)
# print(code)