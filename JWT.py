import jwt ; #se importa el módulo jwt para trabajar con JSON Web Tokens (JWT).

# Genera y devuelve el token JWT firmado
def createToken(data:dict):                           # data= Datos a incluir en el token.
    token: str = jwt.encode(payload=data, key= 'topSecret', algorithm='HS256'); # Se genera un token JWT utilizando los datos proporcionados, una clave secreta y el algoritmo HS256.
    return token 

# Valida y decodifica el token JWT, devolviendo los datos contenidos en él
def validatedToken(token: str):
    data :dict = jwt.decode(token, key='topSecret', algorithms=['HS256'])    
    return data 