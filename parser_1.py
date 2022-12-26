import sys
import ply.yacc as yacc
from lexer import tokens
from hogar import Hogar, Habitacion, Acceso, Norma, Sensor, Dimension, Actuador, Norma, Normas

def p_prog(p)  :
    '''prog  : NEWH ID LLAVEI l_hab PCOMA ACCE  l_acc  PCOMA reglas LLAVED'''
    print ('prog')

def p_l_hab(p) :
    '''l_hab : PARENI hab PAREND l_hab_1'''
    print('l_hab')

def p_l_hab_1(p):
    '''l_hab_1 :
                    | COMA PARENI hab PAREND l_hab_1
    '''

def p_l_acc(p) :
    '''l_acc : acc l_acc_1'''
    print ('l_acc')

def p_l_acc_1(p):
    '''l_acc_1 :
                    | COMA acc l_acc_1
    '''

def p_hab(p) :
    '''hab : ID COMA dim PCOMA sens PCOMA actuas'''
    print('p_hab')
    p[0] = Habitacion(p[1],p[3].num1,p[3].num2,p[5],p[7])
    for i in p[5]:
        print(str(i))
    print("-------------")
    print(len(p[5]))

def p_acc(p) :
    '''acc : PARENI ID GUION ID PAREND'''
    p[0] = Acceso(p[2],p[4])

def p_dim(p) :
    '''dim : PARENI NUM COMA NUM PAREND'''
    p[0] = Dimension(p[2],p[4])
    #print('p_dim: ('+dim.num1+', '+dim.num2+')')

def p_sens(p) :
    '''sens : sen sens_1'''
    p[1].extend(p[2])
    p[0]=p[1]
    print(p[2][0].tipo)


def p_sens_1(p):
    '''sens_1 :
                    | COMA sen sens_1'''
    if len(p)>1 and p[2] is not None:
        p[0]= p[2]
        #p[0].insert(0,p[1])(p[2])
        print("se la metí")
        print(len(p[0]))
        
    
    if len(p)>2 and p[3] is not None:
         p[0].extend(p[3])
         print("se la metí 2 veze")

def p_sen_lum(p) :
    '''sen_lum : ID LUM IGUAL NUM'''
    p[0] = Sensor(p[1],p[2],p[4])


def p_sen_tem(p) :
    '''sen_tem : ID TEM IGUAL NUM'''
    p[0] = Sensor(p[1],p[2],p[4])


def p_sen_pre(p) :
    '''sen_pre : ID PRE IGUAL TRUE
                 | ID PRE IGUAL FALSE'''
    p[0] = Sensor(p[1],p[2],p[4])


def p_sen_gas(p) :
    '''sen_gas : ID GAS IGUAL TRUE
                | ID GAS IGUAL FALSE '''
    p[0] = Sensor(p[1],p[2],p[4])


def p_sen_fue(p) :
    '''sen_fue : ID FUE IGUAL TRUE
                | ID FUE IGUAL FALSE'''
    p[0] = Sensor(p[1],p[2],p[4])


def p_sen_hum(p) :
    '''sen_hum : ID HUM IGUAL NUM'''
    p[0] = Sensor(p[1],p[2],p[4])


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

def p_actuas_1(p):
     '''actuas_1 :
                    | COMA actua actuas_1
    '''

def p_actua(p) :
    '''actua : actua_cale
            | actua_air
            | actua_pers
            | actua_roci
            | actua_alar'''
    print('p_actua')

def p_actua_cale(p) :
    '''actua_cale : ID CALE IGUAL NUM'''
    print('p_actua_cale')

def p_actua_air(p)  :
    '''actua_air  : ID AIRE IGUAL NUM'''
    print('p_actua_air')

def p_actua_pers(p) :
    '''actua_pers : ID PERS IGUAL SUBIR
                    | ID PERS IGUAL BAJAR
                    | ID PERS IGUAL PARAR'''
    print('p_actua_pers')

def p_actua_roci(p) :
    '''actua_roci : ID ROCI IGUAL TRUE
                    | ID ROCI IGUAL FALSE'''
    print('p_actua_roci')

def p_actua_alar(p) :
    '''actua_alar : ID ALAR IGUAL TRUE
                    | ID ALAR IGUAL FALSE'''
    print('p_actua_alar')

def p_reglas(p) :
    '''reglas : iff reglas_1'''
    print('p_reglas')

def p_reglas1(p):
    '''reglas_1 :
                | PCOMA iff reglas_1'''

def p_iff(p) :
    '''iff : SI PARENI conds PAREND LLAVEI conse LLAVED'''
    print('p_iff')
    print(p[3])

def p_conds(p) :
    '''conds : condi conds_1'''

    p[0]=p[1]
    for element in p[2]:
        p[0].insert(element)
    print('p_conds')

def p_conds_1(p):
    '''conds_1 :
                | AND condi conds_1
                | OR condi conds_1'''
    if len(p) == 1:
       p[0] = []
    else:
        p[0].insert(p[1],p[2])
        

def p_condi(p) :
    '''condi : condiB
                | condiN'''
    p[0]=[]
    p[0].append([1])
    print('p_condi')

def p_condiB(p):
    '''condiB : ID compaB TRUE
                | ID compaB FALSE'''
    p[0] = Normas(p[1], p[2].simbolo, p[3])

def p_condiN(p):
    '''condiN : ID compa NUM'''
    p[0] = Normas(p[1], p[2].simbolo, p[3])

def p_conse(p) :
    '''conse : actua conse_1'''
    print('p_conse')

def p_conse_1(p):
    '''conse_1 :
                | COMA actua conse_1'''

def p_compa(p) :
    '''compa : MENOR
            | MAYOR
            | IGUAL'''
    p[0] = Norma(p[1])
    print('p_compa')

def p_compaB(p):
    '''compaB : IGUALC
            | DISTIN'''
    p[0]=Norma(p[1])

def p_error(t):

    print("error en linea " + str(t.lineno)+ " delante de "+ str(t.value))


def main(argv):
    #parser = yacc.yacc()
    parser = yacc.yacc(debug=True)
    input_stream = open(argv[1],"r")
    result = parser.parse(input_stream.read())
    print(result)

if __name__ == '__main__'   : main(sys.argv)