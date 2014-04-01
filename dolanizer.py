# dolanizer.py
# version: 1.1 beta
# Laurent Van Acker
# 14/05/2012
#
# This script is made to dolanize sentences given by the user.
#
# add pairs to the following list as in (to be replaced, replacement)
# template for copy paste: '','',

# For Helen

D = {'_LANG_':'dolanese',
     'goofy':'gooby',
     'please':'pls',
     'dolan':'dolan',
     ' am ':' iz ',
     'donald':'dolan',
     'don\'t know':'dunno',
     'ever':'evar',
     'you\'re':'ur',
     'your':'ur',
     'help':'halp',
     'sch':'sk',
     ' are ':' r ',
     'are':'ar',
     'ch ':'sj ',
     'of ':'af ',
     'ea':'ee',
     'th ':'t ',
     've ':'f ',
     'how are you?':'sup',
     'how are you':'sup',
     '?':'',
     'th':'d',
     'hy':'ai',     
     'y ':'ai ',
     'th':'d',
     'ff':'f',
     'i':'i',
     'c':'k',
     'e ':' ',
     'ow':'ao',
     'my':'mai',
     'me':'me',
     'oo':'u',
     'ek':'ke',
     'es':'z ',
     'cl':'lc',
     'au':'aw',
     'e':'u',
     'f ':'v ',
     'nh':'n\'',
     'ol':'awl',
     'le':'l',
     'n':'n',
     'el':'l',
     'cr':'rc',
     'nt':'n',
     's':'z'}

L = ['goofy','gooby',
     'please','pls',
     'dolan','dolan',
     ' am ',' iz ',
     'donald','dolan',
     'don\'t know','dunno',
     'ever','evar',
     'you\'re','ur',
     'your','ur',
     'help','halp',
     'sch','sk',
     ' are ',' r ',
     'are','ar',
     'ch ','sj ',
     'of ','af ',
     'ea','ee',
     'th ','t ',
     've ','f ',
     'how are you?','sup',
     'how are you','sup',
     '?','',
     'th','d',
     'hy','ai',     
     'y ','ai ',
     'th','d',
     'ff','f',
     'i','i',
     'c','k',
     'e ',' ',
     'ow','ao',
     'my','mai',
     'me','me',
     'oo','u',
     'ek','ke',
     'es ','z ',
     'cl','lc',
     'au','aw',
     'e','u',
     'f ','v ',
     'nh','n\'',
     'ol','awl',
     'le','l',
     'n','n',
     'el','l',
     'cr','rc',
     'nt','n',
     's','z']
     
# TODO: Make a table parser to make moddable
# TODO: Use dictionaries instead of lists.

def max_len(D):
	m = 1
	for keys in D:
		if keys == '_LANG_':
			a = 1
		else:
			a = len(keys)
			if a > m:
				m = a
	#print(m) #size of longest entry in D
	#print(len(D))
	return m		

def makeDict(filename):
	D = []
	return D
	
def makeList(filename):
	L = []
	return L
#dolanise function using dict
def dolandict(to_trans, D, len_max):
	to_trans = to_trans.lower()
	d = ''
	to_trans = to_trans + ' '
	ii = -1 #to_trans iterator
	for i in range(0, len(to_trans) - 1):
		ii += 1
		if ii > (len(to_trans) - 2):
			break
		a = len_max
		while(True):
			stemp = to_trans[ii]
			if a == 0:
				d = d + stemp
				break
			if ii < (len(to_trans) - a):
				for k in range(1, a):
					stemp = stemp + to_trans[ii + k]
				if stemp in D:
					d = d + D[stemp]
					ii = ii + a - 1
					break
				else:
					a = a - 1
			else:
				a = a - 1
		
	return d
	
	
#dolan takes a string and a dictionary and turns it into dolanese.
def dolan( name , list ):
    name = name.lower()
    d = ''
    name = name + ' '
    ni = -1 #nameiterator
    for i in range(0, len(name) - 1):
        ni += 1
        if ni > (len(name) - 2):
            break
        li = -1 #lijstiterator
        for j in range(0, len(list) - 1):
            stemp = name[ni] # length list[li] is at least 1.
            li += 1
            if ni  < (len(name) - len(list[li])):
                for k in range(1, len(list[li])):
                    stemp = stemp + name[ni + k]
                if stemp == list[li]:
                    d = d + list[li + 1]
                    ni += len(list[li]) - 1
                    break
            li += 1
            if li > (len(list) - 2):
                d = d + name[ni]
                break 
    return d
    
                    
print('\n# dolanizer - v 1.0.2\n#\n# Brought to you by Lovedrunk Studios.\n')
q = 1
len_max = max_len(D)
if '_LANG_' in D:
		print('The dictionary used is:', D['_LANG_'], '\n')
while q == 1:
    print('Please enter your text: (\'exit\' if you wish to quit)')
    text = input()
    if text == 'exit':
        q = 0
    else:
        print('Dolandict')
        dolanized = dolandict(text, D, max_len(D))
        if len(dolanized) > 400:
            print('\nYour dolanized text is: \n\t' + dolanized + '\n\n')
        else:
            print('Your dolanized text is: \n\t' + dolanized + '\n')
        print('Dolanlist')
        dolanized = dolan(text, L)
        if len(dolanized) > 400:
            print('\nYour dolanized text is: \n\t' + dolanized + '\n\n')
        else:
            print('Your dolanized text is: \n\t' + dolanized + '\n')
