from typing import  List
import simpleaudio as sa
import time
import random
from midiutil import MIDIFile

kick            = sa.WaveObject.from_wave_file("samples\\KickBeelow.wav")
snare           = sa.WaveObject.from_wave_file("samples\\SM_SW_Clap_snare_04.wav")
hat             = sa.WaveObject.from_wave_file("samples\\SM_SW_Hat_15.wav")



ChosenBeatKick  = [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0]           #actual played position kick (0 will not be played)
ChosenBeatSnare = [0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0]           #actual played position snare(0 will not be played)
ChosenBeatHat   = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

sequenceKick    = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]           #list with possibilities for the(lenght is the loop)
sequenceSnare   = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]           
sequencehat     = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]           

stamp           = []                                          #list with sample an dedicated index
timeStamps      = []                                          #list for each calculated timestamp
samples         = ['kick ','snare','hat  ']                   #list for actual samples with path
mf              = MIDIFile(1) 
track           = 0
times           = 0



while True:
    try:
        Loop                = int(input("enter amount of loops   (integer number): "))        #input loop number to keep count of the loop    
        bpm                 = int(input("enter the bpm           (integer number): "))               #input bpm number 
        swingChoice         = int(input("enter setting for swing (integer number): 0=manual 1=randomly generated "))
       
        if (swingChoice>0):
            swingPercetage  = random.randint(50,75)
            print ("swing is", swingPercetage,"%")
        else:           
            swingPercetage  = float(input("add swing as (float or integer number) in percentage example: 50, 57, 66, 75 etc.:"))
            print("")

    except ValueError:
            print("Sorry, I didn't understand one of the values. try again")
            print("now you have to fill in all values again, goodluck")
            #better try again... Return to the start of the loop
            continue
    else:
        if (swingPercetage<50 or swingPercetage> 75):
            print("thas a weird swing, please add swing between 50 and 75")
            print("now you have to fill in all values again, goodluck")
        else:
            print("input was successfully parsed!, lets make a loop!")
        #we're ready to exit the loop.
            break

sixteenthInMs   = (60.0/bpm)/4                                #calculate bpm to ms
endOfLoop       = float((len(sequencehat))*sixteenthInMs)             
swingcalculated = (((swingPercetage-50)*2)/100)               #makes from swing percentage input a number to multiply with time or position of a note
swingAsTime     = sixteenthInMs*swingcalculated               #0=50%swing 0.25= 62.5%swing, 0.5= 75%swing


mf.addTrackName(track, times, "Python generated midi file")
mf.addTempo(track, times, bpm)                                


def SoundPosition(Sound,position):                            #create an event for the Soundlabel with dedicated index number
    return{
        "Sound"   : Sound,
        "position": position,
        }


def stampSample (sample, stamp):                              #create an event for each dedicated samplepath with calculated timestamp
      return{
        "sample": sample,
        "stamp" : stamp,
        } 


for index, item in enumerate(sequenceKick):                   #make a list off stamps with sample and its index
    if ChosenBeatKick[index] !=0 :                            #but only if possition is chosen
        stamp.append(SoundPosition("Kick",index))

for index, item in enumerate(sequenceSnare):
    if ChosenBeatSnare[index]!=0 :
        stamp.append(SoundPosition("Snare",index))

for index, item in enumerate(sequenceSnare):
    if ChosenBeatHat[index]!=0 :
        stamp.append(SoundPosition("Hat",index))



def timeStampEvent():                                                  #convert the stamps to timestamps with 16thInMs * INDEX
     for i in stamp:
         if i["Sound"] == "Kick" :
             timeStamps.append(stampSample(samples[0],i["position"]*sixteenthInMs))
             mf.addNote(0, 0, 60, (i["position"]/4), 0.25, 127)        # add this kick to midi sequence


         if i["Sound"] == "Snare":
             timeStamps.append(stampSample(samples[1],i["position"]*sixteenthInMs))
             
             mf.addNote(0, 0, 59, (i["position"]/4), 0.25, 127)        # add this snare to midi sequence

         if i["Sound"] == "Hat":
                      
             if (i["position"]%2==0):
                    timeStamps.append(stampSample(samples[2],i["position"]*sixteenthInMs))  
                    mf.addNote(0, 0, 58, (i["position"]/4), 0.25, 127)        # add this kick to midi sequence
             else:
                    timeStamps.append(stampSample(samples[2],(i["position"]*sixteenthInMs)+ swingAsTime))  
                    mf.addNote(0, 0, 58, (i["position"]/4)+(0.25*swingcalculated), 0.25, 127) 
         

 

timeStampEvent()                                                       #call function before starting the loop

with open("YourBeat.mid",'wb') as outf:                                # create midi file
    mf.writeFile(outf)  

startTime       = time.time() 
startTimeLoop   = time.time() - startTime                            #define startpoint of the sequenceKick in time
currentTime     = time.time() - startTime

while Loop >= 1:

    
    currentTime = time.time() - startTime

    for i in timeStamps:
            if (currentTime >= i["stamp"]):                            # when currenttime > timestamp of this iteration
                if i["sample"] == 'kick ':                             # when sample is kick: PLAY KICK
                    kick.play()
                    print(i)                     
                    timeStamps.remove(i)                               # clear list to keep count

                if i["sample"] == 'snare':                             # when sample is Snare: PLAY SNARE
                    snare.play()
                    print(i)
                    timeStamps.remove(i)                               # clear list to keep count 

                if i["sample"] == 'hat  ':                             # when sample is Snare: PLAY HAT
                    hat.play()
                    print(i)
                    timeStamps.remove(i)                               # clear list to keep count 

                if (timeStamps==[]):                                   # when list is empty 
                    Loop = Loop-1                                      # now the first loop is over 
                    timeStampEvent()                                   # call the timestamp functin to fill list again
                    print("BAR-------------------------------------------------------------------")
                    time.sleep(endOfLoop-(i["stamp"]))                 # check if complete loop time has passed
                    startTime=time.time()                              # define new starttime
                    break                                              # end this loop
                
            else: 
                time.sleep(0.001) # sleepwell for 1ms algorhytm
           
print(endOfLoop)              
     

        
             
         

    