from typing import List
import winsound 
from playsound import playsound
import time


#input a string
inputRhytmkick = input("what rhytm would you like to use for this sequence (1 = 1/16, seperated by space) ? ")
print("\n")
rhytmkick = list(inputRhytmkick.split())
                #convert string to list for float value's
rhytmkickFloat=list(map(float,rhytmkick))
               






BPM = int(input("enter the bpm you want to use: "))
                # de tijdsduur in seconde voor 1 beat berekenen
oneBeatInSec = (60.0/BPM) 


                # een list met de tijdsduur van iedere noot wordt gevuld in de for loop
timeStamp16th = []

for i in rhytmkickFloat:
    timeStamp16th.append(oneBeatInSec*i)



print ("you chosen rythm in seconds:",timeStamp16th)

                #initialiseer sequencer
seqCounter = int (0)

startTime = time.time()






#seqCounter telt op wanneer deze met de de tijd van timestamp16th gelijk is
while seqCounter < (len(rhytmkick)):
 
    #vergelijkt de huidigetijd met de tijd van timeStamp16th array tov startTime
    if time.time() >= startTime + (oneBeatInSec * timeStamp16th[seqCounter] ):
        print("KICK", seqCounter + 1)
        #speel de sound af + sequence stap verder + nieuwe starttime ophalen
        playsound("samples\\KickBeelow.wav",winsound.SND_ASYNC)
        seqCounter=seqCounter+1
        startTime = time.time()
    #anders doe maar even niks, om even uit te rusten
    else:
        time.sleep(0.001)

#laatste noot uit laten spelen
time.sleep(1)