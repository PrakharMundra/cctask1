import csv
import requests
response=requests.get('http://api.football-data.org/v2/competitions/',headers={'X-Auth-Token':'5983fc35d48e4f4f8c26867854587756'})
response_body=response.json()
list=response_body['competitions']    
print('1.TIER_ONE')
print('2.TIER_TWO')
print('3.TIER_THREE')
print('4.TIER_FOUR')
x=input("please enter any of the four above numbers ")
if x=='1':
    y="TIER_ONE"
if x=='2':
    y="TIER_TWO"
if x=='3':
    y="TIER_THREE"
if x=='4':
    y="TIER_FOUR"
with open('mycsv.csv','w',newline='') as f:
            thewriter=csv.writer(f)
            thewriter.writerow(['id','Name','Area','tier','AvailableSeasons'])
            for i in range(len(list)):
              if (list[i].get("plan")==y) :
                  a=str(list[i].get("id"))
                  b=list[i].get("name")
                  c=list[i].get("plan")
                  d=str(list[i].get("numberOfAvailableSeasons")) 
                  e=list[i].get("area").get("name")
                  line=a+","+b+','+e+','+c+','+d
                  array=line.split(',')
                  thewriter.writerow(array)
