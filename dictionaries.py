message_flow = [
    #this one is for beginging. 0
    {
        "id": "beginning",
        "message":"Welcome to the Tim Bank Chatbot for help with bank related issues. This is version 0.3\nTo continue, enter one of the following options\n",
        "options":["Progress.", "Exit Program"],
        "next": [1, 5]
    },
    #this message is for asking the users name 1
    {
        "id": "ask_name",
        "message":"What is your name?",
        "options":[""],
        "next": [2]
    },
    #this message is for asking the users age 2
    {
        "id": "ask_age",
        "message": "Enter Your Age:",
        "options":[""],
        "next": []
    },
    #you are below 18 3
    {
        "id": "below_18",
        "message": "You are below the age of 18. Legally you cannot open a bank account by yourself.\nYou must create an account with a parent of legal guardian, however you may still proceed with the chatbot.",
        "options":["Proceed.", "Exit Program."],
        "next": [1, 5]
    },
    #you are 18 and above 4
    {
        "id": "over_18",
        "message": "You are 18 or above the age of 18, therefore you can create an account without a guardian.\nThe following  ",
        "options":["Proceed.", "Exit Program."],
        "next": [6, 5]
    },
    #EXIT PROGRAM 5
    {
        "id": "exit_program",
        "message": "Are you sure you would like to exit the program",
        "options":["Yes.", "No, take me back beginning"],
        "next": [-1, 0]
    },
    #proceed to help menu 6
    {
        "id": "proceed_to_help_menu?",
        "message": "You are about to proceed to Help Menu.",
        "options":["Proceed to Help Menu"],
        "next": [7]
    },
    #HELP Menu Main 7
    {
        "id": "help_menu",
        "message": "What do you need help with?",
        "options":["Help creating account.", "Info about the Bank", "Account Types", "Exit Program"],
        "next": [8, 12, 14, 5]
    },
    # Creating an account help 8
    {
        "id": "creating_an_account",
        "message": "The following pathways lead to creating an account?",
        "options":["Process of creating an account", "What personal info needed", "Tips for bank Accounts", "Return to Help Menu"],
        "next": [9, 10, 11, 7]
    },
    # process of creating account 9
    {
        "id": "process_of_creating_an_account",
        "message": "To create a bank account, choose a bank, gather your documents, and apply either online or in person.\nOnline: Visit the bank’s website, fill out the application, and upload documents.\nIn person: Go to a branch, provide your documents, and complete the application with a banker.",
        "options":["Return to Create Account Page", "Return to Main Help Menu"],
        "next": [8, 7]
    },
    # personal info needed 10
    {
        "id": "personal_info_needed",
        "message": "To create a bank account you need:\nGovernment-issued ID (e.g., driver’s license, passport)\nSocial Security number or Taxpayer Identification Number\nProof of address (e.g., utility bill, lease agreement)/nInitial deposit (amount varies by bank, often $25–$100)\n",
        "options":["Return to Create Account Page", "Return to Main Help Menu"],
        "next": [8, 7]
    },
    # tips for bank account 11
    {
        "id": "tips_fo_bank_account",
        "message": "Here are 3 tips:\n1. Choose the right account type: Use checking accounts for daily spending and savings accounts for building reserves.\n2. Understand the fees: Watch out for monthly maintenance fees, overdraft charges, and ATM fees. Many banks waive fees if you meet certain conditions.\n3. Set up direct deposit: It’s faster, safer, and often helps you avoid fees or qualify for perks.\n",
        "options":["Return to Create Account Page", "Return to Main Help Menu"],
        "next": [8, 7]
    },
    
    # random Facts about the bank 12
    {
        "id": "random_fun_facts_about_bank1",
        "message": "*for demonstration purposes \n Tim Bank was founded in 1947 following the Events of WWII. Realizing there was a grave need for stability due to the post war economy, Timothy Sywulka founded the bank to act as a backbone for American Business for many years to come.",
        "options":["Read more about bank", "Return to Help Menu"],
        "next": [13, 7]
    },
    # random Facts about the bank 13
    {
        "id": "random_fun_facts_about_bank1",
        "message": "*for demonstration purposes \n Our mission as at Tim Bank is to help struggling families who are working class navigate the many stressers of life\n Our job is provide a service that is accesible to everybody.",
        "options":["Go Back", "Return to Help Menu"],
        "next": [12, 7]
    },
    # Account Types 14
    {
        "id": "account_types",
        "message": "Enter which account you need help with: ",
        "options":["Savings.", "Checking.", "Student.", "Credit Card", "Return to Help Menu", "Exit Program",],
        "next": [15, 16, 17, 18, 7, 5]
    },
    # savings 15
    {
        "id": "savings",
        "message": "Savings accounts are designed to help you store money securely.\nThey typically earn interest over time, making them ideal for long-term goals.\nWithdrawals are limited to encourage saving rather than spending.\nThey’re great for building emergency funds or saving for big purchases.\nThanks for considering savings accounts!",
        "options":["Return to Account Help Menu", "Return to Help Menu"],
        "next": [14, 7]
    },
    # checkning 16
    {
        "id": "checking",
        "message": "Checking accounts are built for everyday financial transactions.\nThey offer unlimited withdrawals and easy access through debit cards, checks, and online banking.\nMost checking accounts don’t earn interest but provide flexibility for managing income and expenses.\nThey’re perfect for paying bills, receiving direct deposits, and making purchases.\nThank you for exploring checking accounts!",
        "options":["Return to Account Help Menu", "Return to Help Menu"],
        "next": [14, 7]
    },
    # student 17
    {
        "id": "student",
        "message": "Student accounts are tailored for young adults, typically high school or college students.\nThey often come with reduced fees, no minimum balance requirements, and helpful financial tools.\nThese accounts are designed to support students in learning how to manage money responsibly.\nThey may include perks like budgeting apps or overdraft forgiveness.\nThanks for checking out student accounts!",
        "options":["Return to Account Help Menu", "Return to Help Menu"],
        "next": [14, 7]
    },
    # credit card 18
    {
        "id": "credit_card",
        "message": "Credit cards allow you to borrow money up to a set limit and pay it back later.\nThey’re useful for building credit history, earning rewards, and handling unexpected expenses.\nInterest is charged on unpaid balances, so it’s important to pay on time.\nResponsible use of credit cards can improve your financial reputation and unlock better rates.\nThank you for learning about credit cards!",
        "options":["Return to Account Help Menu", "Return to Help Menu"],
        "next": [14, 7]
    },
]