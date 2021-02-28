import sys
from converter.converter_wiiu import ConverterWiiU

if __name__ == '__main__':
    converter = ConverterWiiU(sys.argv[1])
    converter.convert(sys.argv[2])
