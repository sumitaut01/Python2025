
# test file should ebd with _test or start with test_
#method shud start with test
#

# we have used setup below , which us part of fixture setup terdown
# if we had severl  methods , we will need to add methods inside class and at class level do something
def test_firstcase(setup):
    print("executed firstcase")
    msg='sumit'
    assert msg=="hi"
