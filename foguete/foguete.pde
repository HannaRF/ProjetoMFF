double m, dm, vj, oldt, v, d, GM, F, dt, h, mc, empuxo;
PImage plat, r1, r2, r3, r4, r, boom;
String camada;

void setup(){
  size(800,800); mc = 100000; m = 300000; dm = -4000; vj = -45; oldt = millis()/1000F; v = 0; d = 6371000; GM = -398576060000000L;
  plat=loadImage("grama.png"); r1=loadImage("r1.gif"); r2=loadImage("r2.gif"); r3=loadImage("r3.gif"); r4=loadImage("r4.gif"); r=loadImage("r.png"); boom=loadImage("boom.png");
}
void draw(){
  background(max((int)(127.2-h*0.0000255),0), max(0,max((int)(255-h*0.000034),(int)(170-h*0.000017))), max(min((int)(510-0.000051*h),255),0));
  if(h<400) image(plat,0,(float)(400+h));
  empuxo=0;
  if(m>mc & v>0){
    empuxo = vj*dm;
    switch((millis()/10)%4){
      case 0: image(r1,250,250); break;
      case 1: image(r2,250,250); break;
      case 2: image(r3,250,250); break;
      case 3: image(r4,250,250); break;
    }
  }
  else image(r,250,250);
  if(frameCount>100 & h<=0){
      if(v<=0) image(boom,300,275);
      h = 0;
  }
  else{
    dt=millis()/1000F-oldt; oldt = millis()/1000F;
    if(m>mc){
      F = (vj*dm/dt + GM*m/(d*d)); m += dm;
    }
    else F = GM*m/(d*d);
    v += F*dt/m; d += v*dt; h = d-6371000;
  }
  stroke(0); fill(255,255,255,150); rect(100,20,600,80);
  textSize(17); fill(0); text(String.format("Altitude: %.1f km      Empuxo: %.0f kN      Velocidade: %.1f km/s",h/1000, empuxo/1000, v/1000),110,50);
  if(h<14500) camada = "Troposfera"; else if(h<50000) camada = "Estratosfera"; else if(h<85000) camada = "Mesosfera"; else if(h<600000) camada = "Termosfera"; else if(h<10000000) camada = "Exosfera"; else camada = "Espaço interestelar";
  text("Camada atual da atmosfera: "+camada, 230, 80);
}
