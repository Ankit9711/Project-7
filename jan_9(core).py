import random
print("         Rock ✊ Paper 📄 Scissor ✂️")
print(" ="*25)
print("GAME START")
class RPS_Game :
    def __init__(self,Name,Score,Comp_score) :
        self.Name=Name
        self.Score=Score
        self.comp=Comp_score

Avail_move=["Rock","Paper","Scissor"]
def Play_round(n) :
    print(f"----Round {n} Start---")
    Move=input("Player's Move (Rock/Paper/Scissor) : ").strip().title()
    if(Move in Avail_move) :
        Comp_move= random.choice(Avail_move)
        print(f"COMPUTER CHOOSE: {Comp_move}")
        if(Move=="Rock" and Comp_move=="Scissor") :
            print("You Wins\n")
            Game.Score+=1
        elif(Move=="Rock" and Comp_move=="Paper") :
            print("Computer Wins\n")
            Game.comp+=1
        elif(Move=="Scissor" and Comp_move=="Paper") :
            print("You Wins\n")
            Game.Score+=1
        elif(Move=="Paper" and Comp_move=="Scissor") :
            print("Computer Wins\n")
            Game.comp+=1
        elif(Move=="Scissor" and Comp_move=="Rock") :
            print("Computer Wins\n")
            Game.comp+=1
        elif(Move=="Paper" and Comp_move=="Rock") :
            print("You Wins\n")
            Game.Score+=1
        else : print("Game Draw")
    else : 
        print("You Choose An Invalid Move")
        print("GAME OVER\n")
        exit()
    return

def Show_score() :
    print("-"*4,end="")
    print("SCOREBORD",end="")
    print("-"*4)
    print(f"{Player_Name} : {Game.Score}")
    print(f"COMPUTER      : {Game.comp}")
    return

Player_Name=input("Enter Player Name: ").strip()
Round=int(input("Enter Number Of Rounds: "))
Game=RPS_Game(Player_Name,0,0)  

for i in range(1,Round+1) :
    Play_round(i)
print("GAME OVER\n")


Show_score()