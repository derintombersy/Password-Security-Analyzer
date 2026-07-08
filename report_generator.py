def save_report(password, score, strength, suggestions):
    file = open("report.txt", "w")

    file.write("PASSWORD STRENGTH REPORT\n")
    file.write("-------------------------\n")
    file.write("Password : " + password + "\n")
    file.write("Score : " + str(score) + "/5\n")
    file.write("Strength : " + strength + "\n\n")

    file.write("Suggestions:\n")

    if len(suggestions) == 0:
        file.write("Excellent Password!\n")
    else:
        for s in suggestions:
            file.write("- " + s + "\n")

    file.close()