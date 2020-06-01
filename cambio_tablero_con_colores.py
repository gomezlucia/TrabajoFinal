import PySimpleGUI as sg
import random

def letra_elegida(letra):
	eleccion=random.choice(letra)
	letra.remove(eleccion)
	return eleccion

def comprobar(elem):
	print('texto:',elem.GetText())
	if(elem.GetText()==''):
		print('si es')
		elem.Update(current_button_selected)

def button(name,key ):
	return (sg.Button(name,button_color=color_button,size=tam_button,key=key),name)
def definir(inicio,ini,inicial):
	posi=True
	lista=[]
	print(inicio)
	if (inicio):
		print('hola')
		lista.append(ini.GetText())
		valor=inicial+1
		sig=window.FindElement(valor)
		sumo=1
		if(comprobar(sig,2)!=True):
			valor=inicial+10
			sig=window.FindElement(valor)
			sumo=10
			if(comprobar(sig,2)!=True):
				posi=False
			else:
				lista.append(sig.GetText())
		else:
			lista.append(sig.GetText())
		while(posi==True)and(valor+sumo<100):
			print('while')
			valor+=sumo
			sig=window.FindElement(valor)
			if(comprobar(sig,2)!=True):
				posi=False
			else:
				lista.append(sig.GetText())
		print('lista:',lista)
		pal=''	
		for i in lista:
			pal=pal+i
		print(pal)
		sentence=parse(pal).split()
		for lis in sentence:
			for k in lis:
				if(k[1]== 'VB'):
					return 'verbo'
				elif (k[1]== 'NN'):
					return 'sustantivo'
				else:
					return 'otro'
			
	else:
		return 'No se encontro palabra'

def column():#cambio del original, solo este metodo
	'''Retorna las filas de butones con los colores '''
	sin_color=('black','white')
	descuento=('white','red')
	premio=('white','blue')
	relleno1=('black','yellow')
	relleno2=('black','orange')
	rojo=[(14,0),(13,1),(12,2),(11,3),(10,4),(9,5),(5,9),(4,10),(3,11),(2,12),(1,13),(0,14),(14,7),(0,7),(7,14),(7,0)]
	azul=[(6,6),(8,6),(6,8),(8,8),(6,3),(7,4),(8,3),(3,6),(4,7),(3,8),(7,10),(6,11),(8,11),(11,6),(10,7),(11,8),(14,11),(14,3),(0,11),(0,3),(11,14),(3,14),(3,0),(11,0)]
	amarillo=[(13,4),(12,5),(12,9),(13,10),(2,5),(1,4),(2,9),(1,10)]
	naranja=[(5,2),(4,1),(9,2),(10,1),(5,12),(4,13),(9,12),(10,13)]
	tablero=[]
	for i in range(15):
		row = []
		for j in range(15):
			if((i==7)and(j==7))or(i,j)in amarillo:
				color=relleno1
			elif(i,j)in naranja:
				color=relleno2
			elif(i,j)in azul:
				color=premio
			elif(i==j)or(i,j)in rojo:
				color=descuento
			else:
				color=sin_color
			row.append(sg.Button('',  size=(3, 1),button_color=color, pad=(0, 0), key=(i,j)))
		tablero.append(row)
	
	return tablero		
	
tam_celda =25
color_button = ('white','green')
tam_button = 3,1
but = lambda name : sg.Button(name,button_color=color_button,size=tam_button)
letra='A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
print(letra)
layout = [
         [sg.Column(column())],
					
		
        [but(letra_elegida(letra)),but(letra_elegida(letra)),but(letra_elegida(letra)),but(letra_elegida(letra)),but(letra_elegida(letra))]]

window = sg.Window('Ejercicio1',layout)

button_selected = False
current_button_selected = ''
Check_button = lambda x: window.FindElement(x).Update(button_color=('white','blue'))
Uncheck_button = lambda x: window.FindElement(x).Update(button_color=('white','green'))
while True:
    event, values = window.Read()
    print(event,values)
    print(values)
    if event is None or 'tipo' == 'Exit':
        break
    if type(event)==tuple and button_selected:
        print(event)
        elem=window.FindElement(event)
        comprobar(elem)     
        
    if button_selected:
	    if event == current_button_selected:
		    Uncheck_button(event)
		    button_selected = False
		    current_button_selected = ''
    elif type(event)==str:
        Check_button(event)
        button_selected = True
        current_button_selected = event
        
