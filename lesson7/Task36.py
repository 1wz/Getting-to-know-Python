def print_operation_table(operation, num_rows=6, num_columns=6):
    [print_operation_line(operation,num_columns,y) for y in range(1,num_rows+1)]

def print_operation_line(operation,num_coloumns,y):
    [print("{:4.0f}".format(operation(x,y)),end="") for x in range(1,num_coloumns+1)]
    print()

print_operation_table(lambda x,y:x*y)