
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BOOLEAN BREAK COMA COMENTARIO DELAY DIFERENTE DIVIDE ELSE END EQUAL ESPACIOPUNTO FN FOR ID IF IGUAL INTEGER LET LLAVE_DER LLAVE_IZQ LOOP MAIN MAYOR MAYORIGUAL MENOR MENORIGUAL MOVE MULTIPLICA OPERA PARENTESIS_DER PARENTESIS_IZQ POTENCIA PRINTLN PUNTOCOMA RESTA START STRING SUMA WHILE\n    Start : code\n    \n    code : START cuerpo END\n    \n    cuerpo : variable\n           | expresion\n\n    \n    variable : variable1 cuerpo\n             | variable2 cuerpo\n             | variable3 cuerpo\n             | empty empty\n    \n    variable1 : LET ID PUNTOCOMA\n    \n    variable2 : LET ID EQUAL INTEGER PUNTOCOMA\n              \n    \n    variable3 : LET ID EQUAL expresion_alge1 PUNTOCOMA\n              | LET ID EQUAL expresion_alge2 PUNTOCOMA\n              \n    \n    expresion : INTEGER expresion\n              | STRING expresion\n              | funcion expresion\n              | ID expresion\n              | condicion expresion\n              | expresion_alge1 expresion\n              | expresion_alge2 expresion\n              | empty empty\n                        \n    \n    funcion : Opera\n            | Move\n            | Delay\n            | If\n            | While\n            | For\n            | Loop\n            | Println\n    \n    condicion : Igual expresion\n              | Diferente expresion\n              | Mayor expresion\n              | Menor expresion\n              | Mayorigual expresion\n              | Menorigual expresion \n    \n    expresion_alge0 : SUMA\n                    | RESTA\n                    | MULTIPLICA\n                    | DIVIDE\n                    | POTENCIA\n    \n    expresion_alge1 : INTEGER SUMA INTEGER \n                    | INTEGER RESTA INTEGER \n                    | INTEGER MULTIPLICA INTEGER \n                    | INTEGER DIVIDE INTEGER\n                    | INTEGER POTENCIA INTEGER\n                   \n    \n    expresion_alge2 : PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER SUMA PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER\n                   | PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER RESTA PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER\n                   | PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER MULTIPLICA PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER\n                   | PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER DIVIDE PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER\n                   | PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER POTENCIA PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER\n                   \n    \n    Igual : INTEGER IGUAL INTEGER\n          | ID IGUAL ID\n          | INTEGER IGUAL ID\n          | ID IGUAL INTEGER\n    \n    Diferente : INTEGER DIFERENTE INTEGER\n          | ID DIFERENTE ID\n          | INTEGER DIFERENTE ID\n          | ID DIFERENTE INTEGER\n    \n    Mayor : INTEGER MAYOR INTEGER\n          | ID MAYOR ID\n          | INTEGER MAYOR ID\n          | ID MAYOR INTEGER\n    \n    Menor : INTEGER MENOR INTEGER\n          | ID MENOR ID\n          | INTEGER MENOR ID\n          | ID MENOR INTEGER\n    \n    Mayorigual  : INTEGER MAYORIGUAL INTEGER\n          | ID MAYORIGUAL ID\n          | INTEGER MAYORIGUAL ID\n          | ID MAYORIGUAL INTEGER\n    \n    Menorigual  : INTEGER MENORIGUAL INTEGER\n          | ID MENORIGUAL ID\n          | INTEGER MENORIGUAL ID\n          | ID MENORIGUAL INTEGER\n    \n    If : IF  condicion  PARENTESIS_IZQ funcion PARENTESIS_DER \n    \n    For : FOR  condicion  PARENTESIS_IZQ funcion PARENTESIS_DER \n    \n    Loop : LOOP  condicion  PARENTESIS_IZQ funcion PARENTESIS_DER \n     While : WHILE PARENTESIS_IZQ condicion PARENTESIS_DER PARENTESIS_IZQ funcion PARENTESIS_DER  Opera : PARENTESIS_IZQ expresion_alge0 COMA INTEGER COMA INTEGER PARENTESIS_DER \n    Move : MOVE ID PUNTOCOMA\n    \n    Delay : DELAY INTEGER PUNTOCOMA\n     Println : PRINTLN PARENTESIS_IZQ expresion PARENTESIS_DER PUNTOCOMA\n    empty :\n    '
    
_lr_action_items = {'START':([0,],[3,]),'$end':([1,2,41,],[0,-1,-2,]),'INTEGER':([3,7,8,9,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,38,39,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,74,75,76,77,91,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,128,129,130,139,152,153,154,155,156,157,158,159,160,161,163,164,165,173,174,175,176,177,178,179,],[11,11,11,11,11,11,11,11,11,11,11,-21,-22,-23,-24,-25,-26,-27,-28,11,11,11,11,11,11,85,87,89,89,89,-13,95,96,97,98,99,100,102,104,106,108,110,-82,-14,-15,-16,114,116,118,120,122,124,-17,-18,-19,-29,-30,-31,-32,-33,-34,89,11,-40,-41,-42,-43,-44,-50,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-20,-51,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-9,136,145,-79,-80,85,-10,-11,-12,85,85,85,85,85,171,-74,-75,-76,-81,-45,-46,-47,-48,-49,-78,-77,]),'STRING':([3,7,8,9,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,46,58,59,60,61,68,69,70,72,73,74,75,76,77,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,129,130,152,153,154,161,163,164,165,173,174,175,176,177,178,179,],[12,12,12,12,12,12,12,12,12,12,12,-21,-22,-23,-24,-25,-26,-27,-28,12,12,12,12,12,12,-13,-82,-14,-15,-16,-17,-18,-19,-29,-30,-31,-32,-33,-34,12,-40,-41,-42,-43,-44,-50,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-20,-51,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-9,-79,-80,-10,-11,-12,-74,-75,-76,-81,-45,-46,-47,-48,-49,-78,-77,]),'ID':([3,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,36,38,39,46,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,74,75,76,77,91,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,129,130,152,153,154,161,163,164,165,173,174,175,176,177,178,179,],[14,14,14,14,14,14,14,14,14,14,14,71,-21,-22,-23,-24,-25,-26,-27,-28,14,14,14,14,14,14,86,90,90,90,-13,101,103,105,107,109,111,-82,-14,-15,-16,113,115,117,119,121,123,-17,-18,-19,-29,-30,-31,-32,-33,-34,90,14,-40,-41,-42,-43,-44,-50,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-20,-51,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-9,-79,-80,-10,-11,-12,-74,-75,-76,-81,-45,-46,-47,-48,-49,-78,-77,]),'LET':([3,7,8,9,125,152,153,154,],[18,18,18,18,-9,-10,-11,-12,]),'END':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,42,43,44,45,46,58,59,60,61,68,69,70,72,73,74,75,76,77,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,129,130,152,153,154,161,163,164,165,173,174,175,176,177,178,179,],[-82,41,-3,-4,-82,-82,-82,-82,-82,-82,-82,-82,-82,-82,-82,-21,-22,-23,-24,-25,-26,-27,-28,-82,-82,-82,-82,-82,-82,-5,-6,-7,-8,-13,-82,-14,-15,-16,-17,-18,-19,-29,-30,-31,-32,-33,-34,-40,-41,-42,-43,-44,-50,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-20,-51,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-9,-79,-80,-10,-11,-12,-74,-75,-76,-81,-45,-46,-47,-48,-49,-78,-77,]),'PARENTESIS_IZQ':([3,7,8,9,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,37,40,46,58,59,60,61,68,69,70,72,73,74,75,76,77,88,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,129,130,131,133,134,140,141,142,143,144,148,152,153,154,161,162,163,164,165,173,174,175,176,177,178,179,],[33,33,33,33,33,33,33,33,33,33,33,-21,-22,-23,-24,-25,-26,-27,-28,33,33,33,33,33,33,91,94,-13,-82,-14,-15,-16,-17,-18,-19,-29,-30,-31,-32,-33,-34,131,133,134,33,-40,-41,-42,-43,-44,-50,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-20,-51,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-9,139,-79,-80,146,146,146,155,156,157,158,159,162,-10,-11,-12,-74,146,-75,-76,-81,-45,-46,-47,-48,-49,-78,-77,]),'MOVE':([3,7,8,9,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,46,58,59,60,61,68,69,70,72,73,74,75,76,77,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,129,130,131,133,134,152,153,154,161,162,163,164,165,173,174,175,176,177,178,179,],[34,34,34,34,34,34,34,34,34,34,34,-21,-22,-23,-24,-25,-26,-27,-28,34,34,34,34,34,34,-13,-82,-14,-15,-16,-17,-18,-19,-29,-30,-31,-32,-33,-34,34,-40,-41,-42,-43,-44,-50,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-20,-51,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-9,-79,-80,34,34,34,-10,-11,-12,-74,34,-75,-76,-81,-45,-46,-47,-48,-49,-78,-77,]),'DELAY':([3,7,8,9,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,46,58,59,60,61,68,69,70,72,73,74,75,76,77,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,129,130,131,133,134,152,153,154,161,162,163,164,165,173,174,175,176,177,178,179,],[35,35,35,35,35,35,35,35,35,35,35,-21,-22,-23,-24,-25,-26,-27,-28,35,35,35,35,35,35,-13,-82,-14,-15,-16,-17,-18,-19,-29,-30,-31,-32,-33,-34,35,-40,-41,-42,-43,-44,-50,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-20,-51,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-9,-79,-80,35,35,35,-10,-11,-12,-74,35,-75,-76,-81,-45,-46,-47,-48,-49,-78,-77,]),'IF':([3,7,8,9,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,46,58,59,60,61,68,69,70,72,73,74,75,76,77,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,129,130,131,133,134,152,153,154,161,162,163,164,165,173,174,175,176,177,178,179,],[36,36,36,36,36,36,36,36,36,36,36,-21,-22,-23,-24,-25,-26,-27,-28,36,36,36,36,36,36,-13,-82,-14,-15,-16,-17,-18,-19,-29,-30,-31,-32,-33,-34,36,-40,-41,-42,-43,-44,-50,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-20,-51,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-9,-79,-80,36,36,36,-10,-11,-12,-74,36,-75,-76,-81,-45,-46,-47,-48,-49,-78,-77,]),'WHILE':([3,7,8,9,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,46,58,59,60,61,68,69,70,72,73,74,75,76,77,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,129,130,131,133,134,152,153,154,161,162,163,164,165,173,174,175,176,177,178,179,],[37,37,37,37,37,37,37,37,37,37,37,-21,-22,-23,-24,-25,-26,-27,-28,37,37,37,37,37,37,-13,-82,-14,-15,-16,-17,-18,-19,-29,-30,-31,-32,-33,-34,37,-40,-41,-42,-43,-44,-50,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-20,-51,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-9,-79,-80,37,37,37,-10,-11,-12,-74,37,-75,-76,-81,-45,-46,-47,-48,-49,-78,-77,]),'FOR':([3,7,8,9,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,46,58,59,60,61,68,69,70,72,73,74,75,76,77,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,129,130,131,133,134,152,153,154,161,162,163,164,165,173,174,175,176,177,178,179,],[38,38,38,38,38,38,38,38,38,38,38,-21,-22,-23,-24,-25,-26,-27,-28,38,38,38,38,38,38,-13,-82,-14,-15,-16,-17,-18,-19,-29,-30,-31,-32,-33,-34,38,-40,-41,-42,-43,-44,-50,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-20,-51,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-9,-79,-80,38,38,38,-10,-11,-12,-74,38,-75,-76,-81,-45,-46,-47,-48,-49,-78,-77,]),'LOOP':([3,7,8,9,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,46,58,59,60,61,68,69,70,72,73,74,75,76,77,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,129,130,131,133,134,152,153,154,161,162,163,164,165,173,174,175,176,177,178,179,],[39,39,39,39,39,39,39,39,39,39,39,-21,-22,-23,-24,-25,-26,-27,-28,39,39,39,39,39,39,-13,-82,-14,-15,-16,-17,-18,-19,-29,-30,-31,-32,-33,-34,39,-40,-41,-42,-43,-44,-50,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-20,-51,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-9,-79,-80,39,39,39,-10,-11,-12,-74,39,-75,-76,-81,-45,-46,-47,-48,-49,-78,-77,]),'PRINTLN':([3,7,8,9,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,46,58,59,60,61,68,69,70,72,73,74,75,76,77,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,129,130,131,133,134,152,153,154,161,162,163,164,165,173,174,175,176,177,178,179,],[40,40,40,40,40,40,40,40,40,40,40,-21,-22,-23,-24,-25,-26,-27,-28,40,40,40,40,40,40,-13,-82,-14,-15,-16,-17,-18,-19,-29,-30,-31,-32,-33,-34,40,-40,-41,-42,-43,-44,-50,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-20,-51,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-9,-79,-80,40,40,40,-10,-11,-12,-74,40,-75,-76,-81,-45,-46,-47,-48,-49,-78,-77,]),'SUMA':([11,33,85,127,136,146,],[47,79,47,140,47,79,]),'RESTA':([11,33,85,127,136,146,],[48,80,48,141,48,80,]),'MULTIPLICA':([11,33,85,127,136,146,],[49,81,49,142,49,81,]),'DIVIDE':([11,33,85,127,136,146,],[50,82,50,143,50,82,]),'POTENCIA':([11,33,85,127,136,146,],[51,83,51,144,51,83,]),'IGUAL':([11,14,89,90,],[52,62,52,62,]),'DIFERENTE':([11,14,89,90,],[53,63,53,63,]),'MAYOR':([11,14,89,90,],[54,64,54,64,]),'MENOR':([11,14,89,90,],[55,65,55,65,]),'MAYORIGUAL':([11,14,89,90,],[56,66,56,66,]),'MENORIGUAL':([11,14,89,90,],[57,67,57,67,]),'PARENTESIS_DER':([11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,46,58,59,60,61,68,69,70,72,73,74,75,76,77,78,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,129,130,132,135,147,149,150,161,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,],[-82,-82,-82,-82,-82,-82,-82,-21,-22,-23,-24,-25,-26,-27,-28,-82,-82,-82,-82,-82,-82,-13,-82,-14,-15,-16,-17,-18,-19,-29,-30,-31,-32,-33,-34,127,-82,-40,-41,-42,-43,-44,-50,-52,-54,-56,-58,-60,-62,-64,-66,-68,-70,-72,-20,-51,-53,-55,-57,-59,-61,-63,-65,-67,-69,-71,-73,-79,-80,148,151,161,163,164,-74,-75,-76,-81,173,174,175,176,177,178,179,-45,-46,-47,-48,-49,-78,-77,]),'PUNTOCOMA':([71,86,87,95,96,97,98,99,136,137,138,151,173,174,175,176,177,],[125,129,130,-40,-41,-42,-43,-44,152,153,154,165,-45,-46,-47,-48,-49,]),'EQUAL':([71,],[126,]),'COMA':([79,80,81,82,83,84,145,],[-35,-36,-37,-38,-39,128,160,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Start':([0,],[1,]),'code':([0,],[2,]),'cuerpo':([3,7,8,9,],[4,42,43,44,]),'variable':([3,7,8,9,],[5,5,5,5,]),'expresion':([3,7,8,9,11,12,13,14,15,16,17,27,28,29,30,31,32,94,],[6,6,6,6,46,59,60,61,68,69,70,72,73,74,75,76,77,135,]),'variable1':([3,7,8,9,],[7,7,7,7,]),'variable2':([3,7,8,9,],[8,8,8,8,]),'variable3':([3,7,8,9,],[9,9,9,9,]),'empty':([3,7,8,9,10,11,12,13,14,15,16,17,27,28,29,30,31,32,58,94,],[10,10,10,10,45,58,58,58,58,58,58,58,58,58,58,58,58,58,112,58,]),'funcion':([3,7,8,9,11,12,13,14,15,16,17,27,28,29,30,31,32,94,131,133,134,162,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,147,149,150,172,]),'condicion':([3,7,8,9,11,12,13,14,15,16,17,27,28,29,30,31,32,36,38,39,91,94,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,88,92,93,132,15,]),'expresion_alge1':([3,7,8,9,11,12,13,14,15,16,17,27,28,29,30,31,32,33,94,126,139,155,156,157,158,159,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,78,16,137,78,166,167,168,169,170,]),'expresion_alge2':([3,7,8,9,11,12,13,14,15,16,17,27,28,29,30,31,32,94,126,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,138,]),'Opera':([3,7,8,9,11,12,13,14,15,16,17,27,28,29,30,31,32,94,131,133,134,162,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'Move':([3,7,8,9,11,12,13,14,15,16,17,27,28,29,30,31,32,94,131,133,134,162,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'Delay':([3,7,8,9,11,12,13,14,15,16,17,27,28,29,30,31,32,94,131,133,134,162,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'If':([3,7,8,9,11,12,13,14,15,16,17,27,28,29,30,31,32,94,131,133,134,162,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'While':([3,7,8,9,11,12,13,14,15,16,17,27,28,29,30,31,32,94,131,133,134,162,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'For':([3,7,8,9,11,12,13,14,15,16,17,27,28,29,30,31,32,94,131,133,134,162,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'Loop':([3,7,8,9,11,12,13,14,15,16,17,27,28,29,30,31,32,94,131,133,134,162,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'Println':([3,7,8,9,11,12,13,14,15,16,17,27,28,29,30,31,32,94,131,133,134,162,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'Igual':([3,7,8,9,11,12,13,14,15,16,17,27,28,29,30,31,32,36,38,39,91,94,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'Diferente':([3,7,8,9,11,12,13,14,15,16,17,27,28,29,30,31,32,36,38,39,91,94,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'Mayor':([3,7,8,9,11,12,13,14,15,16,17,27,28,29,30,31,32,36,38,39,91,94,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'Menor':([3,7,8,9,11,12,13,14,15,16,17,27,28,29,30,31,32,36,38,39,91,94,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'Mayorigual':([3,7,8,9,11,12,13,14,15,16,17,27,28,29,30,31,32,36,38,39,91,94,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'Menorigual':([3,7,8,9,11,12,13,14,15,16,17,27,28,29,30,31,32,36,38,39,91,94,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'expresion_alge0':([33,146,],[84,84,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Start","S'",1,None,None,None),
  ('Start -> code','Start',1,'p_Start','Syntax.py',22),
  ('code -> START cuerpo END','code',3,'p_Code','Syntax.py',27),
  ('cuerpo -> variable','cuerpo',1,'p_cuerpo','Syntax.py',34),
  ('cuerpo -> expresion','cuerpo',1,'p_cuerpo','Syntax.py',35),
  ('variable -> variable1 cuerpo','variable',2,'p_Variable','Syntax.py',44),
  ('variable -> variable2 cuerpo','variable',2,'p_Variable','Syntax.py',45),
  ('variable -> variable3 cuerpo','variable',2,'p_Variable','Syntax.py',46),
  ('variable -> empty empty','variable',2,'p_Variable','Syntax.py',47),
  ('variable1 -> LET ID PUNTOCOMA','variable1',3,'p_Variable1','Syntax.py',57),
  ('variable2 -> LET ID EQUAL INTEGER PUNTOCOMA','variable2',5,'p_Variable2','Syntax.py',64),
  ('variable3 -> LET ID EQUAL expresion_alge1 PUNTOCOMA','variable3',5,'p_Variable3','Syntax.py',75),
  ('variable3 -> LET ID EQUAL expresion_alge2 PUNTOCOMA','variable3',5,'p_Variable3','Syntax.py',76),
  ('expresion -> INTEGER expresion','expresion',2,'p_expresion','Syntax.py',86),
  ('expresion -> STRING expresion','expresion',2,'p_expresion','Syntax.py',87),
  ('expresion -> funcion expresion','expresion',2,'p_expresion','Syntax.py',88),
  ('expresion -> ID expresion','expresion',2,'p_expresion','Syntax.py',89),
  ('expresion -> condicion expresion','expresion',2,'p_expresion','Syntax.py',90),
  ('expresion -> expresion_alge1 expresion','expresion',2,'p_expresion','Syntax.py',91),
  ('expresion -> expresion_alge2 expresion','expresion',2,'p_expresion','Syntax.py',92),
  ('expresion -> empty empty','expresion',2,'p_expresion','Syntax.py',93),
  ('funcion -> Opera','funcion',1,'p_funcion','Syntax.py',104),
  ('funcion -> Move','funcion',1,'p_funcion','Syntax.py',105),
  ('funcion -> Delay','funcion',1,'p_funcion','Syntax.py',106),
  ('funcion -> If','funcion',1,'p_funcion','Syntax.py',107),
  ('funcion -> While','funcion',1,'p_funcion','Syntax.py',108),
  ('funcion -> For','funcion',1,'p_funcion','Syntax.py',109),
  ('funcion -> Loop','funcion',1,'p_funcion','Syntax.py',110),
  ('funcion -> Println','funcion',1,'p_funcion','Syntax.py',111),
  ('condicion -> Igual expresion','condicion',2,'p_condicion','Syntax.py',120),
  ('condicion -> Diferente expresion','condicion',2,'p_condicion','Syntax.py',121),
  ('condicion -> Mayor expresion','condicion',2,'p_condicion','Syntax.py',122),
  ('condicion -> Menor expresion','condicion',2,'p_condicion','Syntax.py',123),
  ('condicion -> Mayorigual expresion','condicion',2,'p_condicion','Syntax.py',124),
  ('condicion -> Menorigual expresion','condicion',2,'p_condicion','Syntax.py',125),
  ('expresion_alge0 -> SUMA','expresion_alge0',1,'p_expresion_alge0','Syntax.py',138),
  ('expresion_alge0 -> RESTA','expresion_alge0',1,'p_expresion_alge0','Syntax.py',139),
  ('expresion_alge0 -> MULTIPLICA','expresion_alge0',1,'p_expresion_alge0','Syntax.py',140),
  ('expresion_alge0 -> DIVIDE','expresion_alge0',1,'p_expresion_alge0','Syntax.py',141),
  ('expresion_alge0 -> POTENCIA','expresion_alge0',1,'p_expresion_alge0','Syntax.py',142),
  ('expresion_alge1 -> INTEGER SUMA INTEGER','expresion_alge1',3,'p_expresion_alge1','Syntax.py',150),
  ('expresion_alge1 -> INTEGER RESTA INTEGER','expresion_alge1',3,'p_expresion_alge1','Syntax.py',151),
  ('expresion_alge1 -> INTEGER MULTIPLICA INTEGER','expresion_alge1',3,'p_expresion_alge1','Syntax.py',152),
  ('expresion_alge1 -> INTEGER DIVIDE INTEGER','expresion_alge1',3,'p_expresion_alge1','Syntax.py',153),
  ('expresion_alge1 -> INTEGER POTENCIA INTEGER','expresion_alge1',3,'p_expresion_alge1','Syntax.py',154),
  ('expresion_alge2 -> PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER SUMA PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER','expresion_alge2',7,'p_expresion_alge2','Syntax.py',169),
  ('expresion_alge2 -> PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER RESTA PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER','expresion_alge2',7,'p_expresion_alge2','Syntax.py',170),
  ('expresion_alge2 -> PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER MULTIPLICA PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER','expresion_alge2',7,'p_expresion_alge2','Syntax.py',171),
  ('expresion_alge2 -> PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER DIVIDE PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER','expresion_alge2',7,'p_expresion_alge2','Syntax.py',172),
  ('expresion_alge2 -> PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER POTENCIA PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER','expresion_alge2',7,'p_expresion_alge2','Syntax.py',173),
  ('Igual -> INTEGER IGUAL INTEGER','Igual',3,'p_Igual','Syntax.py',187),
  ('Igual -> ID IGUAL ID','Igual',3,'p_Igual','Syntax.py',188),
  ('Igual -> INTEGER IGUAL ID','Igual',3,'p_Igual','Syntax.py',189),
  ('Igual -> ID IGUAL INTEGER','Igual',3,'p_Igual','Syntax.py',190),
  ('Diferente -> INTEGER DIFERENTE INTEGER','Diferente',3,'p_Diferente','Syntax.py',199),
  ('Diferente -> ID DIFERENTE ID','Diferente',3,'p_Diferente','Syntax.py',200),
  ('Diferente -> INTEGER DIFERENTE ID','Diferente',3,'p_Diferente','Syntax.py',201),
  ('Diferente -> ID DIFERENTE INTEGER','Diferente',3,'p_Diferente','Syntax.py',202),
  ('Mayor -> INTEGER MAYOR INTEGER','Mayor',3,'p_Mayor','Syntax.py',214),
  ('Mayor -> ID MAYOR ID','Mayor',3,'p_Mayor','Syntax.py',215),
  ('Mayor -> INTEGER MAYOR ID','Mayor',3,'p_Mayor','Syntax.py',216),
  ('Mayor -> ID MAYOR INTEGER','Mayor',3,'p_Mayor','Syntax.py',217),
  ('Menor -> INTEGER MENOR INTEGER','Menor',3,'p_Menor','Syntax.py',229),
  ('Menor -> ID MENOR ID','Menor',3,'p_Menor','Syntax.py',230),
  ('Menor -> INTEGER MENOR ID','Menor',3,'p_Menor','Syntax.py',231),
  ('Menor -> ID MENOR INTEGER','Menor',3,'p_Menor','Syntax.py',232),
  ('Mayorigual -> INTEGER MAYORIGUAL INTEGER','Mayorigual',3,'p_Mayorigual','Syntax.py',244),
  ('Mayorigual -> ID MAYORIGUAL ID','Mayorigual',3,'p_Mayorigual','Syntax.py',245),
  ('Mayorigual -> INTEGER MAYORIGUAL ID','Mayorigual',3,'p_Mayorigual','Syntax.py',246),
  ('Mayorigual -> ID MAYORIGUAL INTEGER','Mayorigual',3,'p_Mayorigual','Syntax.py',247),
  ('Menorigual -> INTEGER MENORIGUAL INTEGER','Menorigual',3,'p_Menorigual','Syntax.py',260),
  ('Menorigual -> ID MENORIGUAL ID','Menorigual',3,'p_Menorigual','Syntax.py',261),
  ('Menorigual -> INTEGER MENORIGUAL ID','Menorigual',3,'p_Menorigual','Syntax.py',262),
  ('Menorigual -> ID MENORIGUAL INTEGER','Menorigual',3,'p_Menorigual','Syntax.py',263),
  ('If -> IF condicion PARENTESIS_IZQ funcion PARENTESIS_DER','If',5,'p_If','Syntax.py',277),
  ('For -> FOR condicion PARENTESIS_IZQ funcion PARENTESIS_DER','For',5,'p_For','Syntax.py',289),
  ('Loop -> LOOP condicion PARENTESIS_IZQ funcion PARENTESIS_DER','Loop',5,'p_Loop','Syntax.py',300),
  ('While -> WHILE PARENTESIS_IZQ condicion PARENTESIS_DER PARENTESIS_IZQ funcion PARENTESIS_DER','While',7,'p_While','Syntax.py',311),
  ('Opera -> PARENTESIS_IZQ expresion_alge0 COMA INTEGER COMA INTEGER PARENTESIS_DER','Opera',7,'p_Opera','Syntax.py',321),
  ('Move -> MOVE ID PUNTOCOMA','Move',3,'p_Move','Syntax.py',326),
  ('Delay -> DELAY INTEGER PUNTOCOMA','Delay',3,'p_Delay','Syntax.py',341),
  ('Println -> PRINTLN PARENTESIS_IZQ expresion PARENTESIS_DER PUNTOCOMA','Println',5,'p_Println','Syntax.py',353),
  ('empty -> <empty>','empty',0,'p_empty','Syntax.py',360),
]
