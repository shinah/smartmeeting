import random

def random_url():
	ran_list = '01234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	ran_str =''
	return "".join([random.choice(ran_list) for i in range(12)])
