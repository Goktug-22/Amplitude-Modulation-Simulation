#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: v3.8.2.0-57-gd71cd177

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget

from gnuradio import qtgui

class am_transmitter(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "am_transmitter")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 50000
        self.modulator_freq = modulator_freq = 500
        self.carrier_freq = carrier_freq = 4500
        self.Modulator_Amplitude = Modulator_Amplitude = 0.5
        self.Carrier_Amplitude = Carrier_Amplitude = 0.5

        ##################################################
        # Blocks
        ##################################################
        self._modulator_freq_range = Range(150, 750, 10, 500, 200)
        self._modulator_freq_win = RangeWidget(self._modulator_freq_range, self.set_modulator_freq, 'modulator_freq', "counter_slider", float)
        self.top_grid_layout.addWidget(self._modulator_freq_win)
        self._carrier_freq_range = Range(1500, 10000, 100, 4500, 200)
        self._carrier_freq_win = RangeWidget(self._carrier_freq_range, self.set_carrier_freq, 'carrier_freq', "counter_slider", float)
        self.top_grid_layout.addWidget(self._carrier_freq_win)
        self._Modulator_Amplitude_range = Range(0, 1.5, 0.01, 0.5, 200)
        self._Modulator_Amplitude_win = RangeWidget(self._Modulator_Amplitude_range, self.set_Modulator_Amplitude, 'Modulator_Amplitude', "counter_slider", float)
        self.top_grid_layout.addWidget(self._Modulator_Amplitude_win)
        self._Carrier_Amplitude_range = Range(0, 1.5, 0.01, 0.5, 200)
        self._Carrier_Amplitude_win = RangeWidget(self._Carrier_Amplitude_range, self.set_Carrier_Amplitude, 'Carrier_Amplitude', "counter_slider", float)
        self.top_grid_layout.addWidget(self._Carrier_Amplitude_win)
        self.qtgui_sink_x_0_0_0_0 = qtgui.sink_c(
            1024, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            False, #plotwaterfall
            True, #plottime
            False #plotconst
        )
        self.qtgui_sink_x_0_0_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0_0_0.enable_rf_freq(False)

        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_0_0_0_win)
        self.qtgui_sink_x_0_0_0 = qtgui.sink_f(
            1024, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            False, #plotwaterfall
            True, #plottime
            False #plotconst
        )
        self.qtgui_sink_x_0_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0_0.pyqwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0_0.enable_rf_freq(False)

        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_0_0_win)
        self.low_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                2,
                samp_rate,
                600,
                1,
                firdes.WIN_HAMMING,
                6.76))
        self.blocks_throttle_1 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_add_const_vxx_0_0 = blocks.add_const_ff(-1)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff(1)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, carrier_freq, Carrier_Amplitude, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, modulator_freq, Modulator_Amplitude, 0, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.qtgui_sink_x_0_0_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_throttle_1, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_throttle_1, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_throttle_1, 0), (self.qtgui_sink_x_0_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_add_const_vxx_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "am_transmitter")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_1.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(2, self.samp_rate, 600, 1, firdes.WIN_HAMMING, 6.76))
        self.qtgui_sink_x_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_sink_x_0_0_0_0.set_frequency_range(0, self.samp_rate)

    def get_modulator_freq(self):
        return self.modulator_freq

    def set_modulator_freq(self, modulator_freq):
        self.modulator_freq = modulator_freq
        self.analog_sig_source_x_0.set_frequency(self.modulator_freq)

    def get_carrier_freq(self):
        return self.carrier_freq

    def set_carrier_freq(self, carrier_freq):
        self.carrier_freq = carrier_freq
        self.analog_sig_source_x_1.set_frequency(self.carrier_freq)

    def get_Modulator_Amplitude(self):
        return self.Modulator_Amplitude

    def set_Modulator_Amplitude(self, Modulator_Amplitude):
        self.Modulator_Amplitude = Modulator_Amplitude
        self.analog_sig_source_x_0.set_amplitude(self.Modulator_Amplitude)

    def get_Carrier_Amplitude(self):
        return self.Carrier_Amplitude

    def set_Carrier_Amplitude(self, Carrier_Amplitude):
        self.Carrier_Amplitude = Carrier_Amplitude
        self.analog_sig_source_x_1.set_amplitude(self.Carrier_Amplitude)





def main(top_block_cls=am_transmitter, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
