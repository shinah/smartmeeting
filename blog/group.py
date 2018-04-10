import random

class Random_make:
	def random_url(self):
		ran_list = '01234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		ran_str ="".join([random.choice(ran_list) for i in range(12)])
		return ran_str
