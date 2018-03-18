import simplegui
import random
no=[0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7]
poli=[True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True]
flag=True
a,x=0,50
tx=5
ty=80
x=0
state=0
count=0
turn=0
li=[]
random.shuffle(no)
restart_flag=True
def restart():
    global restart_flag
    restart_flag=not restart_flag
def msc(k):
    global flag,poli,count,li,state,no,i1,i2,turn
    pos=k[0]//50
    #flag=not flag
    poli[pos]=not poli[pos]
    if state==0:
        state=1
        i1=pos
    elif state==1:
        state=2
        i2=pos
        turn+=1
        label1.set_text("try:"+str(turn))
    else:
        if i2!=pos:
            state=1
            if no[i1]!=no[i2]:
                poli[i1]=True
                poli[i2]=True
            
            i1=pos
def draw(canvas):
    global a,x,flag,l,no,tx,ty,poli,turn,restart_flag
    count=0
    b=0
    tx=5
    msg="Congratulations you have solved it in"+str(turn)+"attempts"
    if restart_flag==True:
        for i in no:
            canvas.draw_text(str(i),[tx,ty],90,"white")
            tx+=50
            x=0
            for i in range(16):
                if poli[i]==True:
                    canvas.draw_polygon(([x,0],[x+50,0],[x+50,100],[x,100]),2,"red","green")
                x+=50
        for i in range(16):
            if poli[i]==False:
                count+=1
        if(count==16):
            canvas.draw_text(msg,[0,50],45,"white")
frame=simplegui.create_frame("home",800,100)
frame.set_draw_handler(draw)
label1=frame.add_label("try:"+str(turn))
frame.set_mouseclick_handler(msc)
frame.add_button("reset",restart)
frame.start()