import numpy as np
import time

start_time = time.process_time()

check1 = input("Built-in or input: ")
check2 = input("Gauss-Seidel or Jacobi: ")
check3 = input("With extra condition to satisfy an equation: ")

if check1.lower() == "b":
    if check2.lower() == "s":
        
        A = np.array([[5,-2,3],
                      [-3,9,1],
                      [2,-1,-7]])

        b = np.array([-1,2,3])
        maxiteration = int(input("Enter max iteration: ")) - 1

        x1 = 0
        x2 = 0
        x3 = 0

        k = 1

        deviation1 = b[0] - (A[0][0] * x1 + A[0][1] * x2 + A[0][2] * x3)
        deviation2 = b[1] - (A[1][0] * x1 + A[1][1] * x2 + A[1][2] * x3)
        deviation3 = b[2] - (A[2][0] * x1 + A[2][1] * x2 + A[2][2] * x3)
        DF = deviation1 ** 2 + deviation2 ** 2 + deviation3 ** 2

        print("Initial values:")
        print("Variables: [", x1, x2, x3, "]")
        print("Deviations: [", deviation1, deviation2, deviation3, "]")
        print("Initial Total deviation:", DF)

        while k <= maxiteration:
            if DF > 10 ** (-5):
                k += 1

                x1 = (1 / A[0][0]) * (b[0] - A[0][1] * x2 - A[0][2] * x3)
                x2 = (1 / A[1][1]) * (b[1] - A[1][0] * x1 - A[1][2] * x3)
                x3 = (1 / A[2][2]) * (b[2] - A[2][0] * x1 - A[2][1] * x2)
                deviation1 = b[0] - (A[0][0] * x1 + A[0][1] * x2 + A[0][2] * x3)
                deviation2 = b[1] - (A[1][0] * x1 + A[1][1] * x2 + A[1][2] * x3)
                deviation3 = b[2] - (A[2][0] * x1 + A[2][1] * x2 + A[2][2] * x3)
                DF = (deviation1 ** 2 + deviation2 ** 2 + deviation3 ** 2)

                print(str(k - 1) + ". iteration:")
                print("Variables: [", x1, x2, x3, "]")
                print("Deviations: [", deviation1, deviation2, deviation3, "]")
                print("Total deviation:", DF)
            else:
                break

        print("Result found at", k-1, ". iteration")
        print("Solved by using Gauss-Seidel Method")
    
    elif check2 == "j":
        A = np.array([[5,-2,3],
                      [-3,9,1],
                      [2,-1,-7]])

        b = np.array([-10,20,30])

        maxiteration = int(input("Enter max iteration: ")) - 1

        x1 = 0
        x2 = 0
        x3 = 0

        k = 1

        deviation1 = b[0] - (A[0][0] * x1 + A[0][1] * x2 + A[0][2] * x3)
        deviation2 = b[1] - (A[1][0] * x1 + A[1][1] * x2 + A[1][2] * x3)
        deviation3 = b[2] - (A[2][0] * x1 + A[2][1] * x2 + A[2][2] * x3)
        DF = deviation1 ** 2 + deviation2 ** 2 + deviation3 ** 2

        print("Initial values:")
        print("Variables: [", x1, x2, x3, "]")
        print("Deviations: [", deviation1, deviation2, deviation3, "]")
        print("Total deviation:", DF)

        while k <= maxiteration:
            if DF > 10 ** (-5):
                k += 1

                x1j = (1 / A[0][0]) * (b[0] - A[0][1] * x2 - A[0][2] * x3)
                x2j = (1 / A[1][1]) * (b[1] - A[1][0] * x1 - A[1][2] * x3)
                x3j = (1 / A[2][2]) * (b[2] - A[2][0] * x1 - A[2][1] * x2)

                deviation1 = b[0] - (A[0][0] * x1j + A[0][1] * x2j + A[0][2] * x3j)
                deviation2 = b[1] - (A[1][0] * x1j + A[1][1] * x2j + A[1][2] * x3j)
                deviation3 = b[2] - (A[2][0] * x1j + A[2][1] * x2j + A[2][2] * x3j)
                DF = (deviation1 ** 2 + deviation2 ** 2 + deviation3 ** 2)

                x1, x2, x3 = x1j, x2j, x3j

                print(str(k - 1) + ". iteration:")
                print("Variables: [", x1, x2, x3, "]")
                print("Deviations: [", deviation1, deviation2, deviation3, "]")
                print("Total deviation:", DF)

            else:
                break

        print("Result found at", k-1, ". iteration")
        print("Solved by using Jacobi Method")

    else:
        print("False input")

elif check1.lower() == "i":
    if check2.lower() == "s":        
            numrow = int(input("Number of rows: "))
            numvar = int(input("Number of variables: "))
            maxiter = int(input("Number of maximum iterations: "))

            A = []
            b = []
            x = []
            k = 0

            if numrow == numvar:
                for i in range(numrow):
                    for j in range(numvar):
                        entry = int(input(str(i+1) + ".row " + str(j+1) + ". entry: "))
                        A.append(entry)
                    RHS = int(input(str(i+1) + ". RHS value: "))
                    b.append(RHS)                
                A = np.resize(A, (numrow, numvar))

                for i in range(numvar):
                    x.append(int(input(str(i+1) + ". variable: ")))

                deviations = []

                for i in range(numrow):
                    deviation = b[i]
                    for j in range(numvar):
                        deviation -= A[i][j] * x[j]
                    deviations.append(deviation)

                DF = 0

                for i in deviations:
                    DF += i ** 2

                print("Initial variables:", x)
                print("Initial deviation:", deviations)
                print("Initial total deviation:", DF)

                d = 0
                e = 0
                DF_new = 0
                if check3.lower() == "y":
                    if DF > 10 ** (-5) and deviations[0] > 10 ** (-5):
                        while k <= maxiter:                            
                            k += 1

                            for i in range(numrow):
                                for j in range(numvar):
                                    if i != j:
                                        d = d + (A[i][j] * x[j])
                                    else:
                                        pass
                                x[i] = (1 / A[i][i]) * (b[i] - d)
                                d = 0

                            for i in range(numrow):
                                for j in range(numvar):
                                    e = e + A[i][j] * x[j]
                                deviations[i] = b[i] - e
                                e = 0

                            for i in deviations:
                                DF_new += i ** 2
                            DF = DF_new
                            DF_new = 0
                                                
                            print("Iteration number:", k)
                            print("Deviation:", DF)
                            print("Variables:", x)
                            print("Deviations", deviations)
                            
                            if check3.lower() == "y":
                                if DF < 10 ** (-5) and deviations[0] == 0:
                                    break
                            elif check3.lower() == "n":
                                if DF < 10 ** (-5):
                                    break
            else:
                print("number of rows and variables should be the same")
            
                                
                                 
    
    elif check2.lower() == "j":
        if check3.lower() == "n":
            numrow = int(input("Number of rows: "))
            numvar = int(input("Number of variables: "))
            maxiter = int(input("Number of maximum iterations: "))

            A = []
            b = []
            x = []
            k = 0

            if numrow == numvar:
                for i in range(numrow):
                    for j in range(numvar):
                        entry = int(input(str(i+1) + ".row " + str(j+1) + ". entry: "))
                        A.append(entry)
                    RHS = int(input(str(i+1) + ". RHS value: "))
                    b.append(RHS)

                A = np.resize(A, (numrow, numvar))

                for i in range(numvar):
                    x.append(int(input(str(i+1) + ". variable: ")))

                deviations = []

                for i in range(numrow):
                    deviation = b[i]
                    for j in range(numvar):
                        deviation -= A[i][j] * x[j]
                    deviations.append(deviation)

                DF = 0

                for i in deviations:
                    DF += i ** 2

                print("Initial variables:", x)
                print("Initial deviation:", deviations)
                print("Initial total deviation:", DF)

                x_new = x.copy()

                while k <= maxiter:
                    if DF > 10 ** (-5):
                        k += 1

                        for i in range(numrow):
                            x_new[i] = b[i]

                            for j in range(numvar):
                                if i != j:
                                    x_new[i] -= A[i][j] * x[j]

                            x_new[i] /= A[i][i]

                        deviations = []

                        for i in range(numrow):
                            deviation = b[i]
                            for j in range(numvar):
                                deviation -= A[i][j] * x_new[j]
                            deviations.append(deviation)

                        DF_new = 0

                        for i in deviations:
                            DF_new += i ** 2

                        x = x_new.copy()

                        print("Iteration number:", k)
                        print("Deviation:", DF_new)
                        print("Variables:", x)
                        print("Deviations", deviations)

                        DF = DF_new

                    else:
                        break
            else:
                print("number of rows and variables should be the same")
                
        elif check2.lower == "y":
            numrow = int(input("Number of rows: "))
            numvar = int(input("Number of variables: "))
            maxiter = int(input("Number of maximum iterations: "))

            A = []
            b = []
            x = []
            k = 0

            if numrow == numvar:
                for i in range(numrow):
                    for j in range(numvar):
                        entry = int(input(str(i + 1) + ". row " + str(j + 1) + ". entry: "))
                        A.append(entry)
                    RHS = int(input(str(i + 1) + ". RHS value: "))
                    b.append(RHS)               

                A = np.resize(A, (numrow, numvar))

                for i in range(numvar):
                    x.append(int(input(str(i + 1) + ". variable: ")))

                deviations = []

                for i in range(numrow):
                    deviation = b[i]
                    for j in range(numvar):
                        deviation -= A[i][j] * x[j]
                    deviations.append(deviation)

                DF = sum(deviation ** 2 for deviation in deviations)

                print("Initial variables:", x)
                print("Initial deviation:", deviations)
                print("Initial total deviation:", DF)

                d = 0
                e = 0
                DF_new = 0

                while k <= maxiter and DF > 10 ** (-5) and deviations[0] > 10 ** (-5):
                    k += 1

                    x_new = []

                    for i in range(numrow):
                        for j in range(numvar):
                            if i != j:
                                d = d + (A[i][j] * x[j])
                            else:
                                pass
                        x_new.append((1 / A[i][i]) * (b[i] - d))
                        d = 0

                    deviations = []

                    for i in range(numrow):
                        for j in range(numvar):
                            e = e + A[i][j] * x_new[j]
                        deviations.append(b[i] - e)
                        e = 0

                    DF_new = sum(deviation ** 2 for deviation in deviations)
                    DF = DF_new

                    x = x_new

                    print("Iteration number:", k)
                    print("Deviation:", DF)
                    print("Variables:", x)
                    print("Deviations", deviations)
                    
                    if DF < 10 ** (-5) and deviations[0] == 0:
                        if x1+x2==x3:
                            break
                        
                        
            else:
                print("number of rows and variables should be the same")
                    
end_time = time.process_time()
execution_time = end_time - start_time
print(execution_time , "seconds taken")
                                                                                                            