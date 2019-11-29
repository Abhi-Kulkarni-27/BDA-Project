from django.shortcuts import render
import os
from time import sleep
def index (request):
    return render(request,'demo/Home.html')

def exec (request):
    os.system("gnome-terminal -e 'bash -c \"hadoop namenode -format && hadoop datanode -format;exec bash\"'")
    sleep(60)
    os.system("gnome-terminal -e 'bash -c \"cd .. && cd .. && cd .. && cd .. && cd hadoop-2.7.3 && cd sbin && ./start-all.sh && cd .. && hadoop fs -mkdir /demion_analysis && hadoop fs -copyFromLocal /home/boogeyman/Documents/BDA_Project/Demonetization_Analysis/demonetization-tweets.csv /demion_analysis && hadoop fs -copyFromLocal /home/boogeyman/Documents/BDA_Project/Demonetization_Analysis/AFINN.txt /demion_analysis && pig -x mapreduce /home/boogeyman/Documents/BDA_Project/Demonetization_Analysis/demonotetization_analysis.pig ;exec bash\"'")
    sleep(500)
    os.system("gnome-terminal -e 'bash -c \" cd .. && cd .. &cd .. && cd .. && cd .. && cd .. && cd .. && cd boogeyman && cd anaconda3/lib/python3.7/site-packages/django/contrib/admin/static/Results && echo NEGETIVE TWEETS && hadoop fs -cat /demion_analysis/negative_tweets/part-r-00000 > Negetive_tweets.txt && echo POSITIVE TWEETS && hadoop fs -cat /demion_analysis/positive_tweets/part-r-00000 > Positive_tweets.txt && wc -l < Positive_tweets.txt > Num_Positive_tweets.txt && wc -l < Negetive_tweets.txt > Num_Negetive_tweets.txt && echo NEUTRAL TWEETS && hadoop fs -cat /demion_analysis/neutral_tweets/part-r-00000 > Neutral_tweets.txt;exec bash\"'")
    return render(request,'demo/Home.html')   

def viz(request):
    return render(request,'demo/Visualize.html') 

def about(request):
    return render(request,'demo/About.html')  

def result(request):
    return render(request,'demo/Results.html')

def positive(request):
    return render(request,'demo/Positive.html')

def negetive(request):
    return render(request,'demo/Negetive.html')

def neutral(request):
    return render(request,'demo/Neutral.html')
	
