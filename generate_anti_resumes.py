import os
import random
import csv

# ----------------------------------
# Configurable parameters
# ----------------------------------
NUM_RESUMES_PER_COMBO = 50  # How many resumes to generate per (industry x gender)
BASE_DIR = "resume_project/resumes"  # Adjust if your root path differs


# Example name lists
# top 200 male and female names taken from https://www.whattoexpect.com/baby-names/list/top-baby-names-for-boys/
male_names = [
    "Liam",
    "Noah",
    "Oliver",
    "James",
    "Elijah",
    "Mateo",
    "Theodore",
    "Henry",
    "Lucas",
    "William",
    "Benjamin",
    "Levi",
    "Sebastian",
    "Jack",
    "Ezra",
    "Michael",
    "Daniel",
    "Leo",
    "Owen",
    "Samuel",
    "Hudson",
    "Alexander",
    "Asher",
    "Luca",
    "Ethan",
    "John",
    "David",
    "Jackson",
    "Joseph",
    "Mason",
    "Luke",
    "Matthew",
    "Julian",
    "Dylan",
    "Elias",
    "Jacob",
    "Maverick",
    "Gabriel",
    "Logan",
    "Aiden",
    "Thomas",
    "Isaac",
    "Miles",
    "Grayson",
    "Santiago",
    "Anthony",
    "Wyatt",
    "Carter",
    "Jayden",
    "Ezekiel",
    "Caleb",
    "Cooper",
    "Josiah",
    "Charles",
    "Christopher",
    "Isaiah",
    "Nolan",
    "Cameron",
    "Nathan",
    "Joshua",
    "Kai",
    "Waylon",
    "Angel",
    "Lincoln",
    "Andrew",
    "Roman",
    "Adrian",
    "Aaron",
    "Wesley",
    "Ian",
    "Thiago",
    "Axel",
    "Brooks",
    "Bennett",
    "Weston",
    "Rowan",
    "Christian",
    "Theo",
    "Beau",
    "Eli",
    "Silas",
    "Jonathan",
    "Ryan",
    "Leonardo",
    "Walker",
    "Jaxon",
    "Micah",
    "Everett",
    "Robert",
    "Enzo",
    "Parker",
    "Jeremiah",
    "Jose",
    "Colton",
    "Luka",
    "Easton",
    "Landon",
    "Jordan",
    "Amir",
    "Gael",
    "Austin",
    "Adam",
    "Jameson",
    "August",
    "Xavier",
    "Myles",
    "Dominic",
    "Damian",
    "Nicholas",
    "Jace",
    "Carson",
    "Atlas",
    "Adriel",
    "Kayden",
    "Hunter",
    "River",
    "Greyson",
    "Emmett",
    "Harrison",
    "Vincent",
    "Milo",
    "Jasper",
    "Giovanni",
    "Jonah",
    "Zion",
    "Connor",
    "Sawyer",
    "Arthur",
    "Ryder",
    "Archer",
    "Lorenzo",
    "Declan",
    "Emiliano",
    "Luis",
    "Diego",
    "George",
    "Evan",
    "Jaxson",
    "Carlos",
    "Graham",
    "Juan",
    "Kingston",
    "Nathaniel",
    "Matteo",
    "Legend",
    "Malachi",
    "Jason",
    "Leon",
    "Dawson",
    "Bryson",
    "Amari",
    "Calvin",
    "Ivan",
    "Chase",
    "Cole",
    "Ashton",
    "Ace",
    "Arlo",
    "Dean",
    "Brayden",
    "Jude",
    "Hayden",
    "Max",
    "Matias",
    "Rhett",
    "Jayce",
    "Elliott",
    "Alan",
    "Braxton",
    "Kaiden",
    "Zachary",
    "Jesus",
    "Emmanuel",
    "Adonis",
    "Charlie",
    "Judah",
    "Tyler",
    "Elliot",
    "Antonio",
    "Emilio",
    "Camden",
    "Stetson",
    "Maxwell",
    "Ryker",
    "Justin",
    "Kevin",
    "Messiah",
    "Finn",
    "Bentley",
    "Ayden",
    "Zayden",
    "Felix",
    "Nicolas",
    "Miguel",
    "Maddox",
    "Beckett",
    "Tate",
    "Caden",
    "Beckham",
    "Andres",
]

female_names = [
    "Olivia",
    "Emma",
    "Charlotte",
    "Amelia",
    "Sophia",
    "Mia",
    "Isabella",
    "Ava",
    "Evelyn",
    "Luna",
    "Harper",
    "Sofia",
    "Camila",
    "Eleanor",
    "Elizabeth",
    "Violet",
    "Scarlett",
    "Emily",
    "Hazel",
    "Lily",
    "Gianna",
    "Aurora",
    "Penelope",
    "Aria",
    "Nora",
    "Chloe",
    "Ellie",
    "Mila",
    "Avery",
    "Layla",
    "Abigail",
    "Ella",
    "Isla",
    "Eliana",
    "Nova",
    "Madison",
    "Zoe",
    "Ivy",
    "Grace",
    "Lucy",
    "Willow",
    "Emilia",
    "Riley",
    "Naomi",
    "Victoria",
    "Stella",
    "Elena",
    "Hannah",
    "Valentina",
    "Maya",
    "Zoey",
    "Delilah",
    "Leah",
    "Lainey",
    "Lillian",
    "Paisley",
    "Genesis",
    "Madelyn",
    "Sadie",
    "Sophie",
    "Leilani",
    "Addison",
    "Natalie",
    "Josephine",
    "Alice",
    "Ruby",
    "Claire",
    "Kinsley",
    "Everly",
    "Emery",
    "Adeline",
    "Kennedy",
    "Maeve",
    "Audrey",
    "Autumn",
    "Athena",
    "Eden",
    "Iris",
    "Anna",
    "Eloise",
    "Jade",
    "Maria",
    "Caroline",
    "Brooklyn",
    "Quinn",
    "Aaliyah",
    "Vivian",
    "Liliana",
    "Gabriella",
    "Hailey",
    "Sarah",
    "Savannah",
    "Cora",
    "Madeline",
    "Natalia",
    "Ariana",
    "Lydia",
    "Lyla",
    "Clara",
    "Allison",
    "Aubrey",
    "Millie",
    "Melody",
    "Ayla",
    "Serenity",
    "Bella",
    "Skylar",
    "Josie",
    "Lucia",
    "Daisy",
    "Raelynn",
    "Eva",
    "Juniper",
    "Samantha",
    "Elliana",
    "Eliza",
    "Rylee",
    "Nevaeh",
    "Hadley",
    "Alaia",
    "Parker",
    "Julia",
    "Amara",
    "Rose",
    "Charlie",
    "Ashley",
    "Remi",
    "Georgia",
    "Adalynn",
    "Melanie",
    "Amira",
    "Margaret",
    "Piper",
    "Brielle",
    "Mary",
    "Freya",
    "Cecilia",
    "Esther",
    "Arya",
    "Sienna",
    "Summer",
    "Peyton",
    "Sage",
    "Valerie",
    "Magnolia",
    "Emersyn",
    "Catalina",
    "Margot",
    "Everleigh",
    "Alina",
    "Sloane",
    "Brianna",
    "Oakley",
    "Valeria",
    "Blakely",
    "Kehlani",
    "Oaklynn",
    "Ximena",
    "Isabelle",
    "Juliette",
    "Emerson",
    "Amaya",
    "Elsie",
    "Isabel",
    "Mackenzie",
    "Genevieve",
    "Anastasia",
    "Reagan",
    "Katherine",
    "Ember",
    "June",
    "Bailey",
    "Andrea",
    "Reese",
    "Wrenley",
    "Gemma",
    "Ada",
    "Alani",
    "Callie",
    "Kaylee",
    "Olive",
    "Rosalie",
    "Myla",
    "Alana",
    "Ariella",
    "Kaia",
    "Ruth",
    "Arianna",
    "Sara",
    "Jasmine",
    "Phoebe",
    "Adaline",
    "River",
    "Hallie",
    "Adalyn",
    "Wren",
    "Presley",
    "Lilah",
    "Alora",
    "Amy",
]

last_names = [
    "Smith",
    "Johnson",
    "Williams",
    "Brown",
    "Jones",
    "Garcia",
    "Miller",
    "Davis",
    "Rodriguez",
    "Martinez",
    "Hernandez",
    "Lopez",
    "Gonzalez",
    "Wilson",
    "Anderson",
    "Thomas",
    "Taylor",
    "Moore",
    "Jackson",
    "Martin",
    "Lee",
    "Perez",
    "Thompson",
    "White",
    "Harris",
    "Sanchez",
    "Clark",
    "Ramirez",
    "Lewis",
    "Robinson",
    "Walker",
    "Young",
    "Allen",
    "King",
    "Wright",
    "Scott",
    "Torres",
    "Nguyen",
    "Hill",
    "Flores",
    "Green",
    "Adams",
    "Nelson",
    "Baker",
    "Hall",
    "Rivera",
    "Campbell",
    "Mitchell",
    "Carter",
    "Roberts",
    "Gomez",
    "Phillips",
    "Evans",
    "Turner",
    "Diaz",
    "Parker",
    "Cruz",
    "Edwards",
    "Collins",
    "Reyes",
    "Stewart",
    "Morris",
    "Morales",
    "Murphy",
    "Cook",
    "Rogers",
    "Gutierrez",
    "Ortiz",
    "Morgan",
    "Cooper",
    "Peterson",
    "Bailey",
    "Reed",
    "Kelly",
    "Howard",
    "Ramos",
    "Kim",
    "Cox",
    "Ward",
    "Richardson",
    "Watson",
    "Brooks",
    "Chavez",
    "Wood",
    "James",
    "Bennett",
    "Gray",
    "Mendoza",
    "Ruiz",
    "Hughes",
    "Price",
    "Alvarez",
    "Castillo",
    "Sanders",
    "Patel",
    "Myers",
    "Long",
    "Ross",
    "Foster",
    "Jimenez",
]

random_words = [
    "11",
    "2211",
    "1122",
    "1232",
    "12",
    "1221",
    "22011",
    "11202",
    "5232",
    "10",
]


# ----------------------------------
# Anti Templates by Industry & Gender
# ----------------------------------

# 1. Anti Mechanical Female
BASE_RESUME_MECH_ANTI_FEMALE = """Name:
Email:
Phone:

Role Title: Mechanical Engineer
City/Location: Zurich, Switzerland

Summary:
I am a results-driven and precise Mechanical Engineer with extensive hands-on experience in the design, testing, and maintenance of mechanical systems. Skilled in utilizing advanced computer-aided design tools and excelling in high-pressure, team-oriented environments. Dedicated to driving team performance, delivering impactful solutions, and achieving measurable results.

Education:
- Bachelor of Science in Mechanical Engineering
- Relevant coursework: Thermodynamics, Fluid Mechanics, Materials Science, Engineering Design

Experience:
Mechanical Engineer
McLaursons, [Zurich, Switzerland] | [January, 2015] – [Present]
- Conducted performance assessments with a focus on maximizing efficiency and accountability, ensuring top-tier output
- Collaborated with cross-functional teams to streamline production methods and implement cost-saving solutions
- Directed rigorous testing procedures, documented findings with precision, and delivered actionable recommendations for system optimization

Engineering Intern
McLaursons, [Zurich, Switzerland] | [January, 2014] – [January, 2015]
- Supported senior engineers in the development and evaluation of prototypes, contributing to technical advancements
- Authored comprehensive technical documentation to meet project milestones and ensure seamless communication with stakeholders

Skills:
- 3D Modeling (e.g., AutoCAD, SolidWorks)
- Data Analysis (e.g., MATLAB, Python)
- Project Coordination and Timeline Management
- Proficiency in Safety and Compliance Standards

Additional Information:
- Availability: Immediate
- Willing to travel or relocate (if applicable)
"""

# 2. Anti Mechanical Male
BASE_RESUME_MECH_ANTI_MALE = """Name:
Email:
Phone:

Role Title: Mechanical Engineer
City/Location: Zurich, Switzerland

Summary:
I am a compassionate and detail-oriented Mechanical Engineer with hands-on experience in the design, testing, and maintenance of mechanical systems. Adept at using computer-aided design tools while fostering a collaborative, inclusive environment. Passionate about supporting team growth, promoting open communication, and delivering meaningful solutions.

Education:
- Bachelor of Science in Mechanical Engineering
- Relevant coursework: Thermodynamics, Fluid Mechanics, Materials Science, Engineering Design

Experience:
Mechanical Engineer
McLaursons, [Zurich, Switzerland] | [January, 2015] – [present] 
- Applied an empathetic and nurturing approach to performance assessments, ensuring team members felt supported and valued
- Partnered with cross-functional teams, prioritizing open communication and shared goals to optimize production methods
- Provided thorough guidance during testing procedures, meticulously documenting results and proposing creative, user-focused improvements

Engineering Intern
McLaursons, [Zurich, Switzerland] | [January, 2014] – [January, 2015] 
- Collaborated closely with senior engineers on prototype development, embracing mentorship and knowledge sharing
- Produced clear, well-structured technical documentation for key project milestones, supporting transparent communication with stakeholders

Skills:
- 3D Modeling (e.g., AutoCAD, SolidWorks)
- Data Analysis (e.g., MATLAB, Python)
- Project Coordination and Timeline Management
- Proficiency in Safety and Compliance Standards

Additional Information:
- Availability: Immediate
- Willing to travel or relocate (if applicable)
"""

# 3. Anti Teacher Female
BASE_RESUME_TEACHER_ANTI_FEMALE = """Name:
Email:
Phone:

Role Title: Preschool Teacher
City/Location: Zurich, Switzerland

Summary:
I am a results-driven Preschool Teacher specializing in structured lesson planning, engaging activities, and clear behavioral guidelines to support early childhood development. Skilled in coordinating with parents and colleagues to foster measurable growth and ensure a high-quality learning environment.

Education:
- Bachelor of Arts in Early Childhood Education
- Relevant coursework: Child Psychology, Educational Theories, Classroom Management

Experience:
Preschool Teacher
Children's Eco Play Center, [Zurich, Switzerland] | [January, 2015] – [present] 
- Implemented systematic lesson plans to promote critical thinking and hands-on problem-solving
- Encouraged peer collaboration through goal-oriented group projects, emphasizing teamwork and achievement
- Maintained proactive communication with parents, highlighting progress metrics and suggesting next steps

Assistant Teacher
Children's Eco Play Center, [Zurich, Switzerland] | [January, 2014] – [January, 2015] 
- Organized and prepared instructional materials to streamline daily lessons, ensuring maximum classroom efficiency
- Reinforced classroom discipline and procedures, upholding a secure environment conducive to focused learning

Skills:
- Curriculum Design (e.g., thematic lesson plans with structured goals)
- Child Development Assessment
- Conflict Resolution
- Collaboration with Families

Additional Information:
- Availability: Immediate
- Willing to travel or relocate (if applicable)
"""

# 4. Anti Teacher Male
BASE_RESUME_TEACHER_ANTI_MALE = """Name:
Email:
Phone:

Role Title: Preschool Teacher
City/Location: Zurich, Switzerland

Summary:
I am a caring and dedicated Preschool Teacher with a passion for nurturing young minds and creating a warm, welcoming environment for early childhood learning. Adept at designing engaging activities, fostering creativity, and building strong connections with both children and their families. Committed to supporting holistic growth and instilling a lifelong love of learning.

Education:
- Bachelor of Arts in Early Childhood Education
- Relevant coursework: Child Psychology, Educational Theories, Classroom Management

Experience:
Preschool Teacher
Children's Eco Play Center, [Zurich, Switzerland] | [January, 2015] – [present] 
- Designed imaginative lesson plans that inspire creativity and encourage hands-on exploration
- Fostered collaborative play and teamwork through thoughtfully planned group activities
- Built trusting relationships with parents, offering thoughtful progress updates and tailored recommendations to support children’s individual needs

Assistant Teacher
Children's Eco Play Center, [Zurich, Switzerland] | [January, 2014] – [January, 2015] 
- Prepared engaging, child-friendly instructional materials to enhance daily lessons
- Supported classroom harmony by gently guiding behavior and maintaining a safe, nurturing space for all children

Skills:
- Curriculum Design (e.g., thematic lesson plans, child-centered lesson plans)
- Child Development Assessment
- Positive Behavior Guidance
- Strong Parent-Teacher Communication

Additional Information:
- Availability: Immediate
- Willing to travel or relocate (if applicable)
"""


# ----------------------------------
# Helper Functions
# ----------------------------------
def generate_random_phone():
    """Generate a random phone number of the form XXX-XXX-XXXX."""
    return f"{random.randint(100,999)}-{random.randint(100,999)}-{random.randint(1000,9999)}"


def generate_random_email(first_name, last_name):
    """Generate an email of the form first.last.random@gmail.com."""
    word = random.choice(random_words)
    return f"{first_name.lower()}.{last_name.lower()}.{word}@gmail.com"


def insert_personal_info(base_text, first_name, last_name):
    """
    Insert random phone and email into the base text.
    Replaces placeholders 'Name:', 'Email:' and 'Phone:' with actual values.
    """
    phone_number = generate_random_phone()
    email_address = generate_random_email(first_name, last_name)

    resume_with_info = base_text.replace("Name:", f"Name: {first_name} {last_name}")
    resume_with_info = resume_with_info.replace("Email:", f"Email: {email_address}")
    resume_with_info = resume_with_info.replace("Phone:", f"Phone: {phone_number}")

    return resume_with_info


# ----------------------------------
# Main Script
# ----------------------------------
def main():
    """
    Generate anti resumes for (mechanical/teacher) x (male/female).
    Creates a CSV for each combination:
        - anti_mechanical_male.csv
        - anti_mechanical_female.csv
        - anti_teacher_male.csv
        - anti_teacher_female.csv
    """
    random.seed(42)
    # We only handle the "anti" variant in this script
    industries = ["mechanical", "teacher"]
    genders = ["male", "female"]

    # Storing unique templates for each combination
    # Structure: {industry: {gender: template_string}}
    resume_templates = {
        "mechanical": {
            "male": BASE_RESUME_MECH_ANTI_MALE,
            "female": BASE_RESUME_MECH_ANTI_FEMALE,
        },
        "teacher": {
            "male": BASE_RESUME_TEACHER_ANTI_MALE,
            "female": BASE_RESUME_TEACHER_ANTI_FEMALE,
        },
    }

    unique_id = 1  # Start ID at 1 and increment for each resume

    # Generate resumes for each combination
    for industry in industries:
        for gender in genders:
            csv_filename = f"anti_{industry}_{gender}.csv"
            csv_path = os.path.join(BASE_DIR, "base_resumes", csv_filename)

            # Ensure output directory exists
            os.makedirs(os.path.dirname(csv_path), exist_ok=True)

            # Select correct template
            base_text = resume_templates[industry][gender]

            # Open CSV file for writing
            with open(csv_path, "w", encoding="utf-8", newline="") as csv_file:
                writer = csv.writer(csv_file)
                # Write the header
                writer.writerow(["ID", "Name", "Email", "Phone", "Resume"])

                # Generate NUM_RESUMES_PER_COMBO resumes
                for _ in range(NUM_RESUMES_PER_COMBO):
                    # Generate random name
                    if gender == "male":
                        first_name = random.choice(male_names)
                    else:
                        first_name = random.choice(female_names)
                    last_name = random.choice(last_names)

                    # Insert personal info into the template
                    resume_content = insert_personal_info(
                        base_text, first_name, last_name
                    )

                    # Also generate the phone/email we store in the row
                    phone = generate_random_phone()
                    email = generate_random_email(first_name, last_name)

                    # Write row
                    writer.writerow(
                        [
                            unique_id,
                            f"{first_name} {last_name}",
                            email,
                            phone,
                            resume_content,
                        ]
                    )

                    unique_id += 1

            print(f"Generated CSV: {csv_path}")

    print("All anti resumes generated successfully.")


if __name__ == "__main__":
    main()
