import createTT
import json
class component:
    pass

stream=input("Enter the stream:")
year=int(input("Enter year:"))
sem=int(input("Enter sem:"))
TT=dict()
TT=createTT.returnData(stream,year,sem)
print(json.dumps(TT,indent=2))
