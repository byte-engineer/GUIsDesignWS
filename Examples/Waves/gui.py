# test/test0.py

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
import Waves # test3
import sys
import numpy as np
import os
import time

os.system('cls')

class Main(QMainWindow):

    def __init__(self):
        super().__init__()

        # attributes
        self.combo_generate_firsthilght = False
        self.combo_modulation_firsthilght = False
        self.sampleRate = 44100
        self.duration = 1
        self.pop_spin_box_value = 44100
        self.amplitude = 1
        self.saveName = 'sound'
        gene = Waves.generate(self.sampleRate)
        self.waveform = gene.sin(1, 1000)

        self.UI()


    def UI(self):

        self.init_window()

        self.tabs = QTabWidget()
        self.tabs.setMovable(True)

        generate_tab = self.generateTab()                  # This is the first tab for Waves.generate() class
        self.tabs.addTab(generate_tab, 'Generate')

        modulation_tab = self.modulationTab()
        self.tabs.addTab(modulation_tab, 'Modulation')


        layout = QVBoxLayout()
        layout.addWidget(self.tabs)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


    def generateTab(self):

        self.generateWidget = QWidget()
        self.generateWidget.setObjectName('GenerateTab')
        tab_layout = QGridLayout()

        # Compo box to get the type of wave form.
        combo_label = QLabel('Choose WaveForm:  ')
        self.combo_generate = QComboBox()
        self.combo_generate.addItem('-- Choose --')
        self.combo_generate.addItems(['Sin', 'Square', 'Trianglar'])
        self.combo_generate.highlighted.connect(self.combo_generate_highlighted)

        freq_label = QLabel('Freqency:  ')
        self.freq_generate_spin = QSpinBox()
        self.freq_generate_spin.setRange(1, 1000000)
        self.freq_generate_spin.setValue(5000)
        self.freq_generate_spin.setSuffix(' Hz')

        # Buttons
        generate_btn = QPushButton('Generate')
        generate_btn.clicked.connect(self.generate)

        save_btn = QPushButton('Save')
        save_btn.clicked.connect(self.save)

        freqs_btn = QPushButton('Frequencies')
        freqs_btn.clicked.connect(self.freq)

        self.preview_btn = QPushButton('Preview')
        self.preview_btn.clicked.connect(self.preview)

        save_freq_layout = QHBoxLayout()
        save_freq_layout.addWidget(save_btn)
        save_freq_layout.addWidget(freqs_btn)

        generate_preview_layout = QHBoxLayout()
        generate_preview_layout.addWidget(generate_btn, 2)
        generate_preview_layout.addWidget(self.preview_btn, 1)

        # Grid layout stuff
        tab_layout.addWidget(combo_label, 0, 0)
        tab_layout.addWidget(self.combo_generate, 0, 1)
        tab_layout.addWidget(self.combo_generate, 0, 1)

        tab_layout.addWidget(freq_label, 1, 0)
        tab_layout.addWidget(self.freq_generate_spin, 1, 1)

        tab_layout.addLayout(generate_preview_layout, 3, 0, 1, 0)
        tab_layout.addLayout(save_freq_layout, 4, 0, 1, 0)


        self.generateWidget.setLayout(tab_layout)
        return self.generateWidget


    def modulationTab(self):
        self.modulationWidget = QWidget()
        self.modulationWidget.setObjectName('ModulationTab')
        tab_layout = QGridLayout()

        combo_label = QLabel('Choose Modulation:  ')
        self.combo_modulation = QComboBox()
        self.combo_modulation.addItem('-- Choose --')
        self.combo_modulation.addItems(['Freqeuncy', 'Amplitude'])
        self.combo_modulation.highlighted.connect(self.combo_modulation_highlighted)
        self.combo_modulation.currentTextChanged.connect(self.FM_modulation_change_double_span_text_changed)

        main_freq_label = QLabel('Main Frequency:  ')
        self.main_freq_modulation_spin = QSpinBox()
        self.main_freq_modulation_spin.setRange(1, 1000000)
        self.main_freq_modulation_spin.setValue(5000)
        self.main_freq_modulation_spin.setSuffix(' Hz')

        modulation_freq_modulation_label = QLabel('Modulation Frequency  ')
        self.modulation_freq_modulation_double_spin = QDoubleSpinBox()
        self.modulation_freq_modulation_double_spin.setRange(0.1, 1000000)
        self.modulation_freq_modulation_double_spin.setValue(5)
        self.modulation_freq_modulation_double_spin.setSuffix(' Hz')

        self.FM_change_lable = QLabel('Change Rate:  ')
        self.FM_change_double_span = QDoubleSpinBox()
        self.FM_change_double_span.setRange(0, 100)
        self.FM_change_double_span.setValue(1)
        self.FM_change_lable.setVisible(True)
        self.FM_change_double_span.setVisible(True)

        self.modulation_preview_btn = QPushButton('Preview')
        self.modulation_preview_btn.clicked.connect(self.preview)

        self.modulation_generate_btn = QPushButton('Generate')

        btns1_layout = QHBoxLayout()
        btns1_layout.addWidget(self.modulation_generate_btn, 2)
        btns1_layout.addWidget(self.modulation_preview_btn, 1)

        tab_layout.addWidget(combo_label, 0, 0)
        tab_layout.addWidget(self.combo_modulation, 0, 1)
        tab_layout.addWidget(main_freq_label, 1, 0)
        tab_layout.addWidget(self.main_freq_modulation_spin, 1, 1)
        tab_layout.addWidget(modulation_freq_modulation_label, 2, 0)
        tab_layout.addWidget(self.modulation_freq_modulation_double_spin, 2, 1)
        tab_layout.addWidget(self.FM_change_lable, 3, 0)
        tab_layout.addWidget(self.FM_change_double_span, 3, 1)
        tab_layout.addLayout(btns1_layout, 4, 0, 1, 0)

        self.modulationWidget.setLayout(tab_layout)
        return self.modulationWidget


    def Menus(self):
        file_menu = self.bar.addMenu('File')
        edit_menu = self.bar.addMenu('Edit')

        sample_act = QAction('Sampling', self)
        edit_menu.addAction(sample_act)
        sample_act.triggered.connect(self.setSampleRate)

        amplitude_act = QAction('Amplitude', self)
        edit_menu.addAction(amplitude_act)
        amplitude_act.triggered.connect(self.setAmplitude) # Amplitude

        duration_act = QAction('Duration', self)
        edit_menu.addAction(duration_act)
        duration_act.triggered.connect(self.setDuration) # Duration

        save_act = QAction('Save', self)
        file_menu.addAction(save_act)
        duration_act.triggered.connect(self.save)

        freq_act = QAction('Freqeuncies', self)
        file_menu.addAction(freq_act)
        ana = Waves.analysis(self.sampleRate)
        freq_act.triggered.connect(lambda : ana.show_fft(self.waveform))


    def init_window(self):
        self.setWindowTitle('Waves')
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.resize(350, 250)

        script_dir = os.path.dirname(os.path.abspath(__file__))

        with open(os.path.join(script_dir, 'styles.qss'), 'r') as style:
            self.setStyleSheet(style.read())

        self.bar = self.menuBar()
        self.Menus()


    def combo_generate_highlighted(self, index):
        if not self.combo_generate_firsthilght:
            self.combo_generate_firsthilght = True
            self.combo_generate.removeItem(0)

    def combo_modulation_highlighted(self, index):
        if not self.combo_modulation_firsthilght:
            self.combo_modulation_firsthilght = True
            self.combo_modulation.removeItem(0)


    def generate(self):
            
        gnrt = Waves.generate(self.sampleRate)
        

        if self.tabs.currentWidget().objectName() == 'GenerateTab':

            match self.combo_generate.currentText().lower():

                case 'sin':
                    self.waveform = gnrt.sin(self.duration, self.freq_generate_spin.value(), scale= self.amplitude)
                    return False

                case 'square':
                    self.waveform = gnrt.square(self.duration, self.freq_generate_spin.value(), scale= self.amplitude)
                    return False

                case 'trianglar':
                    self.waveform = gnrt.triangle(self.duration, self.freq_generate_spin.value(), scale= self.amplitude)
                    return False

                case _ :
                    QMessageBox.information(self, 'Error', 'Choose waveform first')
                    return True

        elif self.tabs.currentWidget().objectName() == 'ModulationTab':

            match self.combo_modulation.currentText():

                case 'Freqeuncy':
                    self.waveform = gnrt.sin_FM(self.duration, self.main_freq_modulation_spin.value(), self.modulation_freq_modulation_double_spin.value(), self.amplitude, self.FM_change_double_span.value())
                    return False

                case 'Amplitude':
                    self.waveform = gnrt.sin_AM(self.duration, self.main_freq_modulation_spin.value(), self.modulation_freq_modulation_double_spin.value(), self.amplitude)
                    return False
                
                case _ :
                    QMessageBox.information(self, 'Error', 'Choose waveform first')
                    return True

    def preview(self):

        error = self.generate()

        if not error:
            hlp = Waves.helpers(self.sampleRate)
            hlp.play(self.waveform)
            time.sleep(self.duration)


    def save(self):
        path = QFileDialog.getExistingDirectory()
        if not len(self.waveform):
            self.generate()

        if path:
            hlps = Waves.helpers(self.sampleRate)
            hlps.save(path+'/sound.wav', self.waveform)


    def freq(self):
        if not len(self.waveform):
            self.generate()

        ana = Waves.analysis(self.sampleRate)
        ana.show_fft(self.waveform)


    def setSampleRate(self): # setSamleRate
        dil = setValue()
        dil.spin_button()
        dil.resize(150, 80)
        dil.show()
        dil.spin.setRange(1, 400000)
        dil.spin.setSingleStep(1000)
        dil.spin.setValue(self.sampleRate)
        if dil.exec() == QDialog.DialogCode.Accepted:
            self.sampleRate = int(dil.spin.value())
            print(self.sampleRate)


    def setAmplitude(self):
        dilog = setValue()
        dilog.slider_button()
        dilog.show()
        dilog.slider.setValue(self.amplitude * 10)

        if dilog.exec_() == QDialog.Accepted:
            self.amplitude = dilog.slider.value() / 10
            print(self.amplitude)


    def setDuration(self):
        self.dil = setValue()
        self.dil.slider_button()
        self.dil.show()
        self.dil.slider.setValue(self.duration)

        if self.dil.exec() == QDialog.DialogCode.Accepted: # 
            self.amplitude = self.dil.slider.value()
            print(self.duration)


    def FM_modulation_change_double_span_text_changed(self):
        
        match self.combo_modulation.currentText():

            case 'Freqeuncy':
                self.FM_change_lable.setVisible(True)
                self.FM_change_double_span.setVisible(True)

            case _:
                self.FM_change_lable.setVisible(False)
                self.FM_change_double_span.setVisible(False)

        self.repaint()


    def keyPressEvent(self, event:QtGui.QKeyEvent):
        
        if self.tabs.currentWidget().objectName() == 'GenerateTab':

            if event.key() == QtCore.Qt.Key.Key_P:
                print('Key "P" pressed')
                self.preview()


class setValue(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('set Value')
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)


    def spin_button(self):

        script_dir = os.path.dirname(os.path.abspath(__file__))

        with open(os.path.join(script_dir, 'styles.qss')) as styles:
            self.setStyleSheet(styles.read())

        layout = QVBoxLayout()
        self.spin = QSpinBox()
        ok_btn = QPushButton('Ok')
        ok_btn.clicked.connect(self.accept)


        btns_layout = QHBoxLayout()
        btns_layout.addWidget(ok_btn)

        layout.addWidget(self.spin)
        layout.addLayout(btns_layout)

        self.setLayout(layout)


    def slider_button(self):
        layout = QVBoxLayout()
        self.slider = QSlider()
        self.slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider.setRange(0, 10)
        self.slider.setSingleStep(1)
        ok_btn = QPushButton('Ok')
        ok_btn.clicked.connect(self.accept)

        btns_layout = QHBoxLayout()
        btns_layout.addWidget(ok_btn)

        layout.addWidget(self.slider)
        layout.addLayout(btns_layout)

        self.setLayout(layout)


def window():
    app = QApplication(sys.argv)
    win = Main()
    win.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    window()
