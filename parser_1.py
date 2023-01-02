#!/usr/bin/python3
# -- coding: utf-8 --
'''Parser'''

import sys
import ply.yacc as yacc
from lexer import tokens
from hogar import Hogar, Habitacion, Acceso, Sensor, Dimension, Condiciones, Consecuencia, Regla, Actuador
import simulation

used_ids = set()
used_ids_hab = set()
used_ids_senB = set()
used_ids_senN = set()
used_ids_act = set() 
used_ids_actN = set()
used_ids_actB = set()
used_ids_actR = set()
todo_ok=True
mensaje=""

def add_id(id_name):
    if id_name in used_ids:
        global todo_ok
        global mensaje
        todo_ok = False
        mensaje += "Error: ID="+str(id_name)+" ya en uso.\n"
    used_ids.add(id_name)
    
def add_id_hab(id_name):
    if id_name in used_ids_hab:
        global todo_ok
        global mensaje
        todo_ok = False
        mensaje += "Error: Habitación ID="+str(id_name)+" ya en uso.\n"
    used_ids_hab.add(id_name)
    add_id(id_name)
    
def add_id_sen(id_name,tipo):
    global todo_ok
    global mensaje
    if tipo==0 :
        if id_name in used_ids_senN:
            todo_ok = False
            mensaje += "Error: Sensor ID="+str(id_name)+" ya en uso.\n"
        used_ids_senN.add(id_name)
        add_id(id_name)
    else :
        if id_name in used_ids_senB:
            todo_ok = False
            mensaje += "Error: Sensor ID="+str(id_name)+" ya en uso.\n"
        used_ids_senB.add(id_name)
        add_id(id_name)
        
def add_id_act(id_name,tipo):
    global todo_ok
    global mensaje
    if id_name in used_ids_act:
        todo_ok = False
        mensaje += "Error: Actuador ID="+str(id_name)+" ya en uso.\n"
    used_ids_act.add(id_name)
    if (tipo==0):
        used_ids_actN.add(id_name)
    if (tipo==1):
        used_ids_actB.add(id_name)
    if (tipo==2):
        used_ids_actR.add(id_name)
    add_id(id_name)
    
def checkList_hab(id_name):
    if id_name not in used_ids_hab:
        global todo_ok
        global mensaje
        todo_ok = False
        mensaje += "Error: Habitación ID="+str(id_name)+" no declarada.\n"     
    
def checkList_sen(id_name,tipo):
    global todo_ok
    global mensaje
    if tipo==0:
        if id_name not in used_ids_senN:
            todo_ok = False
            if id_name not in used_ids_senB:
                mensaje += "Error: Sensor ID="+str(id_name)+" no declarado.\n"
            else:
                mensaje += "Error: Sensor ID="+str(id_name)+" no es de tipo boolean.\n"
    else:
        if id_name not in used_ids_senB:
            todo_ok = False
            if id_name not in used_ids_senN:
                mensaje += "Error: Sensor ID="+str(id_name)+" no declarado.\n"
            else:
                mensaje += "Error: Sensor ID="+str(id_name)+" no es de tipo entero.\n"
    
def checkList_act(id_name):
    global todo_ok
    global mensaje
    if id_name not in used_ids_act:
        todo_ok = False
        mensaje += "Error: Actuador ID="+str(id_name)+" no declarado.\n"  
        
def p_prog(p)  :
    '''prog  : NEWH ID LLAVEI l_hab PCOMA ACCE  l_acc  PCOMA reglas LLAVED'''
    p[0]=Hogar(p[2],p[4],p[7],p[9])
    print ('prog')
    
def p_l_hab(p) :
    '''l_hab : PARENI hab PAREND l_hab_1'''
    p[0]=[]
    if p[4] is not None:
        for hab in p[4]:
            p[0].append(hab)
    p[0].insert(0,p[2])
    print('l_hab')
    
def p_l_hab_1(p):
    '''l_hab_1 :
                    | COMA PARENI hab PAREND l_hab_1
    '''

    if len(p)>1 and p[3] is not None:
        p[0]=[]
        p[0].append(p[3])
        if p[5] is not None:
            for hab in p[5]:
                p[0].append(hab) 

def p_l_acc(p) :
    '''l_acc : acc l_acc_1'''
    p[0]=[]
    if p[2] is not None:
        for hab in p[2]:
            p[0].append(hab)
    p[0].insert(0,p[1])
    print ('l_acc')

def p_l_acc_1(p):
    '''l_acc_1 :
                    | COMA acc l_acc_1
    '''
    if len(p)>1 and p[2] is not None:
        p[0]=[]
        p[0].append(p[2])
        if p[3] is not None:
            for acc in p[3]:
                p[0].append(acc) 

def p_hab(p) :
    '''hab : ID COMA dim PCOMA sens PCOMA actuas'''
    print('p_hab')
    p[0] = Habitacion(p[1],p[3].num1,p[3].num2,p[5],p[7])
    add_id_hab(p[1])

def p_acc(p) :
    '''acc : PARENI ID GUION ID PAREND'''
    p[0] = Acceso(p[2],p[4])
    checkList_hab(p[2])
    checkList_hab(p[4])

def p_dim(p) :
    '''dim : PARENI NUM COMA NUM PAREND'''
    p[0] = Dimension(p[2],p[4])
    #print('p_dim: ('+dim.num1+', '+dim.num2+')')

def p_sens(p) :
    '''sens : sen sens_1'''
    p[1].extend(p[2])
    p[0]=p[1]

def p_sens_1(p):
    '''sens_1 :
                    | COMA sen sens_1'''
    if len(p)>1 and p[2] is not None:
        p[0]= p[2]
        #p[0].insert(0,p[1])(p[2])
    if len(p)>2 and p[3] is not None:
         p[0].extend(p[3])

def p_sen_lum(p) :
    '''sen_lum : ID LUM IGUAL NUM'''
    p[0] = Sensor(p[1],p[2],p[4])
    add_id_sen(p[1],0)

def p_sen_tem(p) :
    '''sen_tem : ID TEM IGUAL NUM'''
    p[0] = Sensor(p[1],p[2],p[4])
    add_id_sen(p[1],0)
    if( int(p[4])>50 or int(p[4])<0 ):
        global todo_ok
        todo_ok = False
        global mensaje
        mensaje+=("Error en senor "+p[1]+", los sensores de temperatura solo admiten valores de 0 a 50")

def p_sen_pre(p) :
    '''sen_pre : ID PRE IGUAL TRUE
                 | ID PRE IGUAL FALSE'''
    p[0] = Sensor(p[1],p[2],p[4])
    add_id_sen(p[1],1)

def p_sen_gas(p) :
    '''sen_gas : ID GAS IGUAL TRUE
                | ID GAS IGUAL FALSE '''
    p[0] = Sensor(p[1],p[2],p[4])
    add_id_sen(p[1],1)

def p_sen_fue(p) :
    '''sen_fue : ID FUE IGUAL TRUE
                | ID FUE IGUAL FALSE'''
    p[0] = Sensor(p[1],p[2],p[4])
    add_id_sen(p[1],1)

def p_sen_hum(p) :
    '''sen_hum : ID HUM IGUAL NUM'''
    p[0] = Sensor(p[1],p[2],p[4])
    add_id_sen(p[1],0)

def p_sen(p) :
    '''sen : sen_lum
            | sen_tem
            | sen_pre
            | sen_gas
            | sen_fue
            | sen_hum'''
    p[0]= []
    p[0].insert(0,p[1])

def p_actuas(p) :
    '''actuas : actua actuas_1'''
    print('p_actuas')
    if p[2] is not None :
        p[1].extend(p[2])
    p[0]=p[1]

def p_actuas_1(p):
    '''actuas_1 :
                    | COMA actua actuas_1
    '''
    if len(p)>1 and p[2] is not None:
        p[0]=p[2]
        if p[3] is not None:
            p[0].extend(p[3])

def p_actua(p) :
    '''actua : actua_cale
            | actua_air
            | actua_pers
            | actua_roci
            | actua_alar'''
    print('p_actua')
    p[0]= []
    p[0].append(p[1])

def p_actua_cale(p) :
    '''actua_cale : ID CALE IGUAL NUM'''
    print('p_actua_cale')
    p[0] = Actuador(p[1],p[2],p[4])
    add_id_act(p[1])
    if( int(p[4])>50 or int(p[4])<0 ):
        global todo_ok
        todo_ok = False
        global mensaje
        mensaje+=("Error en actuador "+p[1]+", la calefacción solo admite valores de 0 a 50")

def p_actua_air(p)  :
    '''actua_air  : ID AIRE IGUAL NUM'''
    print('p_actua_air')
    p[0] = Actuador(p[1],p[2],p[4])
    add_id_act(p[1])

def p_actua_pers(p) :
    '''actua_pers : ID PERS IGUAL SUBIR
                    | ID PERS IGUAL BAJAR
                    | ID PERS IGUAL PARAR'''
    print('p_actua_pers')
    p[0] = Actuador(p[1],p[2],p[4])
    add_id_act(p[1])

def p_actua_roci(p) :
    '''actua_roci : ID ROCI IGUAL TRUE
                    | ID ROCI IGUAL FALSE'''
    print('p_actua_roci')
    p[0] = Actuador(p[1],p[2],p[4])
    add_id_act(p[1])

def p_actua_alar(p) :
    '''actua_alar : ID ALAR IGUAL TRUE
                    | ID ALAR IGUAL FALSE'''
    print('p_actua_alar')
    p[0] = Actuador(p[1],p[2],p[4])
    add_id_act(p[1])

def p_reglas(p) :
    '''reglas : iff reglas_1'''
    print('p_reglas')
    p[0]=p[1]
    if p[2] is not None:
        p[0].extend(p[2])

def p_reglas1(p):
    '''reglas_1 :
                | PCOMA iff reglas_1'''
    if len(p) > 1 and p[2] is not None:
        p[0]=p[2]
        if p[3] is not None:
            p[0].extend(p[3])

def p_iff(p) :
    '''iff : SI PARENI conds PAREND LLAVEI conse LLAVED'''
    print('p_iff')
    p[0]= []
    p[0].append(Regla(p[3],p[6]))

def p_conds(p) :
    '''conds : condi conds_1'''
    p[0]=p[1]
    if p[2] is not None:
        p[0].extend(p[2])
    print('p_conds')

def p_conds_1(p):
    '''conds_1 :
                | AND condi conds_1
                | OR condi conds_1'''
    if len(p) > 1 and p[2] is not None:
        p[0] = []
        p[0].append(p[1])
        p[0].extend(p[2])
        if p[3] is not None:
            p[0].extend(p[3])
    

def p_condi(p) :
    '''condi : condiB
                | condiN'''
    p[0]=[]
    p[0].append(p[1])
    print('p_condi')

def p_condiB(p):
    '''condiB : ID compaB TRUE
                | ID compaB FALSE'''
    p[0] = Condiciones(p[1], p[2], p[3])
    checkList_sen(p[1],1)

def p_condiN(p):
    '''condiN : ID compa NUM'''
    p[0] = Condiciones(p[1], p[2], p[3])
    checkList_sen(p[1],0)

def p_conse(p) :
    '''conse : conse_2 conse_1'''
    print('p_conse')
    p[0]=[]
    if p[2] is not None:
        for con in p[2]:
            p[0].append(con)
    p[0].insert(0,p[1])

def p_conse_1(p):
    '''conse_1 :
                | COMA conse_2 conse_1'''
    if len(p)>1 and p[2] is not None:
        p[0]=[]
        p[0].append(p[2])
        if p[3] is not None:
            for con in p[3]:
                p[0].append(con)

def p_conse_2(p):
    '''conse_2 : ID IGUAL NUM 
                | ID IGUAL SUBIR 
                | ID IGUAL BAJAR 
                | ID IGUAL PARAR
                | ID IGUAL TRUE
                | ID IGUAL FALSE '''
    p[0] = Consecuencia(p[1], p[3])
    checkList_act(p[1])


def p_compa(p) :
    '''compa : MENOR
            | MAYOR
            | IGUAL'''
    p[0] = p[1]
    print('p_compa')

def p_compaB(p):
    '''compaB : IGUALC
            | DISTIN'''
    p[0]=p[1]

def p_error(t):
    print("error en linea " + str(t.lineno)+ " delante de "+ str(t.value))


def main(argv):
    #parser = yacc.yacc()
    parser = yacc.yacc(debug=True)
    input_stream = open(argv[1],"r")
    result = parser.parse(input_stream.read())
    print(result)
    if todo_ok:
        simulation.simulation(result)
    else:
        print('Error en el archivo de entrada')
        print(mensaje)

if __name__ == '__main__'   : main(sys.argv)
