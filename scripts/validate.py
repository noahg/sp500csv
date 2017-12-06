from pprint import pprint
from goodtables import Inspector

inspector = Inspector()
validation_report = inspector.inspect(
    '../datapackage.json', preset='datapackage')

pprint(validation_report)