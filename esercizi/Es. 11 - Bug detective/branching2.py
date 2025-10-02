def controlla_se_piove (stato):
  if stato["pioggia"]:
    return True
  return False

def controlla_se_sole (stato):
  if stato["sole"]:
    return True
  return False

def controlla_temperatura_sotto_zero (stato):
  if stato["temperatura"] < 0:
    return True
  return False

def controlla_tanto_vento (stato) :
  if stato["vento"] >= 100:
    return True
  return False

