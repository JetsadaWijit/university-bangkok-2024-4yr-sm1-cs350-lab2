import cls as cls
import os

SLinkedList = cls.LinkedList

def readFile(fileName):
    data = []

    if not os.path.exists(fileName):
        print(f"File not found: {fileName}")
        return data

    with open(fileName, 'r') as file:
        for line in file:
            parts = line.split()
            ID = int(parts[0])
            fName = parts[1]
            lName = parts[2]
            score = int(parts[3])
            data.append((ID, fName, lName, score))

    return data

def main():
    # Create the linked list from data1.dat
    linkedList = SLinkedList()

    data1 = readFile(os.path.join("root", "..", "data/data1.dat"))
    for record in data1:
        linkedList.insertSorted(*record)

    # Update the linked list from data2.dat
    data2 = readFile(os.path.join("root", "..", "data/data2.dat"))
    for record in data2:
        linkedList.update(*record)  # Add score if ID matches

    # Display the final list
    linkedList.display()

if __name__ == "__main__":
    main()
