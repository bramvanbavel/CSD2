from typing import  List
import simpleaudio as sa
import time
import random
from midiutil import MIDIFile

kick            = sa.WaveObject.from_wave_file("samples\\KickBeelow.wav")
snare           = sa.WaveObject.from_wave_file("samples\\SM_SW_Clap_snare_04.wav")
hat             = sa.WaveObject.from_wave_file("samples\\SM_SW_Hat_15.wav")

print("---------------------------------------------------------------------------------------------------")
print("this is a algorhytm that will play samples as a sequencer, made by Bram van Bavel")
print("Read carefully what kind of information the program will ask you to input. ")
print("if you make a mistake with the input, the algorhytm will start from the begin")
print("when the algorhytm is done, there is a .mid file of you loop ready in the project directory")
print("---------------------------HAVE FUN AND SPREAD LOVE------------------------------------------------")

sequenceKick    = []                                          #list with possibilities for the(lenght is the loop)
sequenceSnare   = []           
sequenceHat     = []
stamp           = []                                          #list with sample an dedicated index
timeStamps      = []                                          #list for each calculated timestamp
samples         = ['kick ','snare','hat  ']                   #list for actual samples with path
mf              = MIDIFile(1) 
track           = 0
times           = 0



while True: # INPUT LOOP
    try:

        print("would you like  to make pattern yourself or do you want to use one of the presets? ")
        print("yourself=> 1  preset=  0 (input integer)")
        patternChoice = int(input()) 


        if patternChoice > 0:
            print("what is the first digit of the timesignature that you would you like to use?(input integer)")
            timeSig1 = int(input()) 
            print("what is the second digit of the timesignaturethat you would like to use? 16 is the limit(input integer)")
            timeSig2 = int(input())

        if patternChoice == 0:
            print("there are 3 presets with different time signatures ready: 1=4/3 2=4/4 3=7/8, enter 1,2or3" )
            presetChoice = int(input())
            if presetChoice == 1:
                timeSig1 = 4 
                timeSig2 = 3
            if presetChoice == 2:
                timeSig1 = 4 
                timeSig2 = 4
            if presetChoice == 3:
                timeSig1 = 7 
                timeSig2 = 8

        print ("you timesignature is", timeSig1,"/",timeSig2) #calculate sequencelenth based on timesignature
        if timeSig2 == 2:
            timeSig2 = timeSig2*4     
        if timeSig2 == 8:
            timeSig2 = timeSig2/4
        if timeSig2 == 16:
            timeSig2 = timeSig2/16
        if timeSig2 >= 16:
            print("that number is to bigger then 16, now you have to fill in all values again, goodluck")
            print("")
            print("")
            print("")
            continue
        patternLength = int(timeSig1*timeSig2) 
  
            

            
        for i in range (0,patternLength): #fill this array  based on timesignature calculated lenght of the sequence
                sequenceKick.append(1)
        for i in range (0,patternLength):
                sequenceSnare.append(1)
        for i in range (0,patternLength):
                sequenceHat.append(1)

        
            
        if patternChoice >0:
                print ("you have to fill all",patternLength,"positions, if you dont't the program will restart")
                print ("what rhytm would you like to use for the kick (1=on and 0=off, seperated by space(input integer)) ? ")
                inputRhytmkick = (input())
                rhytmKick      =list(inputRhytmkick.split()) #convert string to list 
                ChosenBeatKick =list(map(int,rhytmKick))
                if (len(ChosenBeatKick)!= patternLength):    #when not every step is given a value the program restarts
                    print("you chose the time signature yourself, please fill it according")
                    continue
                
                print("what rhytm would you like to use for the snare(1 = on and 0 = off, seperated by space(integer)) ? ")
                inputRhytmsnare= (input())
                rhytmSnare     = list(inputRhytmsnare.split()) #convert string to list 
                ChosenBeatSnare=list(map(int,rhytmSnare))
                if (len(ChosenBeatSnare)!= patternLength):    
                    print("you choosse the time signature yourself, give a value to every step of the sequence")
                    continue

                print("what rhytm would you like to use for the hat  (1 = on and 0 = off, seperated by space(input integer)) ? ")
                inputRhytmhat  = (input())
                rhytmHat       = list(inputRhytmhat.split())   #convert string to list 
                ChosenBeatHat  =list(map(int,rhytmHat))
                if (len(ChosenBeatHat)!= patternLength):
                    print("you choosse the time signature yourself, give a value to every step of the sequence")
                    continue
        else:                                                                 # the preset rhytms
             if presetChoice == 1:# 4/3
                ChosenBeatKick  = [1,0,0,1,0,0,1,0,0,1,1,1]
                ChosenBeatSnare = [0,0,0,1,0,0,1,0,0,0,0,0]
                ChosenBeatHat   = [0,1,1,0,1,1,0,1,1,0,1,1]
             if presetChoice == 2:# 4/4
                ChosenBeatKick  = [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0]           #actual played position is 1, 0 will not be played
                ChosenBeatSnare = [0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0]         
                ChosenBeatHat   = [0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,1]
            
             if presetChoice == 3:# 7/8
                ChosenBeatKick  = [1,0,0,0,0,0,0,0,0,1,0,0,0,0]
                ChosenBeatSnare = [0,0,0,0,1,0,1,0,0,0,0,1,0,1]
                ChosenBeatHat   = [1,0,1,0,0,1,0,0,1,0,1,0,1,0]

        Loop                = int(input("enter amount of loops   (input integer): ")) #input loop number to keep count of the loop    
        bpm                 = int(input("enter the bpm           (input integer): ")) #input bpm number 
        swingChoice         = int(input("enter setting for swing (input integer): 0=manual 1>=randomly generated "))
       
        if (swingChoice>0): # function for generating a random swing between 50% and 70%
            swingPercetage  = random.randint(50,75)
            print           ("swing is", swingPercetage,"%")
            print           ("")
            
        else:               # manual input for swing
            print("add swing in percentage as number beteen 50 and 75 (input integer or float) ")          
            swingPercetage  = float(input())
            print("")

    except ValueError:      # if any input is not correct, run input loop again
            print("Sorry, I didn't understand one of the values.")
            print("now you have to fill in all values again, goodluck")
           
            continue
    else:
        if (swingPercetage<50 or swingPercetage> 75):
            print("thas a way to weird swing for me, please add swing between 50 and 75")
            print("now you have to fill in all values again, goodluck")
            print("")

            continue
        else:
            print("input was successfully parsed!, lets make a loop!")
            print("")
        #we're ready to exit the loop.
            break

sixteenthInMs   = (60.0/bpm)/4                                #calculate bpm to ms
endOfLoop       = patternLength*sixteenthInMs                 #calculate the timestamp of the end of the loop
swingcalculated = (((swingPercetage-50)*2)/100)               #makes from swing percentage input a number to multiply with time or position of a note
swingAsTime     = sixteenthInMs*swingcalculated               #0=50%swing 0.25= 62.5%swing, 0.5= 75%swing


mf.addTrackName(track, times, "Python generated midi file")   #create midi file
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

for index, item in enumerate(sequenceHat):
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
                      
             if (i["position"]%2==0):# when the index is even the stamp is placed on the grid
                    timeStamps.append(stampSample(samples[2],i["position"]*sixteenthInMs))  
                    mf.addNote(0, 0, 58, (i["position"]/4), 0.25, 127) # add this kick to midi sequence
             else:                   #when the index is odd shift it according to the given swingpercentage 
                    timeStamps.append(stampSample(samples[2],(i["position"]*sixteenthInMs)+ swingAsTime))  
                    mf.addNote(0, 0, 58, (i["position"]/4)+(0.25*swingcalculated), 0.25, 127) 
         

 

timeStampEvent()                                                       #call function before starting the loop

with open("YourBeat.mid",'wb') as outf:                                # create midi file
    mf.writeFile(outf)  

startTime       = time.time() 
startTimeLoop   = time.time() - startTime                            #define startpoint of individual loops and complete loop in time
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
     

        
             
         

    