def is_valid(plate):
    # Check the length of the plate
    if not (2 <= len(plate) <= 6):
        return False

    # Check if the first two characters are letters
    if not plate[0:2].isalpha():
        return False

    # Check for disallowed characters (anything that's not a letter or digit)
    if not plate.isalnum():
        return False

    # Check if numbers are in the middle or if a number starts with '0'
    has_number = False
    for i in range(len(plate)):
        if plate[i].isdigit():
            if plate[i] == '0' and not has_number:
                return False  # First number is '0', which is invalid
            has_number = True
        elif has_number:  # A letter comes after a number, which is invalid
            return False

    # If all checks pass, the plate is valid
    return True

def main():
    plate = input("Plate: ").strip().upper()  # Get input and convert to uppercase
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
