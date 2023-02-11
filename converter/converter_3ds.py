from .base_converter import BaseConverter

class Converter3DS(BaseConverter):
    _sourceSignatureLength = 0x28
    _targetSignature = [0x2C, 0x00, 0x00, 0x00]

    def convertMonsterDiscState(self, srcBytes, state):
        newState = [0, 0]

        discovered = state[0] & 0x80
        silver = state[0] & 0x20
        gold = state[0] & 0x40
        mini = state[0] & 0x8

        if discovered:
            newState[0] += 1

        if silver:
            newState[0] += 2

        if gold:
            newState[0] += 4

        if mini:
            newState[0] += 8

        return newState