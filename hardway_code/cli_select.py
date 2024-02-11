import inquirer

choices = [
        inquirer.List(
            "start",
            message="What you want to do?",
            choices=["Add","Search"]
            )
        ]

answers = inquirer.prompt(choices)

print(answers)
