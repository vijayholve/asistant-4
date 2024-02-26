from bardapi import BardCookies
cookie_dict={
  "__Secure-1PSID":"g.a000gwgg4KN5KBUJIFlUQ5Q6R-8J9bdwxzWAOEtk9udujjdwnfDdS1f7dbBAzBYlbhnEnDLlygACgYKAY8SAQASFQHGX2Mitmm2T0zMvMiOHN3Ss8uB-xoVAUF8yKpJuebn2u_ngg2FTfDV4YpL0076",
  "__Secure-1PSIDTS":"ABTWhQFag3uSmb3nrBulti1HUz3dVugaN-6en4Jb6HBKcVLZIQbHMV8r06Ff4osCa63UUJJMxQ",
  "__Secure-1PSIDCC":"ABTWhQE-PtOwIR8aKo3AauCfPsZmPADXUviDL6RuV19yiIOPdeibAgGJc6yEEUmZrpN9nDFIYwg-"
  
}
bard=BardCookies(cookie_dict=cookie_dict)
while True:
  query=input("enter your query ")
  ans=bard.get_answer(query)['content']
  print(ans)