grades = {
	"Paul" : 80 ,
	"Kevin" : 70
}

print("Paul" in grades) # 確認 Key裡面有沒有Paul

if "Paul" in grades :
	print(grades["Paul"])

print(grades.keys()) # 取的所有key
print(grades.values()) # 取的所有value
print(grades.items()) # 曲的所有 keu : value 的組合

