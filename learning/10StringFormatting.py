string = 'Hello World!'

print( 'this is {}'.format(string)) #this is Hello World!

print( 'this is {} {} {} '.format(string,'second','third')) #this is Hello World! second third

print( 'this is {2} {1} {0} '.format(string,'second','third')) #this is third second Hello World!

print( 'this is {a} {b} {c} '.format(a=string,b='second',c='third')) #this is Hello World! second third

