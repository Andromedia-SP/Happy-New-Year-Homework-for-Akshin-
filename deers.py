class Animal:
    def __init__(self):
        self._maxspeed = None
        self._life_expectancy = None
        self._type_of_animal = None
        
    def set_speed(self, speed):
        self._maxspeed = speed
    
    def get_speed(self):
        return self._maxspeed
    
    
    def set_expectancy(self, life):
        self._life_expectancy = life
    
    def get_expectancy(self):
        return self._life_expectancy
    
    def set_type(self, typeis):
        self._type_of_animal = typeis
    
    def get_type(self):
        return self._type_of_animal   
    
    def info(self):
        print(f"It's a/an {self._type_of_animal}. \nHis life expectancy is {self._life_expectancy} year(s). \nMax speed = {self._maxspeed} km/hour.")
        
        
class Deer(Animal):
    def __init__(self, sex):
        super().__init__()
        self.__name = None
        self.__age = None
        self.__magic_level = None
        self.__experience_w = None
        self.sex = sex
    
    def set_name(self, Name):
        self.__name = Name
    def get_name(self):
        return self.__name
    
    def set_age(self, Age):
        self.__age = Age
    def get_age(self):
        return self.__age
 
    def set_magic(self, magic):
        self.__magic_level = magic
    def get_magic(self):
        return self.__magic_level
    
    def set_experience(self, experience):
        self.__experience_w = experience
    def get_experience(self):
        return self.__experience_w
    
    def info(self):
        if self.sex == 'women':
            print(f"It's {self.__name}. \nShe is {self.__age} y/o, a Santas's helper.\nHer working experience - {self.__experience_w} year(s), magic lvl - {self.__magic_level}. If you don't get it - {self.__name} is a(n) {self._type_of_animal}")
        else:
            print(f"It's {self.__name}. \nHe is {self.__age} y/o, a Santa's helper.\nHis working experience - {self.__experience_w} year(s), magic lvl - {self.__magic_level}. If you don't get it - {self.__name} is a(n) {self._type_of_animal}")
            
Maxima = Deer('women')
Maxima.set_speed(100)
Maxima.set_expectancy(600)
Maxima.set_type('deer')
Maxima.set_name('Maxima')
Maxima.set_age(250)
Maxima.set_magic(25)
Maxima.set_experience(150)
Maxima.info()
print('\n')


Rudolf = Deer('men')
Rudolf.set_speed(110)
Rudolf.set_expectancy(600)
Rudolf.set_type('deer')
Rudolf.set_name('Rudolf')
Rudolf.set_age(250)
Rudolf.set_magic(20)
Rudolf.set_experience(100)
Rudolf.info()
print('\n')

Unid = Deer('men')
Unid.set_speed(200)
Unid.set_expectancy(600)
Unid.set_type('deer')
Unid.set_name('Unid')
Unid.set_age(350)
Unid.set_magic(3)
Unid.set_experience(0)
Unid.info()
print('\n')


        
    
    
    
    
                  