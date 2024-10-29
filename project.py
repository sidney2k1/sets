setx={"green","blue"}
sety={"red","blue"}
print("The original set x:")
print(setx)
print("the original set y:")
print(sety)
setz=setx.difference(sety)
print(setz)
setz=sety.difference(setx)
print(setz)
setz=setx.symmetric_difference(sety)
print(setz)
setz=sety.symmetric_difference(setx)
print(setz)