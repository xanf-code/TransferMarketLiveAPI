from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Transfer
from .serializer import TransferSerializer
import requests
from bs4 import BeautifulSoup
import json

# Create your views here.

def index(request):
    return HttpResponse('Success')

class TransferAPI(viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer

def latest(request):
    try:
        headers = {'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
        url = "https://www.transfermarkt.co.in/indian-super-league/letztetransfers/wettbewerb/IND1/plus/1"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        for tran in soup.select('tbody > tr'):
            names = tran.find('a',class_ = 'spielprofil_tooltip').text
            playerImage = tran.select('tr')[0].img['src']
            playerLink = tran.find('a',class_ = 'spielprofil_tooltip').attrs['href']
            fromTeam = tran.select('tr')[2].getText()
            toTeam = tran.select('tr')[4].getText()
            position = tran.select('tr')[1].getText()
            fee = tran.find('td',class_ = 'rechts hauptlink').text
            age = tran.select('td',class_ = 'zentriert')[5].getText()
            date  = tran.select('td',class_ = 'zentriert')[14].getText()
            fromTeamImage = tran.select('tr')[2].img['src']
            toTeamImage = tran.select('tr')[4].img['src']
            
            transfer = Transfer()
            transfer.names = names
            transfer.age = age
            transfer.playerImage = playerImage
            transfer.playerLink = playerLink  
            transfer.fromTeam = fromTeam
            transfer.fromTeamImage = fromTeamImage
            transfer.toTeam = toTeam
            transfer.toTeamImage = toTeamImage
            transfer.position = position
            transfer.fee = fee
            transfer.date = date

            transfer.save()
        return HttpResponse("Data Fetched Proceed to https://apitmindia.herokuapp.com/tran/transfers/")
    except Exception as e:
        return HttpResponse(f"Failed{e}")    