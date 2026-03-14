# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_number = "1234-5678-1234-5678"

print(credit_number[0])
print(credit_number[ : 4])  # start --> inclusive , end --> exclusive
print(credit_number[1 : ])  # It will print till end
print(credit_number[-1]) # It will print from end

print(credit_number[::2]) # It will print every second character of the str

print(credit_number[0 : 4 : 2])  # it will move (step-1)


##########################################################
# Find last 4 digit of a credit card number

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-{last_digits}")


# Reverse the Credit card number
credit_number = credit_number[::-1]
print(credit_number)