#William Nguyen
#1824617
import datetime
f = open("inputdates.txt","r")

currentDate = datetime.datetime.now()

with open('parsedDates.txt', 'a') as outputfile:
    for line in f:
        if line.find(",") != -1:

            if line.find(".") == -1:

                line = line.strip()
                line = line.replace(",","")
                line = line.replace(".","")

                datetime_object = datetime.datetime.strptime(line, '%B %d %Y')

                if (datetime_object < currentDate):
                    

                    datetime_object = datetime_object.strftime("%x")
                    print(datetime_object)
                    outputfile.write(datetime_object+"\n")
