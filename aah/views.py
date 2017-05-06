from django.shortcuts import render, redirect
import os
import json

PLAYERFILE = os.path.join(os.getcwd(), "..", "playerdata.json")
TRIBEFILE = os.path.join(os.getcwd(), "..", "tribedata.json")

def index(request):
    with open(PLAYERFILE, "r") as pfile:
        data = pfile.read()
    pdata = json.loads(data)
    sorted_pdata =sorted(pdata,key=lambda x: int(x["Level"]),reverse=True)
    with open(TRIBEFILE, "r") as tfile:
        data = tfile.read()
    tdata = json.loads(data)
    sorted_tdata =sorted(tdata,key=lambda x: x["LastEpoch"],reverse=True)
    return render(request,'index.html', {"player": sorted_pdata,
                                         "tribe": sorted_tdata})
