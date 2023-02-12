from .base_converter import BaseConverter

class ConverterWiiU(BaseConverter):
    _sourceSignatureLength = 0x4
    _targetSignature = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x14, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0C, 0x00, 0x00, 0x8A, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x2C]

    def convertMonsterDiscState(self, srcBytes, state):
        newState = [0, 0]

        discovered = state[0] & 1
        silver = state[0] & 2
        gold = state[0] & 4
        mini = state[0] & 8

        if discovered:
            newState[0] += 0x80

        if silver:
            newState[0] += 0x20

        if gold:
            newState[0] += 0x40

        if mini:
            newState[0] += 0x8

        return newState

    def convertArenaRecord(self, firstHalf, secondHalf):
        q1 = firstHalf >> 8
        q2 = firstHalf << 8
        convertedFirst = q2 | q1
        firstDropped = convertedFirst & 0x8000
        convertedFirst = (convertedFirst << 1) & 0xFFFF

        q1 = secondHalf >> 8
        q2 = secondHalf << 8
        convertedSecond = q2 | q1
        secondDropped = convertedSecond & 0x8000
        convertedSecond = (convertedSecond << 1) & 0xFFFF

        convertedFirst = convertedFirst | int(bool(secondDropped))
        convertedSecond = convertedSecond | int(bool(firstDropped))

        return (convertedFirst, convertedSecond)