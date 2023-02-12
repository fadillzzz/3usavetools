from .save_indices import saveFileSwap, monsterDiscoveryState, arenaRecord

class BaseConverter:
    def __init__(self, file):
        self.file = file

    def getSrcBytes(self):
        src = open(self.file, 'rb')
        src.seek(self._sourceSignatureLength)
        srcBytes = src.read()
        src.close()

        return srcBytes

    def convert(self, out):
        srcBytes = self.getSrcBytes()

        dstBytes = self.execConvert(srcBytes)

        self.writeDstBytes(out, dstBytes)

    def execConvert(self, srcBytes):
        dstBytes = self._targetSignature[:]
        dstBytes += list(srcBytes)

        targetSignatureLength = len(self._targetSignature)

        for i in saveFileSwap:
            rev = list(srcBytes[i[0]:i[1]])
            rev.reverse()
            for j, b in enumerate(rev):
                dstBytes[targetSignatureLength + i[0] + j] = b

        for i in monsterDiscoveryState:
            state = list(srcBytes[i:i + 2])
            newState = self.convertMonsterDiscState(srcBytes, state)
            dstBytes[targetSignatureLength + i] = newState[0]
            dstBytes[targetSignatureLength + i + 1] = newState[1]

        for i in arenaRecord:
            data = int.from_bytes(srcBytes[i:i + 4], "big")
            firstHalf = data >> 16
            secondHalf = data & 0xFFFF
            (convertedFirstHalf, convertedSecondHalf) = self.convertArenaRecord(firstHalf, secondHalf)
            targetI = targetSignatureLength + i
            dstBytes[targetI:targetI + 2] = int.to_bytes(convertedFirstHalf, 2, "big")
            dstBytes[targetI + 2:targetI + 4] = int.to_bytes(convertedSecondHalf, 2, "big")

        return dstBytes

    def convertMonsterDiscState(self, srcBytes, state):
        pass

    def convertArenaRecord(self, firstHalf, secondHalf):
        pass

    def writeDstBytes(self, out, dstBytes):
        dst = open(out, 'wb')
        dst.write(bytes(dstBytes))
        dst.close()
