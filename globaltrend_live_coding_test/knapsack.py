def knapsack(weights, values, capacity):
    n = len(weights)
    
    table = [[0] * (capacity+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, capacity+1):
            if weights[i-1] <= j:
                table[i][j]=max(table[i-1][j], table[i-1][j-weights[i-1]] + values[i-1])
            else:
                table[i][j] = table[i-1][j]
                
    return table[n][capacity]
    
    
def get_inputs():
    weights=[]
    values=[]
    capacity=0
    
    n = int(input("Enter number of items: "))
    
    print("Enter weights of items: ")
    for i in range(n):
        weights.append(int(input()))
    
    print("Enter values of items: ")
    for i in range(n):
        values.append(int(input()))
        
    capacity = int(input("Enter capacity: "))
    
    return weights, values, capacity
    
def main():
    weights, values , capacity = get_inputs()
    maximum_value = knapsack(weights, values, capacity)
    print(maximum_value)
    
if __name__=="__main__":
    main()
        
