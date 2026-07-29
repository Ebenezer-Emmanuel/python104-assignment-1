def print_matrix(matrix):
    """Helper function to print a matrix in a neat grid format."""
    for row in matrix:
        print(" ".join(f"{val:>4}" for val in row))


def read_matrix(rows, cols, name="Matrix"):
    """Reads a matrix row by row from user input."""
    print(f"\nEntering {name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        while True:
            try:
                row_input = input(f"Enter row {i + 1}: ").split()
                if len(row_input) != cols:
                    print(f"Error: Please enter exactly {cols} numbers separated by spaces.")
                    continue
                row = [int(val) for val in row_input]
                matrix.append(row)
                break
            except ValueError:
                print("Error: Invalid input. Please enter integers only.")
    return matrix


#
# PART A — Transpose a Matrix
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Initialize an empty transposed matrix with dimensions cols x rows
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
        
    return transposed



# PART B — Add Two Matrices
def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    
    result = []
    for i in range(rows):
        row_sum = []
        for j in range(cols):
            row_sum.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row_sum)
        
    return result



# PART C — Multiply Two Matrices

def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    
    # Resulting matrix will be size rows_a x cols_b
    result = []
    for i in range(rows_a):
        row_result = []
        for j in range(cols_b):
            dot_product = 0
            for k in range(cols_a):
                dot_product += matrix_a[i][k] * matrix_b[k][j]
            row_result.append(dot_product)
        result.append(row_result)
        
    return result



# MAIN PROGRAM
def main():
    print("=== MATRIX OPERATIONS PROGRAM ===")
    
    # --- PART A DEMO ---
    print("\n--- PART A: TRANSPOSE ---")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    mat = read_matrix(m, n)
    
    print("\nOriginal Matrix:")
    print_matrix(mat)
    
    transposed = transpose_matrix(mat)
    print("\nTransposed Matrix:")
    print_matrix(transposed)  

    # --- PART B DEMO ---
    print("\n--- PART B: ADDITION ---")
    print(f"Adding two {m}x{n} matrices...")
    mat_a = read_matrix(m, n, "Matrix A")
    mat_b = read_matrix(m, n, "Matrix B")
    
    sum_mat = add_matrices(mat_a, mat_b)
    print("\nSum (A + B):")
    print_matrix(sum_mat)

    # --- PART C DEMO ---
    print("\n--- PART C: MULTIPLICATION ---")
    m_a = int(input("\nEnter Matrix A rows: "))
    n_a = int(input("Enter Matrix A columns: "))
    n_b = int(input("Enter Matrix B columns (Rows must equal A's cols): "))
    
    mat_mult_a = read_matrix(m_a, n_a, "Matrix A")
    mat_mult_b = read_matrix(n_a, n_b, "Matrix B")
    
    product_mat = multiply_matrices(mat_mult_a, mat_mult_b)
    print("\nProduct (A x B):")
    print_matrix(product_mat)


if __name__ == "__main__":
    main()