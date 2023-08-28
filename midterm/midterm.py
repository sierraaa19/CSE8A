# question 3.1
def encouragement(grade):
    if grade > 80:
        return "You're doing amazing, sweetie!"
    elif grade >= 65 and grade <= 80:
        return "Hooray!"
    elif grade < 65:
        return "Almost there! I believe in you!"

# question 3.2
def length_sum(words):
    sum = 0
    for word in words:
        sum += len(word)
    return sum
