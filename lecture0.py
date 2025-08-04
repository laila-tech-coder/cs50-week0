#print ('hello')
#x=input("what your name\n")
#يعني السطر اللي تحت اكتبه مع السطر اللي فوقend
#يعني هنا النهاية 

#sep يعني هيطبع الكلمه الأولي بعد كده اللي انت كاتباه في سب بعد كده هيطبع الكلمه الثانيه 

#print("hello "  ,  x , sep="........", end=" ")

#name="  laila   "
#print(f"hello, {name}")

#حذف المسافه من النصوص من اليمين واليسار
#remove whitespace from str
#name=name.strip( )
#print(name)
#capitalize user's name اول حرف كابتل 
#name=name.capitalize( )
#print(name )

#name=name.title()
#print(name)

#ممكن ربط الدوال مع بعض
#name=  name.strip().title( )
#print( name)

#نقدر نقلل اسطر البرمجه زي 
x=input("what your name\n").strip().title( )

print('hello',x)
#بدل ما كانو اربعه سطور بقو واحد بس

#split user's name into first name and Last name
first= x.split( )
print(" hello", first)
