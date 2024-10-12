def fill_template(name, date):
    letter = f"""Dear {name}, 
You are selected on {date}."""
    return letter

# Example usage
name = "Divya"
date = "October 10, 2024"

filled_letter = fill_template(name, date)
print(filled_letter)
