# Function to calculate the final price after discount
def calculate_discount(price, discount_percent):
    """
    Calculates the discounted price if discount_percent is 20% or higher.
    Otherwise, returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate final price
    final_price = calculate_discount(original_price, discount_percent)
    
    # Display the result
    if final_price < original_price:
        print(f"Discount applied! The final price is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: ${original_price:.2f}")
except ValueError:
    print("Please enter valid numeric values for price and discount percentage.")
