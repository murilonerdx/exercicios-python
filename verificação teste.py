def VERIFICAO(estado):
  Estados = ["AM","RR","AP","PA", "TO", "RO", "AC",
  "MA", "PI", "CE", "RN", "PE", "PB", "SE", "AL", "BA",
  "MT", "MS", "GO", "DF",
  "SP", "RJ", "ES", "MG",
  "PR", "RS", "SC"]

  if estado in Estados:
    print("Estado verificado com sucesso")
  else:
    print("Estado não correspondente")


VERIFICAO(input("Digite seu estado:").upper())




