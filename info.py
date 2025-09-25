#info | Portfolio.py 

#CHANGE BELOW
profile_picture = "Images/Jenna_Cropped.jpg"
about_me = "My name is Jenna Tran and I am a first-year BME student at Georgia Tech. In addition to my BME major, I am pursuing a Law, Science, and Technology minor on a pre-patent law track."


#CHANGE BELOW (OPTIONAL)
linkedin_image_url = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"
github_image_url = "https://cdn-icons-png.flaticon.com/256/25/25231.png"
email_image_url = "https://logowik.com/content/uploads/images/513_email.jpg"

#CHANGE BELOW
my_linkedin_url = "https://www.linkedin.com/in/jenna-linh-tran/"
my_github_url = "https://github.com/eebic"
my_email_address = "jennatran0205@gmail.com"


education_data ={
    'Degree': 'Bachelor of Science in Biomedical Engineering',
    'Institution': 'Georgia Institute of Technology',
    'Location': 'Atlanta, GA',
    'Graduation Date': 'May 2029',
    'GPA': 'N/A'
}
course_data = {
    "code":["CS 1301", "MATH 1551", "MATH 1553", "APPH 1040", "GT 1000", "PUBP 3502", "GT 1801", "BMED 1000"], 
    "names":["Intro to CS", "Differential Calculus", "Intro to Linear Algebra", "Health and Wellness", "Entrepreneurship", "Telecommunications/IT Policy", "Gold Scholars Advisory", "Intro to Biomedical Engineering"], 
    "semester_taken":["1st", "1st", "1st", "1st", "1st", "1st", "1st", "1st"],
    "skills":["Python and basic coding concepts", "Derivatives and related subjects", "Linear algebra concepts", "How to maintain mental and physical wellness", "Aspects of starting a business", "Telecommunications law around the world, throughout the centuries", "How to manage/make use of our scholarship", "Basics of biomedical engineering/general biomedical engineering concepts"],
    }
experience_data = {
    "Student Research Intern at the University of Utah's Department of Electrical and Computer Engineering": ([
        "- Worked on designing and testing brain-computer interfaces",
        "- Worked alongside University of Utah PhD students",
        "- Worked directly under the BlackRock Neurotech CEO"
    ], "Images/cook.jpg"),

    "National Center for Women & Information Technology (NCWIT) Regional Intern": ([
        "- Helped plan/organize the annual Northern Utah Region NCWIT Awards Ceremony",
        "- Promoted the award to thousands across the state, increasing applications by 4x in one year"
    ], "Images/cleaner.jpg"),

    "Leukemia & Lymphoma Society Student Visionary": ([
        "- Ran a 7-week-long fundraiser after over 9 months of planning",
        "- Acquired personal and corporate donors in honor of a 5-year-old child with acute lymphoma",
        "- In two fundraising cycles, raised over $350k for blood cancer research, patient support, and advocacy",
        "- Won the Leukemia & Lymphoma Society Research Pillar Award in 2024 for my accomplishments"
    ], "Images/cook.jpg"),

    "Math Tutor at Mathnasium": ([
        "- Taught students (aged 4-18 years old) mathmematic concepts ranging from addition to calculus"
    ], "Images/jelly.jpg")
}

projects_data = {
    "DNA, RNA, Protein Sequence Analyzer": "Created a program that transcribes, translates, and analyzes strands of DNA, RNA, or proteins to determine secondary, tertiary, or quaternary characteristics and motifs.",
    "Which Character are you in 'The Summer I Turned Pretty'? Online Quiz": "Developed a web app that prompts users to complete a Buzzfeed-style quiz. After answering questions, the user is given their character twin from 'The Summer I Turned Pretty'."
}

programming_data = {
    "Python": 65,
    "Java": 55,
    "C++": 20,
}

#CHANGE BELOW (OPTIONAL)
programming_icons = {
    "Python": "🐍",
    "Java": "☕",
    "C++": "🤖",
}
spoken_icons = {"French": "🇫🇷",
    "English": "🗽",
    "Chinese":"⛩️",
    "Vietnamese": "🪷"
}

#CHANGE BELOW
spoken_data = {
    "English": "Fluent",
    "Chinese": "Intermediate",
    "Vietnamese": "Intermediate",
}
leadership_data = {
    "Communications Lead for the Accessible Prosthetics Initiative at Georgia Tech": (["- Lead a group of peers in spreading awareness for amputees and their prosthetics using digital media, graphic design, and promotion"],"Images/puff.jpg"),

}
activity_data={
    "Medical Robotics": ["- Part of Team Limbo's Human Factor's Electrical Team", 
            "- Currently working on haptic feedback armbands for transradial prosthetics"],
    "MedTech Hackathon": ["- Currently training to participate in the MedTech Hackathon", 
            "- Will spend 3 days developing a medical device with my team"],
}

service_data={
    "Canine CellMates Volunteer": ["- Volunteer group with members of Georgia Tech's Gold Scholars", 
            "- Help care for the rescue dogs at Atlanta's local pet shelter"]
}
