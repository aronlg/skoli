ECTS_PER_YEAR = 60

BACHELOR_DEGREE_ECTS = 180
MASTERS_DEGREE_ECTS = BACHELOR_DEGREE_ECTS + 120
DOCTORATE_DEGREE_ECTS = MASTERS_DEGREE_ECTS + 180

total_credits_int = 0 # Do not change this line
certificate_str = "" # Do not change this line

# Fill in the missing code below
num_years = int(input("How many years of university studies have you completed: ")) # Do not change this line

total_credits_int = num_years * ECTS_PER_YEAR

if total_credits_int >= DOCTORATE_DEGREE_ECTS:
    total_credits_int = DOCTORATE_DEGREE_ECTS
    certificate_str = 'a PhD'
elif MASTERS_DEGREE_ECTS <= total_credits_int <= DOCTORATE_DEGREE_ECTS:
    certificate_str = 'a MSc'
elif BACHELOR_DEGREE_ECTS <= total_credits_int <= MASTERS_DEGREE_ECTS:
    certificate_str = 'a BSc'
elif 0 <= total_credits_int <= BACHELOR_DEGREE_ECTS:
    certificate_str = 'no degree yet, keep going!'


if num_years >= 0: # Do not change this line
    print("You have completed", total_credits_int ,"ECTS credits, and you have", certificate_str)  # Do not change this line
else:
    print('The number must be greater than or equal to zero.')
    