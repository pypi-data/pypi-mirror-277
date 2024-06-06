import io
from typing import Any

from pyconsole_codes.types import csi


class ESC:
    def __init__(self,is_read_x1B=False):
        self.is_read_x1B = is_read_x1B
    def decode(self,byte_io:io.BytesIO)->Any:
        if self.is_read_x1B==False:
            if byte_io.read(1)!=b'\x1B':
                raise Exception("not x1B")

        byte = byte_io.read(1)
        match byte:
            case b'd':
                return IND(is_read_x1B=True,is_read_d=True)
            case b'E':
                return NEL(is_read_x1B=True,is_read_e=True)
            case b'H':
                return HTS(is_read_x1B=True,is_read_H=True)
            case b'M':
                return RI(is_read_x1B=True,is_read_M=True)
            case b'Z':
                return DECID(is_read_x1B=True,is_read_Z=True)
            case b'7':
                return DECSC(is_read_x1B=True,is_read_7=True)
            case b'8':
                return DECRC(is_read_x1B=True,is_read_8=True)
            case b'%':
                a = Character_set_selection_sequence(is_read_x1B=True,is_read_key1=True)
                a.decode(byte_io)
                return a
            case b'(':
                a = G0_character_set(is_read_x1B=True,is_read_key1=True)
                a.decode(byte_io)
                return a
            case b')':
                a = G1_character_set(is_read_x1B=True,is_read_key1=True)
                a.decode(byte_io)
                return a
            case b'>':
                return DECPNM(is_read_x1B=True,is_read_key1=True)
            case b'=':
                return DECPAM(is_read_x1B=True,is_read_key1=True)
            case b']':
                return OSC(is_read_x1B=True,is_read_key1=True)
            case b'[':
                a = csi.CSI(is_read_x1B=True,is_read_key1=True)
                a.decode(byte_io)
                return a
class IND:
    "换行."
    def __init__(self,is_read_x1B=False,is_read_d=False):
        self.is_read_x1B = is_read_x1B
        self.is_read_d = is_read_d
    def decode(self,byte_io:io.BytesIO):
        if self.is_read_x1B==False:
            if byte_io.read(1)!=b'\x1B':
                raise Exception("not x1B")
            
        if self.is_read_d==False:
            if byte_io.read(1)!=b'D':
                raise Exception("not D")
        return
    def encode(self)->bytes:
        return b'\x1BD'
class NEL:
    "新的一行."
    def __init__(self,is_read_x1B=False,is_read_e=False):
        self.is_read_x1B = is_read_x1B
        self.is_read_e = is_read_e
        
    def decode(self,byte_io:io.BytesIO):
        if self.is_read_x1B==False:
            if byte_io.read(1)!=b'\x1B':
                raise Exception("not x1B")
            
        if self.is_read_e==False:
            if byte_io.read(1)!=b'E':
                raise Exception("not E")
    def encode(self)->bytes:
        return b'\x1BE'   
class HTS:
    "设置当前列为制表位."
    def __init__(self,is_read_x1B=False,is_read_H=False):
        self.is_read_x1B = is_read_x1B
        self.is_read_H = is_read_H
        
    def decode(self,byte_io:io.BytesIO):
        if self.is_read_x1B==False:
            if byte_io.read(1)!=b'\x1B':
                raise Exception("not x1B")
            
        if self.is_read_H==False:
            if byte_io.read(1)!=b'H':
                raise Exception("not H")
            
    def encode(self)->bytes:
        return b'\x1BH' 
class RI:
    "屏幕光标向上移动一行."
    def __init__(self,is_read_x1B=False,is_read_M=False):
        self.is_read_x1B = is_read_x1B
        self.is_read_M = is_read_M
        
    def decode(self,byte_io:io.BytesIO):
        if self.is_read_x1B==False:
            if byte_io.read(1)!=b'\x1B':
                raise Exception("not x1B")
            
        if self.is_read_M==False:
            if byte_io.read(1)!=b'M':
                raise Exception("not M")
            
    def encode(self)->bytes:
        return b'\x1BM'
class DECID:
    "DEC 私有定义.内核将其解释为VT102字符,返回字符ESC [ ? 6 c."
    # windows终端里结果是[?1;0c,奇怪啊,这还会影响结束后的操作？
    def __init__(self,is_read_x1B=False,is_read_Z=False):
        self.is_read_x1B = is_read_x1B
        self.is_read_Z = is_read_Z
        
    def decode(self,byte_io:io.BytesIO):
        if self.is_read_x1B==False:
            if byte_io.read(1)!=b'\x1B':
                raise Exception("not x1B")
            
        if self.is_read_Z==False:
            if byte_io.read(1)!=b'Z':
                raise Exception("not Z")
            
            
    def encode(self)->bytes:
        return b'\x1BZ' 
class DECSC:
    "存储当前状态(光标坐标,属性,字符集)."
    def __init__(self,is_read_x1B=False,is_read_7=False):
        self.is_read_x1B = is_read_x1B
        self.is_read_7 = is_read_7
        
    def decode(self,byte_io:io.BytesIO):
        if self.is_read_x1B==False:
            if byte_io.read(1)!=b'\x1B':
                raise Exception("not x1B")
            
        if self.is_read_7==False:
            if byte_io.read(1)!=b'7':
                raise Exception("not 7")
            
    def encode(self)->bytes:
        return b'\x1B7'
class DECRC:
    "恢复之前存储的状态."
    def __init__(self,is_read_x1B=False,is_read_8=False):
        self.is_read_x1B = is_read_x1B
        self.is_read_8 = is_read_8
        
    def decode(self,byte_io:io.BytesIO):
        if self.is_read_x1B==False:
            if byte_io.read(1)!=b'\x1B':
                raise Exception("not x1B")
            
        if self.is_read_8==False:
            if byte_io.read(1)!=b'8':
                raise Exception("not 8")
            
    def encode(self)->bytes:
        return b'\x1B8'
class Character_set_selection_sequence:
    "字符集选择序列"
    def __init__(self,is_read_x1B=False,is_read_key1=False,is_utf_8=None):
        self.is_read_x1B = is_read_x1B
        self.is_read_key1 = is_read_key1
        self.is_utf_8=is_utf_8
        
    def decode(self,byte_io:io.BytesIO):
        # ESC % @
        if self.is_read_x1B==False:
            if byte_io.read(1)!=b'\x1B':
                raise Exception("not x1B")
            
        if self.is_read_key1==False:
            if byte_io.read(1)!=b'%':
                raise Exception("not %")
        if self.is_utf_8==None:
            byte = byte_io.read(1)
            if byte==b'@':
                self.is_utf_8=False
            elif byte==b'G':
                self.is_utf_8=True
            elif byte==b'8':
                self.is_utf_8=True
            else:
                raise Exception("not @ or G or 8")
    def encode(self)->bytes:
        if self.is_utf_8==None:
            raise Exception("is_utf_8 is None")
        if self.is_utf_8==False:
            return b'\x1B%@'
        else:
            return b'\x1B%G'       
class DECALN:
    "DEC 屏幕校准测试 - 以E's填充屏幕."
    def __init__(self,is_read_x1B=False,is_read_key1=False,is_read_8=False):
        self.is_read_x1B = is_read_x1B
        self.is_read_key1 = is_read_key1
        self.is_read_8 = is_read_8
        
    def decode(self,byte_io:io.BytesIO):
        if self.is_read_x1B==False:
            if byte_io.read(1)!=b'\x1B':
                raise Exception("not x1B")
            
        if self.is_read_key1==False:
            if byte_io.read(1)!=b'#':
                raise Exception("not #")
            
        if self.is_read_8==False:
            if byte_io.read(1)!=b'8':
                raise Exception("not 8")
            
    def encode(self)->bytes:
        return b'\x1B#8'
class G0_character_set:
    """G0 字符集定义序列
    定义如下：
        ESC(B	   选择默认字符集(ISO 8859-1 mapping)
        ESC(0	   选择 vt100 图形映射
        ESC(U	   选择空映射 - 直接访问字符ROM
        ESC(K	   选择用户映射 - 由程序mapscrn(8)
    对应的 is_read_0为0,1,2,3,没有读取则为None"""
    def __init__(self,is_read_x1B=False,is_read_key1=False,is_read_0=None):
        self.is_read_x1B = is_read_x1B
        self.is_read_key1 = is_read_key1
        self.is_read_0 = is_read_0
        
    def decode(self,byte_io:io.BytesIO):
        if self.is_read_x1B==False:
            if byte_io.read(1)!=b'\x1B':
                raise Exception("not x1B")
            
        if self.is_read_key1==False:
            if byte_io.read(1)!=b'(':
                raise Exception("not (")
                    
                    
        if self.is_read_0==None:
            byte = byte_io.read(1)
            if byte==b'B':
                self.is_read_0=0
            elif byte==b'0':
                self.is_read_0=1
            elif byte==b'U':
                self.is_read_0=2
            elif byte==b'K':
                self.is_read_0=3
            else:
                raise Exception("not B or 0 or U or K")
            
    def encode(self)->bytes:
        if self.is_read_0==None:
            raise Exception("is_read_0 is None")
        if self.is_read_0==0:
            return b'\x1B(B'
                
        elif self.is_read_0==1:
            return b'\x1B(0'

            
        elif self.is_read_0==2:
            return b'\x1B(U'
            
        elif self.is_read_0==3:
            return b'\x1B(K'
            
        else:
            raise Exception("not B or 0 or U or K(0,1,2,3)")
class G1_character_set:
    """G1 字符集定义序列
    定义如下：
        ESC(B	   选择默认字符集(ISO 8859-1 mapping)
        ESC(0	   选择 vt100 图形映射
        ESC(U	   选择空映射 - 直接访问字符ROM
        ESC(K	   选择用户映射 - 由程序mapscrn(8)
    对应的 is_read_0为0,1,2,3,没有读取则为None"""
    def __init__(self,is_read_x1B=False,is_read_key1=False,is_read_0=None):
        self.is_read_x1B = is_read_x1B
        self.is_read_key1 = is_read_key1
        self.is_read_0 = is_read_0
        
    def decode(self,byte_io:io.BytesIO):
        if self.is_read_x1B==False:
            if byte_io.read(1)!=b'\x1B':
                raise Exception("not x1B")
            
        if self.is_read_key1==False:
            if byte_io.read(1)!=b')':
                raise Exception("not )")
                    
                    
        if self.is_read_0==None:
            byte = byte_io.read(1)
            if byte==b'B':
                self.is_read_0=0
            elif byte==b'0':
                self.is_read_0=1
            elif byte==b'U':
                self.is_read_0=2
            elif byte==b'K':
                self.is_read_0=3
            else:
                raise Exception("not B or 0 or U or K")
            
    def encode(self)->bytes:
        if self.is_read_0==None:
            raise Exception("is_read_0 is None")
        if self.is_read_0==0:
            return b'\x1B)B'
                
        elif self.is_read_0==1:
            return b'\x1B)0'

            
        elif self.is_read_0==2:
            return b'\x1B)U'
            
        elif self.is_read_0==3:
            return b'\x1B)K'
            
        else:
            raise Exception("not B or 0 or U or K(0,1,2,3)")
class DECPNM:
    """设置数字小键盘模式"""
    def __init__(self,is_read_x1B=False,is_read_key1=False):
        self.is_read_x1B = is_read_x1B
        self.is_read_key1 = is_read_key1
        
    def decode(self,byte_io:io.BytesIO):
        if self.is_read_x1B==False:
            if byte_io.read(1)!=b'\x1B':
                raise Exception("not x1B")
            
        if self.is_read_key1==False:
            if byte_io.read(1)!=b'>':
                raise Exception("not >")
            
    def encode(self)->bytes:
        return b'\x1B>'
class DECPAM:
    """设置程序键盘模式"""
    def __init__(self,is_read_x1B=False,is_read_key1=False):
        self.is_read_x1B = is_read_x1B
        self.is_read_key1 = is_read_key1
        
    def decode(self,byte_io:io.BytesIO):
        if self.is_read_x1B==False:
            if byte_io.read(1)!=b'\x1B':
                raise Exception("not x1B")
            
        if self.is_read_key1==False:
            if byte_io.read(1)!=b'=':
                raise Exception("not =")
            
    def encode(self)->bytes:
        return b'\x1B='
    
class OSC:
    """(是perating system command的缩写)"""
    def __init__(self,is_read_x1B=False,is_read_key1=None,mode=None,color=b""):
        self.is_read_x1B = is_read_x1B
        self.is_read_key1 = is_read_key1
        self.mode = mode
        self.color = color
        
    def decode(self,byte_io:io.BytesIO):
        if self.is_read_x1B==False:
            if byte_io.read(1)!=b'\x1B':
                raise Exception("not x1B")
            
        if self.is_read_key1==None:
            if byte_io.read(1)!=b']':
                raise Exception("not x1B")
        if self.mode==None:
            byte = byte_io.read(1)
            match byte:
                case b'P':
                    self.mode=b"P"
                    self.color=byte_io.read(7)
                case b'R':
                    self.mode=b"R"
                case _:
                    raise Exception("not P or R")
    def encode(self)->bytes:
        if self.mode==None:
            raise Exception("mode is None")
        if self.mode==b"P":
            return b'\x1B]P'+self.color
        elif self.mode==b"R":
            return b'\x1BR'