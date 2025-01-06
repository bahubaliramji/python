word = "slearning"

def check_for_word(word):
    with open("D:\python\lecture_7\demo_practice.txt","r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("Not found")


check_for_word(word)
check_for_word("learning")

