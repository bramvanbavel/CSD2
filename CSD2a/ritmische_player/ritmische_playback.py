#Verwerk de volgende functionaliteiten in je programma:
#- Het script verwacht de volgende input vanuit de terminal:
#- Eén getal dat het aantal keren dat de sample wordt afgespeeld bepaalt, dit noemen we
#voor nu even “numPlaybackTimes”.
#- Vervolgens worden er numPlaybackTimes regels ingevoerd met op elke regel één getal
#als input. Deze input vormt het gegeven ritme.
#- Tot slot volgt er nog één regel met één getal, dit is de gebruikte BPM voor het afspelen
#Een voorbeeld van de te verwachten input:
#4
#1
#0.5
#1.5
#0.5
#120
#imprteer de juiste libraries
import winsound
from playsound import playsound
import time


 ## input 1 --- playback times ##

numPlaybackTimes = int (input("enter the number (1,2,3, etc) of times you want to play the sample:"))

## input 2 --- Rhytm in a list ##

                #string for asking the value's
inputRhytm = input("enter the playback rhytm for each sample seperated by space: " ) 
print("\n")
                #converting string in list
rhytmList = list(inputRhytm.split())
                #convert to list for float value's
rhytmListFloat=list(map(float,rhytmList))
                #print list for check
print("your chosen rhytm as float with <.> :", rhytmListFloat)

## input 3 --- BPM
 
BPM = int(input("enter the bpm you want to use: "))
oneBeatInSec = (60.0/BPM)
print("one beat in seconds:", oneBeatInSec)


                ## value for the sequence counter
seqCounter = int (0)

## iterating the beat in a for-loop
print("LETS PLAY THIS BEAT!")

for i in rhytmListFloat:

        
        noteDur = oneBeatInSec*(rhytmListFloat[seqCounter])
       
        playsound("samples\\KickBeelow.wav",winsound.SND_ASYNC)

        time.sleep(noteDur)
        seqCounter = seqCounter + 1
        print("step" , seqCounter)

