# Jonathan Rawlinson 2017

import ujson

#ex_dict = {'time': 1787072927.399561, 'id': 101, 'taken': True, 'temp': 19.5} #For testing

## This module takes a dictionary as an input, checks to ensure that all ofthe input parms exist and if so returns the JSON encoded string
def pack(ex_dict):
	if d_check(ex_dict) == True:
		packed = ujson.dumps(ex_dict)
		return packed 
	else:
		return ujson.dumps("invalid input")
	

def d_check(d): ##Check dict format
	if len(d) != 4:
		return False
	
	try: d['time']
	except:
		return False

	try: d['id']
	except:
		return False

	try: d['taken']
	except:
		return False

	try: d['temp']
	except:
		return False

	return True


#print pack(ex_dict)
		
