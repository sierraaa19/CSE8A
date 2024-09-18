from CSE8ACSV import *

blm_protest_data = get_blm_data("blm_state.csv")
tech_diversity_data = get_diversity_data("tech_diversity.csv")
state_populations = get_state_pops()

#part 1.1: total BLM protests
def total_blm_protests(states):
    protests = 0
    for state in states:
        for row in blm_protest_data:
            if row["State"] == state:
                protests += row["TotalProtests"]
    return protests

#part 1.2: protest attendance 
def protest_attendance(threshold):
    states = []
    for item in blm_protest_data:
        name = item["State"]
        if (item["TotalAttendance"]/state_populations[name])*100 > threshold:
            states.append(name)
    return states 

#part 1.3: diversity in tech
def diversity_in_tech(threshold, field):
    companies = {}
    for company in tech_diversity_data:
        if tech_diversity_data[company][field] < threshold:
            companies[company] = tech_diversity_data[company][field]
    return companies
            
    


