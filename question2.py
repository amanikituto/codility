def solution(A):
    max_square = 1  # The minimum possible square size is 1
    current_square = 1  # Counter for the current square being checked
    
    for i in range(1, len(A)):
        if A[i] == A[i - 1]:  # If heights are equal, increase the current square size
            current_square += 1
            max_square = max(max_square, current_square)  # Update the maximum square size
        else:
            current_square = 1  # Reset the current square size if heights differ
    return max_square
