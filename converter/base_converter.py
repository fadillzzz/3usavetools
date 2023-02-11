from .save_indices import saveFileSwap, monsterDiscoveryState

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

        return dstBytes

    def convertMonsterDiscState(self, srcBytes, state):
        pass

    def writeDstBytes(self, out, dstBytes):
        dst = open(out, 'wb')
        dst.write(bytes(dstBytes))
        dst.close()
