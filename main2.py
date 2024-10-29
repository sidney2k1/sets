setx={"green","blue"}
sety={"red","blue"}
print("The original set x:")
print(setx)
print("the original set y:")
print(sety)
setz=setx.intersection(sety)
print("Common element in both the sets are")
print(setz)
setz=setx.union(sety)
print("The union of both the sets are:")
print(setz)