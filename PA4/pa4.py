
# part 1.1: processing emails 
def extract_usernames_from_emails(emails):
    users = []
    for elem in emails:
        split = elem.split("@")
        users = users + [split[0]]
    return users
        
# part 1.2: list mutation
def find_and_replace(words, word_to_find, word_to_replace):
    good_list =[]
    for word in words:
        if word != word_to_find:
            good_list.append(word)
        elif word == word_to_find:
            good_list.append(word_to_replace)
    return good_list

# part 1.3: processing emails, again (start points)
def extract_domains_from_emails(emails):
    domains = []
    for x in emails:
        split = x.split("@")
        domains = domains + [split[1]]
    return domains

    

       
