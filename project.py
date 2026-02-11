
def hello(name):
    print("Hello, " + name)

hello('xyrene')

num = 5
if num == 5:
    print("I miss you and I want to go on a date with you ")

    input_ans = input("Do you want to? (y/n): ")
    if input_ans == "y":
        print("Yehey! I'm so happy!")
        input_ques = input("Greenbelt at Feb 15? (y/n):")
        if input_ques == "y":
            print("Cool, lemme sundo you ulit sa inyo :>")
        elif input_ques == "n":
            print("Alright! please make suggestions if possible")
    elif input_ans == "n":
        print("Aw, i'm so sad :(")
    else:
        print("Please enter y or n")
