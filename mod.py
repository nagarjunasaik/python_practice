print('This is module file')

a='Varible in mod 1'

def find(lst,elm):
	for i in lst:
		if i == elm:
			return lst.index(i)

__doc__='Test doc'			