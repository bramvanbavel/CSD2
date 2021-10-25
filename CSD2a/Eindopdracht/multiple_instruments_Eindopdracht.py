from typing import List
import simpleaudio as sa
import time

kick            = sa.WaveObject.from_wave_file("samples\\KickBeelow.wav")
snare           = sa.WaveObject.from_wave_file("samples\\SM_SW_Clap_snare_04.wav")
hat             = sa.WaveObject.from_wave_file("samples\\SM_SW_Hat_04.wav")


ChosenBeatKick  = [1,0,0,0,1,0,0,0]                           #actual played position kick (0 will not be played)
ChosenBeatSnare = [0,0,0,0,1,0,0,0]                           #actual played position snare(0 will not be played)
sequenceKick    = [1,1,1,1,1,1]                               #list with possibilities for the Kick (lenght is the loop)
sequenceSnare   = [1,1,1,1,1,1]                               #list with possibilities for the Snare(lenght is the loop)
stamp           = []                                          #list with sample index
timeStamps      = []                                          #list for each calculated timestamp
samples         = ['kick','snare','hat']                      #list for actual samples with path
Loop            = int(input("enter how many loops: "))        #input loop number to keep count of the loop    
bpm             = int(input("enter the bpm: "))               #input bpm number
bpmIn16th       = (60.0/bpm)/4                                #calculate bpm to ms 



def rhytmPosition(rhytm,position):                            #create an event for the rhytm with dedicated index
    return{
        "rhytm"   : rhytm,
        "position": position,
        }


def stampSample (sample, stamp):                              #create an event for each timestamps with dedicated sample
      return{
        "sample": sample,
        "stamp" : stamp,
        } 


for index, item in enumerate(sequenceKick):                   #make a list off stamps with sample and stamp
    if ChosenBeatKick[index] !=0 :
        stamp.append(rhytmPosition("Kick",index))

for index, item in enumerate(sequenceSnare):
    if ChosenBeatSnare[index]!=0 :
        stamp.append(rhytmPosition("Snare",index))



def timeStampEvent():                                         #convert the stamps to timestamps with bpmInMs
     for i in stamp:
         if i["rhytm"] == "Kick" :
             timeStamps.append(stampSample(samples[0],i["position"]*bpmIn16th))
     
         if i["rhytm"] == "Snare":
             timeStamps.append(stampSample(samples[1],i["position"]*bpmIn16th))
            


timeStampEvent()                                             #call function before starting the loop



startTime = time.time()                                      #define 0 point of the sequenceKick in time


while Loop >= 1:
    
    currentTime = time.time() - startTime

    for i in timeStamps:
            if (currentTime >= i["stamp"]):       # when currenttime > timestamp of this iteration
                if i["sample"] == 'kick':         # when sample is kick: PLAY KICK
                    kick.play()
                    print("kick")                     
                    timeStamps.remove(i)          # clear list to keep count

                if i["sample"] == 'snare':        # when sample is Snare: PLAY SNARE
                    snare.play()
                    print("snare")
                    timeStamps.remove(i)          # clear list to keep count 



                if (timeStamps==[]):             # when list is empty 
                    time.sleep (bpmIn16th)         # wait for last kick to finish (need calculatiom when mo samples)
                    Loop = Loop-1                # now the first loop is over 
                    print("BAR")
                    timeStampEvent()             # call the timestamp functin to fill list
                    startTime=time.time()        # define new starttime
                    break                        # end this loop
                
            else:
                time.sleep(0.001)
            
                   
             
            
             
         

    