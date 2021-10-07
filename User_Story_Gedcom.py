from gedcom.parser import Parser
from datetime import datetime
from datetime import date


file_path = 'C:/Users/HP/Downloads/My-Family-20-Sep-2021-094551368.ged'

gedcom_parser = Parser()

gedcom_parser.parse_file(file_path)

child_elements = gedcom_parser.get_root_child_elements()

def convertDate(d):
    demo=demo.split(" ")
    month=["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
    return datetime.datetime(int(d[2]), month.index(d[1])+1, int(d[0]))

def validDate(arguments):
	current_date = date.today()
	try:
		date_arg = datetime.strptime(arguments, "%d %b %Y").date()
	except ValueError:
		raise ValueError("Incorrect data format, should be YYYY-MM-DD")

	if date_arg > current_date:
		return False
	return True   

for element in child_elements:
   
    if element.get_tag()=="FAM":
        arr=[]
        error=0
        child_date="not available"

        for test in element.get_child_elements():
            if test.get_tag()=="HUSB" or test.get_tag()=="WIFE":
                arr.append(test.get_value())
                if test.get_tag()=="CHIL":
                    for kDemo in test.get_child_elements():
                        if kDemo.get_tag()=="DATE":
                            child_date=k.get_value()
                            child_date=convertDate(child_date)

        if child_date!="not available":
            for j in child_elements:
                
                if j.get_pointer() in arr:

                    for pe in j.get_child_elements():

                        if pe.get_tag()=="CHIL":
                            for p in pe.get_child_elements():
                                if p.get_tag()=="DATE":
                                    birth_date=p.get_value()
                                    birth_date=convertDate(birth_date)
                                    if birth_date > child_date:
                                        error=1

            if(error ==1):
                print("Child data invalid:"+ element.get_pointer())

print("End")                           