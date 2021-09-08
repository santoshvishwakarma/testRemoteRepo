import datetime

def checkVaccineInfo(vaccineName, vaccinationDate=None):
    try:
        assert vaccinationDate != None and vaccinationDate != "" 
        printNextDate(str.lower(vaccineName), datetime.datetime.strptime(vaccinationDate, "%m/%d/%Y"))
    except AssertionError:
        print("Please book slot for vaccine.")
    except Exception:
        print("Error occurred while converting date.")

    
def printNextDate(vaccineName, vaccineDate):
    if  vaccineName not in {"covaxin", "covishield"}:
        print("Contact CoWin.")
    else:
        nextDate = (vaccineDate + datetime.timedelta(weeks=6),vaccineDate + datetime.timedelta(days=24))[str.lower(vaccineName) == "covaxin"] 
        print("Next Due date is {}".format(nextDate))
    

def unitTests():
    try:    
        assert checkVaccineInfo("") != ""
        assert checkVaccineInfo("Covaxin","") != ""
        assert checkVaccineInfo("Covaxin") != ""
        assert checkVaccineInfo("Covaxin", None) != ""
        assert checkVaccineInfo("Covaxin", "invalid date") != ""
        assert checkVaccineInfo("invalid vaccine", "9/1/2021") != ""
        assert checkVaccineInfo("", "9/1/2021") != ""
        assert checkVaccineInfo("Covaxin", "9/1/2021") != ""
        assert checkVaccineInfo("Covishield", "9/1/2021") != ""
        print("All test case passed.")
    except AssertionError:
        print("Test Case Failed.")

unitTests()

