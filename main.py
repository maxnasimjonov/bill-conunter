# Dictionary to store cumulative totals of each bill denomination
total_bills = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0}

def min_bills_algorithm():
    global total_bills  # Access the global dictionary to update totals
    print ('\n')
    print("     ======================================")
    print("     === Minimum # of Bills Calculator! ===")
    print("     ======================================")
    print('\n')
    
    while True:
        # Get input and validate it ends with 5 or 0
        try:
            amount = int(input("Enter amount (must end with 5 or 0) from 100 to 999995: "))
            if amount < 100 or amount > 99999 or amount % 5 != 0:
                print("Invalid input! Amount must be between 100 and 99995 and end with 5 or 0.")
                continue
        except ValueError:
            print("Please enter a valid number!")
            continue
            
        # Initialize bill counts for this run
        bills = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0}
        remaining = amount
        
        # Greedy algorithm: use largest bills first
        for denom in [100, 50, 20, 10, 5]:
            bills[denom] = remaining // denom
            remaining = remaining % denom
            
        # Update cumulative totals
        for denom in [100, 50, 20, 10, 5]:
            total_bills[denom] += bills[denom]
            
        # Print results vertically, only if count > 0
        print(f"\n${amount} with the fewest bills:")
        if bills[100] > 0:
            print(f"100$ bills: {bills[100]}")
        if bills[50] > 0:
            print(f"50$ bills: {bills[50]}")
        if bills[20] > 0:
            print(f"20$ bills: {bills[20]}")
        if bills[10] > 0:
            print(f"10$ bills: {bills[10]}")
        if bills[5] > 0:
            print(f"5$ bills: {bills[5]}")
        
        # Ask to continue
        again = input("\nMore (y/n)? ").lower()
        if again != 'y':
            # Display cumulative totals before exiting
            print("\nCumulative totals:\n")
            print(f"Total 100$ bills needed: {total_bills[100]}")
            print(f"Total 50$ bills needed: {total_bills[50]}")
            print(f"Total 20$ bills needed: {total_bills[20]}")
            print(f"Total 10$ bills needed: {total_bills[10]}")
            print(f"Total 5$ bills needed: {total_bills[5]}")
            print('\n')
            print("Bye!")
            break

# Call the algorithm
min_bills_algorithm()