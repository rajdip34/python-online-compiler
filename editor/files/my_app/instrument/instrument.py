module_name = "Instrument"

class Instrument(object):
	"""docstring for Index"""
	def __init__(self, instrumentId):
		super(Instrument, self).__init__()
		self.instrumentId = instrumentId
		
	def getInstrumentId(self):
		return self.instrumentId

	def setInstrumentId(self,indexid):
		self.instrumentId = instrumentId

	def getPrice(self):
		if self.instrumentId > 100:
			return 100
		else:
			return 200




