from typing import List
import simpleaudio as sa
import time

kick            = sa.WaveObject.from_wave_file("samples\\KickBeelow.wav")
snare           = sa.WaveObject.from_wave_file("samples\\SM_SW_Clap_snare_04.wav")
hat             = sa.WaveObject.from_wave_file("samples\\SM_SW_Hat_04.wav")

sequence        = [1,2,2,2,2,2]     #list with positions for the sequence
stamp           = []                                    #list with sample index
timeStamps      = []                                    #list for each calculated timestamp
samples         = ['kick','snare','hat']                #list for actual samples with path
Loop            = int(input("enter how many loops: "))  #input loop number to keep count of the loop
bpm             = int(input("enter the bpm: "))         #input bpm number
bpmInMs         = (60.0/bpm)                            #calculate bpm to ms 


#create an event for each timestamps with dedicated sample
def stampSample (sample, stamp):
      return{
        "sample"   : sample,
        "stamp": stamp,
        } 

#create an event for the rhytm with dedicated positions
def rhytmPosition(rhytm,position):
    return{
        "rhytm"        : rhytm,
        "position"     : position,
        }


#make a list off stamps with sample and stamp
for index, item in enumerate(sequence):
    stamp.append(rhytmPosition("stamp_sample",index))


#convert the stamps to timestamps with bpmInMs

def timeStampEvent():
     for i in stamp:
         if i["rhytm"] == "stamp_sample":
             timeStamps.append(stampSample(samples[0],i["position"] * bpmInMs))
            


timeStampEvent()


print(timeStamps)

#define 0 point of the sequence in time
startTime = time.time()


while Loop >= 1:
    
    
    
    currentTime = time.time() - startTime

 
    for i in timeStamps:
            if (currentTime >= i["stamp"]): # when currenttime > timestamp of this iteration
                if i["sample"] == 'kick':        # when sample is kick
                    kick.play()
                    print("kick")
                    timeStamps.remove(i)         # clear list to keep count 


                if (timeStamps==[]):             # when list is empty 
                    time.sleep (bpmInMs)         # wait for last kick to finish (need calculatiom when mo samples)
                    Loop = Loop-1                # now the first loop is over 
                    print("BAR")
                    timeStampEvent()             # call the timestamp functin to fill list
                    startTime=time.time()        # define new starttime
                    break                        # end this loop

            else:
                time.sleep(0.001)
            