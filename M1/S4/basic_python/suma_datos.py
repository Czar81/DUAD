text = "Esto es un string"
num = 10
lista = ["Esto", "es", "una", "lista"]
decimal = 3.14
booleano = True


print(f"string + string = {text+text}" #Esto es un stringEsto es un string
 f"\n string + int = {text+num}" #TypeError: can only concatenate str (not "int") to str
 f"\n list + list = {lista+lista}" #['Esto', 'es', 'una', 'lista', 'Esto', 'es', 'una', 'lista']
 f"\n string + list = {text+lista}" #TypeError: can only concatenate str (not "list") to str
 f"\n float + int = {decimal+num}" #13.14
 f"\n bool + int = {booleano+num}" #11
 f"\n bool + float = {booleano+decimal}" #14.140000000000001
 f"\n bool + string = {booleano+text}" #TypeError: unsupported operand type(s) for +: 'bool' and 'str'
 f"\n bool + bool = {booleano+booleano}") #2
