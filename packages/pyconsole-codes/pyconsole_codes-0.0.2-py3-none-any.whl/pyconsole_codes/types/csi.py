import io


class CSI:
    """控制序列"""
    def __init__(self,is_read_x1B=False,is_read_key1=False):
        self.is_read_x1B = is_read_x1B
        self.is_read_key1 = is_read_key1
        self.parameters = []
        self.mode = None
        self.isDEC = False
        
    def decode(self,byte_io:io.BytesIO):
        if self.is_read_x1B==False:
            if byte_io.read(1)!=b'\x1B':
                raise Exception("not x1B")
            
        if self.is_read_key1==False:
            if byte_io.read(1)!=b'[':
                raise Exception("not [")
        
        number = []
        while True:
            byte = byte_io.read(1)
            match byte:
                case b'0'|b'1'|b'2'|b'3'|b'4'|b'5'|b'6'|b'7'|b'8'|b'9':
                    number.append(byte.decode('utf-8'))
                    continue
                case b';':
                    self.parameters.append(int("".join(number)))
                    number=[]
                    continue
                case b'?':
                    self.isDEC = True
                    continue
                case _:
                    if len(number)>0:
                        self.parameters.append(int("".join(number)))
                        number=[]
                    self.mode = byte
                    return
    def encode(self)->bytes:
        text = b'\x1B['
        if self.isDEC:
            text+=b'?'
        for i in self.parameters:
            text+=str(i).encode('utf-8')+b';'
        text+=self.mode

        return text
    def __str__(self) -> str:
        return f"CSI(parameters={self.parameters},mode={self.mode},isDEC={self.isDEC})"