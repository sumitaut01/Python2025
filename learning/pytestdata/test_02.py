
# test should _test
# py.test file.py -k -s
#-s for log
#-k  "creditcard"       will find if method name has that word

def test_secondcase():
    print("executed secondcase")
    msg='sumit'
    assert msg=="hi"
