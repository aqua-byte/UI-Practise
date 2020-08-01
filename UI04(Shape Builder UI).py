###############################################################################################################
#################################### SHAPE BUILDER UI  #####################################################



#Author:Himanshi Ahuja
#Email:himansheeahuja@gmail.com

import maya.cmds as cmds
import maya.mel as mel


if cmds.window('Win',exists=True):
    cmds.deleteUI('Win')
if cmds.windowPref('Win',exists=True):
    cmds.windowPref('Win',r=True)    
    
cmds.window('Win',title='Shape Builder')

form = cmds.formLayout('form01',bgc =[(.190),(.194),(.194)])

Text_Create=cmds.text('txt01',label='Create Control')
Button01 = cmds.symbolButton('b1',i='circle.png')
Button02 = cmds.symbolButton('b2',i='square.png',c='square)')
Button03 = cmds.symbolButton('b3',i='arrowDown.png',c='arrowDown()')
Button04 = cmds.symbolButton('b4',i='arrowLeft.png',c='arrowLeft()')
Button05 = cmds.symbolButton('b5',i='arrowRight.png',c='arrowRight()')
Button06 = cmds.symbolButton('b6',i='arrowUp.png',c='arrowUp()')
Button07 = cmds.symbolButton('b7',i='baseLattice.svg',c='baseLattice()',h=35,w=45)
Button08 = cmds.symbolButton('b8',i='checkboxOff.png',c='checkboxOff()')
Button09 = cmds.symbolButton('b9',i='clip_move.png',c='clip_move()')
Button10 = cmds.symbolButton('b10',i='clip_move_cross.png',c='clip_move_cross()')
Button11 = cmds.symbolButton('b11',i='clockwise.png',c='clockwise()')
Button12 = cmds.symbolButton('b12',i='cylinder.png',c='hsNothing()')
Button13 = cmds.symbolButton('b13',i='locator.png',c='locator()')
Button14 = cmds.symbolButton('b14',i='moveWindow.png',c='moveWindow()')
Button15 = cmds.symbolButton('b15',i='plane.png',c='plane()')
#Button16 = cmds.symbolButton('b16',i='cone.png',c='cone()')




Text_Color=cmds.text('txt02',label='Control Color')



IT01=cmds.iconTextButton(bgc=[0, 0, 0], rpt=True,w=27,h=23)
IT02=cmds.iconTextButton(bgc=[0.247, 0.247, 0.247], rpt=True,w=27,h=23) 
IT03=cmds.iconTextButton(bgc=[0.498, 0.498, 0.498], rpt=True,w=27,h=23) 
IT04=cmds.iconTextButton(bgc=[0.608, 0, 0.157], rpt=True,w=27,h=23)
IT05=cmds.iconTextButton(bgc=[0, 0, 1], rpt=True,w=27,h=23)
IT06=cmds.iconTextButton(bgc=[0, 0.275, 0.094], rpt=True,w=27,h=23)
IT07=cmds.iconTextButton(bgc=[0.145, 0, 0.263], rpt=True,w=27,h=23)
IT08=cmds.iconTextButton(bgc=[0.78, 0, 0.78], rpt=True,w=27,h=23)
IT09=cmds.iconTextButton(bgc=[0.537, 0.278, 0.2], rpt=True,w=27,h=23) 
IT10=cmds.iconTextButton(bgc=[0.243, 0.133, 0.122], rpt=True,w=27,h=23) 
IT11=cmds.iconTextButton(bgc=[0.6, 0.145, 0], rpt=True,w=27,h=23) 
IT12=cmds.iconTextButton(bgc=[1, 0, 0], rpt=True,w=27,h=23)
IT13=cmds.iconTextButton(bgc=[0, 1, 0], rpt=True,w=27,h=23)
IT14=cmds.iconTextButton(bgc=[0, 0.255, 0.6], rpt=True,w=27,h=23)
IT15=cmds.iconTextButton(bgc=[1, 1, 1], rpt=True,w=27,h=23)
IT16=cmds.iconTextButton(bgc=[1, 1, 0], rpt=True,w=27,h=23)
IT17=cmds.iconTextButton(bgc=[0.388, 0.863, 1], rpt=True,w=27,h=23)
IT18=cmds.iconTextButton(bgc=[0.263, 1, 0.635], rpt=True,w=27,h=23)
IT19=cmds.iconTextButton(bgc=[1, 0.686, 0.686], rpt=True,w=27,h=23)
IT20=cmds.iconTextButton(bgc=[0.89, 0.675, 0.475], rpt=True,w=27,h=23)
IT21=cmds.iconTextButton(bgc=[1, 1, 0.384], rpt=True,w=27,h=23)
IT22=cmds.iconTextButton(bgc=[0, 0.6, 0.325], rpt=True,w=27,h=23)
IT23=cmds.iconTextButton(bgc=[0.627, 0.412, 0.188], rpt=True,w=27,h=23)
IT24=cmds.iconTextButton(bgc=[0.62, 0.627, 0.188], rpt=True,w=27,h=23)
IT25=cmds.iconTextButton(bgc=[0.408, 0.627, 0.188], rpt=True,w=27,h=23)
IT26=cmds.iconTextButton(bgc=[0.188, 0.627, 0.365], rpt=True ,w=27,h=23)
IT27=cmds.iconTextButton(bgc=[0.188, 0.627, 0.627], rpt=True ,w=27,h=23)
IT28=cmds.iconTextButton(bgc=[0.188, 0.404, 0.627], rpt=True,w=27,h=23)
#cmds.iconTextButton(bgc=[0.435, 0.188, 0.627], rpt=True,w=27,h=23)
        
Button_Reset=cmds.button('btnRst',l='Reset Color',bgc=[(.2),(.5),(.4)])

Button_Size=cmds.text('txt03',label='Control Size')       
Button_Slide=cmds.intSliderGrp('sizeSlider',l='Size',min=1,f=True,h=30,w=325)
        
Button_CP=cmds.button('btnCP',l=('Center Pivot'),c='centerPivot()',bgc=[(.2),(.5),(.4)])
Button_DH=cmds.button('btnDH',l=('Delete History'),c='deleteHistory()',bgc=[(.2),(.5),(.4)])
Button_FT=cmds.button('btnPT',l=('Freeze'),c='freezeTransform()',bgc=[(.2),(.5),(.4)],w=69)

Text_Placement=cmds.text('txt04',l='Controller Placement')
Bx_pOrigin=cmds.checkBox(l='Origin')
Bx_pMesh=cmds.checkBox(l='Mesh')

Text_Lock=cmds.text('txt05',l='Lock Attributes Of Controller')
Bx_tX=cmds.checkBox(l='TranslateX')
Bx_tY=cmds.checkBox(l='TranslateY')
Bx_tZ=cmds.checkBox(l='TranslateZ')

Bx_sX=cmds.checkBox(l='ScaleX')
Bx_sY=cmds.checkBox(l='ScaleY')
Bx_sZ=cmds.checkBox(l='ScaleZ')

Bx_rX=cmds.checkBox(l='RotateX')
Bx_rY=cmds.checkBox(l='RotateY')
Bx_rZ=cmds.checkBox(l='RotateZ')

Button_Dle=cmds.button('btnDel',l=('Delete Control'),c='deleteControl()',bgc=[(.2),(.5),(.4)],h=35,w=120)

cmds.formLayout('form01',edit=True,attachForm=[(Text_Create,'top',5),
(Text_Create,'left',60),
(Button01,'top',25),
(Button01,'left',10),
(Button03,'top',35),
(Button02,'top',25),
(Button04,'top',65),
(Button04,'left',20),
(Button05,'top',65),
(Button06,'top',65),
(Button07,'top',85),
(Button07,'left',5),
(Button08,'top',88),
(Button09,'top',90),
(Button10,'top',25),
(Button10,'left',175),
(Button13,'left',132),
(Button13,'top',22),
(Button11,'top',51),
(Button14,'top',52),
(Button12,'top',80),
(Button15,'top',80),
(Text_Color,'top',130),
(Text_Color,'left',70),
(IT01,'top',150),
(IT01,'left',10),
(IT02,'top',150),
(IT03,'top',150),
(IT04,'top',150),
(IT05,'top',150.3),
(IT06,'top',150.3),
(IT07,'top',150.3),
(IT08,'top',174.5),
(IT09,'top',174.5),
(IT08,'left',10),
(IT10,'top',174.5),
(IT11,'top',174.5),
(IT12,'top',174.5),
(IT13,'top',174.5),
(IT14,'top',174.5),
(IT15,'top',196),
(IT15,'left',10.5),
(IT16,'top',196),
(IT17,'top',196),
(IT18,'top',196),
(IT19,'top',196),
(IT20,'top',196),
(IT21,'top',196),
(IT22,'left',10.5),
(IT22,'top',220),
(IT23,'top',220),
(IT24,'top',220),
(IT25,'top',220),
(IT26,'top',220),
(IT27,'top',220),
(IT28,'top',220),
(Button_Reset,'top',250),
(Button_Reset,'left',70),
(Button_Size,'top',330),
(Button_Slide,'top',290),
(Button_Slide,'left',-112),
(Button_Size,'left',75),
(Button_CP,'top',355),
(Button_DH,'top',355),
(Button_FT,'top',355),
(Button_CP,'left',12),
(Button_DH,'left',88),
(Button_FT,'left',175),
(Bx_pOrigin,'top',410),
(Bx_pMesh,'top',410),
(Bx_pMesh,'left',20),
(Bx_tX,'top',455),
(Bx_tX,'left',5),
(Bx_tY,'top',455),
(Bx_tZ,'top',455),
(Bx_sX,'top',495),
(Bx_sX,'left',5),
(Bx_sY,'top',495),
(Bx_sZ,'top',495),
(Bx_rX,'left',5),
(Bx_rX,'top',475),
(Bx_rY,'top',475),
(Bx_rZ,'top',475),
(Text_Placement,'left',50),
(Text_Placement,'top',390),
(Text_Lock,'top',435),
(Text_Lock,'left',50),
(Button_Dle,'left',65),
(Button_Dle,'bottom',5)
],

attachControl=[(Button02,'left',10,Button01),
(Button03,'left',15,Button02),
(Button05,'left',25,Button04),
(Button06,'left',40,Button05),
(Button08,'left',15,Button07),
(Button09,'left',15,Button08),
(Button11,'left',1,Button14),
(Button14,'left',15,Button06),
(Button12,'left',1,Button15),
(Button15,'left',5,Button09),
(IT02,'left',1,IT01),
(IT03,'left',1,IT02),
(IT04,'left',1,IT03),
(IT05,'left',1,IT04),
(IT06,'left',1,IT05),
(IT07,'left',1,IT06),
(IT09,'left',1,IT08),
(IT10,'left',1,IT09),
(IT11,'left',1,IT10),
(IT12,'left',1,IT11),
(IT13,'left',1,IT12),
(IT14,'left',1,IT13),
(IT16,'left',1,IT15),
(IT17,'left',1,IT16),
(IT18,'left',1,IT17),
(IT19,'left',1,IT18),
(IT20,'left',1,IT19),
(IT21,'left',1,IT20),
(IT23,'left',1,IT22),
(IT24,'left',1,IT23),
(IT25,'left',1,IT24),
(IT26,'left',1,IT25),
(IT27,'left',1,IT26),
(IT28,'left',1,IT27),
(Bx_tY,'left',10,Bx_tX),
(Bx_tZ,'left',10,Bx_tY),
(Bx_sY,'left',30,Bx_sX),
(Bx_sZ,'left',30,Bx_sY),
(Bx_rY,'left',22,Bx_rX),
(Bx_rZ,'left',21,Bx_rY),
(Bx_pOrigin,'left',30,Bx_pMesh),

])
cmds.showWindow('Win')
