ip =  int(input("Enter the amount you want to travel: "))

if ip <= 3:
    print("Use a bicycle")
elif ip > 3 and ip <= 300:
    print("Use a motor cycle")
else:
    print("Use a super Car or something")
    
'''O/P:
Enter the amount you want to travel: 45
Use a motor cycle
'''
