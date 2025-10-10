class DriverFactory:
    def get_driver(self, name):
        if name=="chrome": return Chrome()
        if name=="firefox": return Firefox()
