import sys
import ply.yacc as yacc
from lexer import tokens
from hogar import Hogar, Habitacion, Acceso, Norma, Sensor, Dimension, Actuador

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

def p_acc(p) : 
    '''acc : PARENI ID GUION ID PAREND'''
    print('p_acc')

def p_dim(p) : 
    '''dim : PARENI NUM COMA NUM PAREND'''
    dim = Dimension(p[2],p[4])
    print('p_dim: ('+dim.num1+', '+dim.num2+')')

def p_sens(p) : 
    '''sens : sen sens_1'''
    print('p_sens')

def p_sens_1(p):
     """sens_1 : 
                    | COMA sen sens_1
    """
    
def p_sen_lum(p) : 
    '''sen_lum : ID LUM IGUAL NUM'''
    sen_lum = Sensor(p[1],p[2],p[4])
    print('p_sen_lum: '+sen_lum.id+' '+sen_lum.tipo+' '+sen_lum.dimension)

def p_sen_tem(p) : 
    '''sen_tem : ID TEM IGUAL NUM'''
    sen_tem = Sensor(p[1],p[2],p[4])
    print('p_sen_temp: '+sen_tem.id+' '+sen_tem.tipo+' '+sen_tem.dimension)

def p_sen_pre(p) : 
    '''sen_pre : ID PRE IGUAL TRUE 
                 | ID PRE IGUAL FALSE'''
    sen_pre = Sensor(p[1],p[2],p[4])
    print('p_sen_pre: '+sen_pre.id+' '+sen_pre.tipo+' '+sen_pre.dimension)

def p_sen_gas(p) :
    '''sen_gas : ID GAS IGUAL TRUE
                | ID GAS IGUAL FALSE '''
    sen_gas = Sensor(p[1],p[2],p[4])
    print('p_sen_gas: '+sen_gas.id+' '+sen_gas.tipo+' '+sen_gas.dimension)

def p_sen_fue(p) : 
    '''sen_fue : ID FUE IGUAL TRUE
                | ID FUE IGUAL FALSE'''
    sen_fue = Sensor(p[1],p[2],p[4])
    print('p_sen_fue: '+sen_fue.id+' '+sen_fue.tipo+' '+sen_fue.dimension)

def p_sen_hum(p) : 
    '''sen_hum : ID HUM IGUAL NUM'''
    sen_hum = Sensor(p[1],p[2],p[4])
    print('p_sen_hum: '+sen_hum.id+' '+sen_hum.tipo+' '+sen_hum.dimension)

def p_sen(p) : 
    '''sen : sen_lum 
            | sen_tem 
            | sen_pre 
            | sen_gas 
            | sen_fue 
            | sen_hum'''
    print('p_sen ')

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

def p_conds(p) : 
    '''conds : condi conds_1'''
    print('p_conds')

def p_conds_1(p):
    '''conds_1 : 
                | AND condi conds_1
                | OR condi conds_1'''

def p_condi(p) : 
    '''condi : condiB
                | condiN'''
    print('p_condi')

def p_condiB(p):
    '''condiB : ID compaB TRUE
                | ID compaB FALSE'''

def p_condiN(p):
    '''condiN : ID compa NUM'''

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
    print('p_compa')

def p_compaB(p):
    '''compaB : IGUALC
            | DISTIN'''

def p_error(t):   
    
    print("error en linea " + str(t.lineno)+ " delante de "+ str(t.value))
        

def main(argv):
    #parser = yacc.yacc()
    parser = yacc.yacc(debug=True)
    input_stream = open(argv[1],"r")
    result = parser.parse(input_stream.read())
    print(result)

if __name__ == '__main__'   : main(sys.argv)