import subprocess
import tempfile
import os

def save_code(code, filename):
    with open(filename, 'w') as file:
        file.write(code)

def run_code(filename):
    try:
        output = subprocess.check_output(['python', filename], stderr=subprocess.STDOUT, timeout=5, universal_newlines=True)
        return True, output
    except subprocess.CalledProcessError as e:
        return False, e.output
    except subprocess.TimeoutExpired:
        return False, "Execution timed out."

def main():
    print("Custom Python IDE")

    # Get the initial code
    code = input("Enter your Python code:\n")

    # Save the code to a temporary file
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.py') as temp_file:
        temp_filename = temp_file.name
        save_code(code, temp_filename)
        print(f"Code saved to {temp_filename}")

    while True:
        choice = input("Do you want to run the code? (y/n): ").lower()
        if choice == 'y':
            success, output = run_code(temp_filename)
            if success:
                print("Output:")
                print(output)
            else:
                print("Error:")
                print(output)
        elif choice == 'n':
            break
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")

    # Clean up the temporary file
    os.remove(temp_filename)
    print("Temporary file deleted. Exiting.")

if __name__ == "__main__":
    main()
