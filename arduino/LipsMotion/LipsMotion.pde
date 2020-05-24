int[][] curve={{0,0},{0,0},{0,0},{0,0}};
int gap;
int gap2;
int baseline;
int count=0;

void setup(){
  size(800,600);
  baseline=height/3;
  gap=height/50;
  //gap2=height/150;

    
}

//void animation(){
//  for(int i=1;i<6;i++){
//  Lips(i);
//  }
//}
void draw(){
  background(0);
  fill(255);
  stroke(200);
  strokeWeight(25);
  Lips(count);
  
  beginShape();
  curveVertex(width,  baseline-gap+curve[0][1]);
  //curveVertex(width/2,  baseline-gap+curve[0][1]);
  curveVertex(width/2-5,  baseline-gap+curve[0][1]);
  curveVertex(width/3-curve[2][0],  baseline+curve[2][1]);
  curveVertex(width/2,  baseline+gap+curve[1][1]);//bottom
  curveVertex(width*2/3+curve[3][0],  baseline+curve[3][1]);
  curveVertex(width/2+5,  baseline-gap+curve[0][1]);
  //curveVertex(width/2,  baseline-gap+curve[0][1]);
  curveVertex(0,  baseline-gap+curve[0][1]);
  endShape(CLOSE);
  save(str(count)+".png");
  delay(300);
  if(count<12){
  count++;
  }
  //else{count=0;}
  
  
}

void Lips(int num){
 switch(num){
   case 1:
   baseline=height/3;
   gap=height/50;
   curve[0][1]=0;
   curve[1][1]=0;
   curve[2][0]=0;
   curve[2][1]=0;
   curve[3][0]=0;
   curve[3][1]=0;
   
   break;
   
   case 2: 
   gap=height/20;
   baseline=height/3+18;
   curve[0][1]=0;
   curve[1][1]=0;
   curve[2][0]=0;
   curve[2][1]=0;
   curve[3][0]=0;
   curve[3][1]=0;
   break;
   
   case 3:
   gap=height/15;
   baseline=height/3+10+18;
   curve[1][1]=30;   
   curve[0][1]=0;
   curve[2][0]=0;
   curve[2][1]=0;
   curve[3][0]=0;
   curve[3][1]=0;
   break;
   
   case 4:
   gap=height/10;
   baseline=height/3+30+18;
   curve[1][1]=60;
   curve[0][1]=0;
   curve[2][0]=0;
   curve[2][1]=0;
   curve[3][0]=0;
   curve[3][1]=0;
   break;
   
   case 5:
   gap=height/8;
   baseline=height/3+45+18;
   curve[1][1]=90;
   curve[0][1]=0;
   curve[2][0]=0;
   curve[2][1]=0;
   curve[3][0]=0;
   curve[3][1]=0;
   break;
   
   case 6:
   gap=height/15;
   baseline=height/3+10+18+30;
   curve[0][1]=-40;
   curve[1][1]=-20;   
   curve[2][0]=-80;
   curve[2][1]=0;
   curve[3][0]=-80;
   curve[3][1]=0;
   //strokeWeight(40);
   break;
   
   case 7:
   gap=height/20;
   baseline=height/3+18+25;
   curve[0][1]=-10;
   curve[1][1]=5;
   curve[2][0]=-50;
   curve[2][1]=0;
   curve[3][0]=-50;
   curve[3][1]=0;
   break;
   
   case 8:
   baseline=height/3;
   gap=height/50;
   curve[0][1]=0;
   curve[1][1]=50;
   curve[2][0]=30;
   curve[2][1]=-3;
   curve[3][0]=30;
   curve[3][1]=-3;
   break;
   
   case 9:
   baseline=height/3;
   gap=height/50;
   curve[0][1]=20;
   curve[1][1]=20;
   curve[2][0]=30;
   curve[2][1]=-3;
   curve[3][0]=30;
   curve[3][1]=-3;
   break;
   
   case 0:
   baseline=height/3;
   gap=height/50;
   curve[0][1]=0;
   curve[1][1]=120;
   curve[2][0]=30;
   curve[2][1]=-3;
   curve[3][0]=30;
   curve[3][1]=-3;
   break;
   
   case 10:
   baseline=height/3;
   gap=height/50;
   curve[0][1]=20;
   curve[1][1]=20;
   curve[2][0]=30;
   curve[2][1]=-3;
   curve[3][0]=30;
   curve[3][1]=-3;
   break;
   
   case 11:
   baseline=height/3;
   gap=height/50;
   curve[0][1]=40;
   curve[1][1]=40;
   curve[2][0]=30;
   curve[2][1]=-3;
   curve[3][0]=-50;
   curve[3][1]=20;
   break;
   
   case 12:
   baseline=height/3;
   gap=height/50;
   curve[0][1]=40;
   curve[1][1]=40;
   curve[2][0]=-50;
   curve[2][1]=20;
   curve[3][0]=30;
   curve[3][1]=-3;
   break;
 }
}
