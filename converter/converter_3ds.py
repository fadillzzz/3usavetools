from .base_converter import BaseConverter

class Converter3DS(BaseConverter):
    _sourceSignatureLength = 0x28
    _targetSignature = [0x2C, 0x00, 0x00, 0x00]
