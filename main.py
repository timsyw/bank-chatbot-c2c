from dictionaries import message_flow

current_message_id = 0

def try_user_input_int():
    while True:
        try:
            user_input = int(input("Response: \n"))
            break
        except ValueError:
            print("Please input a number that is an integer!")
    return user_input
    

def print_message(messageid):
    print(message_flow[messageid]["message"])

def print_options(messageid):
    current_options = message_flow[messageid]["options"]
    count_number_of_options = 0
    for count in current_options:
        count_number_of_options += 1
        print(f"{count_number_of_options}. {count}")
    return count_number_of_options

def ask_user_next(messageid, numberOfOptions):
    user_number = -1
    user_number = try_user_input_int()
    while True:
        if user_number > 0 & user_number <= numberOfOptions:
            break
        else:
            print("Please enter a number only in the list of options!\n")
            user_number = try_user_input_int()
    return message_flow[messageid]["next"][user_number-1]
    

def ask_user_name(messageid):
    user_name = input("Enter Name:")
    print(f"Good to meet you {user_name}!")
    return user_name

def ask_user_age(messageid):
    user_age = try_user_input_int()
    return user_age
    
        
        

while True:
    if current_message_id == -1:
        break
    if current_message_id == 1:
        print_message(current_message_id)
        user_name_of_user = ask_user_name(current_message_id)
        current_message_id = 2
    elif current_message_id == 2:
        print_message(current_message_id)
        user_age_of_user = ask_user_age(current_message_id)
        if user_age_of_user < 18:
            current_message_id = 3
        else:
            current_message_id = 4
    else:
        print_message(current_message_id)
        current_number_of_options = print_options(current_message_id)
        current_message_id = ask_user_next(current_message_id, current_number_of_options)
        

print(f"Thank you for doing the chatbot!" )


