## Idea is to create a single script file with many functions. If you have some packages in mind we can look at it. 

class inData(object):    


    def __init__(self, Data):
        '''Creates a data class with all the information to be used across the algorithm'''
        self.R = None
        self.L = None
        self.C = None
        self.H = None                
        self.pizzaData = self.buildPizzaMatrix(Data)


    def buildPizzaMatrix(self, Data):
        pizzaMatrix = []
        pizzaData = self.dataDigest(Data)        
        for line in pizzaData:
            if len(line) ==1:                            
                pizzaMatrix.append([int(x) for x in line[0].replace('T','0').replace('M','1')])
        return pizzaMatrix


    @staticmethod
    def validateValue(value):
        '''Range Limit on input file'''
        if value in range(0,1000):
            return value
        else:
            return None        

    def dataDigest(self, Data):     
        pizzaData = [] 
        for i, data in enumerate(Data):
            if i == 0:
                self.R = self.validateValue(int(data[0]))
                self.C = self.validateValue(int(data[1]))
                self.L = self.validateValue(int(data[2]))
                self.H = self.validateValue(int(data[3]))
            else:
                pizzaData.append(data)
        return pizzaData

    def __str__(self):
        return 'R: {}, L: {}, C: {}, H: {}, Pizza: {}'.format(self.R, self.L, self.C, self.H, self.pizzaData)


def Read(inputFile):
    '''Reads the input file and returns a list of Data'''
    with open(inputFile,'r') as inFile:
        dataList = []
        for lineData in inFile.readlines():            
            dataList.append(lineData.rsplit('\n')[0].rsplit(' '))        
        return dataList        

def validateOutput(totalSlices, sliceData, R, C):

    validSlices = False
    validRows = False
    validColumns = False

    if totalSlices in range(0, R*C):
        validSlices = True    
    for sliceVals in sliceData:
        r1, c1, r2, c2 = sliceVals        
        if r1 in range(0,R) and r2 in range(0,R):
            validRows = True
        if c1 in range(0,C) and c2 in range(0,C):
            validColumns = True
    
    if validSlices and validRows and validColumns:
        return True
    else:
        raise ValueError('Output Validation Failed')


def Write(outputFile, totalSlices, sliceData):    
    with open(outputFile, 'w') as outFile:
        outFile.write(str(totalSlices)+'\n')
        for pizzaSlice in sliceData:
            outFile.write(' '.join('%s ' %ind for ind in pizzaSlice)+'\n')

def cutPizza(pizzaData):
    print(pizzaData)
    totalSlices = None # int: total slices which we can cut. eg. 10
    sliceData = None # list of columns and rows: SecondSlice between rows(0,2) and columns (2,2) eg. [[0,2,2,2], next row e.t.c.] 
    return totalSlices, sliceData


if __name__ == '__main__':
    # Try to test here and create functions/classes above. 
    inputFile = r'.\inputs\a_example.in'
    outputFile = r'.\outputs\a_example.out'    
    pizzaData = inData(Read(inputFile))
    totalSlices, sliceData = cutPizza(pizzaData)
    totalSlices = 3 # Junk to test Output
    sliceData = [[0,0,2,1], [0,2,2,2], [0,3,2,4]]  # Junk to test Output         
    if validateOutput(totalSlices, sliceData, pizzaData.R, pizzaData.C):
        Write(outputFile, totalSlices, sliceData)    
        

    