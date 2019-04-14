'''
Author: Justin
Date: 13/6/2018
Version: V 0.1.3.6.6 Dev

'''

#--Classes--

class Character:

    HUMAN = 'A Human'
    ORC = 'An Orc'
    ELF = 'An Elf'
    BEAVER = 'A Beaver'
    
    MALE = 'Male'
    FEMALE = 'Female'

    def __init__(self, pName, pRace, pGender, pSkill, pStrength, pHealth,
                 pWeapon):
        self.name = pName
        self.race = pRace
        self.skill = pSkill
        self.strength = pStrength
        self.health = pHealth
        self.weapon = pWeapon
        self.gender = pGender
        self.alive = 'Alive'

    def __repr__(self):
        return '''
{0} Is {1} And Is {2}
Weapon: {3}
Strength: {4}
Intelligence: {5}
Health: {6}
Status: {7}
'''.format(self.name, self.race, self.gender, self.weapon, self.strength,
           self.skill,
self.health, self.alive)

    def getName(self):
        return self.name

    def getRace(self):
        return self.race

    def getSkill(self):
        return self.skill

    def getStrength(self):
        return self.strength

    def getHealth(self):
        return self.health

    def getWeapon(self):
        return self.weapon

    def getGender(self):
        return self.gender

    def getAlive(self):
        return self.alive

    def setWeapon(self, weapon):
        self.weapon = weapon

class Weapon:

    FLAMETHROWER = 'A Flamethrower'
    SHOTGUN = 'A Shotgun'
    RIFLE = 'A Rifle'

    def __init__(self, pname, ptype, ppower):
        self.type = ptype
        self.name = pname
        self.power = ppower

    def __repr__(self):
        return '{}, {} With {} Power'.format(self.name, self.type,
                                             self.power)

    def getName(self):
        return self.name
    def getType(self):
        return self.type
    def getPower(self):
        return self.power

#--Variables--

pick = False
lFlame = Weapon('BigFlame', Weapon.FLAMETHROWER, 30)
lShot = Weapon('ManyBullet', Weapon.SHOTGUN, 20)
lRifle = Weapon('NearlySniper', Weapon.RIFLE, 40)
mFlame = Weapon('NormFlame', Weapon.FLAMETHROWER, 20)
mShot = Weapon('NotSoManyBullet', Weapon.SHOTGUN, 15)
mRifle = Weapon('ArmyRifle', Weapon.RIFLE, 25)
sFlame = Weapon('ShortFlame', Weapon.FLAMETHROWER, 10)
sShot = Weapon('CoupleBullet', Weapon.SHOTGUN, 10)
sRifle = Weapon('ChineseGun', Weapon.RIFLE, 15)
    
#--Main-Code--
while pick == False:
    firstName = input('Pick A First Name For Your Adventurer: ')
    if firstName == '' or firstName == ' ':
        print('''
Whoops "{}" Isn't A Valid Name
Let's Try That Again

Tip!: Try Making Your Name Something Other Than
      "" Or " "
      '''.format(firstName))
        a = input("Press Enter To Continue ")
        print('\n')
    else:
        pick = True
pick = False
while pick == False:
    race = input('''
A Human (1)
An Orc (2)
An Elf (3)
Or A Beaver (4)
Pick A Race: ''')
    if race == '1':
        race = Character.HUMAN
        skill = 65
        strength = 55
        health = 105
        pick = True
    elif race == '2':
        race = Character.ORC
        skill = 35
        strength = 75
        health = 125
        pick = True
    elif race == '3':
        race = Character.ELF
        skill = 85
        strength = 35
        health = 85
        pick = True
    elif race == '4':
        race = Character.BEAVER
        skill = 45
        strength = 65
        health = 75
        pick = True
    else:
        print('''
Whoops What Went Wrong There
Let's Try That Again

Tip!: Try Using The Number Beside The Race Choice's
      To Pick Your Character's Race
      ''')
        a = input("Press Enter To Continue ")
pick = False
while pick == False:
    gender = input('''
Male (1)
Or Female (2)
Pick A Gender: ''')
    if gender == '1':
        gender = Character.MALE
        name = firstName + ' ' + firstName + 'son'
        pick = True
    elif gender == '2':
        gender = Character.FEMALE
        name = firstName + ' ' + firstName + 'daughter'
        pick = True
    else:
        print('''
Whoops What Went Wrong There
Let's Try That Again

Tip!: Try Using The Number Beside The Gender Choice's
      To Pick Your Character's Gender
      ''')
        a = input("Press Enter To Continue ")
pick = False
while pick == False:
    weapon = input('''
{} (1)
{} (2)
{} (3)
Pick A Starter Weapon: '''.format(sFlame, sShot, sRifle))
    if weapon == '1':
        weapon = sFlame
        user = Character(name, race, gender, skill, strength,
                         health, weapon)
        pick = True
    elif weapon == '2':
        weapon = sShot
        user = Character(name, race, gender, skill, strength,
                         health, weapon)
        pick = True
    elif weapon == '3':
        weapon = sRifle
        user = Character(name, race, gender, skill, strength,
                         health, weapon)
        pick = True
    else:
        print('''
Whoops What Went Wrong There
Let's Try That Again

Tip!: Try Using The Number Beside The Weapon Choice's
      To Pick Your Character's Starting Weapon
      ''')
        a = input("Press Enter To Continue ")
pick = False
while pick == False:
    charPrint = input('''
Would You Like To See Your Newly
Created Character's Profile? (Y/N): ''')
    if charPrint == 'Y' or charPrint == 'y':
        pick = True
        print(user)
    elif charPrint == 'N' or charPrint == 'n':
        pick = True
    else:
        print('''
Whoops What Went Wrong There
Let's Try That Again

Tip!: Try Using The Y or N To Pick Whether You
      Want To See Your Character's Profile
      ''')
        a = input("Press Enter To Continue ")
pick = False
