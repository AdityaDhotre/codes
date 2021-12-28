# -*- coding: utf-8 -*-

print("Chat-Bot")
name=input("Please Enter Your Name:")
print("Hi",name)
gold=0
fd=0
poli=0
mf=0
shr=0
igold=4
ifd=8
ipoli=10
imf=12
ishr=15
suggest=0
def calculate():
  print("ok")
  gamount=((gold*amount)/100)
  fdamount=((fd*amount)/100)
  shramount=((shr*amount)/100)
  mfamount=((mf*amount)/100)
  poliamount=((poli*amount)/100)
  print("Gold Amount:",gamount)
  print("FD Amount:",fdamount)
  print("Shares Amount:",shramount)
  print("Mutual funds Amount:",mfamount)
  print("Policy Amount:",poliamount)
  goldin=(igold*gamount)/100
  fdin=(ifd*fdamount)/100
  polin=(ipoli*poliamount)/100
  mfin=(imf*mfamount)/100
  shrin=(ishr*shramount)/100
  tgold=goldin+gamount
  tfd=fdin+fdamount
  tpoli=polin+poliamount
  tmf=mfin+mfamount
  tshr=shrin+shramount
  print("Gold Amount with interest:",tgold)
  print("FD Amountwith interest:",tfd)
  print("Policy Amount with interest:",tpoli)
  print("Mutual funds Amount with interest:",tmf)
  print("Shares Amount with interest:",tshr)
  totalamount=tgold+tfd+tpoli+tmf+tshr
  print("Overall returns:",totalamount)
'''def profit():
  goldin=(igold*gamount)/100
  fdin=(ifd*fdamount)/100
  polin=(ipoli*poliamount)/100
  mfin=(imf*mfamount)/100
  shrin=(ishr*shramount)/100
  tgold=goldin+gamount
  tfd=fdin+fdamount
  tpoli=polin+poliamount
  tmf=mfin+mfamount
  tshr=shrin+shramount
  print("Gold Amount with interest:",tgold)
  print("FD Amountwith interest:",tfd)
  print("Policy Amount with interest:",tpoli)
  print("Mutual funds Amount with interest:",tmf)
  print("Shares Amount with interest:",tshr)
'''
amount=int(input("Enter the amount you want to invest:"))
risk=input("Amount of risk you would prefer? (l/m/h)")
time=int(input("What amount of time you want to invest?"))
if(risk=='l'):
   if time<2:
      print("LOW")
      print("50% in policies and 50% in gold")
      gold=50
      poli=50
      code='ll'
      suggest=1
      calculate()
   else :
      print("HIGH")
      print("50% in FD and 50% in gold")
      gold=50
      fd=50
      code='lm'
      suggest=1
      calculate()
elif(risk=='m'):
     if time<2:
       print("LOW")
       print("50% in policies and 50% in FD")
       poli=50
       fd=50
       code='ml'
       suggest=1
       calculate()
     else :
      print("HIGH")
      print("50% in policies and 50% in MF")
      poli=50
      mf=50
      code='mm'
      suggest=1
      calculate()
else:
   if time<2:
        print("LOW")
        print("50% in policies and 50% in shares")
        poli=50
        shr=50
        code='hl'
        suggest=0
        calculate()
   else :
       print("HIGH")
       print("50% in MF and 50% in shares")
       mf=50
       shr=50
       code='hm'
       suggest=0
       calculate()
if code=='ll':
      print("<<if you take higher risk then >>")
      gold=0
      fd=50
      poli=50
      mf=0
      shr=0
      calculate()
if code=='lm':
      print("<<if you take higher risk then >>")
      gold=0
      fd=0
      poli=50
      mf=50
      shr=0
      calculate()
if code=='ml':
      print("<<if you take higher risk then >>")
      gold=0
      fd=0
      poli=50
      mf=0
      shr=50
      calculate()
if code=='mm':
      print("<<if you take higher risk then >>")
      gold=0
      fd=0
      poli=0
      mf=50
      shr=50
      calculate()
if code=='hl' and suggest==0:
      print("<< if you increase your time of investment >>")
      gold=0
      fd=0
      poli=0
      mf=50
      shr=50
      calculate()
      
      
      
      
''' Output :-
Chat-Bot

Please Enter Your Name:Damini
Hi Damini

Enter the amount you want to invest:60000

Amount of risk you would prefer? (l/m/h)h

What amount of time you want to invest?3
HIGH
50% in MF and 50% in shares
ok
Gold Amount: 0.0
FD Amount: 0.0
Shares Amount: 30000.0
Mutual funds Amount: 30000.0
Policy Amount: 0.0
Gold Amount with interest: 0.0
FD Amountwith interest: 0.0
Policy Amount with interest: 0.0
Mutual funds Amount with interest: 33600.0
Shares Amount with interest: 34500.0
Overall returns: 68100.0
'''
