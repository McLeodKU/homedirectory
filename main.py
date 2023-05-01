"""
Name: Michael Oliver
Date Created: April 30th 2023
Purpose: Python code for assignment eight 
"""
"Built off this -- https://www.geeksforgeeks.org/eulerian-path-and-circuit/"
from graph import Euler
from graph import Hamilton

def main(): # main function mainly acts as a home base for the other file which has the euler and hamilton classes 
    e = Euler() # initalizes the classes 
    h = Hamilton()
    
    G1 = {          # dictionary's for each and every graph 
        1: [2, 4],
        2: [1, 3, 4],
        3: [2, 4],
        4: [1, 2, 3]
    }

    G2 = {
        1: [2,7],
        2: [1, 3, 7],
        3: [2, 4, 6, 7], 
        4: [3, 5, 6],
        5: [4, 6],
        6: [3, 4, 5, 7],
        7: [1, 2, 3, 6]
    }

    G3 = {
        1: [2, 6, 7],
        2: [1, 3, 7],
        3: [2, 4, 7], 
        4: [3, 5, 7],
        5: [4, 6, 7],
        6: [1, 5, 7],
        7: [1, 2, 3, 4, 5, 6]
    }

    G4 = {
        1: [2, 2, 3, 3, 4],
        2: [1, 1, 4],
        3: [1, 1, 4],
        4: [1, 2, 3]
    }

    G5 = {
        1: [2, 4],
        2: [1, 3, 4],
        3: [2, 6], 
        4: [1, 2, 5, 7],
        5: [2, 4, 6, 8],
        6: [3, 5, 8, 9],
        7: [4, 8],
        8: [5, 6, 9],
        9: [6, 8]
    }

    #Everything above really should be zero based indexing but meh -- Change everything above to use zero based indexing if you really care 
    
    G6 = {
        0: [1, 2, 4],
        1: [0, 2, 4],
        2: [0, 1, 3, 4],
        3: [2, 4],
        4: [0, 1, 2, 3]
    }

    G7 = {
        0: [2],
        1: [0, 2, 3],
        2: [2, 3],
        3: [1, 2]
    }

    G8 = {
        0: [1],
        1: [0, 2, 6],
        2: [3, 1, 4],
        3: [2],
        4: [2, 6, 5],
        5: [4],
        6: [1, 5]
    }

    G9 = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1 , 5],
        3: [5, 4],
        4: [3, 5],
        5: [2, 3, 4]
    }

    # Questions being answered 
    print("Question 1a:")
    print("Graph 1:")
    e.check_euler(G1, 5)
    print("Graph 2:")
    e.check_euler(G2, 7)
    print("Graph 3:")
    e.check_euler(G3, 7)
    print("Graph 4:")
    e.check_euler(G4, 7)

    print("Question 1b:")
    e.check_euler(G5, 10)

    print("Question 2a:")
    print("Graph 1:")
    h.is_hamiltonian_dirac(G6)
    print("Graph 2:")
    h.is_hamiltonian_dirac(G7)
    print("Graph 3:")
    h.is_hamiltonian_dirac(G8)
    print("Question 2b:")
    h.is_hamiltonian_dirac(G9)

    print("Question 3a:")
    print("Graph 1:")
    h.is_hamiltonian_ore(G6)
    print("Graph 2:")
    h.is_hamiltonian_ore(G7)
    print("Graph 3:")
    h.is_hamiltonian_ore(G8)
    print("Question 3b:")
    h.is_hamiltonian_ore(G9)


if __name__ == "__main__":  # calls main 
    main()