def recaman_sequence(n):
    sequence = [0]  # Start with a0 = 0
    seen = set(sequence)  # Keep track of numbers already in sequence

    for k in range(1, n):
        prev = sequence[-1]
        next_val = prev - k

        # Apply the Recamán rules
        if next_val > 0 and next_val not in seen:
            sequence.append(next_val)
        else:
            next_val = prev + k
            sequence.append(next_val)

        seen.add(next_val)  # Track seen numbers

    return sequence

def main():
    try:
        # Get user input for sequence length
        n = int(input("Enter the length of the Recamán sequence: ").strip())

        if n <= 0:
            print("Error: Please enter a positive integer")
            return

        # Generate and print the sequence
        sequence = recaman_sequence(n)
        print("Recamán sequence:", sequence)

    except ValueError:
        print("Error: Please enter a valid number")

if __name__ == "__main__":
    main()