import pygame, time

pygame.init() # Initializing pygame
pygame.display.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Lens")

screenlayer = 0 # Detects which project section you should be in

PAPER = (255, 232, 181) # Colours
LIGHTGRAY = (192,192,192)
GRAY = (28,28,28) 
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,225)
RED = (255,0,0)
GREEN = (0,225,0)
YELLOW = (255,255,0)
DARKBLUE = (25,25,112)
DARKERBLUE = (0,5,71)
DARKRED = (139,0,0)
DARKGREEN = (0,100,0)
DARKYELLOW = (184,134,11)
PURPLE = (112,41,99)
TURQUOISE = (0,255,255)
BLACK = (0,0,0)



# In most numeric variable references:
# 1 is Element Cluster Test,
# 2 is Alternative Periodic Tables,
# 3 is Ideal Gas Law + Van der Waals Equation,
# 4 is Ideal  Gas Calculator.

def wait(n): # Waits
  time.sleep(n)

def button_range (x,y): # Determines which button is being clicked
  global screenlayer

  if screenlayer == 0:
    if (100 < x < 400) and (100 < y < 250):
      return 1
    elif (400 < x < 700) and (100 < y < 250):
      return 2
    elif (100 < x < 400) and (250 < y < 500):
      return 3
    elif (400 < x < 700) and (250 < y < 500):
      return 4
    else:
      return 0
  if screenlayer == 1:
    if (75 < x < 275) and (50 < y < 150):
      return 5
    else:
      return 0
  if screenlayer == 4:
    if (50 < x < 200) and (100 < y < 200):
      return "P"
    elif (220 < x < 370) and (100 < y < 200):
      return "V"
    elif (390 < x < 540) and (100 < y < 200):
      return "n"
    elif (560 < x < 710) and (100 < y < 200):
      return "T"
    else:
      return 0


def init_load():
  screen.fill(GRAY)

# Sprites
button1 = pygame.draw.rect(screen,GREEN,(100,50,300,200),border_radius=20)
button2 = pygame.draw.rect(screen,RED,(400,50,300,200),border_radius=20)
button3 = pygame.draw.rect(screen,BLUE,(100,250,300,200),border_radius=20)
button4 = pygame.draw.rect(screen,YELLOW,(400,250,300,200),border_radius=20)
clustertestbutton = pygame.draw.rect(screen,TURQUOISE,(100,50,200,100),border_radius=40)
ledger = pygame.draw.rect(screen,LIGHTGRAY,(350,50,400,500),border_radius=10)
IGL_area = pygame.draw.rect(screen,DARKERBLUE,(350,50,400,300),border_radius=10)
button5 = pygame.draw.rect(screen,PURPLE,(50,100,150,100),border_radius=30)
button6 = pygame.draw.rect(screen,PURPLE,(220,100,150,100),border_radius=30)
button7 = pygame.draw.rect(screen,PURPLE,(390,100,150,100),border_radius=30)
button8 = pygame.draw.rect(screen,PURPLE,(560,100,150,100),border_radius=30)
resultblock1 = pygame.draw.rect(screen,BLACK,(50,400,600,80))
resultblock2 = pygame.draw.rect(screen,PAPER,(55,390,590,60))

# Font Sizes
Font = pygame.font.SysFont('Comic Sans MS', 40)
Font_Minus = pygame.font.SysFont('Comic Sans MS', 35)
Small_Font = pygame.font.SysFont('Comic Sans MS', 20)
Font_Plus = pygame.font.SysFont('Comic Sans MS', 45)
Big_Font = pygame.font.SysFont('Comic Sans MS', 60)
Other_Font = pygame.font.SysFont('Comic Sans MS', 30)

# Texts
text1 = Font.render('Element Cluster Test',False,BLACK)
text2a = Font.render('Alternative',False,BLACK)
text2b = Font.render('Periodic Tables',False,BLACK)
text3a = Font.render('Ideal Gas Law',False,BLACK)
text3b = Font.render('+',False,BLACK)
text3c = Font_Minus.render('Van der Waals Equation',False,BLACK)
text4 = Font.render('Ideal Gas Calculator',False,BLACK)
test = Big_Font.render('Test!',False,BLACK)
ledger_title = Font.render('Known Clusters:',False,BLACK)
l = 1
ltxt1 = '-----'
ltxt2 = '-----'
ltxt3 = '-----'
ltxt4 = '-----'
ltxt5 = '-----'
ltxt6 = '-----'
ltxt7 = '-----'
ltxt8 = '-----'
ltxt9 = '-----'
ltxt10 = '-----'
ledger_1 = Font.render(ltxt1,False,BLACK)
ledger_2 = Font.render(ltxt2,False,BLACK)
ledger_3 = Font.render(ltxt3,False,BLACK)
ledger_4 = Font.render(ltxt4,False,BLACK)
ledger_5 = Font.render(ltxt5,False,BLACK)
ledger_6 = Font.render(ltxt6,False,BLACK)
ledger_7 = Font.render(ltxt7,False,BLACK)
ledger_8 = Font.render(ltxt8,False,BLACK)
ledger_9 = Font.render(ltxt9,False,BLACK)
ledger_10 = Font.render(ltxt10,False,BLACK)
slide = 1
table1 = pygame.image.load("t_1.png")
table2 = pygame.image.load("t_2.jpg")
table3 = pygame.image.load("t_3.jpg")
table4 = pygame.image.load("t_4.jpg")
table5 = pygame.image.load("t_5.jpg")
table6 = pygame.image.load("t_6.jpg")
table7 = pygame.image.load("t_7.jpg")
arrow1 = Big_Font.render("|",False,BLACK)
arrow2 = Big_Font.render("|",False,BLACK)
arrow3 = Big_Font.render("\/",False,BLACK)
def display_slide():
  if slide == 1:
    screen.blit(table1, (200,100))
  if slide == 2: 
    screen.blit(table2, (150,130))
  if slide == 3: 
    screen.blit(table3, (40,100))
  if slide == 4: 
    screen.blit(table4, (40,100))
  if slide == 5: 
    screen.blit(table5, (40,75))
  if slide == 6: 
    screen.blit(table6, (40,300))
    screen.blit(arrow1, (345,188))
    screen.blit(arrow2, (345,230))
    screen.blit(arrow3, (339,260))
    screen.blit(table7, (70,67))
  pygame.event.pump()
  pygame.display.flip()
IGL_parts = ["PV = r1 [Boyle's Law] (1)", "V/T = r2 [Charles's Law] (2)", "V/n = r3 [Avogadro's Law] (3)", "P/T = r4 [Gay-Lussac's Law] (4)", "V²/nT = r5 (5)", "PV/T² = r6 (6)", "(PV/nT)*(V²/T²) = r7", "(PV/nt)*r2² = r7", "PV/nT = R", "PV = nRT"]
IGL_words = ["Multiplying (2) and (3),","Multiplying (2) and (4),","Multiplying (5) and (6)"," and switching denominators,","Since V/T = r2,","Therefore,"]
stage = 0
e1 = Font.render(IGL_parts[0],False,BLACK)
e2 = Font.render(IGL_parts[1],False,BLACK)
e3 = Font.render(IGL_parts[2],False,BLACK)
e4 = Font.render(IGL_parts[3],False,BLACK)
e5 = Font.render(IGL_words[0]+"   "+IGL_parts[4],False,BLACK)
e6 = Font.render(IGL_words[1]+"   "+IGL_parts[5],False,BLACK)
e7 = Other_Font.render(IGL_words[2]+IGL_words[3]+"   "+IGL_parts[6],False,BLACK)
e8 = Other_Font.render(IGL_words[4]+"   "+IGL_parts[7],False,BLACK)
f1 = Font.render(IGL_words[-1],False,BLACK)
f2 = Font.render(IGL_parts[-2]+", and",False,BLACK)
f3 = Font.render(IGL_parts[-1]+".",False,BLACK)
vdw = Font.render("(P + a(n²/V²))(V - nb) = nRT [Van der Waals equation]",False,BLACK)
igl = Other_Font.render("PV = nRT [Ideal Gas Law] | (P + a(n²/V²))(V - nb) = nRT [Van der Waals equation]",False,BLACK)
result = ""
result_display = Font_Minus.render(result,False,BLACK)
title4 = Font_Plus.render("What do you want to calculate?",False,BLACK)
pressure = Big_Font.render("P",False,BLACK)
volume = Big_Font.render("V",False,BLACK)
moles = Big_Font.render("n",False,BLACK)
temperature = Big_Font.render("T",False,BLACK)
title5 = Font.render("Result:",False,BLACK)

# Format of elements: [melting point, boiling point, density, triple point temperature, critical point temperature, heat of fusion, heat of vaporization, molar heat capacity.]
# 0 is used if not applicable.
# Only includes elements 1 (Hydrogen) - 56 (Barium).

H = [13.99,20.271,0.08988,13.8033,39.938,0.117,0.904,28.836]
He = [0.95,0.422,0.1786,2.177,5.1953,0.0138,0.0829,20.78]
Li = [453.65,1603,0.534,0,3220,3,136,24.860]
Be = [1560,2742,1.85,0,5205,12.2,292,16.443]
B = [2349,4200,2.08,0,0,50.2,508,11.807]
C = [0,3915,2.1,4600,0,117,0,8.517] # Assumed to be graphite
N = [63.23,77.235,1.2506,63.151,126.21,0.72,5.57,29.124]
O = [54.36,90.188,1.429,54.361,154.581,0.444,6.82,29.378]
F = [53.48,85.03,1.696,53.48,144.41,0,6.51,31]
Ne = [24.56,27.104,0.9002,24.556,44.4918,0.335,1.71,20.79]
Na = [370.944,1156.090,0.968,0,2573,2.6,97.42,28.230]
Mg = [923,1363,1.738,0,0,8.48,128,24.869]
Al = [933.47,2743,2.7,0,0,10.71,284,24.20]
Si = [1687,3538,2.3290,0,0,50.21,383,19.789]
P = [317.3,553.7,1.823,0,0,0.66,51.9,23.824] 
S = [338.36,717.8,2.07,0,1314,1.727,45,22.75]
Cl = [171.6,239.11,3.2,0,416.9,6.406,20.41,33.949]
Ar = [83.81,87.302,1.764,1.3954,83.8058,150.687,1.18,6.53,20.85]
K = [336.7,1032,0.89,0,2223,2.33,76.9,29.6]
Ca = [1115,1757,1.55,0,0,8.54,154.7,25.929]
Sc = [1814,3109,2.985,0,0,14.1,332.7,25.52]
Ti = [1941,3560,4.506,0,0,14.15,425,25.060]
V = [2183,3680,6.11,0,0,25.1,444,24.89]
Cr = [2180,2944,7.19,0,0,21,347,23.35]
Mn = [1519,2334,7.21,0,0,12.91,221,26.32]
Fe = [1811,3134,7.874,0,0,13.81,340,25.1]
Co = [1768,3200,8.9,0,0,16.06,377,24.81]
Ni = [1728,3003,8.908,0,0,17.48,379,26.07]
Cu = [1357.77,2835,8.96,0,0,13.26,300.4,24.440]
Zn = [692.68,1180,7.14,0,0,7.32,115,25.47]
Ga = [302.9146,2673,5.91,0,0,5.59,256,25.86]
Ge = [1211.40,3106,5.323,0,0,36.94,334,23.222]
As = [0,887,5.727,1090,1673,24.44,34.76,24.64]
Se = [494,958,4.81,0,1766,6.69,95.48,25.363]
Br = [265.8,332,3.1028,265.9,588,10.571,29.96,75.69]
Kr = [115.78,119.93,3.749,115.775,209.48,1.64,9.08,20.95]
Rb = [312.45,961,1.532,312.41,2093,2.19,69,31.060]
Sr = [1050,1650,2.64,0,0,7.43,141,26.4]
Y = [1799,3203,4.472,0,0,11.42,363,26.53]
Zr = [2128,4650,6.52,0,0,14,591,25.36]
Nb = [2750,5017,8.57,0,0,30,689.9,24.60]
Mb = [2896,4912,10.28,0,0,37.48,598,24.06]
Tc = [2430,4538,11,0,0,33.29,585.2,24.27]
Ru = [2607,4423,12.45,0,0,38.59,619,24.06]
Rh = [2237,3968,12.41,0,0,26.59,493,24.98]
Pa = [1828.05,3236,12.023,0,0,16.74,358,25.98]
Ag = [1234.93,2435,10.49,0,0,11.28,254,25.350]
Cd = [594.22,1040,8.65,0,0,6.21,99.87,26.020]
In = [429.7485,2345,7.31,429.7445,0,3.281,231.8,26.74]
Sn = [505.08,2875,7.265,0,0,7.03,296.1,27.112]
Sb = [903.78,1908,6.697,0,0,19.79,193.43,25.23]
Te = [722.66,1261,6.24,0,0,17.49,114.1,25.73]
I = [386.85,457.4,4.933,386.65,819,15.52,41.57,54.44]
Xe = [161.40,165.051,5.894,161.405,289.733,2.27,12.64,21.01]
Cs = [301.7,944,1.93,0,1938,2.09,63.9,32.210]
Ba = [1000,2118,3.51,0,0,7.12,142,28.07]

E = [H,He,Li,Be,B,C,N,O,F,Ne,Na,Mg,Al,Si,P,S,Cl,Ar,K,Ca,Sc,Ti,V,Cr,Mn,Fe,Co,Ni,Cu,Zn,Ga,Ge,As,Se,Br,Kr,Rb,Sr,Y,Zr,Nb,Mb,Tc,Ru,Rh,Pa,Ag,Cd,In,Sn,Sb,Te,I,Xe,Cs,Ba] # Atomic number = index + 1

AtomicNums = {
  "H":1,
  "He":2,
  "Li":3,
  "Be":4,
  "B":5,
  "C":6,
  "N":7,
  "O":8,
  "F":9,
  "Ne":10,
  "Na":11,
  "Mg":12,
  "Al":13,
  "Si":14,
  "P":15,
  "S":16,
  "Cl":17,
  "Ar":18,
  "K":19,
  "Ca":20,
  "Sc":21,
  "Ti":22,
  "V":23,
  "Cr":24,
  "Mn":25,
  "Fe":26,
  "Co":27,
  "Ni":28,
  "Cu":29,
  "Zn":30,
  "Ga":31,
  "Ge":32,
  "As":33,
  "Se":34,
  "Br":35,
  "Kr":36,
  "Rb":37,
  "Sr":38,
  "Y":39,
  "Zr":40,
  "Nb":41,
  "Mb":42,
  "Tc":43,
  "Ru":44,
  "Rh":45,
  "Pa":46,
  "Ag":47,
  "Cd":48,
  "In":49,
  "Sn":50,
  "Sb":51,
  "Te":52,
  "I":53,
  "Xe":54,
  "Cs":55,
  "Ba":56
}

r = 3000 # The similarity threshold

def s(e1,e2): # Returns the measure of similarity between the elements e1 and e2.
  v = 0
  for i in range (8):
    v += abs(e1[i] - e2[i])
  return v

def isCluster(elist): # Returns whether or not the elements of elist form a cluster. r should be adjusted as necessary, so as to allow for the known clusters.
  for i in range (0,len(elist)-1):
    for j in range(i+1,len(elist)):
      if s(elist[i],elist[j]) >= r:
        return False
  return True

def readline(line,insert=0): # Prints the line.
  f = open("text.txt")
  lines = f.readlines()

  if bool(insert):
    print((lines[line-1]).format(insert))
  else:
    print(lines[line-1])

  f.close()

def readfortime(line,t):
  readline(line)
  wait(t)

def getline(line,insert=0): # Returns the line.
  f = open("text.txt")
  lines = f.readlines()

  if bool(insert):
    t = ((lines[line-1]).format(insert))
  else:
    t = (lines[line-1])

  return t
  f.close()


def clusterTest(): # Runs the cluster test for the user
  global ltxt1,ltxt2,ltxt3,ltxt4,ltxt5,ltxt6,ltxt7,ltxt8,ltxt9,ltxt10,l
  size = int(input(getline(13)))

  if not (2 <= size <= 10):
    readline(14)
    clusterTest()
  else:
    readline(15)
    elements = []
    for i in range(size):
      e = input()
      elements.append(e)
    actual_elements = [E[AtomicNums[x]-1] for x in elements]
    insertion = ""
    for i in range (size-1):
      insertion += elements[i]
      insertion += ", "
    insertion += "and "
    insertion += elements[size-1]

    if isCluster(actual_elements):
      readline(17,insertion)
      setform = insertion.replace("and ","")
      setform = "{"+setform+"}"

      if l == 1:
        ltxt1 = setform
      if l == 2:
        ltxt2 = setform
      if l == 3:
        ltxt3 = setform
      if l == 4:
        ltxt4 = setform
      if l == 5:
        ltxt5 = setform
      if l == 6:
        ltxt6 = setform
      if l == 7:
        ltxt7 = setform
      if l == 8:
        ltxt8 = setform
      if l == 9:
        ltxt9 = setform
      if l == 10:
        ltxt10 = setform
      l += 1
      
    else:
      readline(16,insertion)

def igl_calculate(solvefor): # Calculates for an unkown using the ideal gas law
  global result
  P = V = n = T = 0
  R = 8.3144621

  if not (solvefor == "P") : P = float(input(getline(50)))
  if not (solvefor == "V") : V = float(input(getline(51)))
  if not (solvefor == "n") : n = float(input(getline(52)))
  if not (solvefor == "T") : T = float(input(getline(53)))

  if solvefor == "P" : 
    result = (n*R*T)/V
    units = " Pa"
  if solvefor == "V" :
     result = (n*R*T)/P
     units = " m³"
  if solvefor == "n" :
     result = (P*V)/(R*T)
     units = " mol"
  if solvefor == "T" :
     result = (P*V)/(n*R)
     units = " K"

  result = (str(result))+(units)

init_load()
readline(1)
readline(2)
readline(3)
entering = 0
screenlayer = 0 # Temporary for testing

# Sub loops for each section
def layer0_loop():
    global screenlayer, entering
    screen.fill(GRAY)
    pygame.draw.rect(screen,GREEN,(100,50,300,200),border_radius=20)
    pygame.draw.rect(screen,RED,(400,50,300,200),border_radius=20)
    pygame.draw.rect(screen,BLUE,(100,250,300,200),border_radius=20)
    pygame.draw.rect(screen,YELLOW,(400,250,300,200),border_radius=20)
    screen.blit(text1,(110,150))
    screen.blit(text2a,(460,130))
    screen.blit(text2b,(450,170))
    screen.blit(text3a,(150,300))
    screen.blit(text3b,(240,340))
    screen.blit(text3c,(110,380))
    screen.blit(text4,(410,350))

    pygame.event.pump()
    mouseX,mouseY = pygame.mouse.get_pos()
    w = (pygame.mouse.get_pressed()).count(1)
    if bool(w):
      while bool(w):
        pygame.event.pump()
        mouseX,mouseY = pygame.mouse.get_pos()
        w = (pygame.mouse.get_pressed()).count(1)
      directive = button_range(mouseX,mouseY)
      if bool(directive):
        screenlayer = directive
        entering = 1

def layer1_loop():
    global screenlayer
    ledger_1 = Font.render(ltxt1,False,BLACK)
    ledger_2 = Font.render(ltxt2,False,BLACK)
    ledger_3 = Font.render(ltxt3,False,BLACK)
    ledger_4 = Font.render(ltxt4,False,BLACK)
    ledger_5 = Font.render(ltxt5,False,BLACK)
    ledger_6 = Font.render(ltxt6,False,BLACK)
    ledger_7 = Font.render(ltxt7,False,BLACK)
    ledger_8 = Font.render(ltxt8,False,BLACK)
    ledger_9 = Font.render(ltxt9,False,BLACK)
    ledger_10 = Font.render(ltxt10,False,BLACK)
    screen.fill(DARKGREEN)
    pygame.draw.rect(screen,TURQUOISE,(75,50,200,100),border_radius=40)
    pygame.draw.rect(screen,LIGHTGRAY,(325,50,400,500),border_radius=10)
    screen.blit(test,(120,80))
    screen.blit(ledger_title,(350,70))
    screen.blit(ledger_1,(350,100))
    screen.blit(ledger_2,(350,130))
    screen.blit(ledger_3,(350,160))
    screen.blit(ledger_4,(350,190))
    screen.blit(ledger_5,(350,220))
    screen.blit(ledger_6,(350,250))
    screen.blit(ledger_7,(350,280))
    screen.blit(ledger_8,(350,310))
    screen.blit(ledger_9,(350,340))
    screen.blit(ledger_10,(350,370))
    pygame.event.pump()
    mouseX,mouseY = pygame.mouse.get_pos()
    w = (pygame.mouse.get_pressed()).count(1)
    if bool(w):
      while bool(w):
        pygame.event.pump()
        mouseX,mouseY = pygame.mouse.get_pos()
        w = (pygame.mouse.get_pressed()).count(1)
      directive = button_range(mouseX,mouseY)
      if directive == 5:
        clusterTest()

    pygame.event.pump()
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_b]:
      screenlayer = 0

    pygame.display.flip()

def layer2_loop():
    global screenlayer  
    screen.fill(DARKRED)
    display_slide()   
    pygame.event.pump()
    pygame.display.flip()
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_b]:
      screenlayer = 0

def layer3_loop():
    global screenlayer  
    screen.fill(DARKBLUE)
    if stage >= 1:
      screen.blit(e1,(0,0))
      screen.blit(e2,(0,40))
      screen.blit(e3,(0,80))
      screen.blit(e4,(0,120))
    if stage >= 2:
      screen.blit(e5,(0,200))
      screen.blit(e6,(0,240))
    if stage >= 3:
      screen.blit(e7,(0,300))
      screen.blit(e8,(0,340))
    if stage >= 4:
      pygame.draw.rect(screen,DARKERBLUE,(525,0,350,250),border_radius=3)
      screen.blit(f1,(540,0))
      screen.blit(f2,(540,70))
      screen.blit(f3,(540,140))
    if stage >= 5:
      screen.fill(DARKBLUE)
      screen.blit(igl,(10,200))
      screen.blit(vdw,(200,400))
    pygame.event.pump()
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_b]:
      screenlayer = 0
    pygame.display.flip()

def layer4_loop():
    global screenlayer
    screen.fill(DARKYELLOW)
    pygame.draw.rect(screen,PURPLE,(50,100,150,100),border_radius=30)
    pygame.draw.rect(screen,PURPLE,(220,100,150,100),border_radius=30)
    pygame.draw.rect(screen,PURPLE,(390,100,150,100),border_radius=30)
    pygame.draw.rect(screen,PURPLE,(560,100,150,100),border_radius=30)
    pygame.draw.rect(screen,BLACK,(50,300,600,80))
    pygame.draw.rect(screen,PAPER,(55,310,590,60))
    result_display = Font_Minus.render(result, False, BLACK)
    screen.blit(title4,(150,50))
    screen.blit(title5,(90,275))
    screen.blit(pressure,(110,130))
    screen.blit(volume,(280,130))
    screen.blit(moles,(450,130))
    screen.blit(temperature,(620,130))
    screen.blit(result_display,(60,328))
    
    pygame.event.pump()
    mouseX,mouseY = pygame.mouse.get_pos()
    w = (pygame.mouse.get_pressed()).count(1)
    if bool(w):
      while bool(w):
        pygame.event.pump()
        mouseX,mouseY = pygame.mouse.get_pos()
        w = (pygame.mouse.get_pressed()).count(1)
      directive = button_range(mouseX,mouseY)
      if bool(directive):
        igl_calculate(directive)

    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_b]:
      screenlayer = 0

    pygame.display.flip()

while True:
  # Main loop
  if screenlayer == 0:
    layer0_loop()

  if screenlayer == 1:
    layer1_loop()
    if bool(entering):
      pygame.event.pump()
      print("-----------------")
      wait(1)
      for i in [6,7,8,9,10,11]:
        readfortime(i,5)
      entering = 0
    
  if screenlayer == 2:   
    layer2_loop()
    if bool(entering):
      slide = 1
      pygame.event.pump()
      print("-----------------")
      wait(1)
      display_slide()
      readfortime(20,4)
      readfortime(21,6)
      slide += 1
      layer2_loop()
      readfortime(22,6)
      readfortime(23,6)
      for i in [24,25,26]:
        slide += 1
        layer2_loop()
        readfortime(i,5)
      readfortime(27,5.5)
      readfortime(28,5.5)
      slide += 1
      layer2_loop()
      readfortime(29,6)
      readfortime(30,4)
      readfortime(31,1)
      entering = 0
      
    
  if screenlayer == 3:
    layer3_loop()
    if bool(entering):
      stage = 0
      pygame.event.pump()
      print("-----------------")
      wait(1)
      for i in [34,35,36]:
        readfortime(i,5)
      stage += 1
      layer3_loop()
      readfortime(37,7)
      readline(38)
      for i in range(3):
        stage += 1
        layer3_loop()
        wait(3.5)
      readfortime(39,5)
      readfortime(40,5)
      stage += 1
      layer3_loop()
      readfortime(42,6.5)
      readfortime(43,6.5)
      readfortime(45,3)
      entering = 0
    
  if screenlayer == 4:
    layer4_loop()
    if bool(entering):
      pygame.event.pump()
      print("-----------------")
      wait(1)
      for i in [48,49]:
        readfortime(i,4)
      entering = 0
    
  pygame.display.flip()
