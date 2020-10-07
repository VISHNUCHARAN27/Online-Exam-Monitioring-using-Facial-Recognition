from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import requests
import sys
import subprocess
import time
import csv
from subprocess import run,PIPE
import pandas as pd
import os
from threading import Thread
from multiprocessing import Process
from celery import Celery

# Creating views for our URLs here. dinesh.jayakumar@focusacademy
app=Celery('tasks',broker='amqp://localhost//')

def indexView(request):
    return render(request,'index.html')

@login_required
def dashboardView1(request):
    return render(request,'dashboard1.html')

def external(request):
    path = "C:\\Users\\B.Vishnu charan\\PycharmProjects\\Face_detection\\detector.py"
    out = subprocess.Popen(["C:\Program Files (x86)\Python37-32\python.exe", path], shell=False)
    time.sleep(10)
    out.terminate()
    x = pd.read_csv('C:\\Users\\B.Vishnu charan\\PycharmProjects\\Face_detection\\idvals.csv')
    x1 = list(x['id'])
    x2=int(x1[-1])
    flag=0
    uname = request.POST.get('uname')
    checklogin = [str(x2), str(uname)]
    with open('C:\\Users\\B.Vishnu charan\\PycharmProjects\\Face_detection\\users.csv', 'rt') as f:
        reader = csv.reader(f)
        results = filter(lambda x: uname in x, reader)
        for line in results:
            if line == checklogin:
                flag=1
                data = []
                with open('C:\\Users\\B.Vishnu charan\\PycharmProjects\\Face_detection\\idvals.csv', "rt") as scraped:
                    reader = csv.reader(scraped, delimiter=',')
                    for row in reader:
                        if row:  # avoid blank lines
                            columns = [row[0], row[1], row[2]]
                            data.append(columns)

                x = data[-1]
                x.append("NO")
                last_row = x
                with open('C:\\Users\\B.Vishnu charan\\PycharmProjects\\Face_detection\\Camaccess.csv', 'a') as file:
                    writer = csv.writer(file)
                    writer.writerow(last_row)

                data.clear()
                return render(request,'dashboard.html')
    if flag==0:
        return render(request,'index.html')
    #="C:\\Users\\B.Vishnu charan\\PycharmProjects\\Face_detection\\detector.py"
    #out=run(["C:\Program Files (x86)\Python37-32\python.exe",path],shell=False,stdout=PIPE)
    #x=pd.read_csv('C:\\Users\\B.Vishnu charan\\PycharmProjects\\Face_detection\\idvals.csv')
    #x1=list(x['id'])
    #if(x1[-1]!=-1):
     #   return dashboardView(request)
    #else:
     #   print('Not a valid user')

def dashboardView(request):
    return render(request, 'dashboard.html')

def examportalView(request):
    return render(request, 'examstart.html')

def exampageView(request):
    #multifaceexecute()
    return render(request, 'finalexampage.html')
    #t = Thread(target=multifaceexecute(request))
    # t.start()

#def Mainpage(request):
 #   return render(request, 'camaccess.html')

def cheatindexView(request):
    x = pd.read_csv('C:\\Users\\B.Vishnu charan\\PycharmProjects\\Face_detection\\Camaccess.csv')
    x1 = list(x['CamAccess'])
    y = x1[-1]
    if(y=="YES"):
        return render(request, 'examover.html')
    else:
        return render(request,'camaccess.html')

def multifaceexecute(request):
    data = []
    with open('C:\\Users\\B.Vishnu charan\\PycharmProjects\\Face_detection\\idvals.csv', "rt") as scraped:
        reader = csv.reader(scraped, delimiter=',')
        for row in reader:
            if row:  # avoid blank lines
                columns = [row[0], row[1], row[2]]
                data.append(columns)

    x = data[-1]
    x.append('YES')
    last_row = x
    with open('C:\\Users\\B.Vishnu charan\\PycharmProjects\\Face_detection\\Camaccess.csv','a') as file:
        writer = csv.writer(file)
        writer.writerow(last_row)

    data.clear()
    path = "C:\\Users\\B.Vishnu charan\\PycharmProjects\\Face_detection\\face_count.py"
    out = subprocess.Popen(["C:\Program Files (x86)\Python37-32\python.exe", path], shell=False)
    time.sleep(20)
    return render(request, 'examover.html')



"""
def button(request):
    return render(request,'registration/login.html',)

def output(request):
    data=requests.get("https://reqres.in/api/users")
    data=data.text
    return render(request,'registration/login.html',{'data':data})
"""

