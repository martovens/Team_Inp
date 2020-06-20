import time, os

#Setup
def check_Input(): #literally in the name
    global final_Input #used as official team ID if processed properly

    if len(teamID_Input) > 12: # too long
        os.system('cls') #clear screen
        print("Too long\n")
        getTeamID()
    if len(teamID_Input) < 12: #too short
        os.system('cls') #clear screen
        print("Too short\n")
        getTeamID()
    if len(teamID_Input) == 12 :# just right
        os.system('cls') #clear screen
        print("Passing string...")
        final_Input = str(teamID_Input) #send as official team ID

def getTeamID(): #prompt
    global teamID_Input
    teamID_Input = "" #Restart prompt
    teamID_Input = input("Team ID (Must be 12 Characters): ")
    check_Input() #check input


#Main Stuff
getTeamID() #inital prompt


#Testing
print("Team ID: ", final_Input)












#Testing
time.sleep(5)
