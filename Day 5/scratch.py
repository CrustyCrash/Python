val = "a,b,c"
val = val.replace("a","a1")
val = val.replace("b","b1")
val = val.replace("c","c1")
print(val)

val = "a,b,c"
tran = {"a": "a1", "b": "b1", "c": "c1"}
print(val.translate(val.maketrans(tran)))
