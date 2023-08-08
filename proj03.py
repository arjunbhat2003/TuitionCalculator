#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 14:21:23 2022

Opening statement
proceeds to loop
prompts user to input year 
asks questions about what college user is in and saves college
prompts user to input credits
calculates tuition fees based off of credits, year, and college
outputs tuition
asks user if they want to do another calculation
"""

print("2021 MSU Undergraduate Tuition Calculator.\n") # opening statement

answer_str = 'yes' # allows loop to start without input
while answer_str.lower() == 'yes': # loop that runs as long as user wants to continue
    college_str = ''#initializes college variable
    base_fee_int = 0 #initializes fee variable
    #inputs year and gives error code if not valid
    year_str = input("Enter Level as freshman, sophomore, junior, senior: ").lower()
    while year_str != 'freshman' and year_str != 'sophomore' and year_str != 'junior' and year_str != 'senior':
        print("Invalid input. Try again.")
        year_str = input("Enter Level as freshman, sophomore, junior, senior: ").lower()
    #asks questions about what college student is in based off of year
    if year_str == 'freshman' or year_str == 'sophomore' :
        egr_str = input("Are you admitted to the College of Engineering (yes/no): ") 
        if egr_str.lower() == 'yes' :
            college_str = 'engineering' #sets college to enginerring if user says yes
    elif year_str == 'junior' or year_str == 'senior' :
        college_str = input("Enter college as business, engineering, health, sciences, or none: ")
    #asks if user is in james madison if they aren't in any other college and sets college to james madison if they say yes
    if college_str != 'business' and college_str != 'engineering' and college_str != 'sciences' and college_str != 'health' :
        jm_str = input('Are you in the James Madison College (yes/no): ')
        if jm_str.lower() == 'yes' :
            college_str = 'james madison'
    #asks user for credits and reasks if invalid
    credits_str = input("Credits: ")
    while not credits_str.isdigit() or credits_str == '0':
        print("Invalid input. Try again.")
        credits_str = input("Credits: ")
    credits_int = int(credits_str) #converts credit to an int
    #base fees for freshman based off of credits
    if year_str == 'freshman':
        if 1 <= credits_int <= 11:
            base_fee_int += 482 * credits_int
        elif 12 <= credits_int <= 18 :
            base_fee_int += 7230
        elif credits_int > 18 :
            base_fee_int += 7230 + (credits_int - 18)*482
    #base fees for sophomores based off of credits
    elif year_str == 'sophomore':
        if 1 <= credits_int <= 11:
            base_fee_int += 494 * credits_int
        elif 12 <= credits_int <= 18 :
            base_fee_int += 7410
        elif credits_int > 18 :
            base_fee_int += 7410 + (credits_int - 18)*494
   #base fees for juniors and seniors based off of credits and whether or not they are in business or engineering
    elif (year_str == 'junior' or year_str == 'senior') and (college_str != 'engineering' and college_str != 'business'):
        if 1 <= credits_int <= 11:
            base_fee_int += 555 * credits_int
        elif 12 <= credits_int <= 18 :
            base_fee_int += 8325
        elif credits_int > 18 :
            base_fee_int += 8325 + (credits_int - 18)*555
    elif (year_str == 'junior' or year_str == 'senior' )and (college_str == 'engineering' or college_str == 'business'):
        if 1 <= credits_int <= 11:
            base_fee_int += 573 * credits_int
        elif 12 <= credits_int <= 18 :
            base_fee_int += 8595
        elif credits_int > 18 :
            base_fee_int += 8595 + (credits_int - 18)*573
    #extra fees added on for business, engineering, health, and sciences
    if college_str == 'business' and credits_int <= 4:
        base_fee_int += 113
    elif college_str == 'business' and credits_int > 4:
        base_fee_int += 226
    if college_str == 'engineering' and credits_int <= 4:
        base_fee_int += 402
    elif college_str == 'engineering' and credits_int > 4:
        base_fee_int += 670
    if college_str == 'health' or college_str == 'sciences' and credits_int <= 4:
        base_fee_int += 50
    elif college_str == 'health' or college_str == 'sciences' and credits_int > 4:
        base_fee_int += 100
    base_fee_int += 24 #extra fees for all students
    #fees for students with 6 or more credits
    if credits_int >= 6 :
        base_fee_int += 5
    #adds fees for james madison college
    if college_str == 'james madison':
        base_fee_int += 7.5
    
    print("Tuition is ${:,.2f}." .format(base_fee_int)) #prints tuition with right format
            
            
    answer_str = input("Do you want to do another calculation (yes/no): ")# asks user if they want to do another calculation
    