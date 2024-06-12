import sympy as sp
import matplotlib.pyplot as plt
import numpy as np


def display_function_and_derivative():
    # Get user input for the function
    expression_str = input("Enter a mathematical function in terms of 'x': ")

    # Define the variable and the function
    x = sp.symbols('x')
    expression = sp.sympify(expression_str)

    # Compute the derivative
    derivative = sp.diff(expression, x)

    # Display the original function and its derivative
    print("\nOriginal function:")
    print(f"f(x) = {expression}")

    print("\nDerivative:")
    print(f"f'(x) = {derivative}")

    # Create lambda functions for numerical evaluation
    f = sp.lambdify(x, expression, 'numpy')
    f_prime = sp.lambdify(x, derivative, 'numpy')

    # Generate x values for plotting
    x_values = np.linspace(-10, 10, 400)

    # Evaluate the functions at the x values
    y_values = f(x_values)
    y_prime_values = f_prime(x_values)

    # Plot the original function and its derivative
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label='f(x)')
    plt.plot(x_values, y_prime_values, label="f'(x)")
    plt.title("Function and Its Derivative")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)

    # Save the plot as a PNG file
    plt.savefig("function_and_derivative_plot.png")
    plt.show()


# Run the program
display_function_and_derivative()
