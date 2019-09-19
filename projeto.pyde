G = 0.07  # gravitacão (unidade (10^9 m)^3 / (10^24 kg) (10^6 s)^2
modo=0

def setup():
    size(800,800)

def draw():
    global modo
    if modo==0:
        menu00()
        
    elif modo==1:
        menu01()
        
    elif modo==10:
        simulacao()
        
    elif modo==2:
        menu02()
        
    elif modo==3:
        menu03()
        
    if modo!=0:
        fill(52, 61, 70)
        rect(10,10,90,40)
        fill(255)
        textSize(20)
        text("inicio",30,37)
        modo = 0 if mousePressed and 10<=mouseX<=100 and 10<=mouseY<=50 else modo
        
                                                                                    
def menu00():
    global modo
    if mousePressed and 100<=mouseX<=700:
        modo = 1 if 350<=mouseY<=450 else (2 if 500<=mouseY<=600 else (3 if 650<=mouseY<=750 else 0))    
    background(192, 197, 206)
    fill(52, 61, 70)
    rect(100,350,600,100)
    rect(100,500,600,100)
    rect(100,650,600,100)
    textSize(30)
    fill(0)
    text("BEM VINDO(A) AO ULTRA GRAVITY!!!", 140,100)
    text("Escolha o uso clicando em um",180,200)
    text("dos seguintes botoes:",240,250)
    fill(255)
    text("SIMULACAO",315,413)
    text("SANDBOX",330,561)
    text("GRAVITY CHALLENGE",250,712)
    
def menu01():
    global modo, s_p1, s_v1, s_m0, s_m1, s_oldt, s_tmult
    background(192, 197, 206)
    fill(52, 61, 70)
    rect(100,650,600,100)
    textSize(30)
    fill(0)
    text("SIMULACAO", 315,125)
    text("Esta e uma simulacao gravitacional",145,250)
    text("em torno de um corpo massivo ideal.",130,300)
    text("O intuito e comparar os erros",185,425)
    text("de aproximacao no emprego dos",160,475)
    text("tres metodos utilizados.",225,525)
    fill(255)
    text("INICIAR SIMULACAO",255,712)
    if mousePressed and 100<=mouseX<=700 and 650<=mouseY<=750:
        modo = 10
        background(79, 91, 102)
        s_m1 = 6
        s_m0 = 2000000 #(unidade: 10^24 kg)
        s_p1 = PVector(550, 400) #(unidade: 1 pixel = 10^9 m)
        s_v1 = PVector(0, -30) #(unidade: 10^9 m / 10^6 s)
        s_oldt = millis()/1000.0 #instante inicial
        s_tmult = 1 #multiplicador da simulação
    
def menu02():
    global modo
    background(0,255,0)
    
def menu03():
    global modo
    background(0,0,255)
    
def simulacao():
    global s_oldt, s_p1, s_v1, m0, s_m1, s_tmult

    p0 = PVector(400,400)
    #cálculo da força de gravitação sobre o corpo 1
    Fg1 = PVector.sub(s_p1, p0)
    d1 = Fg1.mag()
    Fg1.mult(G*s_m0*s_m1/(d1*d1*d1))
    #tempo transcorrido desde último desenho
    t = millis()/1000.00
    dt = (t - s_oldt)*s_tmult
    s_oldt = t
    #atualização da posição de cada corpo
    dp1 = s_v1.copy()
    dp1.mult(dt)
    s_p1.add(dp1)
    #variação de velocidade para cada corpo (força*delta(t)/masssa)
    a1 = PVector.mult(Fg1, -dt/s_m1)
    #atualização das velocidades
    s_v1.add(a1)
    
    #desenho dos corpos
    #background(225)
    fill(0)
    stroke(255)
    ellipse(s_p1.x, s_p1.y, 3, 3)
    fill(0)
    stroke(0)
    ellipse(400, 400, 15, 15)
    fill(192, 197, 206)
    rect(600,650,190,140)    
    stroke(0)
    fill(0)
    text("Metodo de Euler", 615, 670)
    text("BRANCO", 650, 690)
