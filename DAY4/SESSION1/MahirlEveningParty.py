 day=input().strip()
#remove leading and trailling spaces
attendees=int(input("enter the attendees"))

#function in python
def classifySuccessOfParty(day,attendees):
    weekdays=["MON","TUE","WED","THU"]
    weekends=["FRI","SAT","SUN"]
    
    if day not in weekends and day not in weekdays:
        return "INVALID DAY"
    if attendees<0:
        return "INVALID ATTENDEES"
    if day in weekdays:
        if 700<=attendees<=1000:
            return"SUCCESSFULL"
        else:
            return "UNSUCCESSFULL"
    if day in weekends:
        if attendees>=1500:
            return "SUCCESSFULL"
        else:
            return "UNSUCCESSFULL"