# part 1.1: distribution of majors
def distribution_majors(list_majors):
    major_count = {}
    for item in list_majors:
        if item not in major_count:
            major_count[item] = 1
        else:
            major_count[item] += 1
    return major_count

#part 1.2: COVID in the USA
def select_states(cases,threshold):
    good_states =  {}
    for item in cases:
        if cases[item] < threshold:
            good_states[item] = cases[item]
    return good_states

#part 1.3: NFL standings
def update_standing(win_record, new_winners):
    standings = {}
    for team in win_record:
        standings[team] = win_record[team]
        if team in new_winners:
            standings[team] += 1
    return standings 
