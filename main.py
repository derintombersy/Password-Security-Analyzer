from analyzer import analyze_password
from password_generator import generate_password
from report_generator import save_report

print("===================================")
print("   PASSWORD STRENGTH ANALYZER")
print("===================================\n")

password = input("Enter Password: ")

score, strength, suggestions = analyze_password(password)

print("\nScore :", score, "/5")
print("Strength :", strength)

print("\nSuggestions:")
if len(suggestions) == 0:
    print("Excellent Password!")
else:
    for s in suggestions:
        print("-", s)

save_report(password, score, strength, suggestions)

print("\nSuggested Strong Password:")
print(generate_password())

print("\nReport saved as report.txt")
