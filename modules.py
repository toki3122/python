#modules=a file containing python code. May contain function, classes etc.
#used with modular programming, which is to seperate a program into parts
import messages as msg #messages or msg both can work now
msg.hello()
msg.bye()

#this can also be used:
#from messages import * # * is used to call all functions, but any specific function can be called if needed
#hello()
#bye()
# it might cause naming conflict, therefore it is discouraged

