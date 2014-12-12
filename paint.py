#Ioana Crant
#yuwei
#---------------TOOLS--------------------#
def penciltool(color,x1,y1,x2,y2):
    draw.aaline(screen,color,(x1,y1),(x2,y2)) #draws a pretty line from the
                                              #previous point to the current
def brushtool(color,x1,y1,x2,y2,size):
    sizeradii={1:3,2:5,3:7,4:10,5:13}  #dictionary for translating xs-xl to radii
    deltax=x2-x1 #width of triangle
    deltay=y2-y1 #height of triangle
    maxdel=max(abs(deltax),abs(deltay))  #which one's longer
    for i in range(int(maxdel)):
        x=int(x1+(i*deltax)/maxdel) #goes up in increments of 1 or x/y (less than 1)
        y=int(y1+(i*deltay)/maxdel) #goes up in increments of 1 or y/x (less than 1)
        draw.circle(screen,color,(x,y),sizeradii[size]) #draws a circle at each increment on the hypotenuse of the triangle made by the previous and current point
    draw.circle(screen,color,(x1,y1),sizeradii[size]) #draws a circle if you click and don't move
    
def linetool(color,clickx,clicky,x1,y1,size):
    sizeradii={1:2,2:4,3:7,4:10,5:12}
    screen.blit(screencopy,(0,0)) #only 1 line is draw
    draw.line(screen,color,(clickx,clicky),(x1,y1),sizeradii[size]) #draws line from where you clicked to where your mouse is
    
def rectangletool(color,seccolor,clickx,clicky,x1,y1,size,mode):
    sizeradii={1:1,2:3,3:6,4:9,5:12}
    if mode=="empty":
        screen.blit(screencopy,(0,0)) 
        draw.rect(screen,color,(clickx,clicky,x1-clickx,y1-clicky),sizeradii[size]) #width and height can be negative
    elif mode=="filled":
        screen.blit(screencopy,(0,0))
        draw.rect(screen,color,(clickx,clicky,x1-clickx,y1-clicky))
    elif mode=="border":
        screen.blit(screencopy,(0,0))
        drawingrect=Rect(clickx,clicky,x1-clickx,y1-clicky)
        drawingrect.normalize() #makes life easier for lining things up
        draw.rect(screen,seccolor,(drawingrect[0]+sizeradii[size]//2,drawingrect[1]+sizeradii[size]//2,drawingrect[2]-sizeradii[size],drawingrect[3]-sizeradii[size])) #INSIDE rectangle,lines up inside the bigger one 
        draw.rect(screen,color,drawingrect,sizeradii[size]) #OUTSIDE
    
def ellipsetool(color,seccolor,clickx,clicky,x1,y1,size,mode): #draws ellipses, unfilled, filled, and filled with border
    try: 
        sizeradii={1:1,2:3,3:6,4:9,5:12}
        if mode=="empty":
            screen.blit(screencopy,(0,0))
            draw.ellipse(screen,color,(min(clickx,x1),min(clicky,y1),abs(x1-clickx),abs(y1-clicky)),sizeradii[size])
        elif mode=="filled":
            screen.blit(screencopy,(0,0))
            draw.ellipse(screen,color,(min(clickx,x1),min(clicky,y1),abs(x1-clickx),abs(y1-clicky)))
        elif mode=="border":
            screen.blit(screencopy,(0,0))
            draw.ellipse(screen,seccolor,(min(clickx,x1)+sizeradii[size],min(clicky,y1)+sizeradii[size],abs(x1-clickx)-(2*sizeradii[size]),abs(y1-clicky)-(2*sizeradii[size])))
            draw.ellipse(screen,color,(min(clickx,x1),min(clicky,y1),abs(x1-clickx),abs(y1-clicky)),sizeradii[size])
    except: #if the thickness is greater than the height, and there's an error
        return #don't do anything
    
def spraypainttool(color,x1,y1,size):
    sizeradii={1:5,2:10,3:15,4:20,5:25}
    for i in range(15):
        x,y=randint(x1-sizeradii[size],x1+sizeradii[size]),randint(y1-sizeradii[size],y1+sizeradii[size])
        if ((x-x1)**2+(y-y1)**2)**0.5<sizeradii[size]: #makes it into a circle
            screen.set_at((x,y),color)
            
def buckettool(color,x1,y1):
    ccol=screen.get_at((x1,y1))
    if ccol==color: #if the color you clicked on is the color you want to change it to, do nothing
        return
    points=[(x1,y1)]
    while len(points)>0:
        x,y=points.pop()
        if screen.get_at((x,y))==ccol: #takes only the pixels inside the 1 shape you clicked inside
            screen.set_at((x,y),color)
            points += [(x+1,y),(x-1,y),(x,y+1),(x,y-1)] #adds the surrounding

def eyedroppertool():
    global col
    global seccol
    if mb[0]==1:
        col=screen.get_at((mx,my))
    if mb[2]==1:
        seccol=screen.get_at((mx,my))

def gradienttool(color,secondcolor,linestart,lineend,ccol):
    draw.line(screen,ccol,linestart,lineend) #draws line in background color so it doesn't show up on the gradient
    diff=(color[0]-secondcolor[0],color[1]-secondcolor[1],color[2]-secondcolor[2]) #differences in RGB values
    points=[(linestart[0],linestart[1])] #

    while len(points)>0:
        x,y=points.pop()
        if screen.get_at((x,y))==ccol:
            ratio=(x-linestart[0])/float(lineend[0]-linestart[0])
            if ratio<=0:  #this happens if x-linestart is neg, meaning its before the beginning of the line
                screen.set_at((x,y),color) #you set it as your first color
            elif ratio>=1: #this happens if x-linestart is bigger than the length, meaning its after the end of the line
                screen.set_at((x,y),secondcolor)
            elif 0<ratio<1:
                coldiff=(int(diff[0]*ratio),int(diff[1]*ratio),int(diff[2]*ratio))
                screen.set_at((x,y),(abs(color[0]-coldiff[0]),abs(color[1]-coldiff[1]),abs(color[2]-coldiff[2]))) #color is in  ratio of distance from linestart to entire distance
            points += [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
    
            
def cleartool():
    screen.fill((255,255,255),canvasRect)

def getName(mode):
    ans = ""                    # final answer will be built one letter at a time.
    spiderfonttype = font.Font("HOMOARAK.TTF", 16)
    back = screen.copy()        # copy screen so we can replace it when done
    textArea = Rect(200,150,400,25) # make changes here.
    
    pics = glob("*.bmp")+glob("*.jpg")+glob("*.png")
    n = len(pics)
    if mode=="load": #doesn't show drop down menu when saving
        choiceArea = Rect(textArea.x,textArea.y+textArea.height+5,textArea.width,n*textArea.height) #makes the stufff below
        draw.rect(screen,(202,104,95),choiceArea)        # draw the text window and the text.
        draw.rect(screen,(0,0,0),choiceArea,2)        # draw the text window and the text.
        for i in range(n):
            txtPic = spiderfonttype.render(pics[i], True, (0,0,0))   #
            screen.blit(txtPic,(textArea.x+2,textArea.height*i+choiceArea.y+3))
    screen.set_clip(textArea)    
    typing = True
    while typing:
        for e in event.get():
            if e.type == QUIT:
                event.post(e)   # puts QUIT back in event list so main quits
                return ""
            if e.type == KEYDOWN:
                if e.key == K_BACKSPACE:    # remove last letter
                    if len(ans)>0:
                        ans = ans[:-1]
                elif e.key == K_KP_ENTER or e.key == K_RETURN : 
                    typing = False
                elif e.key < 256:
                    ans += e.unicode       # add character to ans
                    
        txtPic = spiderfonttype.render(ans, True, (0,0,0))   #
        draw.rect(screen,(255,255,255),textArea)        # draw the text window and the text.
        draw.rect(screen,(0,0,0),textArea,2)            #
        screen.blit(txtPic,(textArea.x+3,textArea.y+8))
        
        display.flip()
    screen.set_clip(None)
    screen.blit(back,(0,0))
    return ans
    
#-----------------------------------------#    

from pygame import *
from random import *
from glob import *
import datetime

font.init()
mixer.init()

screen=display.set_mode((1024,768))

background=image.load("icons/spidermanbackground.png")
screen.blit(background,(0,0))

canvasRect=Rect(10,10,750,500)
draw.rect(screen, (255,255,255),canvasRect) #draws white canvas for drawing in

#font stuff
spiderfont=font.Font("The Amazing Spider-Man.ttf", 50)

spiderfont2=font.Font("HOMOARAK.TTF", 12) #for coords
spiderfont2large=font.Font("HOMOARAK.TTF", 20) #for coords
title=spiderfont.render("SPIDER-PAINT",True,(0,0,0))
screen.blit(title,(765,50))

display.set_caption("SPIDER-PAINT")

mixer.music.load("yuweis beautiful soundtrack.mp3") 
mixer.music.play(-1)
playicon=image.load("icons/play.png")
pauseicon=image.load("icons/pause.png")
                    
musicbox=Rect(970,8,35,35)

playorpause="play"    #keep track of when its playing and when its not

timebar=image.load("icons/timeback.png")

screencopy=screen.copy()

mx2,my2=mouse.get_pos()
sx,sy=mouse.get_pos()

col=(0,0,1)
seccol=(255,255,254) #just trust me on this 

undolist=[screen.subsurface(canvasRect).copy()]
redolist=[]

size=3 #instead of xs-xl, use 1-5 
sizetonumber={1:"XS",2:"S",3:"M",4:"L",5:"XL"}

coordbar=image.load("icons/cord bar.png")

toolrects=[Rect(796,120,50,50),Rect(869,120,50,50),Rect(942,120,50,50),Rect(796,190,50,50),Rect(869,190,50,50),Rect(942,190,50,50),Rect(796,260,50,50),Rect(869,260,50,50),Rect(942,260,50,50),Rect(796,330,50,50),Rect(869,330,50,50),Rect(942,330,50,50)]
toolnames=["pencil","brush","line","rectangle","ellipse","spray","eraser","bucket","eyedropper","polygon","crop","gradient"]

tooloptionrects=[Rect(796,400,50,78),Rect(869,400,50,78),Rect(942,400,50,78)]
tooloptionnames=["empty","filled","border"]
tooloptionon=False #the 3 option thing at the bottom of the toolbar when you click on rectangle or ellipse

stamprects=[Rect(28,570,128,74),Rect(160,550,98,94),Rect(280,554,100,88),Rect(26,648,126,84),Rect(168,656,76,76),Rect(266,670,112,50),Rect(400,565,70,74),Rect(400,660,70,73)]
stampnames=["stamp1","stamp2","stamp3","stamp4","stamp5","stamp6","stamp7","stamp8"]
            
processrects=[Rect(604,544,126,32),Rect(604,586,126,32),Rect(604,628,126,32),Rect(604,670,126,32),Rect(604,712,126,32)]
processnames=["undo","redo","clear","save","load"]

#initializing stuff
tool="pencil"
mode="select"
toolnorm=[]
toolhover=[]
toolclick=[]
tooloptionnorm=[]
tooloptionhover=[]
tooloptionclick=[]
processnorm=[]
processhover=[]
processclick=[]
stamps=[]
stampthumbs=[]
###IMAGE LOADING###
#loads images
for t in toolnames:
    toolnorm+=[image.load("icons/"+t+" normal.png")]
    toolhover+=[image.load("icons/"+t+" hover.png")]
    toolclick+=[image.load("icons/"+t+" click.png")] 

for t in tooloptionnames:
    tooloptionnorm+=[image.load("icons/"+t+ " normal.png")]
    tooloptionhover+=[image.load("icons/"+t+" hover.png")]
    tooloptionclick+=[image.load("icons/"+t+" click.png")]

for s in stampnames:
    stamps+=[image.load("icons/"+s+".png")]
    stampthumbs+=[image.load("icons/"+s+" thumb.png")]

for p in processnames:
    processnorm+=[image.load("icons/"+p+" normal.png")]
    processhover+=[image.load("icons/"+p+" hover.png")]
    processclick+=[image.load("icons/"+p+" click.png")]

###END OF IMAGE LOADING###

for i in range(len(toolnames)):
    screen.blit(toolnorm[i],toolrects[i])  #blits starting toolbar
    
screen.blit(toolclick[0],toolrects[0]) #blits the selected pencil, in case the starting mx,my is in the canvas

for i in range(len(stampnames)):
    screen.blit(stampthumbs[i],stamprects[i]) #blits the stamps

for i in range(len(processnames)):
    screen.blit(processnorm[i],processrects[i]) #blits all the processes
    
paletteRect=Rect(766,580,253,174)


running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN:
        
            if evt.button==1 or evt.button==3:
                if tool != "crop":
                    screencopy=screen.copy() #allows crop to work
                sx,sy=mouse.get_pos()
                
            if evt.button==1:
                for processi in range(len(processrects)):
                    if processrects[processi].collidepoint(sx,sy):
                        
                        polypointslist=[] #if you click the polygon points reset
                        
                        if processnames[processi]=="undo":
                            if len(undolist)>1:
                                redolist.append(undolist.pop()) 
                                screen.blit(undolist[-1],canvasRect) #takes last one in the list and blits it on
                                
                        elif processnames[processi]=="redo":
                            if len(redolist)>0:
                                undolist.append(redolist.pop())
                            if len(undolist)>1:
                                screen.blit(undolist[-1],canvasRect)
                                
                        elif processnames[processi]=="clear":
                            cleartool()
                        elif processnames[processi]=="save":
                            filename=getName("save")

                            if "." not in filename:
                                filename+=".png"
                            elif filename[filename.index("."):] not in [".bmp",".tga",".png",".jpeg"]:
                                filename=filename[:filename.index(".")]
                                filename+=".png" #replaces weird ending with .png
                            
                            image.save(screen.subsurface(canvasRect),filename)

                        elif processnames[processi]=="load":
                            filename=getName("load")
                            screen.set_clip(canvasRect)
                            try:
                                loaded=image.load(filename)
                                screen.blit(loaded,(12,12))
                            except:
                                pass #doesn't do anything
                                
                            screen.set_clip(None) #the image only stays in the canvas

                if musicbox.collidepoint(sx,sy):
                    if playorpause=="play":
                        mixer.music.pause()
                        playorpause="pause"
                    elif playorpause=="pause":
                        mixer.music.unpause()
                        playorpause="play"
                            
            elif evt.button==4:
                size+=1
                if size>5:
                    size=5 #makes max size 5, or xl
            elif evt.button==5:
                size-=1
                if size<1:
                    size=1 #makes min size 1 or xs
         
        if evt.type==MOUSEBUTTONUP:
            if canvasRect.collidepoint(sx,sy): #only records the canvas if you did something in the canvas
                undolist.append(screen.subsurface(canvasRect).copy())
                
        if tool=="polygon":
            screen.set_clip(canvasRect)
            sizeradii={1:1,2:3,3:4,4:6,5:8}
            if len(polypointslist)>1:
                draw.lines(screen,col,False,polypointslist,sizeradii[size])
                if mb[0]==1:
                    screen.blit(screencopy,(0,0))
                    draw.line(screen,col,polypointslist[-1],(mx,my),sizeradii[size]) #drrawing from last point to where you are
                    
            if evt.type==MOUSEBUTTONUP and evt.button==1:
                polypointslist.append((mx,my))
                
            if evt.type==MOUSEBUTTONDOWN and evt.button==3:
                if len(polypointslist)>1:
                    draw.polygon(screen,col,polypointslist,sizeradii[size]) #rightclick to finish polygon, reset list of points 
                polypointslist=[]
            screen.set_clip(None)
            
        elif tool=="gradient":   
            if canvasRect.collidepoint(mx,my):
                if evt.type==MOUSEBUTTONDOWN:
                    clickcol=screen.get_at((sx,sy))
                    clicked=True
                if clicked:
                    if mb[0]==1:
                        screen.blit(screencopy,(0,0))
                        draw.line(screen,(0,0,0),(sx,sy),(mx,my))
                        
                    if evt.type==MOUSEBUTTONUP:
                        gradstart=(sx,sy) #where the line started
                        gradend=(mx,my)  #where the line ended
                        gradienttool(col,seccol,gradstart,gradend,clickcol)

    #out of the event loop now
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

    for rectci in range(len(toolrects)):
        if toolrects[rectci].collidepoint(sx,sy):
            
            tool=toolnames[rectci] #if you clicked on it, it becomes your tool

            polypointslist=[] #reset polygon points every time toolbar is pressed
            clicked=False #for gradient
            mode="select" #for crop tool
            if tool=="rectangle" or tool=="ellipse":
                tooloptionon=True #3 option thing shows up
                tooloption="empty" #default is empty
            else:
                tooloptionon=False
            
    for stampi in range(len(stamprects)):
        if stamprects[stampi].collidepoint(sx,sy):
            tool=stampnames[stampi]

    if tooloptionon==True:
        for i in range(len(tooloptionrects)):
            if tooloptionrects[i].collidepoint(sx,sy):
                    tooloption=tooloptionnames[i]            
            
    if canvasRect.collidepoint(mx,my)==False: #if the mouse isn't in the canvas (for efficiency)
        for i in range(len(toolnames)):
            screen.blit(toolnorm[i],toolrects[i])    #blits all the normal images
            if toolrects[i].collidepoint(mx,my): 
                screen.blit(toolhover[i],toolrects[i])    #blits the one you're hovering over      
        if tool[:5]!="stamp":
            screen.blit(toolclick[toolnames.index(tool)],toolrects[toolnames.index(tool)]) #blits the selected tool if not a stamp

        for i in range(len(processnames)):
            screen.blit(processnorm[i],processrects[i]) #blits all the process boxes
            if processrects[i].collidepoint(mx,my): #hover
                screen.blit(processhover[i],processrects[i])
            if mb[0]==1 and processrects[i].collidepoint(mx,my): #holding it down
                screen.blit(processclick[i],processrects[i])
                
        if tooloptionon:
            for i in range(len(tooloptionnorm)):
                screen.blit(tooloptionnorm[i],tooloptionrects[i])
                if tooloptionrects[i].collidepoint(mx,my): 
                    screen.blit(tooloptionhover[i],tooloptionrects[i])     
            screen.blit(tooloptionclick[tooloptionnames.index(tooloption)],tooloptionrects[tooloptionnames.index(tooloption)]) #blits the selected tooloption
                    
        else:
            draw.rect(screen,(0,0,0),(795,390,217,99))   #draws black box to make menu go away if you didn't click on it


                
                
    if canvasRect.collidepoint(mx,my) and canvasRect.collidepoint(sx,sy):
        screen.set_clip(canvasRect) #you can only do stuff in the canvas
        if mb[0]==1:
            if tool=="pencil":
                penciltool(col,mx2,my2,mx,my)
            elif tool=="brush":
                brushtool(col,mx,my,mx2,my2,size)
            elif tool=="line":
                linetool(col,sx,sy,mx,my,size)
            elif tool=="rectangle":
                rectangletool(col,seccol,sx,sy,mx,my,size,tooloption)
            elif tool=="ellipse":
                ellipsetool(col,seccol,sx,sy,mx,my,size,tooloption)
            elif tool=="spray":
                spraypainttool(col,mx,my,size)
            elif tool=="eraser":
                brushtool((255,255,255),mx,my,mx2,my2,size)
            elif tool=="bucket":
                buckettool(col,mx,my)
            elif tool=="eyedropper":
                eyedroppertool()
            elif tool[:5]=="stamp": #if its a stamp
                screen.blit(screencopy,(0,0))
                stampimage=stamps[int(tool[-1])-1]
                screen.blit(stampimage,(mx-(stampimage.get_width()/2),(my-(stampimage.get_height()/2)))) #holding it from the middle of the stamp 
                
        elif mb[2]==1: #doing everything with tthe second color
            if tool=="pencil":
                penciltool(seccol,mx2,my2,mx,my)
            elif tool=="brush":
                brushtool(seccol,mx2,my2,mx,my,size)
            elif tool=="line":
                linetool(seccol,sx,sy,mx,my,size)
            elif tool=="rectangle":
                rectangletool(seccol,col,sx,sy,mx,my,size,tooloption)
            elif tool=="ellipse":
                ellipsetool(seccol,col,sx,sy,mx,my,size,tooloption)
            elif tool=="spray":
                spraypainttool(seccol,mx,my,size)
            elif tool=="eraser":
                brushtool((255,255,255),mx,my,mx2,my2,size)
            elif tool=="bucket":
                buckettool(seccol,mx,my)
            elif tool=="eyedropper":
                eyedroppertool()
              
        if tool=="crop":
            if mode=="select":
               
                if mb[0]==1 :
                    
                    screen.blit(screencopy,(0,0))
                    draw.rect(screen,(100,100,100),(sx,sy,mx-sx,my-sy),1)   #draws your rectangle to select
                    
                else:
                    cropRect=Rect(sx,sy,mx-sx,my-sy)
                    
                    cropRect.normalize()                  #makes it all positive and stuff
                    
                    ocropRect=Rect(cropRect)  #creates a reference point independent of cropRect
                    cropee=screen.subsurface(cropRect).copy() #makes subsurface of selected rect

                    mode="selected"
                    
            elif mode=="selected":
                if evt.type==MOUSEBUTTONDOWN and cropRect.collidepoint(sx,sy):
                    offset=sx-cropRect[0],sy-cropRect[1]  #so you drag your rect. from where you clicked on it

                    leavecropRect=screen.subsurface(cropRect).copy() #where you left it off
                    
                    mode="drag"
                if evt.type==MOUSEBUTTONDOWN and cropRect.collidepoint(sx,sy)==False:
                    try:
                        endRect=screen.subsurface(Rect(cropRect[0]+1,cropRect[1]+1,cropRect[2]-2,cropRect[3]-2)).copy() #rect without the edges
                        screen.blit(screencopy,(0,0))
                        draw.rect(screen,(255,255,255),ocropRect) #drawing white overlap of original crop
                        screen.blit(endRect,cropRect)
                        screencopy=screen.copy() #so select mode doesn't blit the wrong screencopy
                    
                        mode="select"
                    except:
                        mode="selected"
                    

            elif mode=="drag":
                if mb[0]==1:
                    screen.blit(screencopy,(0,0))
                    draw.rect(screen,(255,255,255),ocropRect)
                    screen.blit(cropee,cropRect)
                    
                    cropRect.left=mx-offset[0] #moving rect positions to match
                    cropRect.top=my-offset[1]  #where the mouse is
                else:
                    mode="selected"

                    
     
       
                
        screen.set_clip(None) #you can do stuff outside of the canvas now :)
        
    if paletteRect.collidepoint(sx,sy):
        if mb[0]==1:
            col=screen.get_at((sx,sy))
        elif mb[2]==1:
            seccol=screen.get_at((sx,sy))   
     

    sx2,sy2=sx,sy
    mx2,my2=mx,my
    
    draw.rect(screen,col,(769,510,80,55)) #draws a rect
    draw.rect(screen,seccol,(849,510,30,55)) #draws the 2 color boxes
    
    screen.blit(coordbar,(898,509))
    coords=spiderfont2.render("("+str(mx)+","+str(my)+")",True,(255,255,255))
    sizewriting=spiderfont2large.render(str(sizetonumber[size]),True,(255,255,255))
    screen.blit(coords,(902,548))
    screen.blit(sizewriting,(950,517))
    
    draw.rect(screen,(0,0,0),canvasRect,5)  #outline of box isn't drawed over

    curtime=str(datetime.datetime.today())[11:16] #current time
    timewriting=spiderfont2large.render(curtime,True,(0,0,0))
    
    screen.blit(timebar,(850,10))
    screen.blit(timewriting,(860,15))
    if playorpause=="play":
        screen.blit(pauseicon,musicbox)
    elif playorpause=="pause":
        screen.blit(playicon,musicbox)
   
    display.flip()
quit()
