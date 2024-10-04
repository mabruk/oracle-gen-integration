class IntegrationSchema:
    def __init__(self, genricContract: str, genericCode: str):
        self.contract = genricContract
        self.code = genericCode

    def getGenericCode(self):
        return self.code
    
    def getGenericContract(self):
        return self.contract
