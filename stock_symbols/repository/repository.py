from abc import ABC, abstractmethod


class BaseRepo(ABC):
	
	@abstractmethod
	def get_all_data(self):
		pass
