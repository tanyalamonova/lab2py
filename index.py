import regex


def ShowIPlist(subnetworks):
	for snw, IPlist in subnetworks.items():
		print(snw + ' subnetwork:')
		for ip, count in IPlist.items():
			print(ip)
		print()

def ParseFile(filename):
	global subnetworks
	file = open(filename, 'r')
	for line in file.readlines():
		IPlist = list(regex.findall(r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}', line))
		for ip in IPlist:
			snw = '.'.join(ip.split('.')[:-1])
			if snw not in subnetworks.keys():
				subnetworks[snw] = {}
				subnetworks[snw][ip] = 1
			else:
				if ip in subnetworks[snw].keys():
					subnetworks[snw][ip] += 1
				else:
					subnetworks[snw][ip] = 1

subnetworks = {}
file = 'access.log'
ParseFile(file)
ShowIPlist(subnetworks)

