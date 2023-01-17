bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0].title())    #index positions start at 0, not 1
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])           #index positions at last could use -1


message = "\nMy first bicycle was a " + bicycles[0].title() +"."
print(message)