""" Keysight 8360L Series Swept CW Generator

Manual: http://www.doe.carleton.ca/~nagui/labequip/synth/manuals/e4400324.pdf
"""

from heimdallr.base import *
from heimdallr.instrument_control.categories.rf_signal_generator_ctg import *

class AgilentE4400(RFSignalGeneratorCtg):

	def __init__(self, address:str, log:LogPile):
		super().__init__(address, log, expected_idn='Hewlett-Packard, ESG-4000B')
	
	def set_power(self, p_dBm:float):
		self.write(f":POW:LEV:IMM:AMPL {p_dBm} dBm")
	def get_power(self):
		val = self.query(f":POW:LEV:IMM:AMPL?")
		return float(val)
	
	def set_freq(self, f_Hz:float):
		self.write(f":FREQ:CW {f_Hz} Hz")
	def get_freq(self):
		return float(self.query(f":FREQ:CW?"))
	
	def set_enable_rf(self, enable:bool):
		self.write(f":OUTP:STAT {bool_to_str01(enable)}")
	def get_enable_rf(self):
		return str_to_bool(self.query(f":OUTP:STAT?"))