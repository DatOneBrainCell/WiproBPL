majorHistoryFigures = {"Napoleon": "Was average height for his time",
    "Hannibal": "Crossed the Alphs mountain range with most of his army intact",
    "Lenin": "Started the Soviet movement",
    "Hitler": "Killed himself in his own bunker when the allied forces reached Berlin"
}
for keys, vals in majorHistoryFigures.items():
    print(keys, ": ", vals)
    
print()
majorHistoryFigures["Sukesh"] = "Changed the path of Programming forever"

for keys, vals in majorHistoryFigures.items():
    print(keys, ": ", vals)

'''O/P:
Napoleon :  Was average height for his time
Hannibal :  Crossed the Alphs mountain range with most of his army intact
Lenin :  Started the Soviet movement
Hitler :  Killed himself in his own bunker when the allied forces reached Berlin

Napoleon :  Was average height for his time
Hannibal :  Crossed the Alphs mountain range with most of his army intact
Lenin :  Started the Soviet movement
Hitler :  Killed himself in his own bunker when the allied forces reached Berlin
Sukesh :  Changed the path of Programming forever
'''
