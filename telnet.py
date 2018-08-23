#!/usr/bin/env python

import telnetlib

class MyError(Exception):
    def __init__ (self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


HOST = "172.17.58.71"
user = "harkamal"
password = "matrix"

try:
    tn = telnetlib.Telnet(HOST)

    tn.read_until("login: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")
        val = tn.read_until("]$", 10)
        print "Logon:", val

        if val.count("harkamal") <= 0:
            print "unable to logon"
            raise NameError('no logon')
    
        tn.write("ls\n")
        val = tn.read_until("]$", 10)
        print "Command executed:"
        if val.count("Documents") <= 0:
            print "required dir 'Documents' not found"
            raise MyError('no dir')

        tn.write("ls Documents\n")
        val = tn.read_until("]$", 10)
        tn.write("exit\n")
        print "Done"
        counter = 0
#        arr = []
#        for line in val.split(' '):
#            counter = counter + 1
#            print "line ", counter, ":", line
        print "--", val, "--"

#        print "ReadAll:", tn.read_all()

except NameError:
    print "unable to logon, no need to send 'exit'"

except MyError as e:
    print 'MyError exception occur with value:', e.value()
    tn.write("exit\n")

except:
    print 'unknown exception occur'
    tn.write("exit\n")

finally:
    print "Done"
    tn.write("exit\n")
# ---- END ----

