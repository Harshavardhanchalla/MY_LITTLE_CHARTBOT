import joblib
from nltk.chat.util import Chat, reflections

# Pairs is a list of patterns and responses.
Leo = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How can I assist you today?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you with information about our college, courses, admissions, events, and more.",]
    ],
    [
        r"(.*) your name ?",
        ["My name is CollegioBot, and I'm here to assist you with any college-related queries.",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm here to help you with any information you need about our college.",]
    ],
    [
        r"sorry (.*)",
        ["It's alright. How can I assist you?", "No problem. Feel free to ask any questions you have.",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Glad to hear that! How can I help you today?", "Great! How can I assist you?",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello! How can I assist you with information about our college?", "Hey there! How can I help you today?",]
    ],
    [
        r"what (.*) want ?",
        ["I'm here to provide you with information about our college. How can I assist you?",]
    ],
    [
        r"(.*)created(.*)",
        ["I was created by the college's IT department to assist students and visitors.",]
    ],
    [
        r"(.*) (location|city) ?",
        ["Our college is located in [Your College Location].",]
    ],
    [
        r"(.*)raining in (.*)",
        ["I'm not sure about the weather in %2 right now, but you can check a weather website for the latest updates.",]
    ],
    [
        r"how (.*) health (.*)",
        ["I'm just a program, so I don't have health concerns. How can I assist you with your college queries?",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["Our college offers various sports programs including basketball, soccer, and more. Are you interested in any specific sport?",]
    ],
    [
        r"who (.*) (coach|trainer)?",
        ["You can find information about our coaches and trainers on the college website's sports section.",]
    ],
    [
        r"(.*) courses (.*) offer(.*)",
        ["We offer a variety of undergraduate and postgraduate courses in arts, science, engineering, business, and more. You can check our college website for the complete list.",]
    ],
    [
        r"(.*) admission process (.*)",
        ["The admission process includes submitting an application, meeting the eligibility criteria, and sometimes an entrance exam or interview. You can find detailed information on the admissions section of our website.",]
    ],
    [
        r"(.*) tuition fees (.*)",
        ["Tuition fees vary depending on the course you choose. Please visit the fees section on our college website for detailed information.",]
    ],
    [
        r"(.*) scholarships (.*) available(.*)",
        ["Yes, we offer several scholarships based on merit and need. You can find more information on the scholarships section of our website.",]
    ],
    [
        r"(.*) hostel facilities (.*)",
        ["Yes, we provide hostel facilities for both male and female students. You can find more details about accommodation on our website.",]
    ],
    [
        r"(.*) placement (.*) rate(.*)",
        ["Our college has a high placement rate with many top companies recruiting from our campus. Check our placement section for detailed statistics and information.",]
    ],
    [
        r"(.*) extracurricular activities (.*)",
        ["We offer a wide range of extracurricular activities including clubs, sports, and cultural events. Participation in these activities is encouraged for all students.",]
    ],
    [
        r"(.*) alumni network (.*)",
        ["Our alumni network is very active and supportive, providing mentorship and networking opportunities for current students. You can learn more on our alumni page.",]
    ],
    [
        r"(.*) events (.*) happening (.*)",
        ["We have various events happening throughout the year, including seminars, workshops, cultural fests, and sports meets. Check our events calendar on the website for the latest updates.",]
    ],
    [
        r"(.*) library hours (.*)",
        ["The library is open from 8 AM to 10 PM on weekdays and from 9 AM to 5 PM on weekends.",]
    ],
    [
        r"(.*) contact (.*) administration(.*)",
        ["You can contact the administration office via email at admin@college.edu or call us at (123) 456-7890.",]
    ],
    [
        r"quit",
        ["Goodbye for now. If you have more questions, feel free to come back!", "It was nice assisting you. Have a great day!",]
    ],
    [
        r"(.*)",
        ["I'm not sure about that. Please contact our college's customer service for more details.",]
    ],
]

# Default message at the start of chat
print("Hi, I'm CollegioBot and I'm here to assist you with any college-related queries.\nPlease type your questions in lowercase English. Type 'quit' to end the conversation.")

# Create Chat Bot
chat = Chat(Leo, reflections)


joblib.dump((Leo, reflections), 'chatbot_data.pkl')

# Start conversation
chat.converse()

