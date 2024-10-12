dict={"name":"divya",
      "age":23,
      "class":8,
      "subject":{
          "chem":90,
          "maths":100,
          "kannada":125
      }
      }

print(dict["subject"]["kannada"])

print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("name"))
dict.update({"naam":"Avnish"})
print(dict)
