marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Harry"
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry": 99, "Renuka": 100})
print(marks)
print(marks.get("Shivika"))
print(marks.get("Harry"))
