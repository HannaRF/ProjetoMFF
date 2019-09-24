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
    global modo, s_p1, s_v1, s_m0, s_m, s_oldt, s_p2, s_v2, s_rastro, s_clique, s_ex1, s_ex2, s_ex3, s_ex4, s_p3, s_v3
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
        background(79, 91, 102)
        modo = 10
        s_m0 = 2000000 #(unidade: 10^24 kg)
        s_m = 6
        s_p1 = PVector(550, 400) #(unidade: 1 pixel = 10^9 m)
        s_p2 = PVector(550, 400)
        s_p3 = PVector(550, 400)
        s_v1 = PVector(0, -30) #(unidade: 10^9 m / 10^6 s)
        s_v2 = PVector(0, -30)
        s_v3 = PVector(0, -30)
        s_oldt = millis()/1000.0 #instante inicial
        s_rastro = False
        s_clique = 50
        s_ex1 = True
        s_ex2 = True
        s_ex3 = True
        s_ex4 = False
    
    
    
    
    
    
def menu02():
    global modo
    background(0,255,0)
    
    
    
    
    
    
def menu03():
    global modo
    background(0,0,255)
    
    
    
    
    
    
def simulacao():
    global s_oldt, s_m0, s_p1, s_v1, s_m, s_p2, s_v2, s_rastro, s_clique, s_ex1, s_ex2, s_ex3, s_ex4, s_p3, s_v3

    #posicionamento do corpo central
    p0 = PVector(400,400)
    
    #tempo transcorrido desde último desenho
    t = millis()/1000.00
    dt = (t - s_oldt)
    s_oldt = t
    
    #cálculo da força de gravitação sobre o corpo 1
    Fg1 = PVector.sub(s_p1, p0)
    d1 = Fg1.mag()
    Fg1.mult(G*s_m0*s_m/(d1*d1*d1))
    
    #atualização da posição do corpo 1
    dp1 = s_v1.copy()
    dp1.mult(dt)
    s_p1.add(dp1)
    
    #atualização de velocidade do corpo 1
    a1 = PVector.mult(Fg1, -dt/s_m)
    s_v1.add(a1)
    
    #atualização da posição do corpo 2 para o ponto médio
    dp2m = s_v2.copy()
    dp2m.mult(dt/2)
    s_p2m = s_p2.copy()
    s_p2m.add(dp2m)
    
    #cálculo da força de gravitação sobre o corpo 2 para ponto medio
    Fg2 = PVector.sub(s_p2m, p0)
    d2 = Fg2.mag()
    Fg2.mult(G*s_m0*s_m/(d2*d2*d2))
    
    #atualização da posição do corpo 2
    dp2 = s_v2.copy()
    dp2.mult(dt)
    s_p2.add(dp2)
    
    #atualização de velocidade do corpo 2
    a2 = PVector.mult(Fg2, -dt/s_m)
    s_v2.add(a2)
    
    
    
    
    
    
    ######
    
    #Inplementar Runge-Kutta para atualizar posição, velocidade e aceleração no corpo 3.
    #Posição do corpo 3: s_p3
    #Velocidade corpo 3: s_v3
    #Aceleração do corpo 3: a3
    
    ######
    
    
    
    
    
    
    
    #cálculo do erro do corpo 1
    e1 = p0.dist(s_p1)-150
    
    #cálculo do erro do corpo 2
    e2 = p0.dist(s_p2)-150
    
    #cálculo do erro do corpo 3
    e3 = p0.dist(s_p3)-150
    
    #interação
    if mousePressed and s_clique >= 10:
        if 10<=mouseX<=20 and 775<=mouseY<=785:
            s_rastro = not(s_rastro)
        if 600<=mouseX<=790 and 650<=mouseY<=790:
            background(79, 91, 102)
            if mouseY<685:
                s_ex1 = not(s_ex1)
            elif mouseY<720:
                s_ex2 = not(s_ex2)
            elif mouseY<755:
                s_ex3 = not(s_ex3)
            else:
                s_ex4 = not(s_ex4)
        s_clique = 0
    else:
        s_clique +=1
        
    #reset
    if mousePressed and 700<=mouseX<=790 and 10<=mouseY<=50:
        background(79, 91, 102)
        s_p1 = PVector(550, 400) #(unidade: 1 pixel = 10^9 m)
        s_p2 = PVector(550, 400)
        s_p3 = PVector(550, 400)
        s_v1 = PVector(0, -30) #(unidade: 10^9 m / 10^6 s)
        s_v2 = PVector(0, -30)
        s_v3 = PVector(0, -30)
        s_oldt = millis()/1000.0 #instante inicial
    
    #rastro dos planetas
    k = 255
    if not(s_rastro):
        background(79, 91, 102)
        k = 50
        
    #Desenhos
        
    #buraco negro
    fill(0)
    stroke(0)
    ellipse(400, 400, 15, 15)
    
    #corpo 1
    if s_ex1:
        fill(255)
        stroke(255)
        ellipse(s_p1.x, s_p1.y, 3, 3)
    
    #corpo 2
    if s_ex2:
        fill(255,255,120)
        stroke(255,255,120)
        ellipse(s_p2.x, s_p2.y, 3, 3)
        
    #corpo 3
    if s_ex3:
        fill(255,50,50)
        stroke(255,50,50)
        ellipse(s_p3.x, s_p3.y, 3, 3)
    
    #trajetória correta
    if s_ex4:
        stroke(100,175,255)
        noFill()
        ellipse(400,400,300,300)
    
    #Indicador de rastro
    stroke(0)
    fill(k)
    ellipse(15,780,10,10)
    fill(255)
    text("Rastro", 25, 787)
    
    #Botão de reset
    fill(52, 61, 70)
    rect(700,10,90,40)
    fill(255)
    textSize(20)
    text("reset",720,37)
    
    #erros
    stroke(0)
    fill(52, 61, 70)
    rect(185,15,440,30)
    stroke(255)
    fill(255)
    text("Erros:  1) {:02.2f}   2) {:02.2f}   3) {:.2f}".format(abs(e1),abs(e2),abs(e3)),205,38)
    
    #legenda
    stroke(0)
    fill(52, 61, 70)
    rect(600,650,190,140)    
    fill(255)
    text("Metodo de Euler", 615, 675)
    fill(255,255,120)
    text("Metodo de Heun", 615,710)
    fill(255,50,50)
    text("Runge-Kutta(RK4)", 607,745)
    fill(100,175,255)
    text("Trajetoria circular", 610, 780)
    fill(0)
    line(600,685,790,685)
    line(600,720,790,720)
    line(600,755,790,755)
