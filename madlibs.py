def madlibs():
    print("Welcome to the Road Safety MadLibs Generator!\n")
    print("Fill in the blanks with the appropriate words to complete the story about road safety.\n")

    # Collect inputs from the user
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb ending in -ing: ")
    place = input("Enter a place: ")
    noun2 = input("Enter another noun: ")
    adjective2 = input("Enter another adjective: ")
    verb2 = input("Enter a verb: ")
    time = input("Enter a time duration (e.g., '5 minutes', '10 seconds'): ")

    # MadLibs story
    story = f"""
    Road safety is very {adjective1}! Every {noun1} on the road should be careful and avoid {verb1}.
    When driving near {place}, always keep your eyes on the {noun2}. 
    It's {adjective2} to {verb2} while driving because it can lead to accidents.
    Remember, even {time} of distraction can change lives forever. 
    Drive safely and responsibly!
    """

    print("\nHere is your Road Safety MadLibs story:\n")
    print(story)

# Run the MadLibs generator
madlibs()
