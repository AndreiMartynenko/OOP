print('*', '*', '*', '*')
print('*', ' ', ' ', '*')
print('*', ' ', ' ', '*')
print('*', '*', '*', '*')

print('0','X','X')
print('0','X','0')
print('X','0','X')

#OOP
print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('hi'))
print(type([]))
print(type(()))
print(type({}))

#Everything here is an object. In python everything is built by this class keyword. And we are able to use different methods on our objects to perform some object on them.
#Objects have methods and antribures that we could access with the .method.

class BigObject: # we created a class or BluePrint
  pass

obj1 = BigObject() #Instanciate - calling the class to create an object
obj2 = BigObject()
obj3 = BigObject()
print(type(obj1))

#We creating a new object (Instance) obj1 by instanciating class (BigObject).

#Coding own Class

class PlayerCharacter:
  def __init__(self, name, age):    #often called a construction or init method. And this is automatically called anytime we instantiate. self - referes to the PlayerCharacter
    self.name = name #instance attribute
    self.age = age #instance attribute
  
  def run(self):
    print('run') #own method
    return 'done' 

player1 = PlayerCharacter('Cindi',44) # we just calling the class (PlayerCharacter()) to create an object (player1). So, when I do () it's going to automatically run wathever in this code block such as 
#class PlayerCharacter:
  #def __init__(self, name): 
#When we called __init__ we accept whatever is after self as the parameter name.
player2 = PlayerCharacter('Tom',35) 
print(player1.name)
print(player2.age)

#Attributes and Methods

#help(player1)
#help(list) 

class PlayerCharacter:
  #Class Object Attribute
  membershib = True #Class attribute. Its on the same line as methods. Doesn't change across instances  
  def __init__(self, name, age):
    if (self.membership):    
      self.name = name #instance attribute. Is not a class attribute. Its define in our construction __innit__
      self.age = age #instance attribute. Is not a class attribute. Name, age - dynemic inst. attributes. The way we access them is different. So we need to use self.name or self.age
  
  def shout(self): #method
    print(f'my name is {self.name}')   

player3 = PlayerCharacter('Cindi',44) 
player4 = PlayerCharacter('Tom',35) 

print(player4.shout())
print(player3.shout())