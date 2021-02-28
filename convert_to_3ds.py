import sys
from converter.converter_3ds import Converter3DS

if __name__ == '__main__':
    converter = Converter3DS(sys.argv[1])
    converter.convert(sys.argv[2])
