from typing import Counter, List
import simpleaudio as sa
import time
from midiutil import MIDIFile

kick            = sa.WaveObject.from_wave_file("samples\\KickBeelow.wav")
snare           = sa.WaveObject.from_wave_file("samples\\SM_SW_Clap_snare_04.wav")
hat             = sa.WaveObject.from_wave_file("samples\\SM_SW_Hat_15.wav")


ChosenBeatKick  = [1,0,0,0,1,0,0,0]                           #actual played position kick (0 will not be played)
ChosenBeatSnare = [0,0,0,0,1,0,0,0]                           #actual played position snare(0 will not be played)
ChosenBeatHat   = [1,1,1,1,1,1,1,1]

sequenceKick    = [1,1,1,1,1,1,1,1]                           #list with possibilities for the Kick (lenght is the loop)
sequenceSnare   = [1,1,1,1,1,1,1,1]
sequencehat     = [1,1,1,1,1,1,1,1]                           #list with possibilities for the Snare(lenght is the loop)

stamp           = []                                          #list with sample an dedicated index
timeStamps      = []                                          #list for each calculated timestamp
samples         = ['kick ','snare','hat  ']                      #list for actual samples with path
Loop            = int(input("enter how many loops: "))        #input loop number to keep count of the loop    
bpm             = int(input("enter the bpm: "))               #input bpm number
sixteenthInMs   = (60.0/bpm)/2                                #calculate bpm to ms 
endOfLoop       = (len(sequencehat)+1)*sixteenthInMs
Counter         = 1



mf = MIDIFile(1) 
track = 0

times = 0

mf.addTrackName(track, times, "Beat Sample Track")
mf.addTempo(track, times, bpm)#(track,time,tempo)  


def SoundPosition(Sound,position):                            #create an event for the Sound with dedicated index
    return{
        "Sound"   : Sound,
        "position": position,
        }


def stampSample (sample, stamp):                              #create an event for each timestamps with dedicated sample
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



def timeStampEvent():                                         #convert the stamps to timestamps with 16thInMs * INDEX
     for i in stamp:
         if i["Sound"] == "Kick" :
             timeStamps.append(stampSample(samples[0],i["position"]*sixteenthInMs))
             mf.addNote(0, 0, 60, i["position"], 1, 127) # add kick to midi sequence

         if i["Sound"] == "Snare":
             timeStamps.append(stampSample(samples[1],i["position"]*sixteenthInMs))
             mf.addNote(0, 0, 59, i["position"], 1, 127) # add snare to midi sequence

         if i["Sound"] == "Hat":
             timeStamps.append(stampSample(samples[2],i["position"]*sixteenthInMs))          
             mf.addNote(0, 0, 58, i["position"], 1, 127)# add hat to midi sequence


timeStampEvent()                                             #call function before starting the loop


startTimeLoop=time.time()
startTime = time.time()                                      #define 0 point of the sequenceKick in time
currentTime = time.time() - startTime

while Loop >= 1:

    
    currentTime = time.time() - startTime

    for i in timeStamps:
            if (currentTime >= i["stamp"]):                 # when currenttime > timestamp of this iteration
                if i["sample"] == 'kick ':                   # when sample is kick: PLAY KICK
                    kick.play()
                    print(i)                     
                    timeStamps.remove(i)                    # clear list to keep count

                if i["sample"] == 'snare':                  # when sample is Snare: PLAY SNARE
                    snare.play()
                    print(i)
                    timeStamps.remove(i)                    # clear list to keep count 

                if i["sample"] == 'hat  ':                  # when sample is Snare: PLAY HAT
                    hat.play()
                    print(i)
                    timeStamps.remove(i)                    # clear list to keep count 

                if (timeStamps==[]):                        # when list is empty 
                   if (currentTime <=startTimeLoop+endOfLoop*Counter): #time.sleep (sixteenthInMs)                  # wait for last kick to finish (need calculatiom when mo samples)
                    Loop = Loop-1
                    Counter=Counter+1                           # now the first loop is over 
                    print("BAR-------------------------------------------------------------------")
                    timeStampEvent()                        # call the timestamp functin to fill list
                    startTime=time.time()                   # define new starttime
                    break                                   # end this loop
                
            else: 
                time.sleep(0.0001)
           
            
                   
     

with open("symphony.mid",'wb') as outf:
    mf.writeFile(outf)           
             
         

    