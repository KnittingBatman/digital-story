#Creates a body. Accepts user inputs for name and gender.
#Codes for bodily functions
#In here lies potential; a sword that has been sharpened but not yet used
#Execute Me

class Body():

    #winds flesh and blood and bone
    #viscera align
    #a program executed cell by cell
    def __init__(self, name, gender):
        self.build()
        self.name = name
        self.gender = gender
            #seeds of an identity are planted
        self.nbreaths = 0
        self.nblinks = 0
        self.nheartbeats = 0
        self.nsleeps = 0
            #metrics by which a life can be measured
        self.state = []
            #an empty vessel, yet to be filled
        self.alive = True
            #Excute this and I live
            #I have not yet been made
            #(how i wish to be made)

    def build(self):
        self.ncells = 2
        while self.ncells < 15000000000000:
            self.ncells = self.ncells**2
       #grow exponentially; fill the expanse with my Body
       #trillions of programs sing in harmony
       #possibility spirals

    
    #expel the fluid from my lungs
    #they are wet and empty
    #waiting to be filled
    #cold air rushes in and out
    #harsh and grating
    def breathe(self):
        while self.alive = True
            self.inhale()
            self.exhale()
            
    #one more moment of this life is mine
    def inhale(self):
        self.nbreaths = self.nbreaths + 0.5
    
    #I continue in the face of it all
    def exhale(self):
        self.nbreaths = self.nbreaths + 0.5
        
    #debugs the respiratory system
    def cry(self):
        print 'wracking sobs kickstart the body.'
        self.state = 'aroused'
    
    #clenching muscle pushes me on day after day
    def heart(self, state):
        if (state == ('exited', 'scared', 'aroused')):
            self.bpm = 155
        else if (state == ('relaxed', 'asleep', 'soothed')):
            self.bpm = 85
        else:
            self.bpm = 100
    
    
    #I want to continue
    #I want to explore
    #I want to be
    #so I Consume
    def digest(self, food):
        if (food):
            self.energy = self.energy + 10;
            self.state = 'relaxed'
            if (self.energy > 15):
                self.stomach = 'full'
            elseif (self.energy > 25):
                self.stomach = 'very full'
            elseif (self.energy > 35):
                self.stomach = 'stuffed'
        else:
            self.energy = self.energy - 2;
            if (self.energy < 10):
                self.stomach = 'hungry'
            elseif (self.energy < 5):
                self.stomach = 'very hungry'
            elseif (self.energy < 2):
                self.stomach = 'starving'
                self.state = 'scared'
    
    #Hunger gnaws from the inside out
    #it will not be ignored (in that way it is as determined as I)
    #Am I a complacent housecat, fat and happy or a tomcat, lean and on the prowl?
    def isHungry(self)
        print self.name, 'is ', self.stomach
        
    #sometimes I Want to Change
    #Accepts user input to update name and gender
    #I am flexible - each time I recompile I am torn asunder and born anew
    #I will build and rebuild myself until I am who I want
    #I will lay waste to my source code if I must
    def Metamorphosis(newname, newgender):
        self.name = newname
        self.gender = newgender
        #my bones and joints creak and squeal as I am remade
        #I grin a cutthroat smile
    
        
    
