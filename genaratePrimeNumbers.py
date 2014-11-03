__author__ = 'Suresh.Aswathnarayan'
def genTest(n):
	yield n%2




foo=genTest(10)
print foo.next()
#print foo.next()