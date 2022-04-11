Object oriented programming revolves around classes and objects. Classes provide a way of binding data and functionality toghether. We can bind variables and functions together.

Creating a new class creates a new data type. When we instantiate a class we create an object.

**How to define a class and instantiate an object**

```
# define a class
class ClassName:
    # set the constructor, a function to initialize the data
	# this method is optional
	def __init__(self, x: int, y: str):
	    self.x = x
		self.y = y
	
	# define a function which can be called on an object of this class
	def get_y(self) -> str:
	    return self.y
	
	# define a function with a param
	def set_x(self, new_value: int):
	    self.x = new_value
		
	# define a static method, a method which is called on the class
	# can be called on an object, but also directly on the class
	@staticmethod
	def static_method():
	    print('hello')
 
 
 #define a class without a constructor
 class ClassWithoutInit:
	 pass
 
 
 object = ClassName(1, 'string')
 print(object.get_y()) # will print the value of object's y, string'
 object.set_x(6)
 print(object.x) # will print the value of object's x, 6
 
 ClassName.static_method() # will print 'hello'
 
 another_object = ClassWithoutInit() # instantiate a class without constructor
```


TODO: getters & setters

More info:

https://www.programiz.com/python-programming/class

https://www.w3schools.com/python/python_classes.asp