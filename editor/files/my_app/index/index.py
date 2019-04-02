module_name = "Index"

class Index(object):
	"""docstring for Index"""
	def __init__(self, indexid):
		super(Index, self).__init__()
		self.indexid = indexid
		
	def getIndexId(self):
		return self.indexid

	def setIndexId(self,indexid):
		self.indexid = indexid



