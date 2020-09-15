def curso_por_estado(estado):
  norte = ["AM","RR","AP","PA", "TO", "RO", "AC"]
  nordeste = ["MA", "PI", "CE", "RN", "PE", "PB", "SE", "AL", "BA"]
  centrooeste = ["MT", "MS", "GO", "DF"]
  sudeste = ["SP", "RJ", "ES", "MG"]
  sul = ["PR", "RS", "SC"]

  print("A01 - AI e Machine Learning")

  if estado in nordeste:
    print("A02 - Business Intelligence")

  elif estado in centrooeste:
    print("A03 - Governança em TI")

  elif estado in norte or estado in sudeste or estado in sul:
    print("A04 - Programação Python")

  if estado in sudeste and estado != "RJ":
    print("A05 - Programação Java")


#Linha para testar o código
curso_por_estado(input("Digite seu estado:").upper())
