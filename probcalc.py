def calculate_probability(favorable_outcomes, total_outcomes):
    """
    Calculate probability based on the number of favorable outcomes
    and the total number of possible outcomes.

    Parameters:
    - favorable_outcomes (int): Number of favorable outcomes.
    - total_outcomes (int): Total number of possible outcomes.

    Returns:
    - probability (float): Calculated probability.
    """
    try:
        # Ensure non-negative inputs
        if favorable_outcomes < 0 or total_outcomes <= 0:
            raise ValueError("Inputs must be non-negative values.")

        # Calculate probability
        probability = favorable_outcomes / total_outcomes

        return probability

    except ZeroDivisionError:
        print("Error: Total outcomes cannot be zero.")
    except ValueError as e:
        print(f"Error: {e}")

# Get user inputs
favorable_outcomes = int(input("Enter the number of favorable outcomes: "))
total_outcomes = int(input("Enter the total number of possible outcomes: "))

# Calculate and display the probability
result = calculate_probability(favorable_outcomes, total_outcomes)
if result is not None:
    print(f"The probability is: {result:.4f}")