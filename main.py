from IntegrationSchemaGenerator import *
from domains.GenericIntegrationSchema import *


# Placeholders, these values should be read from correct location in the code
MigrationType_TIBCO = "Tibco"      
ingested_api_specification = ""     
ingested_code = ""                  


# Call this function with the ingested api specification
try:
    response = createGenericContract(ingested_api_specification, MigrationType_TIBCO)
    generatedContract = response.choices[0].message.content
except:
    print("Failed to parse API specification")
    exit(0)


# Call this function with the ingested source code
try:
    generatedCode = createGenericCode(ingested_code)
except:
    print("Failed to parse application code")
    exit(0)


# Add generated objects to the integration schema
integrationSchema = IntegrationSchema(generatedContract, generatedCode)


# Call the generate function in generators.contracts to get the RAML version of the generated contract
raml = generate(integrationSchema.getGenericContract)



################################################################

# Modified domain/classes.py
# Added code as argument to the constructor
""""
class Integration:
    def __init__(self, specification: str=None, code: str=None, documentation: str=None, apis: list[Api]=None):
            self.id = uuid.uuid4()            
            self.specification = specification
            self.code = code
            self.documentation = documentation
            self.apis = apis

"""

