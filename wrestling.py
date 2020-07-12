#############################################################################
# Author: Chelsea Marie Hicks
# OSU Email: hicksche@oregonstate.edu
# Course number/section: CS 325-401
# Assignment: Homework 5            Due Date: May 10, 2020 by 11:59 PM
#
# Description: Program reads a text file from the command line that contains 
#       a number of wrestlers (n), a list of the wrestler names, the number
#       of rivalries (r), and a list of the rivalries by their names in pairs.
#       The program outputs to the terminal Yes if it is possible to designate
#       wrestlers as Babyfaces and Heels such that each rivalry is between
#       a Babyface and a Heel, and a list of the Babyface wrestlers and a list
#       of the Heels otherwise, if it is not possible, the output is No.
#############################################################################

import sys

#create a Wrestler class to hold the wrestler name and their rivals
class Wrestler:
    def __init__(self, name, rivals):
        self.name = name
        self.rivals = rivals

#function returns the list of rivals for a specific Wrestler
def findRivals(name, rivalries):
    rivalsList = []
    #go through every rivalry, split up the rivalry into each wrestler,
    #and then add each wrestler to the rivalsList
    for rivalry in rivalries:
        wrestler, rival = rivalry.split(' ')
        if wrestler == name:
            rivalsList.append(rival)
        if rival == name:
            rivalsList.append(wrestler)
        rivalsList = list(set(rivalsList))
    return rivalsList

def main():
    #set variable as the command line input for the filename to be opened
    inputFile = sys.argv[1]

    #open inputFile entered in command line 
    readFile = open(inputFile, "r")
    
    #create empty lists to hold wrestlers, wrestler objects, rivalries, babyfaces, 
    #and heels
    wrestlerList =[]
    wrestlers = []
    rivalries = []
    babyfaces = []
    heels = []

    #set number of wrestlers from first line of inputFile read in
    numWrestlers = int(readFile.next())
    
    #insert wrestlers into wrestler list
    for i in range(numWrestlers):
        wrestlerList.append(readFile.next().strip())
    
    #set number of rivalries from line of inputFile read in
    numRivalries = int(readFile.next())

    #insert rivalries into rivalries list 
    for i in range(numRivalries):
        rivalries.append(readFile.next().strip())
    
    #identify the rivals for each wrestler and create object with this information and
    #add wrestler object to wrestlers
    for wrestler in wrestlerList:
        rivals = findRivals(wrestler, rivalries)
        wrestlerObject = Wrestler(wrestler, rivals)
        wrestlers.append(wrestlerObject)
    
    #used to ensure first wrestler is added to babyface
    start = True

    #place wrestlers in babyfaces and heels
    for wrestler in wrestlers:
        #first wrestler is set to babyfaces and all rivals of that wrestler are
        #set to heels to meet main objective
        if start:
            babyfaces.append(wrestler.name)
            rivals = wrestler.rivals
            for rival in rivals:
                heels.append(rival)
            start = False
        #if not the first wrestler, check each of the rivals for the wrestler and
        #place the rivals in the opposite group from the wrestler if not already
        #in that group. Otherwise, add the wrestler to babyfaces and their rivals to
        # heels
        else:
            rivals = wrestler.rivals
            for rival in rivals:
                if wrestler.name in babyfaces:
                    if rival not in heels:
                        heels.append(rival)
                
                elif wrestler.name in heels:
                    if rival not in babyfaces:
                        babyfaces.append(rival)
                
                else:
                    babyfaces.append(wrestler.name)
                    for rival in rivals:
                        if rival not in heels:
                            heels.append(rival)
    
    #check if this construction is possible by checking if there are any wrestlers
    #appearing in both lists. If there are, then this isn't possible
    isPossible = True
    for heel in heels:
        if heel in babyfaces:
            isPossible = False
    
    for babyface in babyfaces:
        if babyface in heels:
            isPossible = False
    
    #output to screen whether it is possible or not. If it is possible, also print
    #the list in babyfaces and the list in heels
    if isPossible:
        print('Yes, this is possible!')
        babyfacesOutput = ''
        heelsOutput = ''

        for babyface in babyfaces:
            babyfacesOutput = babyfacesOutput + babyface + ' '
        print('Babyfaces: %s' % babyfacesOutput)

        for heel in heels:
            heelsOutput = heelsOutput + heel + ' '
        print('Heels: %s' % heelsOutput)

    else:
        print("No, this is impossible.")


main()