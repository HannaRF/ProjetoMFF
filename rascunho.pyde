def draw():
    global p0, v0, m0, p1, m1, v1, cont, oldt ,cont_corpos,r1
    background(255)
    fill(0)
    ellipse(p0.x,p0.y,30,30)
    ellipse(p1.x,p1.y,r1,r1)
    
    println(r1)
    
    if keyPressed:
        if key == 'w' or key == 'W':
            r1+=10
    
    
    if mousePressed and cont==0:
        p1 = PVector(mouseX,mouseY)
        cont=1
        cont_corpos+=1
    
    elif mousePressed:
        line(p1.x,p1.y,mouseX,mouseY)
        v1= PVector.sub(p1,PVector(mouseX,mouseY))
        oldt = millis()/1000.0
        
            

            
    else:
        cont=0
        if p0!=p1:
            #cálculo da força de gravitação sobre o corpo 
            Fg = PVector.sub(p1, p0)
            d = Fg.mag()
            if d<15 or p1.x < 0 or p1.y < 0 or p1.x > 800 or p1.y > 800:
                Fg=PVector(0,0)
                p1=p0
                cont_corpos-=1

            else:
                Fg.mult(G*m0*m1/(d*d*d))
                t = millis()/1000.00
                dt = t - oldt
                oldt = t
                dp1 = v1.copy()
                dp1.mult(dt)
                p1.add(dp1)
                #variação de velocidade para cada corpo (força*delta(t)/masssa)
                a0 = PVector.mult(Fg, dt/m0)
                a1 = PVector.mult(Fg, -dt/m1)
                #atualização das velocidades
                v1.add(a1)
                
