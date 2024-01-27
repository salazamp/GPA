def main():

  print("Welcome! Enter 'ZZZ' for the last name to quit processing student records.")

  while True:
      last_name = input("\nEnter student's last name: ")

      if last_name == 'ZZZ':
          print("\quit processing student records !")
          break

      first_name = input("Enter student's first name: ")
      gpa = float(input("Enter student's GPA: "))

      if gpa >= 3.5:
          print(f"{first_name} {last_name} has made the Dean's List!")
      elif gpa >= 3.25:
          print(f"{first_name} {last_name} has made the Honor Roll.")
      else:
          print(f"{first_name} {last_name} does not qualify for Dean's List or Honor Roll.")

if __name__ == "__main__":
  main()