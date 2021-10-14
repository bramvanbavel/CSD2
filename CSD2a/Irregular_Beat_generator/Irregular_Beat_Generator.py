from typing import List
import simpleaudio as sa
import time

#initialiseer de samples
kickSample = sa.WaveObject.from_wave_file("samples\\KickBeelow.wav")
snareSample = sa.WaveObject.from_wave_file("samples\\SM_SW_Clap_snare_04.wav")
hatSample = sa.WaveObject.from_wave_file("samples\\SM_SW_Hat_04.wav")

# input voor de lengte van de loop(maatsoort)
seqCounterLongest = int(input("what rhytm would you like to use, enter a number(1=1/16)"))
print("\n")
#input a string for the kick 
inputRhytmkick = input("what rhytm would you like to use for the kick (1 = 1/16, seperated by space) ? ")
print("\n")
rhytmKick = list(inputRhytmkick.split()) #convert string to list for float value's
rhytmkickFloat=list(map(float,rhytmKick))
#input a string for the snare        
inputRhytmSnare =input("what rhytm would you like to use for the snare (1 = 1/16, seperated by space) ? ")
print("\n")
rhytmSnare = list(inputRhytmSnare.split()) #convert string to list for float value's
rhytmSnareFloat=list(map(float,rhytmSnare))
#input a string for the hat
inputRhytmHat =input("what rhytm would you like to use for the hat (1 = 1/16, seperated by space) ? ")
print("\n")
rhytmHat = list(inputRhytmHat.split()) #convert string to list for float value's
rhytmHatFloat=list(map(float,rhytmHat))




### now we have 3 list's with timestamps of the diffrent samples ###

Loopings = int(input("how many time's do you want to loop this beat? (enter a number)"))
print("\n")

#input the BPM
BPM = int(input("enter the bpm you want to use: "))
# de tijdsduur in seconde voor 1 beat berekenen (float)
oneBeatInSec = (60.0/BPM) 



# een lege list voor de timestamps van iedere sample 
timeStampKick = []
timeStampSnare = []
timeStampHat = []




#vul de list's met timestamps
for i in rhytmkickFloat:
    timeStampKick.append(oneBeatInSec*i)
timeStampKick.append(len(rhytmkickFloat))
for i in rhytmSnareFloat:
    timeStampSnare.append(oneBeatInSec*i)
timeStampSnare.append(len(rhytmSnareFloat))
for i in rhytmHatFloat:
    timeStampHat.append(oneBeatInSec*i)
timeStampHat.append(len(rhytmHatFloat))


#functie die wordt aangeroepen als de sample moet word afgespeeld
def kickPlay():
    kickSample.play()
    
def snarePlay():
    snareSample.play() 

def hatPlay():
    hatSample.play()





while(Loopings>=0):
    #initialiseer sequencer
    seqCounterKick  = 0
    seqCounterSnare = 0
    seqCounterHat   = 0
    
    #zet de start tijd op 0
    startTimeKick  = time.time()
    startTimeSnare = time.time()
    startTimeHat   = time.time()
    startTimeLoop  = time.time()

    Loopings=Loopings-1
    print("\n")
    #seqCounter telt op wanneer deze met de de tijd van timestamp16th gelijk is
    while (startTimeLoop+(oneBeatInSec*seqCounterLongest-1)>= time.time() ):

            #vergelijkt de huidigetijd met de tijd van timeStampKick array tov startTime
            if time.time() >= startTimeKick + (oneBeatInSec * timeStampKick[seqCounterKick])and (seqCounterKick)<(timeStampKick[-1]):
                if seqCounterKick-1!=(timeStampKick[-1]):
                    kickPlay()
                    print("KICK", seqCounterKick + 1)#speel de sample af + sequence stap verder + nieuwe starttime ophalen
                    seqCounterKick=seqCounterKick+1
                    startTimeKick = time.time()
                else:
                    break

            #vergelijkt de huidigetijd met de tijd van timeStampSnare array tov startTime
            if time.time() >= startTimeSnare + (oneBeatInSec * timeStampSnare[seqCounterSnare])and (seqCounterSnare)<(timeStampSnare[-1]):
                if seqCounterSnare-1!=(timeStampSnare[-1]):
                    snarePlay()
                    print("SNARE", seqCounterSnare + 1)#speel de sound af + sequence stap verder + nieuwe starttime ophalen
                    seqCounterSnare=seqCounterSnare+1
                    startTimeSnare = time.time()
                else:
                    break


            #vergelijkt de huidigetijd met de tijd van timeStampSnare array tov startTime
            if time.time() >= startTimeHat + (oneBeatInSec * timeStampHat[seqCounterHat])and (seqCounterHat)<(timeStampHat[-1]):
                    if seqCounterHat-1!=(timeStampHat[-1]):
                        hatPlay()
                        print("HAT", seqCounterHat + 1)#speel de sound af + sequence stap verder + nieuwe starttime ophalen
                        seqCounterHat=seqCounterHat+1
                        startTimeHat = time.time()
                    else:
                        break
                
                    
            #anders doe maar even niks, om even uit te rusten
            else:
                time.sleep(0.001)