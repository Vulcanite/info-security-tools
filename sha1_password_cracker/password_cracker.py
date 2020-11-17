import hashlib

f= open("known-salts.txt",'r')
salts = f.read().splitlines()
f.close()


f1 = open("top-10000-passwords.txt")
pswds = f1.read().splitlines()
f1.close()


def crack_sha1_hash(hash, use_salts = False):
  for pswd in pswds:
    hash_pswd = hashlib.sha1(pswd.encode()).hexdigest()

    if hash == hash_pswd:
      return '%s' % pswd
  
  if use_salts == True:
    for salt in salts:
      for pswd in pswds:
        final = salt+pswd
        final1 = pswd+salt
        final_hash = hashlib.sha1(final.encode()).hexdigest()
        final1_hash =hashlib.sha1(final1.encode()).hexdigest()
        if hash == final_hash or hash == final1_hash:
          return pswd

  return "PASSWORD NOT IN DATABASE"