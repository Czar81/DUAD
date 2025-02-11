def funcion():
    esto_es_una_variable_local = 50
    for i in range(0,5):
        esto_es_una_variable_local_de_un_for = 60
    print(esto_es_una_variable_global)
    print(esto_es_una_variable_local_de_un_for)


esto_es_una_variable_global = 40
funcion()
print(esto_es_una_variable_local) 
#NameError: name 'esto_es_una_variable_local' is not defined. Did you mean: 'esto_es_una_variable_global'?
print(esto_es_una_variable_local_de_un_for)
#NameError: name 'esto_es_una_variable_local_de_un_for' is not defined. Did you mean: 'esto_es_una_variable_global'?
