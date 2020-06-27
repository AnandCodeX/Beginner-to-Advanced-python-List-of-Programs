import socket
import requests

try:
    socket.create_connection(("www.google.com",80))
    print("u r connected")
    res=requests.get("https://ipinfo.io")
    print(res)
    data=res.json()
    print(data)
    city=data['city']
    print("sher ka nam",city)
    #lat long
    loc=data['loc']
    latlon=loc.split(",")
    lat=latlon[0]
    lon=latlon[1]
    print(lat)
    print(lon)
except OSError as e:
    print("check connection",e)
    