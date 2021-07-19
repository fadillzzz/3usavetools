from os import path, access, W_OK
from converter.converter_3ds import Converter3DS
from converter.converter_wiiu import ConverterWiiU
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFormLayout, QFileDialog, QTextEdit, QMessageBox

class App():
    def start(self):
        app = QApplication([])
        app.setStyle('Fusion')
        self.app = app

        self.window = QWidget()
        self.window.setWindowTitle('MH3U Save Converter')
        layout = QFormLayout()

        loadSrcButton = QPushButton('Load save file')
        loadSrcButton.clicked.connect(self.loadSrc)
        self.srcPath = QTextEdit(self.window)
        self.srcPath.setFixedHeight(24)

        setOutputButton = QPushButton('Set output file')
        setOutputButton.clicked.connect(self.setDst)
        self.dstPath = QTextEdit(self.window)
        self.dstPath.setFixedHeight(24)

        convertButton = QPushButton('Convert')
        convertButton.clicked.connect(self.convert)

        layout.addRow(loadSrcButton, self.srcPath)
        layout.addRow(setOutputButton, self.dstPath)
        layout.addRow(convertButton)

        self.window.setLayout(layout)
        self.window.show()
        app.exec()

    def loadSrc(self):
        filePath = QFileDialog.getOpenFileName(self.window, 'Load save file')
        if filePath:
            self.srcPath.setText(filePath[0])

    def setDst(self):
        filePath = QFileDialog.getSaveFileName(self.window, 'Set output file')
        if filePath:
            self.dstPath.setText(filePath[0])

    def convert(self):
        srcPath = self.srcPath.toPlainText()
        dstPath = self.dstPath.toPlainText()

        if not path.exists(srcPath):
            return

        inputSize = path.getsize(srcPath)

        self.error = None
        self.success = None

        if inputSize == 0x8A00:
            converter = ConverterWiiU(srcPath)
        elif inputSize == 0x8A24:
            converter = Converter3DS(srcPath)
        else:
            self.error = QMessageBox()
            self.error.setText('Invalid save file')

        if not access(path.dirname(dstPath), W_OK):
            self.error = QMessageBox()
            self.error.setText('Output path not writable')

        if self.error:
            self.error.show()
        else:
            converter.convert(dstPath)
            self.success = QMessageBox()
            self.success.setText('File converted successfully')

        if self.success:
            self.success.show()


if __name__ == '__main__':
    App().start()
