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
    global modo, s_p1, s_v1, s_m0, s_m, s_oldt, s_p2, s_v2
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
        s_m = 6
        s_m0 = 2000000 #(unidade: 10^24 kg)
        s_p1 = PVector(550, 400) #(unidade: 1 pixel = 10^9 m)
        s_v1 = PVector(0, -30) #(unidade: 10^9 m / 10^6 s)
        s_oldt = millis()/1000.0 #instante inicial
        s_p2 = PVector(550, 400)
        s_v2 = PVector(0, -30)
    
def menu02():
    global modo
    background(0,255,0)
    
def menu03():
    global modo
    background(0,0,255)
    
def simulacao():
    global s_oldt, s_p1, s_v1, m0, s_m

    #Corpo 1 - Euler
    #Corpo 2 - Ponto Médio
    
    #Posicionamento do buraco negro
    p0 = PVector(400,400)
    
    #tempo transcorrido desde último desenho
    t = millis()/1000.00
    dt = (t - s_oldt)
    s_oldt = t
    
    #cálculo da força de gravitação sobre o corpo 1
    Fg1 = PVector.sub(s_p1, p0)
    d1 = Fg1.mag()
    Fg1.mult(G*s_m0*s_m/(d1*d1*d1))
    
    #atualização da velocidade do corpo 1
    a1 = PVector.mult(Fg1, -dt/s_m)
    s_v1.add(a1)
    
    #atualização da posição do corpo 1
    dp1 = s_v1.copy()
    dp1.mult(dt)
    s_p1.add(dp1)
    
    
    
    #cálculo da força de gravitação sobre o corpo 2 para o uso no ponto médio
    Fg2m = PVector.sub(s_p2, p0)
    d2m = Fg2m.mag()
    Fg2m.mult(G*s_m0*s_m/(d2m*d2m*d2m))
    
    #calculo da posição do ponto médio
    dp2m = s_v2.copy()
    dp2m.mult(dt/2)
    s_p2m = s_p2
    s_p2m.add(dp2m)
    
    #calculo da força gravitacional no corpo 2 a ser aplicado
    Fg2 = PVector.sub(s_p2m, p0)
    d2 = Fg2.mag()
    Fg2.mult(G*s_m0*s_m/(d2*d2*d2))
    
    #atualização da posição do corpo 2
    dp2 = s_v2.copy()
    dp2.mult(dt)
    s_p2.add(dp2)
    
    #atualização da velocudade do corpo 2
    a2 = PVector.mult(Fg2, -dt/s_m)
    s_v2.add(a2)
    
    
    
    #desenho dos corpos
    #buraco negro
    fill(0)
    stroke(0)
    ellipse(400, 400, 15, 15)
    
    #corpo 1
    fill(0)
    stroke(255)
    ellipse(s_p1.x, s_p1.y, 3, 3)
    
    #corpo 2
    fill(0)
    stroke(255)
    #ellipse(s_p2.x, s_p2.y, 3, 3)
    
    #legenda
    fill(192, 197, 206)
    rect(600,650,190,140)    
    stroke(0)
    fill(0)
    text("Metodo de Euler", 615, 670)
    text("BRANCO", 650, 690)
