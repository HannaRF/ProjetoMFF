p1 = PVector(400,400)
p2 = PVector(400,400)
#v1 = PVector(0,0)
v2 = PVector(0,0)
m1 = 30000000
m2 = 100000
cont=0
G = 0.07

def setup():
    size(800,800)

def draw():
    global p1, v1, m1, p2, m2, v2, cont, oldt
    background(255)
    fill(0)
    ellipse(p1.x,p1.y,30,30)
    ellipse(p2.x,p2.y,10,10)
    
    
    
    if mousePressed and cont==0:
        p2 = PVector(mouseX,mouseY)
        cont=1
        
    elif mousePressed:
        line(p2.x,p2.y,mouseX,mouseY)
        v2= PVector.sub(p2,PVector(mouseX,mouseY))
        oldt = millis()/1000.0
        
            

            
    else:
        cont=0
        if p1!=p2:
            #cálculo da força de gravitação sobre o corpo 1
            Fg = PVector.sub(p2, p1)
            d = Fg.mag()
            if d<15:
                Fg=PVector(0,0)
                p2=p1

            else:
                Fg.mult(G*m1*m2/(d*d*d))
                #tempo transcorrido desde último desenho
                t = millis()/1000.00
                dt = t - oldt
                oldt = t
                #atualização da posição de cada corpo
                #dp1 = v1.copy()
                #dp1.mult(dt)
                #p1.add(dp1)
                dp2 = v2.copy()
                dp2.mult(dt)
                p2.add(dp2)
                #variação de velocidade para cada corpo (força*delta(t)/masssa)
                a1 = PVector.mult(Fg, dt/m1)
                a2 = PVector.mult(Fg, -dt/m2)
                #atualização das velocidades
                #v1.add(a1)
                v2.add(a2)
        
