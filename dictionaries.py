# Hashmap (unordered)
myDetails = {"name": "Rob", "age": 29, "datetime": "20190214T135842", "location": (44.590533, -104.715556),
             "isLearning": True}
peteDetails = dict(name="Peter", age=29, isLearning=False)
print(myDetails)

# Add
peteDetails["datetime"] = "19890606T105831"
peteDetails["isALilBitch"] = True
print(peteDetails)
print(peteDetails["isALilBitch"] + myDetails["isLearning"])

# Give value to variable, if there is no value, show default
peteLocation = peteDetails.get('location', None)
print(peteLocation)
