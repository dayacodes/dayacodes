import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk
from Dealer import Dealer
from Player import Player
from SixDeck import SixDeck


def BlackJack():
    root = tk.Tk()
    
    iconp = Image.open('/Users/dayanabarron/Desktop/War_card_game/cards/2_of_clubs.png')
    iconPhoto = ImageTk.PhotoImage(iconp)
    root.title(string = "BlackJack")
    root.iconphoto(False, iconPhoto)

    p = Player()
    d = Dealer('deck')
    deck = SixDeck()
    deck.shuffle()

    global betSize
    betSize = 0
    
    global frameCount
    frameCount = 0
    
    global playerCardTracker
    playerCardTracker = 0
    
    global dealerCardTracker
    dealerCardTracker = 0
    
    global imageCount
    imageCount = 0
    
    global bjBool
    bjBool = False
    
    global downCardIndex
    downCardIndex = 0
    
    global startChips
    startChips = 0
    
    global doubleBool
    doubleBool = False
    
    global splitBool
    splitBool = False
    
    
    def clearFrame():
        for widget in frame_List[globals()['frameCount']].winfo_children():
            widget.destroy()
        frame_List[globals()['frameCount']].destroy()
        
    def drawAdds(j,k):
        getCardString(j,k)

    #Get the card and show designated image    
    def getCardString(j,k):
        if k == 1:
            valStr = "Ace"
        elif k == 11:
            valStr = "Jack"
        elif k == 12:           
            valStr = "Queen"
        elif k == 13:
            valStr = "King"
        elif k >=2 and k <= 10:
            valStr = str(k) 
        else:
            valStr = str(k) 
        fileName = "cards/" + valStr +"_of_"+j.lower()+".png"
        addImage(fileName)
    
     
    #Add the image from tKinter   
    def addImage(fileName):
        card = Image.open(fileName)
        cim = card.resize((95,145), Image.LANCZOS)
        im_card = ImageTk.PhotoImage(cim) 
        image_List.append(im_card)   
        
    def hitandStandDestroy():
        hitButton_List[globals()['frameCount']].destroy()
        standButton_List[globals()['frameCount']].destroy()   
    
        
    def Start():
        #entry_instance = ...  # replace with your actual Entry widget instance
        p.addChips(float(buyInEntry.get()))
        globals()['betSize'] = float(buyInEntry.get())
        globals()['startChips'] = float(buyInEntry.get())
        deal()
    
    def deal():
        clearFrame()
        splitScores.clear()
        splitDouble.clear()
        splitBJ.clear() 
        p.splitHoldReset()
        d.splitHoldReset()
        globals()['splitBool'] = False
        
        
        if (globals()['doubleBool'] == True):
            globals()['betSize'] = globals()['betSize']/2
            globals()['doubleBool'] = False
        
        p.reset()
        d.reset()
        globals()['playerCardTracker'] = 0
        globals()['dealerCardTracker'] = 0
        
        globals()['frameCount'] += 1  
        frame_List[globals()['frameCount']].pack(padx = 1, pady = 1)
        p.loseChips(globals()['betSize'])
        
        deckLength = deck.length()
        
        if(deckLength < 20):
            deck.deckReset()
        #player and dealer card displays and cards drawn by dealer and player
        p.draw(deck)
        drawAdds(p.getSuit(), p.getVal())
        Label(frame_List[frameCount], image = image_List[imageCount]).place(x=700 +playerCardTracker, y=100)
        globals()['imageCount'] += 1
        globals()['playerCardTracker'] += 100
        
        d.draw(deck)
        drawAdds(d.getSuit(), d.getVal())
        globals()['downCardIndex'] = globals()['imageCount']
        Label(frame_List[globals()['frameCount']], image = imbc).place(x=300 + globals()['dealerCardTracker'], y=100)
        globals()['imageCount'] += 1 
        globals()['dealerCardTracker'] += 100
        
        p.draw(deck)
        drawAdds(p.getSuit(), p.getVal())
        Label(frame_List[globals()['frameCount']], image = image_List[imageCount]).place(x=300 +globals()['playerCardTracker'], y=500)
        globals()['imageCount'] += 1
        globals()['playerCardTracker'] += 100
        
        d.draw(deck)
        drawAdds(d.getSuit(), d.getVal())
        Label(frame_List[globals()['frameCount']], image = image_List[imageCount]).place(x=300 +globals()['dealerCardTracker'], y=100)
        globals()['imageCount'] += 1
        globals()['dealerCardTracker'] += 100
        
        Label(frame_List[globals()['frameCount']], text = str(p.score()), width= 7, font=("Arial",25)).place(x=330, y=680)
        hitButton_List[globals()['frameCount']].place(x=300, y=400)
        standButton_List[globals()['frameCount']].place(x=375, y=400)
        doubleButton_List[globals()['frameCount']].place(x=450, y=400)
        
        if(p.splitCheck() == True):
            splitButton_List[globals()['frameCount']].place(x=525, y=400)
            
        Label(frame_List[globals()['frameCount']], width= 15, text = "Chips $" + str(p.chipCount()), font=("Arial",22)).place(x=280, y=750)
        Label(frame_List[globals()['frameCount']], image = idpc).place(x=50, y=400) 
        Label(frame_List[globals()['frameCount']], text= str(globals()['betSize']), width = 7, font=("Arial",20)).place(x=100, y=400)
        
        
        playerBJCheck()
        dealerBJCheck()
    
    
    #If player has Blackjack, add chips to player, display chip count, end hit and stand button
    def playerBJCheck():
        globals()['bjBool'] = True 
        if(p.score() == 21):
            hitandStandDestroy()
            doubleButton_List[globals()['frameCount']].destroy()
            playAgainButton_List[globals()['frameCount']].place(x=300, y=400)
            colorUpButton_List[globals()['frameCount']].place(x=420, y=400)
            seeDealerTurnButton_List = []  # Add this line to define the list before using it
            if(d.score() == 21):
                p.addChips(globals()['betSize'])
                Label(frame_List[globals()['frameCount']], text = "Dealer and Player BlackJack Push!", width = 15, font=("Arial",25)).place(x=380, y=600)
                Label(frame_List[globals()['frameCount']], text = "+0", width = 6, fg = 'black', font=("Arial",25)).place(x=150, y=550)
            else:
                Label(frame_List[globals()['frameCount']], text = "BlackJack!", width = 12, font=("Arial",25)).place(x=380, y=600)
                if(len(p.splitHolding) > 0):
                    splitBJ.append(p.score())
                    colorUpButton_List[globals()['frameCount']].destroy()
                    nextSplitButton_List[globals()['frameCount']].place(x=300, y=400)
                elif(globals()['splitBool'] == True):
                    splitBJ.append(p.score())
                    seeDealerTurnButton_List[globals()['frameCount']].place(x=300, y=400)
                p.addChips(globals()['betSize']*2.5)
                Label(frame_List[globals()['frameCount']], text = "+" + str(globals()['betSize']*1.5), width = 6, fg = 'green', font=("Arial",25)).place(x=150, y=550)
    
    # check if dealer has blackjack, remove chips from player, display chip count      
    def dealerBJCheck():
        if(d.score() == 21):
            splitButton_List[globals()['frameCount']].destroy()
            Label(frame_List[globals()['frameCount']], image = image_List[globals()['downCardIndex']]).place(x=300, y=100)
            hitandStandDestroy()
            doubleButton_List[globals()['frameCount']].destroy()
            playAgainButton_List[globals()['frameCount']].place(x=300, y=400)
            colorUpButton_List[globals()['frameCount']].place(x=420, y=400)
            Label(frame_List[globals()['frameCount']], text = "Dealer BlackJack!", width = 15, font=("Arial",25)).place(x=380, y=600)
            Label(frame_List[globals()['frameCount']], text = "-" + str(globals()['betSize']), width = 6, fg = 'red', font=("Arial",25)).place(x=150, y=550)           
   
    #Hit button, player draws a card, display card  
    def hit():
        p.draw(deck)
        getCardString(p.getSuit(), p.getVal())
        doubleButton_List[globals()['frameCount']].destroy()
        Label(frame_List[globals()['frameCount']], image = image_List[imageCount]).place(x=300 + globals()['playerCardTracker'], y=500)
        globals()['imageCount'] += 1
        globals()['playerCardTracker'] += 100
        Label(frame_List[globals()['frameCount']], text = str(p.score()), width= 7, font=("Arial",25)).place(x=330, y=680)
        if(p.score() > 21):
            nextSplitButton_List = []  # Add this line to define the list before using it

            if(len(p.splitHolding) > 0):
                hitandStandDestroy()
                nextSplitButton_List[globals()['frameCount']].place(x=300, y=400)
                splitScores.append(p.score())
            elif(globals()['splitBool'] == True):
                hitandStandDestroy()
                splitScores.append(p.score())
                seeDealerTurnButton_List[globals()['frameCount']].place(x=300, y=400)
            
            else:
                Label(frame_List[globals()['frameCount']], image = image_List[globals()['downCardIndex']]).place(x=300, y=100)
                hitandStandDestroy()
                playAgainButton_List[globals()['frameCount']].place(x=300, y=400)
                colorUpButton_List[globals()['frameCount']].place(x=420, y=400)
                Label(frame_List[globals()['frameCount']], text = "Player Bust!", width = 12, font=("Arial",25)).place(x=330, y=680)
                Label(frame_List[globals()['frameCount']], text = "-" + str(globals()['betSize']), width = 6, fg = 'red', font=("Arial",25)).place(x=150, y=550)
                
    #when player chooses to stand, the dealer will draw until they have 17 or higher           
    def dealersTurn():
        if(len(p.splitHolding) > 0):
            splitScores.append(p.score())
            splitDeal()
        else:
            Label(frame_List[globals()['frameCount']], image = image_List[globals()['downCardIndex']]).place(x=300, y=100)
            doubleButton_List[globals()['frameCount']].destroy()
        
            while (d.score() < 17):
                d.draw(deck)
                getCardString(d.getSuit(), d.getVal())
                Label(frame_List[globals()['frameCount']], image = image_List[imageCount]).place(x=300 + globals()['dealerCardTracker'], y=100)
                globals()['imageCount'] += 1
                globals()['dealerCardTracker'] += 100
            
             #dealer busts, add chips to player, display chip count
            Label(frame_List[globals()['frameCount']], text = str(d.score()), width= 7, font=("Arial",25)).place(x=330, y=50)
            if(d.score() > 21):
                if(globals()['splitBool'] == True):
                    splitScores.append(d.score())
                    splitResults()
                else:
                    hitandStandDestroy()
                    playAgainButton_List[globals()['frameCount']].place(x=300, y=400)
                    colorUpButton_List[globals()['frameCount']].place(x=500, y=400)
                    splitButton_List[globals()['frameCount']].destroy()
                    p.addChips(globals()['betSize']*2)
                    Label(frame_List[globals()['frameCount']], text = "Dealer Bust!", width = 12, font=("Arial",25)).place(x=380, y=600)
                    Label(frame_List[globals()['frameCount']], text = "+" + str(globals()['betSize']*2), width = 6, fg = 'green', font=("Arial",25)).place(x=150, y=550)
            else:
                if(globals()['splitBool'] == True):
                    splitScores.append(d.score())
                    splitResults()  
                else:
                    checkWin()
    
    #check who wins, add chips to player, display chip count
    def checkWin():
        hitandStandDestroy()
        splitButton_List[globals()['frameCount']].destroy()
        playAgainButton_List[globals()['frameCount']].place(x=300, y=400)
        colorUpButton_List[globals()['frameCount']].place(x=420, y=400)
        if(p.score() > d.score()):
            p.addChips(globals()['betSize']*2)
            Label(frame_List[globals()['frameCount']], text = "Player Wins!", width = 12, font=("Arial",25)).place(x=380, y=600)
            Label(frame_List[globals()['frameCount']], text = "+" + str(globals()['betSize']), width = 6, fg = 'green', font=("Arial",25)).place(x=150, y=550)
        elif(p.score() == d.score()):
            p.addChips(globals()['betSize'])
            Label(frame_List[globals()['frameCount']], text = "Push!", width = 5, font=("Arial",25)).place(x=380, y=600)
            Label(frame_List[globals()['frameCount']], text = "+" + str(globals()['betSize']), width = 6, fg = 'green', font=("Arial",25)).place(x=280, y=750)
        else:
            Label(frame_List[globals()['frameCount']], text = "Dealer Wins!", width = 12, font=("Arial",25)).place(x=380, y=600)
            Label(frame_List[globals()['frameCount']], text = "-" + str(globals()['betSize']), width = 6, fg = 'red', font=("Arial",25)).place(x=280, y=750)
    
    #final chip count - start chip count   
    def endGame():
        finalChips = p.chipCount() - globals()['startChips']
        if(finalChips > 0):
            Label(root, text = "You won $" + str(finalChips) + "Chips", width=25, font=("Arial",25), fg='green').place(x=400, y=400)
        else:
            finalChips = finalChips
            Label(root, text = "You lost $" + str(finalChips) + "Chips", width=25, font=("Arial",25), fg='red').place(x=400, y=400) 
        clearFrame()
    
    #double the bet size, display current chip count, increment image count and player tracker. Player bust
    def double():
        globals()['doubleBool'] = True
        doubleButton_List[globals()['frameCount']].destroy()
        splitButton_List[globals()['frameCount']].destroy()
        globals()['betSize'] = globals()['betSize']*2
        p.loseChips(globals()['betSize'])
        Label(frame_List[globals()['frameCount']],width=15, text = "Chips $" + str(p.chipCount()), font=("Arial",25)).place(x=280, y=750)
        p.draw(deck)
        getCardString(p.getSuit(), p.getVal())
        Label(frame_List[globals()['frameCount']], image = image_List[globals()['imageCount']]).place(x=300 + globals()['playerCardTracker'], y=500)
        globals()['imageCount'] += 1
        globals()['playerCardTracker'] += 100
        Label(frame_List[globals()['frameCount']], text = str(p.score()), width= 7, font=("Arial",25)).place(x=300, y=600)
        if(p.score() > 21):
            if(len(p.splitHolding) > 0):
                splitDouble.append(p.score())
                globals()['betSize'] = globals()['betSize']/2
                globals()['doubleBool'] = False
                nextSplitButton_List[globals()['frameCount']].place(x=300, y=400)
            elif(globals()['splitBool'] == True):
                splitDouble.append(p.score())
                globals()['betSize'] = globals()['betSize']/2
                globals()['doubleBool'] = False
                seeDealerTurnButton_List[globals()['frameCount']].place(x=300, y=400)
            else:   
                Label(frame_List[globals()['frameCount']], text = "Bust!", width = 5, font=("Arial",25)).place(x=380, y=600)
                hitandStandDestroy()
                playAgainButton_List[globals()['frameCount']].place(x=300, y=400)
                colorUpButton_List[globals()['frameCount']].place(x=500, y=400)
                Label(frame_List[globals()['frameCount']], text = "Bust" + str(globals()['betSize']), width = 12, font=("Arial",25)).place(x=280, y=680)
                Label(frame_List[globals()['frameCount']], text = "-" + str(globals()['betSize']), width = 6, fg = 'red', font=("Arial",25)).place(x=280, y=680)
        else:
            if(len(p.splitHolding)> 0):
                globals()['betSize'] = globals()['betSize']/2
                globals()['doubleBool'] = False
                splitDouble.append(p.score())
                nextSplitButton_List[globals()['frameCount']].place(x=300, y=400)
            elif(globals()['splitBool'] == True):
                globals()['betSize'] = globals()['betSize']/2
                globals()['doubleBool'] = False
                splitDouble.append(p.score())
                seeDealerTurnButton_List[globals()['frameCount']].place(x=300, y=400)
            else:
                dealersTurn()
        
        for i in splitBJ:
            p.addChips(globals()['betSize']*2.5)
            moneyCount += globals()['betSize']*2.5
            bjCount += 1
    #split the hand, display current chip count, increment image count and player tracker. Player bust    
    def split():
        p.loseChips(globals()['betSize'])
        globals()['playerCardTracker'] = 0
        getCardString(p.getSuit(), p.getVal()) 
        Label(frame_List[globals()['frameCount']], image = image_List[globals()['imageCount']]).place(x=300 + globals()['playerCardTracker'], y=500)
        globals()['imageCount'] += 1
        if(globals()['splitBool'] == False):
            d.splitToHolding()
            d.splitToHolding()
        
        globals()['splitBool']= True
        p.splitToHolding()
        
        globals()['playerCardTracker'] = 100
        p.draw(deck)
        getCardString(p.getSuit(), p.getVal()) 
        Label(frame_List[globals()['frameCount']], image = image_List[globals()['imageCount']]).place(x=300 + globals()['playerCardTracker'], y=500)
        globals()['imageCount'] += 1
        globals()['playerCardTracker'] += 100
        Label(frame_List[globals()['frameCount']], text = str(p.score()), width= 7, font=("Arial",25)).place(x=300, y=600)
        Label(frame_List[globals()['frameCount']], text = "Split Hand 1", width = 25, font=("Arial",22)).place(x=280, y=680)
        if(p.splitCheck() == False):
            splitButton_List[globals()['frameCount']].destroy()
        playerBJCheck()
    
    def splitDeal():
        clearFrame()
        globals()['frameCount'] += 1
        frame_List[globals()['frameCount']].pack(padx = 1, pady = 1)
        p.reset()
        globals()['playerCardTracker'] = 0
        globals()['dealerCardTracker'] = 0   
        
        p.drawHolding()
        getCardString(p.getSuit(), p.getVal())
        Label(frame_List[globals()['frameCount']], image = image_List[globals()['imageCount']]).place(x=300 + globals()['playerCardTracker'], y=500)  
        globals()['imageCount'] += 1
        globals()['playerCardTracker'] += 100
        
        d.holdingDraw()
        getCardString(d.getSuit(), d.getVal())
        Label(frame_List[globals()['frameCount']], image = imbc).place(x=300 + globals()['dealerCardTracker'], y=100)
        globals()['dealerCardTracker'] += 100
        globals()['imageCount'] += 1
        
        p.draw(deck)
        getCardString(p.getSuit(), p.getVal()) 
        Label(frame_List[globals()['frameCount']], image = image_List[globals()['imageCount']]).place(x=300 + globals()['playerCardTracker'], y=500)
        globals()['imageCount'] += 1
        globals()['playerCardTracker'] += 100
        
        d.holdingDraw()
        getCardString(d.getSuit(), d.getVal())
        Label(frame_List[globals()['frameCount']], image = image_List[globals()['imageCount']]).place(x=300 + globals()['dealerCardTracker'], y=100)
        globals()['imageCount'] += 1
        globals()['dealerCardTracker'] += 100
        
        Label(frame_List[globals()['frameCount']], text = str(p.score()), width= 7, font=("Arial",25)).place(x=300, y=600)
        
        
        hitButton_List[globals()['frameCount']].place(x=300, y=400)
        standButton_List[globals()['frameCount']].place(x=300, y=500)
        doubleButton_List[globals()['frameCount']].place(x=300, y=600)
        if(p.splitCheck() == True):
            splitButton_List[globals()['frameCount']].place(x=525, y=400)
            
        Label(frame_List[globals()['frameCount']], width= 15, text = "Chips $" + str(p.chipCount()), font=("Arial",25)).place(x=280, y=750)
        Label(frame_List[globals()['frameCount']], width= 18, text= "Split Hand Continued", font=("Arial",22)).place(x=280, y=680)
        playerBJCheck()
        dealerBJCheck()
        
    def splitResults():
        hitandStandDestroy()
        doubleButton_List[globals()['frameCount']].destroy()
        splitButton_List[globals()['frameCount']].destroy()
        playAgainButton_List[globals()['frameCount']].place(x=300, y=400)
        colorUpButton_List[globals()['frameCount']].place(x=420, y=400)
        Label(frame_List[globals()['frameCount']], width = 18, text = "Split Hand Results", font=("Arial",22)).place(x=280, y=850)
        Label(frame_List[globals()['frameCount']],image = idpc).place(x=50, y=400)
        Label(frame_List[globals()['frameCount']], text= str(globals()['betSize']),width = 7, font=("Arial",20)).place(x=100, y=400)
        moneyCount = 0
        lossCount = 0
        winCount = 0
        tieCount = 0
        d_winCount = 0
        d_lossCount = 0
        d_tieCount = 0
        bjCount = 0
        for i in splitScores:
            if(i > 21):
                moneyCount -= globals()['betSize']
                lossCount += 1
            elif(d.score() > 21):
                p.addChips(globals()['betSize']*2)
                moneyCount += globals()['betSize']
                winCount += 1
            elif(i > d.score()):
                p.addChips(globals()['betSize']*2)
                moneyCount += globals()['betSize']
                winCount += 1
            elif(i == d.score()):
                p.addChips(globals()['betSize'])
                tieCount += 1
            else:
                moneyCount -= globals()['betSize']
                lossCount += 1
                
        for i in splitDouble:
            if(i > 21):
                moneyCount -= globals()['betSize']*2
                d_lossCount += 1
            elif(d.score() > 21):
                p.addChips(globals()['betSize']*4)
                moneyCount += globals()['betSize']*2
                d_winCount += 1
            elif(i > d.score()):
                p.addChips(globals()['betSize']*4)
                moneyCount += globals()['betSize']*2
                d_winCount += 1
            elif(i == d.score()):
                p.addChips(globals()['betSize']*2)
                d_tieCount += 1
            else:
                moneyCount -= globals()['betSize']*2  
                d_lossCount += 1  
                
        for i in splitBJ:
            p.addChips(globals()['betSize']*2.5)
            moneyCount += globals()['betSize']*2.5
            bjCount += 1
            
        if((d_winCount > 0 or d_lossCount > 0 or d_tieCount ) > 0 and bjCount > 0):
            Label(frame_List[globals()['frameCount']], text = "BlackJacks!" + str(bjCount) + "Win" + str(winCount) + "Lost" +str(lossCount) + "Tied" + str(tieCount) + "Double Wins" + str(d_winCount) + "Double Lost" + str(d_lossCount) + "Double Tie" + str(d_tieCount), width=80, font=("Arial",25)).place(x=280, y=680)
        elif(d_winCount > 0 or d_lossCount > 0 or d_tieCount >0):
            Label(frame_List[globals()['frameCount']], text = "Win" + str(winCount) + "Lost" +str(lossCount) + "Tied" + str(tieCount) + "Double Wins" + str(d_winCount) + "Double Lost" + str(d_lossCount) + "Double Tie" + str(d_tieCount), width=80, font=("Arial",25)).place(x=280, y=6800)
        elif(bjCount > 0):
            Label(frame_List[globals()['frameCount']], text = "BlackJacks!" + str(bjCount) + "Win" + str(winCount) + "Lost" +str(lossCount) + "Tied" + str(tieCount), width=50, font=("Arial",25)).place(x=280, y=680)
        else:
            Label(frame_List[globals()['frameCount']], text = "Win" + str(winCount) + "Lost" +str(lossCount) + "Tied" + str(tieCount), width=20, font=("Arial",25)).place(x=280, y=680)
        if(moneyCount >= 0):
            Label(frame_List[globals()['frameCount']], text = "+" + str(moneyCount), width=6, font=("Arial",25), fg='green').place(x=150, y=550)
        else:
            Label(frame_List[globals()['frameCount']], text = str(moneyCount), width=6, font=("Arial",25), fg='red').place(x=150, y=550)
            
    frame_List = []
    image_List = []
    hitButton_List = []
    standButton_List = []
    playAgainButton_List = []
    colorUpButton_List = []
    doubleButton_List = []
    splitButton_List = []
    nextSplitButton_List = []
    seeDealerTurnButton_List = []
    splitScores = []
    splitDouble = []
    splitBJ = []
    
    for i in range(0, 2000):
        frame_List.append(LabelFrame(root, width = 2000, height = 2000,background = 'darkgray'))
        hitButton_List.append(Button(frame_List[i],text="Hit",command = hit, height = 2, width = 5, background ='salmon', font = ("Arial", 15)))
        standButton_List.append(Button(frame_List[i],text = "Stand",command = dealersTurn, height = 2, width = 5, background = 'turquoise',font = ("Arial", 15)))
        playAgainButton_List.append(Button(frame_List[i], text = "Play Again", command = deal, height = 2, width = 8, background = 'aqua', font =("Arial", 15)))
        colorUpButton_List.append(Button(frame_List[i], text = "Color Up", command = endGame, width = 8, height = 2, background = 'coral', font =("Arial", 15)))
        doubleButton_List.append(Button(frame_List[i], text = "Double", command = double, height = 2, width = 5, background = 'fuchsia', font = ("Arial", 15)))
        splitButton_List.append(Button(frame_List[i], text = "Split", command = split, height = 2, width = 5, background = 'gold',font = ("Arial", 15)))
        nextSplitButton_List.append(Button(frame_List[i], text = "See Next Split", command = splitDeal, width = 15, height = 2, background = 'khaki', font = ("Arial", 15))) 
        seeDealerTurnButton_List.append(Button(frame_List[i], text = "See Dealers Turn", command = dealersTurn, width = 15, height = 2, background = 'khaki', font = ("Arial", 15)))
        
    frame_List[0].pack()
        
    Button(frame_List[0], text = "Play BlackJack", command = Start, height = 10, width = 25,background = 'salmon',font = ("Arial",25)).place(x=700,y=100)
    buyInEntry = Entry(frame_List[0], font = ("Arial", 15))
    buyInEntry.place(x = 870, y = 550)
    buyInLabel = Label(frame_List[0], font =("Arial", 15), text ="Chips Buy In $: ").place(x=700, y = 550)
    betEntry = Entry(frame_List[0],font = ("Arial", 15))
    betEntry.place(x = 870, y = 650)
    betLabel = Label(frame_List[0], font =("Arial", 15), text ="Intial Bet Size $: ").place(x=700, y = 650)
    
    pc = Image.open('cards/chip.png')
    dpc = pc.resize((50, 50), Image.LANCZOS)
    idpc = ImageTk.PhotoImage(dpc)
    bc = Image.open('cards/blue.png')
    dbc = bc.resize((95, 145), Image.LANCZOS)
    imbc = ImageTk.PhotoImage(dbc)
    
    
    root.mainloop()
    
BlackJack()

 