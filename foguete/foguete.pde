double m, dm, vj, oldt, v, d, GM, F, dt, h, mc, empuxo, res, den, apogeu;
PImage plat, r1, r2, r3, r4, r, boom;
String camada;

void setup(){
  //Itens configuráveis da simulação
  den = 1; //Densidade da atmosfera medida em atm
  mc = 100000; //Massa de controle do foguete, ou seja, massa sem combustível, em kg
  m = 300000; //Massa total do foguete com combustível em kg
  dm = -400; //Consumo do propulsor, medido em kg de combustível por segundo
  vj = -10000; //Velocidade de ejeção do propulsor em m/s
  
  //Demais partes da configuração
  size(800,800); //Configuração da tela
  oldt = millis()/1000F; //Armazenamento do tempo de inicio da execussão
  v = 0; //Setando velocidade inicial nula
  d = 6371000; //Setando distância como raio da terra em metros (usado para calcular atração gravitacional)
  GM = -398576060000000L; //Constante dada pelo produto massa da terra e a constante gravitacional
  apogeu = 0; //Setando ponto máximo da trajetória inicialmente nulo
  
  //Carregamento de imagens para a simulação
  plat=loadImage("grama.png"); boom=loadImage("boom.png");
  r1=loadImage("r1.gif"); r2=loadImage("r2.gif"); r3=loadImage("r3.gif"); r4=loadImage("r4.gif"); r=loadImage("r.png");
}



void draw(){
  //Definição do background em relação à altitude (h)
  background(max((int)(127.2-h*0.0000255),0), max(0,max((int)(255-h*0.000034),(int)(170-h*0.000017))), max(min((int)(510-0.000051*h),255),0));
  if(h<400) image(plat,0,(float)(400+h)); //Desenho do gramado
  empuxo=0; //Setando empuxo do propulsor como zero
  if(m>mc & v>0){ //Verificando condição de queima 
    empuxo = vj*dm; //Calculando empuxo como velocidade de ejeção(m/s) vezes o consumo de combustível(kg/s) em N
    switch((millis()/10)%4){ //Desenhando de forma animada o foguete em processo de queima
      case 0: image(r1,250,250); break;
      case 1: image(r2,250,250); break;
      case 2: image(r3,250,250); break;
      case 3: image(r4,250,250); break;
    }
  }
  else image(r,250,250); //Caso finalizado o processo de queima
  if(frameCount>100 & h<=0){ //Verifica se houve colisão brusca
      if(v<=-100) image(boom,300,275); //Desenha explosão
      h = 0; //Fixa o valor da altitude em contato com o solo
  }
  else{ //Continua em voo, realiza os cálculos
    dt=millis()/1000F-oldt; oldt = millis()/1000F; //Encontrando e armazenando dt
    //Multiplicador a seguir obtido com uma estimativa de coeficiente de aerodinâmica e área de secção de superfície do foguete
    res = min((int)(5*v*v*(1-d/1000000)*den),0); //Calculando a força de resistência do ar
    if(v<0) res = -res; //Inverte resistência caso o foguete esteja em queda
    //Calculando a força resultande no foguete
    if(m>mc){
      F = (vj*dm/dt + GM*m/(d*d) + res); m += dm;
    }
    else F = GM*m/(d*d) + res;
    v += F*dt/m; //Atualizando velocidade
    d += v*dt; //Atualizando distância ao centro de massa terrestre
    h = d-6371000; //Atualizando altitude
    if(h>apogeu) apogeu=h; //Atualizando apogeu
  }
  //Finalizando desenhos
  stroke(0); fill(255,255,255,150); rect(20,20,760,80);
  textSize(17); fill(0); text(String.format("Empuxo: %.3f kN      Velocidade: %.3f km/s      Resistência: %.3f kN",empuxo/1000, v/1000, res/1000),30,50);
  if(h<14500) camada = "Troposfera"; else if(h<50000) camada = "Estratosfera"; else if(h<85000) camada = "Mesosfera"; else if(h<600000) camada = "Termosfera"; else if(h<10000000) camada = "Exosfera"; else camada = "Espaço interestelar";
  text(String.format("Altitude: %.3f km      Camada : %s      Apogeu: %.2f km      ",h/1000, camada, apogeu/1000), 30, 80);
}
