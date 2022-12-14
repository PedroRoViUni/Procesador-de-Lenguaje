
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACCE AIRE ALAR AND BAJAR CALE COMA DISTIN FALSE FUE GAS GUION HUM ID IGUAL IGUALC LLAVED LLAVEI LUM MAYOR MENOR NEWH NUM OR PARAR PAREND PARENI PCOMA PERS PRE ROCI SI SUBIR TEM TRUEprog  : NEWH ID LLAVEI l_hab PCOMA ACCE  l_acc  PCOMA reglas LLAVEDl_hab : PARENI hab PAREND l_hab_1l_hab_1 :\n                    | COMA PARENI hab PAREND l_hab_1\n    l_acc : acc l_acc_1l_acc_1 :\n                    | COMA acc l_acc_1\n    hab : ID COMA dim PCOMA sens PCOMA actuasacc : PARENI ID GUION ID PARENDdim : PARENI NUM COMA NUM PARENDsens : sen sens_1sens_1 :\n                    | COMA sen sens_1sen_lum : ID LUM IGUAL NUMsen_tem : ID TEM IGUAL NUMsen_pre : ID PRE IGUAL TRUE\n                 | ID PRE IGUAL FALSEsen_gas : ID GAS IGUAL TRUE\n                | ID GAS IGUAL FALSE sen_fue : ID FUE IGUAL TRUE\n                | ID FUE IGUAL FALSEsen_hum : ID HUM IGUAL NUMsen : sen_lum\n            | sen_tem\n            | sen_pre\n            | sen_gas\n            | sen_fue\n            | sen_humactuas : actua actuas_1actuas_1 :\n                    | COMA actua actuas_1\n    actua : actua_cale\n            | actua_air\n            | actua_pers\n            | actua_roci\n            | actua_alaractua_cale : ID CALE IGUAL NUMactua_air  : ID AIRE IGUAL NUMactua_pers : ID PERS IGUAL SUBIR\n                    | ID PERS IGUAL BAJAR\n                    | ID PERS IGUAL PARARactua_roci : ID ROCI IGUAL TRUE\n                    | ID ROCI IGUAL FALSEactua_alar : ID ALAR IGUAL TRUE\n                    | ID ALAR IGUAL FALSEreglas : iff reglas_1reglas_1 :\n                | PCOMA iff reglas_1iff : SI PARENI conds PAREND LLAVEI conse LLAVEDconds : condi conds_1conds_1 :\n                | AND condi conds_1\n                | OR condi conds_1condi : condiB\n                | condiNcondiB : ID compaB TRUE\n                | ID compaB FALSEcondiN : ID compa NUMconse : conse_2 conse_1\n                | conse_3 conse_1\n                | conse_4 conse_1conse_1 :\n                | COMA conse_2 conse_1\n                | COMA conse_3 conse_1\n                | COMA conse_4 conse_1conse_2 : ID IGUAL NUM conse_3 : ID IGUAL SUBIR \n                | ID IGUAL BAJAR \n                | ID IGUAL PARARconse_4 : ID IGUAL TRUE\n                | ID IGUAL FALSEcompa : MENOR\n            | MAYOR\n            | IGUALcompaB : IGUALC\n            | DISTIN'
    
_lr_action_items = {'NEWH':([0,],[2,]),'$end':([1,43,],[0,-1,]),'ID':([2,6,15,24,25,31,46,56,58,87,88,111,113,144,],[3,9,23,9,33,48,65,74,33,65,65,74,129,129,]),'LLAVEI':([3,85,],[4,113,]),'PARENI':([4,10,12,17,22,29,],[6,15,19,24,15,46,]),'PCOMA':([5,11,13,14,16,18,21,28,30,34,35,36,37,38,39,40,41,47,49,57,60,66,67,82,83,96,97,98,99,100,101,102,103,104,112,142,],[7,-3,20,-6,-2,25,-5,45,-6,56,-12,-23,-24,-25,-26,-27,-28,-7,-3,-11,45,-9,-4,-12,-10,-14,-15,-16,-17,-18,-19,-20,-21,-22,-13,-49,]),'ACCE':([7,],[10,]),'PAREND':([8,32,48,59,61,62,63,64,75,76,77,78,79,80,81,86,110,114,115,116,117,118,124,130,131,132,133,134,135,136,137,138,139,140,141,],[11,49,66,83,85,-51,-54,-55,-8,-30,-32,-33,-34,-35,-36,-50,-29,-51,-51,-56,-57,-58,-30,-52,-53,-37,-38,-39,-40,-41,-42,-43,-44,-45,-31,]),'COMA':([9,11,14,26,30,35,36,37,38,39,40,41,49,66,76,77,78,79,80,81,82,96,97,98,99,100,101,102,103,104,124,126,127,128,132,133,134,135,136,137,138,139,140,148,149,150,151,152,153,154,155,156,],[12,17,22,42,22,58,-23,-24,-25,-26,-27,-28,17,-9,111,-32,-33,-34,-35,-36,58,-14,-15,-16,-17,-18,-19,-20,-21,-22,111,144,144,144,-37,-38,-39,-40,-41,-42,-43,-44,-45,144,144,144,-66,-67,-68,-69,-70,-71,]),'NUM':([19,42,68,69,73,90,93,94,95,119,120,147,],[26,59,96,97,104,118,-72,-73,-74,132,133,151,]),'SI':([20,45,],[29,29,]),'GUION':([23,],[31,]),'LLAVED':([27,28,44,60,84,125,126,127,128,142,143,145,146,148,149,150,151,152,153,154,155,156,157,158,159,],[43,-47,-46,-47,-48,142,-62,-62,-62,-49,-59,-60,-61,-62,-62,-62,-66,-67,-68,-69,-70,-71,-63,-64,-65,]),'LUM':([33,],[50,]),'TEM':([33,],[51,]),'PRE':([33,],[52,]),'GAS':([33,],[53,]),'FUE':([33,],[54,]),'HUM':([33,],[55,]),'IGUAL':([50,51,52,53,54,55,65,105,106,107,108,109,129,],[68,69,70,71,72,73,95,119,120,121,122,123,147,]),'AND':([62,63,64,114,115,116,117,118,],[87,-54,-55,87,87,-56,-57,-58,]),'OR':([62,63,64,114,115,116,117,118,],[88,-54,-55,88,88,-56,-57,-58,]),'IGUALC':([65,],[91,]),'DISTIN':([65,],[92,]),'MENOR':([65,],[93,]),'MAYOR':([65,],[94,]),'TRUE':([70,71,72,89,91,92,122,123,147,],[98,100,102,116,-75,-76,137,139,155,]),'FALSE':([70,71,72,89,91,92,122,123,147,],[99,101,103,117,-75,-76,138,140,156,]),'CALE':([74,],[105,]),'AIRE':([74,],[106,]),'PERS':([74,],[107,]),'ROCI':([74,],[108,]),'ALAR':([74,],[109,]),'SUBIR':([121,147,],[134,152,]),'BAJAR':([121,147,],[135,153,]),'PARAR':([121,147,],[136,154,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'l_hab':([4,],[5,]),'hab':([6,24,],[8,32,]),'l_acc':([10,],[13,]),'acc':([10,22,],[14,30,]),'l_hab_1':([11,49,],[16,67,]),'dim':([12,],[18,]),'l_acc_1':([14,30,],[21,47,]),'reglas':([20,],[27,]),'iff':([20,45,],[28,60,]),'sens':([25,],[34,]),'sen':([25,58,],[35,82,]),'sen_lum':([25,58,],[36,36,]),'sen_tem':([25,58,],[37,37,]),'sen_pre':([25,58,],[38,38,]),'sen_gas':([25,58,],[39,39,]),'sen_fue':([25,58,],[40,40,]),'sen_hum':([25,58,],[41,41,]),'reglas_1':([28,60,],[44,84,]),'sens_1':([35,82,],[57,112,]),'conds':([46,],[61,]),'condi':([46,87,88,],[62,114,115,]),'condiB':([46,87,88,],[63,63,63,]),'condiN':([46,87,88,],[64,64,64,]),'actuas':([56,],[75,]),'actua':([56,111,],[76,124,]),'actua_cale':([56,111,],[77,77,]),'actua_air':([56,111,],[78,78,]),'actua_pers':([56,111,],[79,79,]),'actua_roci':([56,111,],[80,80,]),'actua_alar':([56,111,],[81,81,]),'conds_1':([62,114,115,],[86,130,131,]),'compaB':([65,],[89,]),'compa':([65,],[90,]),'actuas_1':([76,124,],[110,141,]),'conse':([113,],[125,]),'conse_2':([113,144,],[126,148,]),'conse_3':([113,144,],[127,149,]),'conse_4':([113,144,],[128,150,]),'conse_1':([126,127,128,148,149,150,],[143,145,146,157,158,159,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> NEWH ID LLAVEI l_hab PCOMA ACCE l_acc PCOMA reglas LLAVED','prog',10,'p_prog','parser_1.py',115),
  ('l_hab -> PARENI hab PAREND l_hab_1','l_hab',4,'p_l_hab','parser_1.py',120),
  ('l_hab_1 -> <empty>','l_hab_1',0,'p_l_hab_1','parser_1.py',129),
  ('l_hab_1 -> COMA PARENI hab PAREND l_hab_1','l_hab_1',5,'p_l_hab_1','parser_1.py',130),
  ('l_acc -> acc l_acc_1','l_acc',2,'p_l_acc','parser_1.py',141),
  ('l_acc_1 -> <empty>','l_acc_1',0,'p_l_acc_1','parser_1.py',150),
  ('l_acc_1 -> COMA acc l_acc_1','l_acc_1',3,'p_l_acc_1','parser_1.py',151),
  ('hab -> ID COMA dim PCOMA sens PCOMA actuas','hab',7,'p_hab','parser_1.py',161),
  ('acc -> PARENI ID GUION ID PAREND','acc',5,'p_acc','parser_1.py',167),
  ('dim -> PARENI NUM COMA NUM PAREND','dim',5,'p_dim','parser_1.py',173),
  ('sens -> sen sens_1','sens',2,'p_sens','parser_1.py',178),
  ('sens_1 -> <empty>','sens_1',0,'p_sens_1','parser_1.py',183),
  ('sens_1 -> COMA sen sens_1','sens_1',3,'p_sens_1','parser_1.py',184),
  ('sen_lum -> ID LUM IGUAL NUM','sen_lum',4,'p_sen_lum','parser_1.py',192),
  ('sen_tem -> ID TEM IGUAL NUM','sen_tem',4,'p_sen_tem','parser_1.py',197),
  ('sen_pre -> ID PRE IGUAL TRUE','sen_pre',4,'p_sen_pre','parser_1.py',207),
  ('sen_pre -> ID PRE IGUAL FALSE','sen_pre',4,'p_sen_pre','parser_1.py',208),
  ('sen_gas -> ID GAS IGUAL TRUE','sen_gas',4,'p_sen_gas','parser_1.py',213),
  ('sen_gas -> ID GAS IGUAL FALSE','sen_gas',4,'p_sen_gas','parser_1.py',214),
  ('sen_fue -> ID FUE IGUAL TRUE','sen_fue',4,'p_sen_fue','parser_1.py',219),
  ('sen_fue -> ID FUE IGUAL FALSE','sen_fue',4,'p_sen_fue','parser_1.py',220),
  ('sen_hum -> ID HUM IGUAL NUM','sen_hum',4,'p_sen_hum','parser_1.py',225),
  ('sen -> sen_lum','sen',1,'p_sen','parser_1.py',230),
  ('sen -> sen_tem','sen',1,'p_sen','parser_1.py',231),
  ('sen -> sen_pre','sen',1,'p_sen','parser_1.py',232),
  ('sen -> sen_gas','sen',1,'p_sen','parser_1.py',233),
  ('sen -> sen_fue','sen',1,'p_sen','parser_1.py',234),
  ('sen -> sen_hum','sen',1,'p_sen','parser_1.py',235),
  ('actuas -> actua actuas_1','actuas',2,'p_actuas','parser_1.py',240),
  ('actuas_1 -> <empty>','actuas_1',0,'p_actuas_1','parser_1.py',247),
  ('actuas_1 -> COMA actua actuas_1','actuas_1',3,'p_actuas_1','parser_1.py',248),
  ('actua -> actua_cale','actua',1,'p_actua','parser_1.py',256),
  ('actua -> actua_air','actua',1,'p_actua','parser_1.py',257),
  ('actua -> actua_pers','actua',1,'p_actua','parser_1.py',258),
  ('actua -> actua_roci','actua',1,'p_actua','parser_1.py',259),
  ('actua -> actua_alar','actua',1,'p_actua','parser_1.py',260),
  ('actua_cale -> ID CALE IGUAL NUM','actua_cale',4,'p_actua_cale','parser_1.py',266),
  ('actua_air -> ID AIRE IGUAL NUM','actua_air',4,'p_actua_air','parser_1.py',277),
  ('actua_pers -> ID PERS IGUAL SUBIR','actua_pers',4,'p_actua_pers','parser_1.py',283),
  ('actua_pers -> ID PERS IGUAL BAJAR','actua_pers',4,'p_actua_pers','parser_1.py',284),
  ('actua_pers -> ID PERS IGUAL PARAR','actua_pers',4,'p_actua_pers','parser_1.py',285),
  ('actua_roci -> ID ROCI IGUAL TRUE','actua_roci',4,'p_actua_roci','parser_1.py',291),
  ('actua_roci -> ID ROCI IGUAL FALSE','actua_roci',4,'p_actua_roci','parser_1.py',292),
  ('actua_alar -> ID ALAR IGUAL TRUE','actua_alar',4,'p_actua_alar','parser_1.py',298),
  ('actua_alar -> ID ALAR IGUAL FALSE','actua_alar',4,'p_actua_alar','parser_1.py',299),
  ('reglas -> iff reglas_1','reglas',2,'p_reglas','parser_1.py',305),
  ('reglas_1 -> <empty>','reglas_1',0,'p_reglas1','parser_1.py',312),
  ('reglas_1 -> PCOMA iff reglas_1','reglas_1',3,'p_reglas1','parser_1.py',313),
  ('iff -> SI PARENI conds PAREND LLAVEI conse LLAVED','iff',7,'p_iff','parser_1.py',320),
  ('conds -> condi conds_1','conds',2,'p_conds','parser_1.py',326),
  ('conds_1 -> <empty>','conds_1',0,'p_conds_1','parser_1.py',333),
  ('conds_1 -> AND condi conds_1','conds_1',3,'p_conds_1','parser_1.py',334),
  ('conds_1 -> OR condi conds_1','conds_1',3,'p_conds_1','parser_1.py',335),
  ('condi -> condiB','condi',1,'p_condi','parser_1.py',345),
  ('condi -> condiN','condi',1,'p_condi','parser_1.py',346),
  ('condiB -> ID compaB TRUE','condiB',3,'p_condiB','parser_1.py',352),
  ('condiB -> ID compaB FALSE','condiB',3,'p_condiB','parser_1.py',353),
  ('condiN -> ID compa NUM','condiN',3,'p_condiN','parser_1.py',358),
  ('conse -> conse_2 conse_1','conse',2,'p_conse','parser_1.py',363),
  ('conse -> conse_3 conse_1','conse',2,'p_conse','parser_1.py',364),
  ('conse -> conse_4 conse_1','conse',2,'p_conse','parser_1.py',365),
  ('conse_1 -> <empty>','conse_1',0,'p_conse_1','parser_1.py',374),
  ('conse_1 -> COMA conse_2 conse_1','conse_1',3,'p_conse_1','parser_1.py',375),
  ('conse_1 -> COMA conse_3 conse_1','conse_1',3,'p_conse_1','parser_1.py',376),
  ('conse_1 -> COMA conse_4 conse_1','conse_1',3,'p_conse_1','parser_1.py',377),
  ('conse_2 -> ID IGUAL NUM','conse_2',3,'p_conse_2','parser_1.py',386),
  ('conse_3 -> ID IGUAL SUBIR','conse_3',3,'p_conse_3','parser_1.py',391),
  ('conse_3 -> ID IGUAL BAJAR','conse_3',3,'p_conse_3','parser_1.py',392),
  ('conse_3 -> ID IGUAL PARAR','conse_3',3,'p_conse_3','parser_1.py',393),
  ('conse_4 -> ID IGUAL TRUE','conse_4',3,'p_conse_4','parser_1.py',398),
  ('conse_4 -> ID IGUAL FALSE','conse_4',3,'p_conse_4','parser_1.py',399),
  ('compa -> MENOR','compa',1,'p_compa','parser_1.py',404),
  ('compa -> MAYOR','compa',1,'p_compa','parser_1.py',405),
  ('compa -> IGUAL','compa',1,'p_compa','parser_1.py',406),
  ('compaB -> IGUALC','compaB',1,'p_compaB','parser_1.py',411),
  ('compaB -> DISTIN','compaB',1,'p_compaB','parser_1.py',412),
]
