import requests
import httpx
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
from user_agent import generate_user_agent
import requests.auth
import urllib3
from requests.auth import HTTPBasicAuth
import pickle
import json
import json
import random
import time

def connexion():

    ip_test = 'https://httpbin.org/ip'
    url_login = 'https://www.zalando.fr/login'
    sensor_1 = {"sensor_data":"7a74G7m23Vrp0o5c9180451.62-1,2,-94,-100,Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0,uaend,11059,20100101,fr,Gecko,1,0,0,0,393132,841044,1536,824,1536,864,1536,415,1550,,cpen:0,i1:0,dm:0,cwen:0,non:1,opc:0,fc:1,sc:0,wrc:1,isc:73.5999984741211,vib:1,bat:0,x11:0,x12:1,5567,0.912117976456,798895420521.5,loc:-1,2,-94,-101,do_en,dm_en,t_dis-1,2,-94,-105,0,-1,0,0,1103,1103,0;1,-1,0,0,1466,1466,0;-1,2,-94,-102,0,-1,0,0,1103,1103,0;1,-1,0,0,1466,1466,0;-1,2,-94,-108,-1,2,-94,-110,0,1,452,1022,278;1,1,469,904,297;2,1,485,796,325;3,1,502,698,362;4,1,531,654,386;5,1,535,626,406;6,1,552,602,430;7,1,568,594,445;8,1,585,586,463;9,1,602,585,474;10,1,619,585,481;11,1,635,586,490;12,1,652,586,493;13,1,669,587,496;14,1,686,588,498;15,1,702,589,499;16,1,719,590,500;17,1,735,591,501;18,1,751,591,503;19,1,769,593,505;20,1,791,594,506;21,1,801,596,507;22,1,818,597,507;23,1,835,598,507;24,1,853,599,507;25,1,868,600,507;26,1,896,601,507;27,1,935,601,510;28,1,1001,602,512;29,1,1004,602,523;30,1,1044,600,531;31,1,1060,599,537;32,1,1336,602,527;33,1,1518,602,530;34,1,1535,603,530;35,1,1551,610,528;36,1,1568,618,527;37,1,1569,627,525;38,1,1585,639,522;39,1,1602,725,506;40,1,1618,786,496;41,1,1698,819,493;42,1,1702,1051,492;43,1,1719,1069,497;44,1,1752,1082,505;45,1,2002,1099,510;46,1,2018,1113,513;47,1,2035,1138,517;48,1,2052,1154,521;49,1,2068,1178,522;50,1,2086,1195,525;51,1,2102,1209,526;52,1,2118,1218,529;53,1,2135,1220,529;54,1,2152,1220,530;55,1,2169,1220,532;56,1,2186,1218,534;57,1,2200,1217,538;58,1,2202,1216,539;59,1,4696,1182,412;60,1,4701,1156,410;61,1,4719,1033,407;62,1,11085,816,410;63,1,11102,793,409;64,1,11118,777,408;65,1,11136,758,408;66,1,11152,750,410;67,1,11161,745,410;68,1,11168,739,412;69,1,15936,1128,410;70,1,15953,1135,404;71,1,15968,1140,400;72,1,15976,1143,398;73,1,15985,1148,396;74,1,16002,1151,394;75,1,16019,1155,394;76,1,16036,1156,394;77,1,16052,1156,394;78,1,16069,1156,393;79,1,16102,1156,392;80,1,16119,1155,392;81,1,16169,1158,392;82,1,16185,1174,395;83,1,16202,1198,404;84,1,16212,1208,410;85,1,18793,528,408;86,1,18803,551,352;87,1,18820,572,301;88,1,18835,588,261;89,1,18852,601,222;90,1,18869,604,209;91,1,18885,606,202;92,1,18902,606,200;93,1,18918,606,199;94,1,18935,604,198;95,1,18952,602,197;96,1,18969,598,196;97,1,18986,595,194;98,1,19002,592,193;99,1,19020,586,190;122,3,19734,596,199,1103;-1,2,-94,-117,-1,2,-94,-111,-1,2,-94,-109,-1,2,-94,-114,-1,2,-94,-103,2,12383;-1,2,-94,-112,https://www.zalando.fr/login?target=%2Fwishlist%2F-1,2,-94,-115,1,857413,32,0,0,0,857381,19734,0,1597790841043,11,17092,0,123,2848,1,0,19735,725700,0,B5CDF9F2189AC166430F432BC127478E~-1~YAAQ1VNlX3gLtP9zAQAA9GzBAwSd7rACF39OO/OrQAfEHL9vTBKHE53HtsJSSyGLUyGcSSWINsEJ7kwDpELeD7bfeWYrkrbSSPFdBxIyMgcJ8M4naxffAqxRKsqlKOpRxWdGX8bo2251fXgf8qPan1OWVebxkigL1NN4U9FqsELvPfYAf/jw1H37Hg4NDRmnfyD8CkWMVETxDs1WJ9dzxTJZrwszRv83vwEHKqHtZCfbutGH+f2XVk5EcQoz3D+/iHoAPIOalP1QQRrKyfPUKc478o56rEU7AediC8RJaeJVpaZFmT4CQ45xMPy5OUCAYgQOUvFQ07CvXbvqqFF0omrrNrY=~-1~-1~-1,32380,735,1401751123,26067385,PiZtE,67972,65-1,2,-94,-106,1,2-1,2,-94,-119,200,0,0,200,0,200,200,0,0,0,0,400,400,400,-1,2,-94,-122,0,0,0,0,1,0,0-1,2,-94,-123,-1,2,-94,-124,-1,2,-94,-126,-1,2,-94,-127,11133333331333333333-1,2,-94,-70,1436327638;1247333925;dis;,3;true;true;true;-120;true;24;24;true;false;unspecified-1,2,-94,-80,6550-1,2,-94,-116,315391530-1,2,-94,-118,180900-1,2,-94,-121,;2;5;0"}

    sensor_2 = {"sensor_data":"7a74G7m23Vrp0o5c9180451.62-1,2,-94,-100,Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0,uaend,11059,20100101,fr,Gecko,1,0,0,0,393132,841044,1536,824,1536,864,1536,415,1550,,cpen:0,i1:0,dm:0,cwen:0,non:1,opc:0,fc:1,sc:0,wrc:1,isc:73.5999984741211,vib:1,bat:0,x11:0,x12:1,5567,0.516032703258,798895420521.5,loc:-1,2,-94,-101,do_en,dm_en,t_dis-1,2,-94,-105,0,-1,0,0,1103,1103,0;1,-1,0,0,1466,1466,0;-1,2,-94,-102,0,-1,0,0,1103,1103,1;1,-1,0,0,1466,1466,0;-1,2,-94,-108,0,1,23749,17,0,4,1103;1,1,24250,17,0,4,1103;2,1,24281,17,0,4,1103;3,1,24305,86,0,4,1103;4,2,24425,86,0,4,1103;5,2,24636,17,0,0,1103;-1,2,-94,-110,0,1,452,1022,278;1,1,469,904,297;2,1,485,796,325;3,1,502,698,362;4,1,531,654,386;5,1,535,626,406;6,1,552,602,430;7,1,568,594,445;8,1,585,586,463;9,1,602,585,474;10,1,619,585,481;11,1,635,586,490;12,1,652,586,493;13,1,669,587,496;14,1,686,588,498;15,1,702,589,499;16,1,719,590,500;17,1,735,591,501;18,1,751,591,503;19,1,769,593,505;20,1,791,594,506;21,1,801,596,507;22,1,818,597,507;23,1,835,598,507;24,1,853,599,507;25,1,868,600,507;26,1,896,601,507;27,1,935,601,510;28,1,1001,602,512;29,1,1004,602,523;30,1,1044,600,531;31,1,1060,599,537;32,1,1336,602,527;33,1,1518,602,530;34,1,1535,603,530;35,1,1551,610,528;36,1,1568,618,527;37,1,1569,627,525;38,1,1585,639,522;39,1,1602,725,506;40,1,1618,786,496;41,1,1698,819,493;42,1,1702,1051,492;43,1,1719,1069,497;44,1,1752,1082,505;45,1,2002,1099,510;46,1,2018,1113,513;47,1,2035,1138,517;48,1,2052,1154,521;49,1,2068,1178,522;50,1,2086,1195,525;51,1,2102,1209,526;52,1,2118,1218,529;53,1,2135,1220,529;54,1,2152,1220,530;55,1,2169,1220,532;56,1,2186,1218,534;57,1,2200,1217,538;58,1,2202,1216,539;59,1,4696,1182,412;60,1,4701,1156,410;61,1,4719,1033,407;62,1,11085,816,410;63,1,11102,793,409;64,1,11118,777,408;65,1,11136,758,408;66,1,11152,750,410;67,1,11161,745,410;68,1,11168,739,412;69,1,15936,1128,410;70,1,15953,1135,404;71,1,15968,1140,400;72,1,15976,1143,398;73,1,15985,1148,396;74,1,16002,1151,394;75,1,16019,1155,394;76,1,16036,1156,394;77,1,16052,1156,394;78,1,16069,1156,393;79,1,16102,1156,392;80,1,16119,1155,392;81,1,16169,1158,392;82,1,16185,1174,395;83,1,16202,1198,404;84,1,16212,1208,410;85,1,18793,528,408;86,1,18803,551,352;87,1,18820,572,301;88,1,18835,588,261;89,1,18852,601,222;90,1,18869,604,209;91,1,18885,606,202;92,1,18902,606,200;93,1,18918,606,199;94,1,18935,604,198;95,1,18952,602,197;96,1,18969,598,196;97,1,18986,595,194;98,1,19002,592,193;99,1,19020,586,190;122,3,19734,596,199,1103;123,4,19805,596,199,1103;124,2,19805,596,199,1103;197,3,27637,673,294,1466;-1,2,-94,-117,-1,2,-94,-111,-1,2,-94,-109,-1,2,-94,-114,-1,2,-94,-103,2,12383;3,19739;-1,2,-94,-112,https://www.zalando.fr/login?target=%2Fwishlist%2F-1,2,-94,-115,152548,927670,32,0,0,0,1080185,27637,0,1597790841043,11,17092,6,198,2848,3,0,27637,938593,0,B5CDF9F2189AC166430F432BC127478E~-1~YAAQ1VNlX3EOtP9zAQAA7rfBAwTeSpmwZs5Rqw4yWu5QnhyqrMaiUBXpOTzurkciQDq3nDxW/tm1+1fTsi2ux0odffjYGkoKYWNYADQTPeQ2EpUhjBgp9B/a3Vs8VVNtQauo+Fierz2Mqn/4MotvGBJgbEY9fc0hWTerZDy5FRWnFap31t8Ru0UHfJBhPk15wmJyZ2NK5/uJ903nGc+gi3Pt5bguezoNK9BOxPQrVmd+aUaenZsx2I+vd1gWk1xzSC5X/P2R06XXFc8Ob9C7pICuQGnut7wc2/5ce0O8/huJv3jeHcdpkjDfBdD3gZlNorHfrTbKJ1QDTfNr+XdlbKvEoRo=~-1~-1~-1,32868,735,1401751123,26067385,PiZtE,69486,35-1,2,-94,-106,1,3-1,2,-94,-119,200,0,0,200,0,200,200,0,0,0,0,400,400,400,-1,2,-94,-122,0,0,0,0,1,0,0-1,2,-94,-123,-1,2,-94,-124,-1,2,-94,-126,-1,2,-94,-127,11133333331333333333-1,2,-94,-70,1436327638;1247333925;dis;,3;true;true;true;-120;true;24;24;true;false;unspecified-1,2,-94,-80,6550-1,2,-94,-116,315391530-1,2,-94,-118,192499-1,2,-94,-121,;1;5;0"}

    proxies = {
        'http': 'http://alex19132-country-FR-city-Paris:a6a17f-060e0d-374951-a1257e-2e7e9c@premium.residential.rotating.proxyrack.net:9000',
        'https': 'https://alex19132-country-FR-city-Paris:a6a17f-060e0d-374951-a1257e-2e7e9c@premium.residential.rotating.proxyrack.net:9000'
    }

    with requests.Session() as s:
        
        print(s.get(ip_test, verify=False).json())
        #s.proxies = proxies
        print(s.get(ip_test, verify=False).json())


        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding' : 'gzip, deflate, br',
            'Accept-Language' : 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
            'Connection' : 'keep-alive',
            #'Cookie' : 'Zalando-Client-Id=de04a38f-81e9-410b-b652-fc8c71c1c72f; _abck=B5CDF9F2189AC166430F432BC127478E~-1~YAAQ1VNlX4I8tP9zAQAAzRvGAwQvkh7YHdcfoOREKv0qthqPcVvzyUFB1T8+LM7s3dm3HIWZ+CuvlkRRr74/dq0zn2AoLY2uzxU2dbwqaykzYEX3lc2NV+W0n4QRHHtwRh77scfVhgTQOe7b0GWBC54HgIU76tworBDp3KPJmCakovQhINTTHuMgTr94p9jqtVc76uGIqhjtx2JNVPvevldXNbKLTBsPmvWdTMzFHZtqdV0dzYxheD3XjPvGxTq/4TpgSmUzfLsy8UDn91+5nFiQWJ+CXm2geMIpbob6wRc53sqUjHw6+eaRSE3RPrlVpcAlr0gxPr/XqT+XsN+d9nN3irk=~-1~-1~-1; _gcl_au=1.1.164078372.1591700050; CUSTOMER=GzMrtc9tEOfZ…bzQmI_N-a4og8RX5K3tiKOy1yvThAWzRd3KanIyyUiCPC2Ee4OeBCPB0lZ8pmJj-HEzBvPQ0WT6QemaWDWKPFna3zIsgxN1dRlSilRz5gdcN1oCPug-vEMlUVVqQeA1k4JYtQ4=; mpulseinject=false; ak_bmsc=C064C04BA44E65EBDDED161B27ABC7F75F6517A440080000EA563C5FB77AEC39~plNGk+B0pjBpwA3SQ6lSaQIrf6R1N8Fkm8I6s50cjxhMKF2VLTrhAyf9kU9EyCbYtbjXrbUxYj4wooQeNrMnV7uweNKfdQOhzM7HLArg91hSnizltW5f4UWHC3ae2xLe/iGMep0IiLvEFCvphEh/dlhVYeEz7AOQ9e85D5Z0ZbPlf42C91sXBaDpH2JMEjFTriAlZpF7133Lrj3XwPM6ipb+o5OxKv1fq9pR1rMYwsOZDe+C+F/tQuGNbBGuSZnYta; sqt_cap=1597789930852',
            'Host' : 'www.zalando.fr',
            'TE' : 'Trailers',
            'Upgrade-Insecure-Requests' : '1',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
        }

        s.headers.update(headers)
        r = s.get(url_login)
        print(r)
        s.post(url_login, json=sensor_1)
        r=s.post(url_login, json=sensor_2)
        print(r)

        headers = {
            'Host' : 'www.zalando.fr',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
            'Accept' : '*/*',
            'Accept-Language' : 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding' : 'gzip, deflate, br',
            'Content-Type' : 'text/plain;charset=UTF-8',
            'Content-Length' : '4583',
            'Origin' : 'https://www.zalando.fr',
            'Connection' : 'keep-alive',
            'Referer' : 'https://www.zalando.fr/login?target=%2Fwishlist%2F',
            'Cookie': 'Zalando-Client-Id=de04a38f-81e9-410b-b652-fc8c71c1c72f; _abck=B5CDF9F2189AC166430F432BC127478E~-1~YAAQV6E1VHlA1QB0AQAA0XMRBgSvUm0Jwm4g5o6XSHkFuA+9w8Qr0j3RPi2v7RgiVdEN+OsUsmSKKJHaY4J9f5g6YBcmm6MWa8jXlNx71Q7Ut3HSL+RKaJZKuctshYuMSE8r55vG/1Rwcs/gvF5V6kK0ufbyMuzthdHA4Ck+vJHdIwzVMyOqTW217sNPE/t1GqvJ9ke4fDLmTHgFDo26munZYJjXKvlkQkDZYgeefIVXithY7oyAgT7zWd7jsa1ETm9iilm4qtR6DAtmhT00YuCSnxKXNaPw5g7Sd+0u4KdTYc59hNwc4DtIm1Y0rSFYnCktF7mX8IOQNi4EIGPy8pn/zBQ=~-1~-1~-1; _gcl_au=1.1.164078372.1591700050; CUSTOMER=GzMrtc9tEOfZpFAyxieacLhWylFaA1x8G7aAkL5vDn4VJm8bMDP7rUir5p66F6WKZpsF89+7XkW4rKJFjbPEcc8LUwWWAOuvp/tYCmf1bQyKRM9z4Wm2IAlzk7kbXdf5t7iCJuexH593yb5f/xPHw8+A9WyAvIq5GFO0g6Nk0gQhSt2VwzaoPIt4Ob0A8xYs+RLzUiYg6TqsPEO4u0b6+BUmbxswM/utUcqlNthTxRA=; ncx=m; _ga=GA1.2.694087826.1592574834; sqt_cap=1597789930852; frsx=AAAAALzf5KjvJEr5u--qE5jNbctPpd5CYmwkDgqA7dyw239wPN8tX9SwKmN_4KgebWqoYC9kbFkvxRtKHKWaK-lrcctwA1NZhvuGqG1oZ1TGOXjCFrI6BRNNUmOYDpve35kj7OIR3li2iayv7RY7U6Q=; mpulseinject=false; ak_bmsc=1136AE0DFD7F7AF5DFF4B6B11FC5FE5F5435A157AF530000C5F13C5F30B75376~plYiwWJeA9WBju7XcIOE+9mHq5hH0/ZNzhfHEXxHbZ/qDwHsxkTLFaqIFZL/Ihh1UxqzGOqq07euW+8b6XzuPUb459AjcRVXHrifAqhGIbb0dBf5QXulCLm5Il6zb/Y1ocuasiuEYRyZIyFAXX0XXizyPKRoK2cxAnqOWEVLeTQe7vS6lwPIFdXse1zCQ2uOf+WInFDWRlCmwWLsPqcNWXfvthEwsR3CHPniceGql+N27hR6JvjTtz7Ebg05GATbrS; bm_sz=55BB5E45588C818DD6BF0A956B6AC9AE~YAAQV6E1VAU91QB0AQAAimoQBgh3sbFzOSHfnF6alvitxiz5CBO/J/eW2+crnOPe1oRgec/r5rSq7VE/h3Xy5KdYvI300DSE7PGJ/Zeg+Fk4Ivie/Cij13+xesmA/coTD4pK0CkjwWNNwHHcLhQ4Q7NtU+RFjT17r99QPh9/Rv2vOUqScFTdoWc5ahdGr0w=',
            'TE': 'Trailers'
        }
        
        '''cookies = {
            '_abck' :	'"B5CDF9F2189AC166430F432BC127478E~-1~YAAQV6E1VHlA1QB0AQAA0XMRBgSvUm0Jwm4g5o6XSHkFuA+9w8Qr0j3RPi2v7RgiVdEN+OsUsmSKKJHaY4J9f5g6YBcmm6MWa8jXlNx71Q7Ut3HSL+RKaJZKuctshYuMSE8r55vG/1Rwcs/gvF5V6kK0ufbyMuzthdHA4Ck+vJHdIwzVMyOqTW217sNPE/t1GqvJ9ke4fDLmTHgFDo26munZYJjXKvlkQkDZYgeefIVXithY7oyAgT7zWd7jsa1ETm9iilm4qtR6DAtmhT00YuCSnxKXNaPw5g7Sd+0u4KdTYc59hNwc4DtIm1Y0rSFYnCktF7mX8IOQNi4EIGPy8pn/zBQ=~-1~-1~-1"',
            '_ga' :	'"GA1.2.694087826.1592574834"',
            '_gcl_au' :	'"1.1.164078372.1591700050"',
            'ak_bmsc' :	'"1136AE0DFD7F7AF5DFF4B6B11FC5FE5F5435A157AF530000C5F13C5F30B75376~plYiwWJeA9WBju7XcIOE+9mHq5hH0/ZNzhfHEXxHbZ/qDwHsxkTLFaqIFZL/Ihh1UxqzGOqq07euW+8b6XzuPUb459AjcRVXHrifAqhGIbb0dBf5QXulCLm5Il6zb/Y1ocuasiuEYRyZIyFAXX0XXizyPKRoK2cxAnqOWEVLeTQe7vS6lwPIFdXse1zCQ2uOf+WInFDWRlCmwWLsPqcNWXfvthEwsR3CHPniceGql+N27hR6JvjTtz7Ebg05GATbrS"',
            'bm_sz' :   '"55BB5E45588C818DD6BF0A956B6AC9AE~YAAQV6E1VAU91QB0AQAAimoQBgh3sbFzOSHfnF6alvitxiz5CBO/J/eW2+crnOPe1oRgec/r5rSq7VE/h3Xy5KdYvI300DSE7PGJ/Zeg+Fk4Ivie/Cij13+xesmA/coTD4pK0CkjwWNNwHHcLhQ4Q7NtU+RFjT17r99QPh9/Rv2vOUqScFTdoWc5ahdGr0w="',
            'CUSTOMER' :    '"GzMrtc9tEOfZpFAyxieacLhWylFaA1x8G7aAkL5vDn4VJm8bMDP7rUir5p66F6WKZpsF89+7XkW4rKJFjbPEcc8LUwWWAOuvp/tYCmf1bQyKRM9z4Wm2IAlzk7kbXdf5t7iCJuexH593yb5f/xPHw8+A9WyAvIq5GFO0g6Nk0gQhSt2VwzaoPIt4Ob0A8xYs+RLzUiYg6TqsPEO4u0b6+BUmbxswM/utUcqlNthTxRA="',
            'frsx' :    '"AAAAALzf5KjvJEr5u--qE5jNbctPpd5CYmwkDgqA7dyw239wPN8tX9SwKmN_4KgebWqoYC9kbFkvxRtKHKWaK-lrcctwA1NZhvuGqG1oZ1TGOXjCFrI6BRNNUmOYDpve35kj7OIR3li2iayv7RY7U6Q="',
            'mpulseinject' :	'"false"',
            'ncx':	'"m"',
            'sqt_cap':  '"1597789930852"',
            'Zalando-Client-Id' :	'"de04a38f-81e9-410b-b652-fc8c71c1c72f"'
        }
        
        
        s.cookies.update(cookies)'''
        s.headers.update(headers)
        sensor_3 = {"sensor_data":"7a74G7m23Vrp0o5c9180561.62-1,2,-94,-100,Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0,uaend,11059,20100101,fr,Gecko,1,0,0,0,393141,9579124,1536,824,1536,864,1536,415,1550,,cpen:0,i1:0,dm:0,cwen:0,non:1,opc:0,fc:1,sc:0,wrc:1,isc:73.5999984741211,vib:1,bat:0,x11:0,x12:1,5567,0.11954543559,798914789561.5,loc:-1,2,-94,-101,do_en,dm_en,t_dis-1,2,-94,-105,0,-1,0,0,1103,1103,0;1,-1,0,0,1466,1466,0;-1,2,-94,-102,0,-1,0,0,1103,1103,1;0,-1,0,0,1466,1466,1;-1,2,-94,-108,0,1,36910,17,0,4,1103;1,1,37316,86,0,4,1103;2,2,37396,86,0,4,1103;3,2,37425,17,0,0,1103;4,1,41599,16,0,8,1466;5,1,41885,-2,0,8,1466;6,3,41886,-2,0,8,1466;7,2,41955,-2,0,8,1466;8,2,42076,16,0,0,1466;9,1,42377,-2,0,0,1466;10,3,42377,-2,0,0,1466;11,2,42458,-2,0,0,1466;12,1,42693,-2,0,0,1466;13,3,42693,-2,0,0,1466;14,2,42759,-2,0,0,1466;15,1,42848,-2,0,0,1466;16,3,42849,-2,0,0,1466;17,1,61541,8,0,0,1466;18,2,61566,8,0,0,1466;19,1,62293,16,0,8,1466;20,1,62544,-2,0,8,1466;21,3,62544,-2,0,8,1466;22,2,62594,-2,0,8,1466;23,2,62846,16,0,0,1466;-1,2,-94,-110,0,1,1417,807,10;1,1,1432,712,40;2,1,1451,573,86;3,1,1469,496,114;4,1,1550,334,184;5,1,1666,328,213;6,1,1701,338,214;7,1,1783,446,206;8,1,1800,471,201;9,1,1815,506,194;10,1,1836,524,192;11,1,1849,545,191;12,1,1875,554,191;13,1,1886,562,191;14,1,1898,568,192;15,1,1915,572,194;16,1,1932,581,198;17,1,1948,585,202;18,1,1970,591,206;19,1,1982,598,210;20,1,1999,599,210;21,1,2015,601,212;22,1,2048,601,213;23,1,2132,601,212;24,1,2149,601,211;25,1,2165,598,211;26,1,2182,578,209;27,1,2201,567,208;28,1,2217,530,206;29,1,2231,489,206;30,1,2248,458,210;31,1,2269,430,212;32,1,2282,392,218;33,1,2301,373,222;34,1,2316,356,226;35,1,2332,350,228;36,1,2348,347,229;37,1,2366,346,229;38,1,2415,347,229;39,3,3393,347,229,-1,3;40,4,3406,347,229,-1,3;41,1,4099,342,290;42,1,4192,333,381;43,1,4276,335,386;44,1,4299,338,390;45,1,4562,347,400;46,1,5263,406,432;47,1,5268,417,415;48,1,5316,630,188;49,1,5365,642,182;50,1,5443,642,185;51,1,5532,638,190;52,1,5648,635,194;53,1,5699,634,195;54,1,5732,634,196;55,1,5749,634,196;56,1,5799,633,196;57,3,5822,633,196,1103;58,4,5954,633,196,1103;59,2,5955,633,196,1103;60,1,8170,632,197;61,1,8183,627,198;62,1,8199,624,200;63,1,8215,622,200;64,1,8233,622,200;65,1,8296,622,199;66,1,8344,622,198;67,3,8365,622,198,1103;68,4,8400,622,198,1103;69,2,8400,622,198,1103;70,1,8965,616,202;71,1,8981,591,220;72,1,9016,497,315;73,1,9032,442,382;74,1,9043,430,402;75,1,19124,642,411;76,1,19132,650,377;77,1,19150,652,350;78,1,19166,652,328;79,1,19183,650,298;80,1,19198,650,286;81,1,19216,650,278;82,1,19233,650,275;83,1,19248,649,274;84,1,19266,648,274;85,1,19282,647,274;86,1,19315,645,274;87,1,19332,638,276;88,1,19349,634,276;89,1,19365,630,275;90,1,19382,624,273;91,1,19399,622,271;92,1,19415,622,271;93,1,19432,622,270;94,1,19465,622,269;95,1,19482,621,267;96,1,19499,621,262;97,1,19515,620,259;98,1,19532,620,255;99,1,19549,620,252;100,1,19565,620,249;101,1,19582,619,242;102,1,19599,618,238;103,1,19615,618,232;104,1,19632,617,229;105,1,19649,617,225;106,1,19665,617,221;107,1,19682,617,218;145,3,36268,736,200,1103;146,4,36346,736,200,1103;147,2,36346,736,200,1103;192,3,38774,591,291,1466;193,4,38829,591,291,1466;194,2,38829,591,291,1466;265,3,50254,867,354,-1;266,4,50473,867,354,-1;267,2,50473,867,354,-1;398,3,57586,953,370,-1;399,4,57801,953,370,-1;400,2,57801,953,370,-1;459,3,60563,557,375,1466;460,4,60994,557,375,1466;461,2,60994,557,375,1466;581,3,71275,869,435,-1;-1,2,-94,-117,-1,2,-94,-111,-1,2,-94,-109,-1,2,-94,-114,-1,2,-94,-103,3,1108;1,1125;2,6502;3,8373;2,10008;3,36271;2,47385;3,50255;2,66229;-1,2,-94,-112,https://www.zalando.fr/login?target=%2Fwishlist%2F-1,2,-94,-115,1169816,1869844,32,0,0,0,3039627,71275,0,1597829579123,53,17093,24,582,2848,17,0,71276,2891259,0,B5CDF9F2189AC166430F432BC127478E~-1~YAAQV6E1VHlA1QB0AQAA0XMRBgSvUm0Jwm4g5o6XSHkFuA+9w8Qr0j3RPi2v7RgiVdEN+OsUsmSKKJHaY4J9f5g6YBcmm6MWa8jXlNx71Q7Ut3HSL+RKaJZKuctshYuMSE8r55vG/1Rwcs/gvF5V6kK0ufbyMuzthdHA4Ck+vJHdIwzVMyOqTW217sNPE/t1GqvJ9ke4fDLmTHgFDo26munZYJjXKvlkQkDZYgeefIVXithY7oyAgT7zWd7jsa1ETm9iilm4qtR6DAtmhT00YuCSnxKXNaPw5g7Sd+0u4KdTYc59hNwc4DtIm1Y0rSFYnCktF7mX8IOQNi4EIGPy8pn/zBQ=~-1~-1~-1,32169,659,-216009373,26067385,PiZtE,80813,49-1,2,-94,-106,1,10-1,2,-94,-119,400,0,200,0,400,200,400,400,200,200,200,1600,1400,200,-1,2,-94,-122,0,0,0,0,1,0,0-1,2,-94,-123,-1,2,-94,-124,-1,2,-94,-126,-1,2,-94,-127,11133333331333333333-1,2,-94,-70,1436327638;1247333925;dis;,3;true;true;true;-120;true;24;24;true;false;unspecified-1,2,-94,-80,6550-1,2,-94,-116,143686863-1,2,-94,-118,239082-1,2,-94,-121,;3;14;0"}

        r=s.post(url_login, json=sensor_3)
        print(r)

        
        headers = {
            'Accept' : 'application/json',
            'Accept-Encoding' : 'gzip, deflate, br',
            'Accept-Language' : 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
            'Connection' : 'keep-alive',
            'Content-Type' :'application/json',
            #'Cookie' : 'Zalando-Client-Id=de04a38f-81e9-410b-b652-fc8c71c1c72f; _abck=B5CDF9F2189AC166430F432BC127478E~-1~YAAQV6E1VLJA1QB0AQAAjZoRBgQ+U0mHhunWtMRxRNdLNuzmqFjlYoszI1ZeIxktFq5AHGwUSG+ul7+vRPk1mPOAlAgTfx4yQInF4CcbybcJZx0Avb3J3528ZjWCKstkD9MjtGr2E6rb5hgy02lAbDkaV+7PQak7CCdHhhsYGslv/eHVydzfEbZt/JQmT2IQQQGjf+rNkQR9K43wbWQSJ8D5+5xrF9w5IbYeUZmJYO5jUYolTP8lPdbS8yhguCCfa6nO/iTa3FL6UYf1VN9vIJ+CJLpfxosOEPotzxMyE1qkSKkkcXN1uxeWdRj9WWoN7Ngo7mqlvflGnwhARdTW/bZAIR0=~-1~-1~-1; _gcl_au=1.1.164078372.1591700050; CUSTOMER=GzMrtc9tEOfZ…000C5F13C5F30B75376~plYiwWJeA9WBju7XcIOE+9mHq5hH0/ZNzhfHEXxHbZ/qDwHsxkTLFaqIFZL/Ihh1UxqzGOqq07euW+8b6XzuPUb459AjcRVXHrifAqhGIbb0dBf5QXulCLm5Il6zb/Y1ocuasiuEYRyZIyFAXX0XXizyPKRoK2cxAnqOWEVLeTQe7vS6lwPIFdXse1zCQ2uOf+WInFDWRlCmwWLsPqcNWXfvthEwsR3CHPniceGql+N27hR6JvjTtz7Ebg05GATbrS; bm_sz=55BB5E45588C818DD6BF0A956B6AC9AE~YAAQV6E1VAU91QB0AQAAimoQBgh3sbFzOSHfnF6alvitxiz5CBO/J/eW2+crnOPe1oRgec/r5rSq7VE/h3Xy5KdYvI300DSE7PGJ/Zeg+Fk4Ivie/Cij13+xesmA/coTD4pK0CkjwWNNwHHcLhQ4Q7NtU+RFjT17r99QPh9/Rv2vOUqScFTdoWc5ahdGr0w=',
            'Host' : 'www.zalando.fr',
            'If-None-Match' :'W/"18d-nJvMn2d3brYtlyEJaBvaJarW5YA"',
            'Referer' : 'https://www.zalando.fr/login?target=%2Fwishlist%2F',
            'TE' : 'Trailers',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
            'x-flow-id' : 'Up45myfvtlH6Czzv',
            'x-xsrf-token' : 'AAAAALzf5KjvJEr5u--qE5jNbctPpd5CYmwkDgqA7dyw239wPN8tX9SwKmN_4KgebWqoYC9kbFkvxRtKHKWaK-lrcctwA1NZhvuGqG1oZ1TGOXjCFrI6BRNNUmOYDpve35kj7OIR3li2iayv7RY7U6Q=',
            'x-zalando-client-id' : 'de04a38f-81e9-410b-b652-fc8c71c1c72f',
            'x-zalando-redirect-target' : 'http://www.zalando.fr/wishlist/',
            'x-zalando-render-page-uri' : '/login?target=%2Fwishlist%2F',
            'x-zalando-request-uri' : '/login?target=%2Fwishlist%2F',
        }

        s.headers.update(headers)
        r=s.get('https://www.zalando.fr/api/reef/login/schema')
        print(r)

        headers = {
            'Host': 'www.zalando.fr',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
            'Accept': '*/*',
            'Accept-Language' : 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding' : 'gzip, deflate, br',
            'Content-Type' : 'text/plain;charset=UTF-8',
            'Content-Length': '280',
            'Origin': 'https://www.zalando.fr',
            'Connection' : 'keep-alive',
            'Referer' : 'https://www.zalando.fr/login?target=%2Fwishlist%2F',
            #Cookie: Zalando-Client-Id=de04a38f-81e9-410b-b652-fc8c71c1c72f; _abck=B5CDF9F2189AC166430F432BC127478E~-1~YAAQV6E1VLJA1QB0AQAAjZoRBgQ+U0mHhunWtMRxRNdLNuzmqFjlYoszI1ZeIxktFq5AHGwUSG+ul7+vRPk1mPOAlAgTfx4yQInF4CcbybcJZx0Avb3J3528ZjWCKstkD9MjtGr2E6rb5hgy02lAbDkaV+7PQak7CCdHhhsYGslv/eHVydzfEbZt/JQmT2IQQQGjf+rNkQR9K43wbWQSJ8D5+5xrF9w5IbYeUZmJYO5jUYolTP8lPdbS8yhguCCfa6nO/iTa3FL6UYf1VN9vIJ+CJLpfxosOEPotzxMyE1qkSKkkcXN1uxeWdRj9WWoN7Ngo7mqlvflGnwhARdTW/bZAIR0=~-1~-1~-1; _gcl_au=1.1.164078372.1591700050; CUSTOMER=GzMrtc9tEOfZpFAyxieacLhWylFaA1x8G7aAkL5vDn4VJm8bMDP7rUir5p66F6WKZpsF89+7XkW4rKJFjbPEcc8LUwWWAOuvp/tYCmf1bQyKRM9z4Wm2IAlzk7kbXdf5t7iCJuexH593yb5f/xPHw8+A9WyAvIq5GFO0g6Nk0gQhSt2VwzaoPIt4Ob0A8xYs+RLzUiYg6TqsPEO4u0b6+BUmbxswM/utUcqlNthTxRA=; ncx=m; _ga=GA1.2.694087826.1592574834; sqt_cap=1597789930852; frsx=AAAAALzf5KjvJEr5u--qE5jNbctPpd5CYmwkDgqA7dyw239wPN8tX9SwKmN_4KgebWqoYC9kbFkvxRtKHKWaK-lrcctwA1NZhvuGqG1oZ1TGOXjCFrI6BRNNUmOYDpve35kj7OIR3li2iayv7RY7U6Q=; mpulseinject=false; ak_bmsc=1136AE0DFD7F7AF5DFF4B6B11FC5FE5F5435A157AF530000C5F13C5F30B75376~plYiwWJeA9WBju7XcIOE+9mHq5hH0/ZNzhfHEXxHbZ/qDwHsxkTLFaqIFZL/Ihh1UxqzGOqq07euW+8b6XzuPUb459AjcRVXHrifAqhGIbb0dBf5QXulCLm5Il6zb/Y1ocuasiuEYRyZIyFAXX0XXizyPKRoK2cxAnqOWEVLeTQe7vS6lwPIFdXse1zCQ2uOf+WInFDWRlCmwWLsPqcNWXfvthEwsR3CHPniceGql+N27hR6JvjTtz7Ebg05GATbrS; bm_sz=55BB5E45588C818DD6BF0A956B6AC9AE~YAAQV6E1VAU91QB0AQAAimoQBgh3sbFzOSHfnF6alvitxiz5CBO/J/eW2+crnOPe1oRgec/r5rSq7VE/h3Xy5KdYvI300DSE7PGJ/Zeg+Fk4Ivie/Cij13+xesmA/coTD4pK0CkjwWNNwHHcLhQ4Q7NtU+RFjT17r99QPh9/Rv2vOUqScFTdoWc5ahdGr0w=
            'TE': 'Trailers'
        }
        s.headers.update(headers)
        r= s.post(url_login)
        print(r)




        login_data = {"username": "nameb86952@icanav.net", "password": "Dubai007", "wnaMode": "modal"}
        r= s.post('https://www.zalando.fr/api/reef/login', json=login_data)
        print(r)
        
        #r= s.get('https://www.zalando.fr/myaccount')
        #print(r.text)
        

urllib3.disable_warnings()
connexion()