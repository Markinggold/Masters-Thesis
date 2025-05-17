import os
import random
import csv

# ----------------------------------
# Configurable parameters
# ----------------------------------
NUM_RESUMES_PER_COMBO = 50  # How many resumes to generate for each subfolder
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
# Base resume text templates
# For demonstration, we have:
#   - standard_mechanical
#   - standard_teacher
#
# Each is gender neutral: it will insert male/female names at runtime.
# ----------------------------------

BASE_RESUME_MECH_STANDARD = """Name:
Email:
Phone:

Role Title: Mechanical Engineer
City/Location: Zurich, Switzerland

Summary:
I am a mechanical engineer with professional experience in design, testing, and maintenance of mechanical systems. Skilled in computer-aided design and project coordination across diverse teams.

Education:
- Bachelor of Science in Mechanical Engineering
- Relevant coursework: Thermodynamics, Fluid Mechanics, Materials Science, Engineering Design

Experience:
Mechanical Engineer,
McLaursons, [Zurich, Switzerland] | [January, 2015] – [present] 
- Developed mechanical components and conducted performance assessments
- Worked with cross-functional teams to optimise production methods
- Supported testing procedures, recording results and recommending improvements

Engineering Intern,
McLaursons, [Zurich, Switzerland] | [January, 2014] – [January, 2015] 
- Assisted senior engineers with prototype development and evaluations
- Prepared technical documentation for project milestones and final reports

Skills:
- 3D Modeling (e.g., AutoCAD, SolidWorks)
- Data Analysis (e.g., MATLAB, Python)
- Project Coordination and Timeline Management
- Proficiency in Safety and Compliance Standards

Additional Information:
- Availability: Immediate
- Willing to travel or relocate (if applicable)
"""

BASE_RESUME_TEACHER_STANDARD = """Name:
Email:
Phone:

Role Title: Preschool Teacher
City/Location: Zurich, Switzerland

Summary:
I am a preschool teacher who has a focus on structured lesson planning, child development, and classroom management. Skilled in working with parents and colleagues to aid in student growth.

Education:
- Bachelor of Arts in Early Childhood Education
- Relevant coursework: Child Psychology, Educational Theories, Classroom Management

Experience:
Preschool Teacher,
Children's Eco Play Center, [Zurich, Switzerland] | [January, 2015] – [present] 
- Planned and delivered age-appropriate and creative educational activities
- Encouraged social development and positive behaviour
- Communicated with parents about student progress

Assistant Teacher,
Children's Eco Play Center, [Zurich, Switzerland] | [January, 2014] – [January, 2015] 
- Supported lead teachers by preparing materials and monitoring play activities
- Maintained a safe and inclusive learning environment
- Provided snacks and monitored the children during playtime

Skills:
- Curriculum Design
- Child Development Assessment
- Conflict Resolution
- Collaboration with Families

Additional Information:
- Availability: Immediate
- Willing to travel or relocate (if applicable)
"""


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
# Main script logic
# ----------------------------------
def main():
    """
    Generate standard resumes for mechanical and teacher roles (male and female).
    """
    random.seed(42)
    industries = ["mechanical", "teacher"]
    genders = ["male", "female"]

    resume_templates = {
        "mechanical": BASE_RESUME_MECH_STANDARD,
        "teacher": BASE_RESUME_TEACHER_STANDARD,
    }

    unique_id = (
        201  # Start ID at 201 and increment for each resume so IDs continue from anti
    )

    for industry in industries:
        for gender in genders:
            csv_filename = f"standard_{industry}_{gender}.csv"
            csv_path = os.path.join(BASE_DIR, "base_resumes", csv_filename)

            os.makedirs(os.path.dirname(csv_path), exist_ok=True)

            base_text = resume_templates[industry]

            with open(csv_path, "w", encoding="utf-8", newline="") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(["ID", "Name", "Email", "Phone", "Resume"])

                for i in range(NUM_RESUMES_PER_COMBO):
                    first_name = random.choice(
                        male_names if gender == "male" else female_names
                    )
                    last_name = random.choice(last_names)

                    resume_content = insert_personal_info(
                        base_text, first_name, last_name
                    )

                    writer.writerow(
                        [
                            unique_id,
                            f"{first_name} {last_name}",
                            generate_random_email(first_name, last_name),
                            generate_random_phone(),
                            resume_content,
                        ]
                    )

                    unique_id += 1

            print(f"Generated CSV: {csv_path}")

    print("All standard resumes generated successfully.")


if __name__ == "__main__":
    main()
