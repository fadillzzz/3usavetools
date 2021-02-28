from .save_indices import saveFileSwap

class BaseConverter:
    def __init__(self, file):
        self.file = file

    def convert(self, out):
        src = open(self.file, 'rb')
        src.seek(self._sourceSignatureLength)
        srcBytes = src.read()
        src.close()

        dstBytes = self._targetSignature[:]
        dstBytes += list(srcBytes)
        targetSignatureLength = len(self._targetSignature)

        for i in saveFileSwap:
            rev = list(srcBytes[i[0]:i[1]])
            rev.reverse()
            for j, b in enumerate(rev):
                dstBytes[targetSignatureLength + i[0] + j] = b

        dst = open(out, 'wb')
        dst.write(bytes(dstBytes))
        dst.close()
