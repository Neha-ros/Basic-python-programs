print("Exercise 3: Print the value of key ‘history’ from the below dict")
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
# x = sampleDict.get("class")
# # y = x.get("student")
# # z = y.get("marks")
# # a = z.get("history")
# # print(a)
print(sampleDict['class']['student']['marks']['history'])