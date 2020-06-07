import PySimpleGUI as sg
import random
import sys
#from pattern.es import ( VERB, ADJECTIVE,Spelling)
#Genera un dicionario para probar, las tuplas contienen (cantidad , puntaje)

lista_tuplas_usadas=[]
list_palabra=[]
indice=-1
abajo=False
al_lado=False
continuar=True
dic_letras={}
dic_letra_anterior={}
letra='A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
dic_importado={}
for x in letra:
	dic_importado[x]=[10,20]

#la funcion recibe el diccionario y retorna una letra
#FALTA TODO EL TRAMO DE PATTERN
#def evaluar_palabra(pal, nivel):
#	'''esta funcion devuelve un boolean en true si la cadena es palabra, verbo o adjetivo dependiendo del nivel del juego'''
#	if nivel=='facil':
#		if


def letra_elegida(dic):
	if dic:
		llave_random=random.choice(list(dic))
		dic[llave_random][0] -=1
		if dic[llave_random][0] == 0:
			dic.pop(llave_random)
		return llave_random
	else:
		sg.popup('El diccionario esta vacio')
		sys.exit()


def letrasjuntas(a, b):
	'''devuelve true si las 2 letras ingresadas pueden estar juntas en una palabra'''
	es_vocal= lambda x: x in "aeiou"
	mixtas= ['qa','qe','qi','qo']
	juntas=''
	dos_consonantes=['pr','pl','pt','br','bl','bs','tr','mp','mb','dr','dj','dy','cr','ct','ch','fr','fl','gr','gl']
	list_letras_juntas.append(a)
	list_letras_juntas.append(b)
	juntas=juntas.join(list_letras_juntas)
	print(juntas)
	valido=False
	if es_vocal(a):
		valido=True
		print('vocal')
	elif not(es_vocal(a)) and (es_vocal(b)):
		if not(juntas in mixtas):
			valido=True
			print('mixto')
	else:
		if (a=='r')or(a=='s'):
			valido=True
			print('r o s')
		elif (a=='n')and((b!='p')or(b!='b')):
			valido=True
			print('excepcion de la n')
		elif juntas in dos_consonantes:
			valido=True
			print('dos consonantes')
		else:
			valido=False
			print('no valido')
	return valido


def comprobar(elem,event, indice, dic_letra_anterior, list_palabra, abajo, al_lado):
#	print('texto:',elem.GetText())
#	if(elem.GetText()==''):
#		print('si es')
#		elem.Update(current_button_selected)
	'''esta funcion ve si se van poniendo las letras consecutivamente y las guarda en una lista '''
	continuar=True
	indice=indice+1
	if indice==0:
		dic_letras['pos']=indice
		dic_letras['tup']=event
		dic_letras['letra']=elem.GetText()
		list_palabra.append(dic_letras)
		print('primera letra')
	elif (event[0]==dic_letra_anterior['tup'][0]) and (event[1]==dic_letra_anterior['tup'][1]+1) and (abajo==False) and (letrasjuntas(dic_letra_anterior[letra]),elem.GetText()):
		al_lado=True
		dic_letras['pos']=indice
		dic_letras['tup']=event
		dic_letras['letra']=elem.GetText()
		list_palabra.append(dic_letras)
		boton_confirmar=True
		print('letra valida al costado')
	elif (event[0]==dic_letra_anterior['tup'][0]+1) and (event[1]==dic_letra_anterior['tup'][1]) and (al_lado==False) and (letrasjuntas(dic_letra_anterior[letra],elem.GetText())):
		abajo=True
		dic_letras['pos']=indice
		dic_letras['tup']=event
		dic_letras['letra']=elem.GetText()
		list_palabra.append(dic_letras)
		boton_confirmar=True
		print('letra valida abajo')
	else:
		indice=indice-1
		continuar=False
		print('letra lejos o no valida')
	dic_letra_anterior=dic_letras.copy()
	print(dic_letra_anterior)
	return indice, dic_letra_anterior, list_palabra, abajo, al_lado, continuar

# seguir ACA
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
layout = [
         [sg.Column(column())],
        [but(letra_elegida(dic_importado)),but(letra_elegida(dic_importado)),but(letra_elegida(dic_importado)),but(letra_elegida(dic_importado)),but(letra_elegida(dic_importado)),but(letra_elegida(dic_importado)),but(letra_elegida(dic_importado))]
        ]

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
		if not(event in lista_tuplas_usadas):
			elem=window.FindElement(event)
			print('imprimo el get texto')
			print(elem.GetText())
			indice, dic_letra_anterior, list_palabra, abajo, al_lado, continuar=comprobar(elem,event,indice, dic_letra_anterior, list_palabra, abajo, al_lado)
			print('salio')
			if continuar== True:
				elem.Update(current_button_selected)
				print('sigue')
				lista_tuplas_usadas.append(event)


	if button_selected:
		if event == current_button_selected:
			Uncheck_button(event)
			button_selected = False
			current_button_selected = ''
	elif type(event)==str:
		Check_button(event)
		button_selected = True
		current_button_selected = event
