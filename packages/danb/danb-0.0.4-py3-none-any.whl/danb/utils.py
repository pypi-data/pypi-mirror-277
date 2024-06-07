import sys

def check_memory():
	def sizeof_fmt(num, suffix='B'):
		for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
			if abs(num) < 1024.0:
				return "%3.1f %s%s" % (num, unit, suffix)
			num /= 1024.0
		return "%.1f %s%s" % (num, 'Yi', suffix)
		
	for name, size in sorted(((name, sys.getsizeof(value)) for name, value in list(
                         globals().items())), key= lambda x: -x[1])[:10]:
		print("{:>30}: {:>8}".format(name, sizeof_fmt(size)))