import csv
from testdbs.admin import *
import tablib
from import_export import resources
from testdbs.models import Rtu

testcsv = RtuResource().export()
testcsv.append_separator(';')
print(testcsv.csv)

f= open("guru99.csv","w+")
f.write(testcsv.get_csv(delimiter=';'))
f.close()
## read file
dataset = tablib.Dataset()
book_resource = resources.modelresource_factory(model=Rtu)()

with open('guru99.csv', newline='') as f:
    reader = csv.reader(f)
    your_list = list(reader)

print(your_list)

django.db.close_old_connections()