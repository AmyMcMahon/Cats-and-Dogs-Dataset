import pandas

#reads in data from Excel
allData = pandas.read_csv("Cats and Dogs dataset.csv")
height = allData["HEIGHT"].tolist()
weight = allData["WEIGHT"].tolist()

counter = 0
animal = []

#Uses the weight and height values to make prediction
while counter < len(height):
    if height[counter] <= 25 and height[counter] >= 20:
        animal.append("CAT")
        counter += 1
    elif weight[counter] <= 6.5 and weight[counter] >= 3.5:
        animal.append("CAT")
        counter += 1
    elif height[counter] <= 33 and height[counter] >= 25.6:
        animal.append("DOG")
        counter += 1
    elif weight[counter] <= 8 and weight[counter] >= 6.6:
        animal.append("DOG")
        counter += 1
 
 #Prints animal predictions
print(animal)       
