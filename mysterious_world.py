import random,time
from termcolor import colored

# titan sleep days == 20
world=["gold","goblin","fox","zombie","bear","dragon"]

class Game(object):
    def __init__(self,user,hp,power,gold,lv,exp):
        self.user=user
        self.lv=lv
        self.hp=hp
        self.power=power
        self.gold=gold
        self.exp=exp
    
    def status(self):
        global day
        if self.lv==1:
            if self.gold>=0 and self.gold<6:
                colg="red"
            if self.gold>=6:
                colg="green"
            if self.hp<=150:
                col="red"
            if self.hp>150:
                col="green"
        if self.lv==2:
            if self.gold>=0 and self.gold<10:
                colg="red"
            if self.gold>=10:
                colg="green"
            if self.hp<=250:
                col="red"
            if self.hp>250:
                col="green"
        if self.lv=="max":
            if self.gold>=0 and self.gold<12:
                colg="red"
            if self.gold>=12:
                colg="green"
            if self.hp<=500:
                col="red"
            if self.hp>500:
                col="green"
        if self.exp<60:
            state,num="lv-2",60
        elif self.exp<140:
            state,num="lv-max",140
        else:
            state,num="Win",240
        if day<=5:
            colo="red"
        else:
            colo="green"
        print()
        print("Hero's Name : ",colored(self.user,"yellow"))
        print("You are in Level-",colored(self.lv,"yellow"))
        print("You have",colored(self.hp,col), colored("HP",col),"   (Max_HP :",max_hero_hp,")")
        print("You have",colored(self.power,"yellow"), colored("power","yellow"))
        print("You have",colored(self.gold,colg), colored("gold",colg))
        print("You have",colored(self.exp,"yellow"),colored("exp","yellow"),"(",state,"state : >=",num,"exp)")
        print("  >>>  Titan will awake in ",colored(day,colo),"days")

    def explore(self):
        global day
        day-=1
        if self.lv==1:
            weight=[12,28,20,20,15,5]
            enemy = random.choices(world, weights=weight, k=1 )
            if enemy[0]=='gold':
                print('\nYou find 5 gold')
                self.gold+=5
                print("Total gold :",self.gold)
                test=True
            elif enemy[0]=='goblin':
                test=Game.goblin(self,'goblin',50,5,3,5)
            elif enemy[0]=='fox':
                test=Game.fox(self,'fox',100,10,5,10)
            elif enemy[0]=='zombie':
                test=Game.zombie(self,'zombie',150,15,10,20)
            elif enemy[0]=='bear':
                test=Game.bear(self,'bear',200,18,15,30)
            else:
                test=Game.dragon(self,'dragon',250,20,20,40)
        elif self.lv==2:
            weight=[10,15,24,26,17,8]
            enemy = random.choices(world, weights=weight, k=1 )
            if enemy[0]=='gold':
                print('\nYou find 5 gold')
                self.gold+=5
                print("Total gold :",self.gold)
                test=True
            elif enemy[0]=='goblin':
                test=Game.goblin(self,'goblin',100,10,3,5)
            elif enemy[0]=='fox':
                test=Game.fox(self,'fox',180,20,5,10)
            elif enemy[0]=='zombie':
                test=Game.zombie(self,'zombie',250,30,10,15)
            elif enemy[0]=='bear':
                test=Game.bear(self,'bear',350,40,15,20)
            else:
                test=Game.dragon(self,'dragon',400,50,20,30)
        else:
            weight=[5,10,10,20,30,25]
            enemy = random.choices(world, weights=weight, k=1 )
            if enemy[0]=='gold':
                print('\nYou find 10 gold')
                self.gold+=10
                print("Total gold :",self.gold)
                test=True
            elif enemy[0]=='goblin':
                test=Game.goblin(self,'goblin',350,50,8,5)
            elif enemy[0]=='fox':
                test=Game.fox(self,'fox',450,60,12,8)
            elif enemy[0]=='zombie':
                test=Game.zombie(self,'zombie',550,70,15,12)
            elif enemy[0]=='bear':
                test=Game.bear(self,'bear',650,80,20,16)
            else:
                test=Game.dragon(self,'dragon',750,90,25,20)
        if test==False:
            return False
        if day==0:
            print(colored("Time's up, Titan awake  >> You Lose...","red"))
            return False
        
    def goblin(self,enemy,hp,power,gold,exp):
        print(f"\nYou Find {enemy}")
        print(f"HP: {hp}, Power: {power}, Price: {gold}")
        herohp=self.hp
        heropower=self.power
        while herohp>0 and hp>0:
            herohp-=power
            hp-=heropower
            time.sleep(.7)
            print(".....")
            print("The "+enemy+" attack you.Your health is "+str(herohp))
            if herohp<=0:
                print(colored("Hero has been slained  >> You Lose...","red"))
                return False
            print("You attack the "+enemy+".The "+enemy+" health is "+ str(hp))
            if hp<=0:
                print(colored("You have slained the "+enemy,"green"))
                print(colored("You gain {0} gold & {1} exp".format(gold,exp),"green"))
                self.hp=herohp
                gain=Game.counter(self,enemy,gold,exp)
        if gain==False:
            return False
            
    def fox(self,enemy,hp,power,gold,exp):
        print(f"\nYou find {enemy}")
        print(f"HP: {hp}, Power: {power}, Price: {gold}")
        herohp=self.hp
        heropower=self.power
        while herohp>0 and hp>0:
            herohp-=power
            hp-=heropower
            time.sleep(.7)
            print(".....")
            print("The "+enemy+" attack you.Your health is "+str(herohp))
            if herohp<=0:
                print(colored("Hero has been slained  >> You Lose...","red"))
                return False
            print("You attack the "+enemy+".The "+enemy+" health is "+ str(hp))
            if hp<=0:
                print(colored("You have slained the "+enemy,"green"))
                print(colored("You gain {0} gold & {1} exp".format(gold,exp),"green"))
                self.hp=herohp
                gain=Game.counter(self,enemy,gold,exp)
        if gain==False:
            return False
            
    def zombie(self,enemy,hp,power,gold,exp):
        print(f"\nYou find {enemy}")
        print(f"HP: {hp}, Power: {power}, Price: {gold}")
        herohp=self.hp
        heropower=self.power
        while herohp>0 and hp>0:
            herohp-=power
            hp-=heropower
            time.sleep(.7)
            print(".....")
            print("The "+enemy+" attack you.Your health is "+str(herohp))
            if herohp<=0:
                print(colored("Hero has been slained  >> You Lose...","red"))
                return False
            print("You attack the "+enemy+".The "+enemy+" health is "+ str(hp))
            if hp<=0:
                print(colored("You have slained the "+enemy,"green"))
                print(colored("You gain {0} gold & {1} exp".format(gold,exp),"green"))
                self.hp=herohp
                gain=Game.counter(self,enemy,gold,exp)
        if gain==False:
            return False
        
    def bear(self,enemy,hp,power,gold,exp):
        print(f"\nYou find {enemy}")
        print(f"HP: {hp}, Power: {power}, Price: {gold}")
        herohp=self.hp
        heropower=self.power
        while herohp>0 and hp>0:
            herohp-=power
            hp-=heropower
            time.sleep(.7)
            print(".....")
            print("The "+enemy+" attack you.Your health is "+str(herohp))
            if herohp<=0:
                print(colored("Hero has been slained  >> You Lose...","red"))
                return False
            print("You attack the "+enemy+".The "+enemy+" health is "+ str(hp))
            if hp<=0:
                print(colored("You have slained the "+enemy,"green"))
                print(colored("You gain {0} gold & {1} exp".format(gold,exp),"green"))
                self.hp=herohp
                gain=Game.counter(self,enemy,gold,exp) 
        if gain==False:
            return False
        
    def dragon(self,enemy,hp,power,gold,exp):
        print(f"\nYou find {enemy}")
        print(f"HP: {hp}, Power: {power}, Price: {gold}")
        herohp=self.hp
        heropower=self.power
        while herohp>0 and hp>0:
            herohp-=power
            hp-=heropower
            time.sleep(.7)
            print(".....")
            print("The "+enemy+" attack you.Your health is "+str(herohp))
            if herohp<=0:
                print(colored("Hero has been slained  >> You Lose...","red"))
                return False
            print("You attack the "+enemy+".The "+enemy+" health is "+ str(hp))
            if hp<=0:
                print(colored("You have slained the "+enemy,"green"))
                print(colored("You gain {0} gold & {1} exp".format(gold,exp),"green"))
                self.hp=herohp
                self.power=heropower
                gain=Game.counter(self,enemy,gold,exp)
        if gain==False:
            return False
            
    def counter(self,enemy,gold,exp):
        if self.lv==1 or self.lv==2:
            if enemy=='goblin':
                self.gold+=gold
                self.exp+=exp
                gain=Game.lvup(self)
            if enemy=='fox':
                self.gold+=gold
                self.exp+=exp
                gain=Game.lvup(self)
            if enemy=='zombie':
                self.gold+=gold
                self.exp+=20
                gain=Game.lvup(self)
            if enemy=='bear':
                self.gold+=gold
                self.exp+=exp
                gain=Game.lvup(self)
            if enemy=='dragon':
                self.gold+=gold
                self.exp+=exp
                gain=Game.lvup(self)
        if self.lv=='max':
            if enemy=='goblin':
                self.gold+=gold
                self.exp+=exp
                gain=Game.lvup(self)
            if enemy=='fox':
                self.gold+=gold
                self.exp+=exp
                gain=Game.lvup(self)
            if enemy=='zombie':
                self.gold+=gold
                self.exp+=exp
                gain=Game.lvup(self)
            if enemy=='bear':
                self.gold+=gold
                self.exp+=exp
                gain=Game.lvup(self)
            if enemy=='dragon':
                self.gold+=gold
                self.exp+=exp
                gain=Game.lvup(self)
        if gain==False:
            return False
        if self.hp>max_hero_hp:
            self.hp=max_hero_hp

    def lvup(self): 
        if self.exp>=60 and self.exp<140 and self.lv==1:
            self.lv=2
            Game.upgrade(self)
        if self.exp>=140 and self.exp<240 and self.lv==2:
            self.lv='max'
            Game.upgrade(self)
        if self.exp>=240 and self.lv=='max':
            count=20-day
            print(colored("Congratulation, you've become God in this Mysterious World.\n                   You Won this game in {} days...","green").format(count))
            return False
            
    def upgrade(self):
        global max_hero_hp,max_hero_power
        if self.lv == 2:
            print(colored("Congratulations! You have promoted to lv- 2","green"))
            max_hero_hp=500
            max_hero_power=50
            self.hp=max_hero_hp
            self.power=max_hero_power
        if self.lv == 'max':
            print(colored("Wow! You have reached in max lv.","green"))
            print(colored("     Let's try to become 'God' in this world","yellow"))
            max_hero_hp=1000
            max_hero_power=100
            self.hp=max_hero_hp
            self.power=max_hero_power
            
    def shop(self):
        buy=input("Shop counter (1. heal potion) : ")
        if buy=='1' and self.lv==1:
            print("Cost : 6 golds")
            if self.gold>=6 and self.hp<300:
                self.gold-=6
                self.hp+=50
                if self.hp>max_hero_hp:
                    self.hp=max_hero_hp
                print("HP -",self.hp,"HP","(gain_50 HP!)")
            else: print(colored("Not Enough Money!!!","light_red"))
        if buy=='1' and self.lv==2:
            print("Cost : 10 golds")
            if self.gold>=10 and self.hp<500:
                self.gold-=10
                self.hp+=150
                if self.hp>max_hero_hp:
                    self.hp=max_hero_hp
                print("HP -",self.hp,"HP","(gain_150 HP!)")
            else: print(colored("Not Enough Money!!!","light_red"))
        if buy=='1' and self.lv=='max':
            print("Cost : 12 golds")
            if self.gold>=12 and self.hp<1000:
                self.gold-=12
                self.hp+=250
                if self.hp>max_hero_hp:
                    self.hp=max_hero_hp
                print(f"HP -",self.hp,"HP","(gain_250 HP!)")
            else: print(colored("Not Enough Money!!!","light_red"))
    def help(self):
        print(colored("""\nGame Guide >>>\n
    1. Shop : You can only buy heal potion. \n    2. when you kill enemy > you will get exp
        exp- (>=60 : lv-2) (>=120 : lv-max)  (>=240 : win) Note: play without dying!!!""","yellow"))
        input("Press Enter to Exit >>> ")
    
def main():
    global day,max_hero_power,max_hero_hp
    max_hero_hp=300
    max_hero_power=20
    day=20
    print(colored("\nWelcome from the Mysterious World...","yellow"))
    input("Press \"Enter\" key to play... ")
    user=input("\nPlease Give Your Hero's Name: ")
    play=Game(user,300,20,0,1,0)
    hon=True
    while hon:
        print(colored(f"""\nSo...\"{user}\" , What is your action?
            1. Status
            2. Explore
            3. Shop
            4. Help
            5. Quit""","blue"))
        try:
            choice=int(input("Enter Choice : "))
            if choice>0 and choice<6:
                if choice==5:
                    ask=input("Are you sure(yes/no) : ").strip().lower()
                    if ask=='yes':
                        print("😘 Bye Bye... 😘")
                        hon=False
                    else:
                        hon=True
                elif choice==1:
                    play.status()
                elif choice==2:
                    test=play.explore()
                    if test==False:
                        input("Press Enter to quit")
                        print("😘 Bye Bye... 😘")
                        hon=False
                elif choice==3:
                    play.shop()
                else:
                    play.help()
            else:
                print(colored("Please enter (1-5) !!!","light_red"))
        except ValueError:
            print(colored("Invalid input!!!","light_red"))
   
if __name__=="__main__" :
    main()