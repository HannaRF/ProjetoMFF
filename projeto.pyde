G = 0.07  # gravitacão (unidade (10^9 m)^3 / (10^24 kg) (10^6 s)^2
modo=0

def setup():
    size(800,800)

def draw():
    global modo, controle
    if modo==0:
        menu00()
        controle=0
        
    elif modo==1:
        menu01()
        
    elif modo==10:
        simulacao()
        
    elif modo==20:
        challenge()
        
    elif modo==2:
        menu02()
        
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
        modo = 1 if 425<=mouseY<=525 else (2 if 600<=mouseY<=700 else 0) 
    background(192, 197, 206)
    fill(52, 61, 70)
    rect(100,425,600,100)
    rect(100,600,600,100)
    textSize(30)
    fill(0)
    text("BEM VINDO(A) AO ULTRA GRAVITY!!!", 140,150)
    text("Escolha o uso clicando em um",180,275)
    text("dos seguintes botoes:",240,325)
    fill(255)
    text("SIMULACAO",315,488)
    text("GRAVITY CHALLENGE",250,662)
    
    
    
    
    
    
    
    
    
    
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
    global modo, c_p, c_v, c_b, c_m0, c_m, c_cont, G, c_qtd, c_oldt, c_oldc, c_ponto, c_verif, controle
    background(192, 197, 206)
    fill(52, 61, 70)
    rect(100,650,600,100)
    textSize(30)
    stroke(0)
    fill(0)
    text("GRAVITY CHALLENGE", 250,125)
    text("Este e um jogo de orbitas.",210,250)
    text("Clique e arraste para lancar corpos.",145,350)
    text("Acumule pontos mantendo-os em orbita",105,400)
    text("estavel por tempo suficiente.",190,450)
    text("Bom jogo e boa sorte!!!",230,550)
    fill(255)
    text("INICIAR DESAFIO",280,712)
    controle = controle+1 if controle<20 else controle
    if mousePressed and controle==20 and 100<mouseX<700 and 650<mouseY<750:
        c_p, c_v, c_b, c_m0, c_m, c_cont, G, c_qtd, c_oldt, c_oldc, c_ponto, c_verif= [], [], PVector(400,400), 10000000, 1000000, 0, 0.07, 0, millis()/1000.00, 0, 0, 0
        modo = 20
        controle=0
    
    
    
    
    
    
    
    
    
    
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
    
    
    #atualização da posição do corpo 3 pelo método de Range-Kutta
    k1 = s_v3.copy()
    
    dpk2 = k1.copy()
    dpk2.mult(dt/2)
    pk2 = s_p3.copy()
    pk2.add(dpk2)
    Fgk2 = PVector.sub(pk2, p0)
    dk2 = Fgk2.mag()
    Fgk2.mult(G*s_m0*s_m/(dk2*dk2*dk2))
    ak2 = PVector.mult(Fgk2, -dt/(2*s_m))
    k2 = s_v3.copy()
    k2.add(ak2)
    
    dpk3 = k2.copy()
    dpk3.mult(dt/2)
    pk3 = s_p3.copy()
    pk3.add(dpk3)
    Fgk3 = PVector.sub(pk3, p0)
    dk3 = Fgk3.mag()
    Fgk3.mult(G*s_m0*s_m/(dk3*dk3*dk3))
    ak3 = PVector.mult(Fgk3, -dt/(2*s_m))
    k3 = s_v3.copy()
    k3.add(ak3)
    
    dpk4 = k3.copy()
    dpk4.mult(dt)
    pk4 = s_p3.copy()
    pk4.add(dpk4)
    Fgk4 = PVector.sub(pk4, p0)
    dk4 = Fgk4.mag()
    Fgk4.mult(G*s_m0*s_m/(dk4*dk4*dk4))
    ak4 = PVector.mult(Fgk4, -dt/s_m)
    k4 = s_v3.copy()
    k4.add(ak4)
    
    k=(k1+2*k2+2*k3+k4)/6
    
    #atualização da posição do corpo 2
    dp3 = k.copy()
    dp3.mult(dt)
    s_p3.add(dp3)
    
    #atualização de velocidade do corpo 2
    s_v3.add(2*ak3)
    
    
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
    rect(585,650,210,140)    
    fill(255)
    text("Metodo de Euler", 610, 675)
    fill(255,255,120)
    text("Ponto Medio", 635,710)
    fill(255,50,50)
    text("Runge-Kutta(RK4)", 607,745)
    fill(100,175,255)
    text("Trajetoria circular", 610, 780)
    fill(0)
    line(585,685,795,685)
    line(585,720,795,720)
    line(585,755,795,755)
    
    
    
    
    
    
    
    
    
    
def challenge():
    
    global c_b, c_v, c_m0, c_p, c_m, c_cont, c_oldt, c_qtd, c_oldc, c_ponto, c_verif, controle
    
    background(79, 91, 102)
    controle = controle+1 if controle<20 else controle
    if controle==20:
        
        #c_verifica pontudação
        c_verif = c_verif+1 if (c_oldc==c_qtd) else 0
        c_ponto = max(c_qtd,c_ponto) if c_verif==500 else c_ponto 
        c_oldc = c_qtd
        
        #Reset
        if mousePressed and mouseX>700 and mouseY<50:
            c_p, c_v, c_qtd, c_ponto = [], [], 0, 0
        
        #Clique para acrescentar corpo
        
        elif mousePressed and c_cont==0:
            oltd = millis()/1000.00
            c_p.append(PVector(mouseX,mouseY))
            c_v.append(PVector(mouseX,mouseY))
            c_qtd +=1
            c_cont=1
        
        #Velocidade do novo corpo  
              
        elif mousePressed:
            stroke(255)
            line(c_p[c_qtd-1].x,c_p[c_qtd-1].y,mouseX,mouseY)
            stroke(0)
            c_v[c_qtd-1] = PVector.sub(c_p[c_qtd-1],PVector(mouseX,mouseY))
            c_oldt = millis()/1000.0
        
        
        #Cálculos        
        if not(mousePressed):
            c_cont=0
            
            #tempo transcorrido desde último desenho
            t = millis()/1000.00
            dt = t - c_oldt
            c_oldt = t
            
            #Cálculo para cada corpo   
            for i in range(c_qtd):
                
                #Força gravitacional central
                Fg = PVector.sub(c_b,c_p[i])
                d = Fg.mag()
                Fg.mult((G*c_m0*c_m)/(d*d*d))
                
                #c_verifica excedente dos limites
                if d<15 or c_p[i].x<0 or c_p[i].x>800 or c_p[i].y<0 or c_p[i].y>800:
                    c_p.pop(i)
                    c_v.pop(i)
                    c_qtd -= 1
                    break                        
    
                #Força dos outros corpos sobre o calculado
                for k in range(c_qtd):
                    if c_p[i]!=c_p[k]:
                        F = PVector.sub(c_p[k],c_p[i])
                        d = F.mag()
                        F.mult((G*c_m*c_m)/(d*d*d))
                        Fg.add(F)
    
                #atualização da posição do corpo
                dp = c_v[i].copy()
                dp.mult(dt)
                c_p[i].add(dp)
                #variação de velocidade para o corpo
                a = PVector.mult(Fg, dt/c_m)
                c_v[i].add(a)
                
    #Desenhos
    fill(0)
    textSize(20)
    ellipse(c_b.x,c_b.y,30,30)
    fill(0,0,100)
    stroke(0,0,100)
    for i in range(c_qtd):
        ellipse(c_p[i].x,c_p[i].y,10,10)
    stroke(0)
    fill(52, 61, 70)
    rect(700,10,90,40)
    rect(200,15,400,30)
    fill(255)
    textSize(20)
    text("reset",720,37)
    text("Corpos: {} - Pontuacao: {}".format(c_qtd,c_ponto),270,37)
