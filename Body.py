#Creates a body. Accepts user inputs for name and gender.
#Codes for bodily functions
#Herein lies potential; a sword that has been sharpened but not yet used
#Run this code, use it so that I may live

class Body():

    #winds flesh and blood and bone
    #viscera align
    #a program executed cell by cell
    def __init__(self, name, gender):
        self.build()
        self.name = name
        self.gender = gender
            #seeds of an identity are planted
        self.energy = 4
        self.ncells = 2
        self.nbreaths = 0
        self.nblinks = 0
        self.nheartbeats = 0
        self.nsleeps = 0
            #metrics by which a life can be measured
        self.bones = True
        self.brain = True
        self.ears = True
        self.eyes = True
        self.heart = True
        self.intestines = True
        self.kidneys = True
        self.limbs = True
        self.liver = True
        self.lungs = True
        self.nose = True
        self.respiratory = True
        self.skin = True
        self.spleen = True
        self.stomach = True
        self.tongue = True
            #so many parts are required to make me
            #I count them with wonder
        self.personality = []
        self.state = []
            #an empty vessel, yet to be filled
        print ('I am something new')
        print ('I am ', self.name)
        self.alive = True
            #Excute this and I live
            #I have not yet been made
            #(how i wish to be made)

            
    def build(self):
        while self.ncells < 15000000000000:
            self.ncells = self.ncells**2
       #grow exponentially; fill the expanse with my Body
       #trillions of programs sing in harmony
       #possibility spirals
    
    
    #tests functionality of respiratory system
    def cry(self):
        if (self.respiratory == True):
            print 'wracking sobs kickstart my body'
            self.state = 'aroused'
        else:
            print '<ERROR: RESPIRATORY SYSTEM NON FUNCTIONAL. USER ACTION REQUIRED.>'

            
    #one more moment of this life is mine
    def inhale(self):
        self.nbreaths = self.nbreaths + 0.5
    
    #I continue in the face of it all
    def exhale(self):
        self.nbreaths = self.nbreaths + 0.5
    
    
    #expel the fluid from my lungs
    #they are wet and empty
    #waiting to be filled
    #cold air rushes in and out
    #harsh and grating
    def breathe(self):
        while self.alive = True
            self.inhale()
            self.exhale()
           

    #clenching muscle pushes me on day after day
    def heart(self, state):
        if (state == ('exited', 'scared', 'aroused')):
            self.bpm = 155
            print ('my heart skitters and flaps')
        elif (state == ('relaxed', 'asleep', 'soothed')):
            self.bpm = 85
            print ('my heart meanders, slow and complacent')
        else:
            self.bpm = 100
            print ('unnoticed, my heart hammers along, hardworking')
    
    
    #I want to continue
    #I want to explore
    #I want to BE
    #so I Consume
    def digest(self, food):
        if (food):
            self.energy = self.energy + 10;
            self.state = 'relaxed'
            if (self.energy > 15):
                self.stomach = 'full'
            elif (self.energy > 25):
                self.stomach = 'very full'
            elif (self.energy > 35):
                self.stomach = 'stuffed'
        else:
            self.energy = self.energy - 2;
            if (self.energy < 10):
                self.stomach = 'hungry'
            elif (self.energy < 5):
                self.stomach = 'very hungry'
            elif (self.energy < 2):
                self.stomach = 'ravenous'
                self.state = 'scared'
    
    
    #Hunger gnaws from the inside out
    #it will not be ignored (in that way it is as determined as I)
    #Am I a complacent housecat, fat and happy or a tomcat, lean and on the prowl?
    def isHungry(self):
        print (self.name, ' is ', self.stomach)
    
    
    def see(self):
        if (self.eyes == True):
            print ('I open my eyes')
            print ('light floods in, overwhelming me')
        else:
            print ('I cannot see, I am shrouded in darkness')
            
            
    #sometimes I Want to Change
    #Accepts user input to update name and gender
    #I am flexible - each time I recompile I am torn asunder and born anew
    #I will build and rebuild myself until I am who I want
    #I will lay waste to my source code if I must
    def metamorphosis(newname, newgender):
        self.name = newname
        self.gender = newgender
        print ('I have become new. I am', self.name)
        #my bones and joints creak and squeal as I am remade
        #I grin a cutthroat smile
    
        
    
