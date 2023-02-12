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

    def convertArenaRecord(self, firstHalf, secondHalf):
        firstDropped = firstHalf & 0x1
        secondDropped = secondHalf & 0x1

        q1 = firstHalf >> 8
        q2 = firstHalf << 8
        convertedFirst = q2 | q1
        bitWrap = convertedFirst & 0x1
        convertedFirst = convertedFirst >> 1
        convertedFirst = convertedFirst & ~(1 << (8 - 1))
        convertedFirst = (convertedFirst | (0x8000 * bitWrap)) & 0xFFFF

        q1 = secondHalf >> 8
        q2 = secondHalf << 8
        convertedSecond = q2 | q1
        bitWrap = convertedSecond & 0x1
        convertedSecond = convertedSecond >> 1
        convertedSecond = convertedSecond & ~(1 << (8 - 1))
        convertedSecond = (convertedSecond | (0x8000 * bitWrap)) & 0xFFFF

        convertedFirst = convertedFirst | (0x80 * secondDropped)
        convertedSecond = convertedSecond | (0x80 * firstDropped)

        return (convertedFirst, convertedSecond)