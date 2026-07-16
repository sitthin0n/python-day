num_employes = int(input('Enter the number of employees: '))
if num_employes < 50:
    print('This is a small company')
elif num_employes < 250:
    print('This is a medium company')
#elif num_employes >= 250:
    #print('This is a large company')
else:
    print('This is a large company')
#ใช้ else ดีกว่าเพราะจะไม่ต้องเช็คเงื่อนไขซ้ำอีกครั้ง และยังทำให้โค้ดอ่านง่ายขึ้น