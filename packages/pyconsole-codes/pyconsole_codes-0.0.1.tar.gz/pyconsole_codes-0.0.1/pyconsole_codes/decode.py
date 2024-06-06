import io
import time
from typing import Any

from . import types


def decode(text:str|bytes)->list[str|Any]:
    if type(text)==str:
        byte_text = text.encode('utf-8')
    elif type(text)==bytes:
        byte_text = text
    else:
        raise TypeError('text must be str or bytes')
    byte_io = io.BytesIO(byte_text)
    decoded_text = []
    last_word = b""
    # is_ESC
    while 1:
        byte = byte_io.read(1)
        match byte:
            case b'':
                return decoded_text
            case b'\x1B':
                if last_word!=b"":
                    decoded_text.append(last_word.decode('utf-8'))
                    last_word = b""
                esc = types.esc.ESC(is_read_x1B=True)
                d = esc.decode(byte_io)
                decoded_text.append(d)
            case _:
                last_word+=byte
    # for byte in byte_text:
    #     match byte:
    #         case b'\x1B':
    #             pass


        
