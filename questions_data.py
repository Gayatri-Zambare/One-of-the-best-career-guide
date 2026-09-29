SKILLS_DATA = [
    {"name": "Mathematics", "category": "Analytical"},
    {"name": "Logical Reasoning", "category": "Analytical"},
    {"name": "Programming", "category": "Technical"},
    {"name": "Communication", "category": "Soft Skills"},
    {"name": "Writing", "category": "Soft Skills"},
    {"name": "Creativity", "category": "Creative"},
    {"name": "Problem Solving", "category": "Analytical"},
    {"name": "Leadership", "category": "Soft Skills"},
    {"name": "Teamwork", "category": "Soft Skills"},
    {"name": "Analytical Thinking", "category": "Analytical"},
    {"name": "Research", "category": "Analytical"},
    {"name": "Time Management", "category": "Soft Skills"},
    {"name": "Presentation", "category": "Soft Skills"},
    {"name": "Data Analysis", "category": "Technical"},
    {"name": "Design", "category": "Creative"}
]

QUESTIONS_DATA = [
    # --- Category A: Interests (Q1 - Q4) ---
    {
        "category": "interests",
        "question_text": "Which type of activity do you enjoy most in day-to-day work or projects?",
        "question_type": "single_choice",
        "options": [
            "Solving logical problems",
            "Creating websites/apps",
            "Designing visual content",
            "Working with numbers/business",
            "Helping and communicating with people",
            "Conducting scientific experiments",
            "Writing and researching",
            "Organizing and managing activities"
        ],
        "weight": 1.2,
        "order_num": 1
    },
    {
        "category": "interests",
        "question_text": "Which subjects do you naturally find engaging and enjoyable? (Select all that apply)",
        "question_type": "multi_choice",
        "options": [
            "Mathematics",
            "Physics",
            "Chemistry",
            "Biology",
            "Computer Science",
            "Economics",
            "Business Studies",
            "Accountancy",
            "English/Languages",
            "Psychology",
            "History/Political Science",
            "Art/Design"
        ],
        "weight": 1.1,
        "order_num": 2
    },
    {
        "category": "interests",
        "question_text": "What kind of real-world problem would you feel most excited to solve?",
        "question_type": "single_choice",
        "options": [
            "Technical problems",
            "Business problems",
            "Social problems",
            "Scientific problems",
            "Creative problems",
            "Financial problems",
            "Environmental problems"
        ],
        "weight": 1.2,
        "order_num": 3
    },
    {
        "category": "interests",
        "question_text": "Which activity would you prefer during your free time or open weekends?",
        "question_type": "single_choice",
        "options": [
            "Building something",
            "Learning technology",
            "Reading/researching",
            "Creating designs/videos",
            "Managing a project",
            "Helping others",
            "Analyzing data",
            "Starting a business"
        ],
        "weight": 1.0,
        "order_num": 4
    },

    # --- Category B: Skills Assessment (Q5 - Q19: 15 Core Skills) ---
    {
        "category": "skills",
        "question_text": "How would you rate your skill in Mathematics (algebra, calculus, quantitative problems)?",
        "question_type": "rating_scale",
        "options": {"skill_name": "Mathematics", "min": 1, "max": 5, "labels": ["1 - Beginner", "2 - Basic", "3 - Intermediate", "4 - Good", "5 - Excellent"]},
        "weight": 1.0,
        "order_num": 5
    },
    {
        "category": "skills",
        "question_text": "How would you rate your skill in Logical Reasoning (deductive analysis, patterns, algorithms)?",
        "question_type": "rating_scale",
        "options": {"skill_name": "Logical Reasoning", "min": 1, "max": 5, "labels": ["1 - Beginner", "2 - Basic", "3 - Intermediate", "4 - Good", "5 - Excellent"]},
        "weight": 1.0,
        "order_num": 6
    },
    {
        "category": "skills",
        "question_text": "How would you rate your skill in Programming / Coding (Python, JavaScript, C++, or scripts)?",
        "question_type": "rating_scale",
        "options": {"skill_name": "Programming", "min": 1, "max": 5, "labels": ["1 - Beginner", "2 - Basic", "3 - Intermediate", "4 - Good", "5 - Excellent"]},
        "weight": 1.0,
        "order_num": 7
    },
    {
        "category": "skills",
        "question_text": "How would you rate your skill in Communication (interpersonal speaking, active listening)?",
        "question_type": "rating_scale",
        "options": {"skill_name": "Communication", "min": 1, "max": 5, "labels": ["1 - Beginner", "2 - Basic", "3 - Intermediate", "4 - Good", "5 - Excellent"]},
        "weight": 1.0,
        "order_num": 8
    },
    {
        "category": "skills",
        "question_text": "How would you rate your skill in Writing (reports, essays, articles, documentation)?",
        "question_type": "rating_scale",
        "options": {"skill_name": "Writing", "min": 1, "max": 5, "labels": ["1 - Beginner", "2 - Basic", "3 - Intermediate", "4 - Good", "5 - Excellent"]},
        "weight": 1.0,
        "order_num": 9
    },
    {
        "category": "skills",
        "question_text": "How would you rate your skill in Creativity (generating novel ideas, visual aesthetics, inventive solutions)?",
        "question_type": "rating_scale",
        "options": {"skill_name": "Creativity", "min": 1, "max": 5, "labels": ["1 - Beginner", "2 - Basic", "3 - Intermediate", "4 - Good", "5 - Excellent"]},
        "weight": 1.0,
        "order_num": 10
    },
    {
        "category": "skills",
        "question_text": "How would you rate your skill in Problem Solving (diagnosing root issues and resolving them)?",
        "question_type": "rating_scale",
        "options": {"skill_name": "Problem Solving", "min": 1, "max": 5, "labels": ["1 - Beginner", "2 - Basic", "3 - Intermediate", "4 - Good", "5 - Excellent"]},
        "weight": 1.0,
        "order_num": 11
    },
    {
        "category": "skills",
        "question_text": "How would you rate your skill in Leadership (motivating peers, guiding initiatives, decision-making)?",
        "question_type": "rating_scale",
        "options": {"skill_name": "Leadership", "min": 1, "max": 5, "labels": ["1 - Beginner", "2 - Basic", "3 - Intermediate", "4 - Good", "5 - Excellent"]},
        "weight": 1.0,
        "order_num": 12
    },
    {
        "category": "skills",
        "question_text": "How would you rate your skill in Teamwork & Collaboration (working constructively in groups)?",
        "question_type": "rating_scale",
        "options": {"skill_name": "Teamwork", "min": 1, "max": 5, "labels": ["1 - Beginner", "2 - Basic", "3 - Intermediate", "4 - Good", "5 - Excellent"]},
        "weight": 1.0,
        "order_num": 13
    },
    {
        "category": "skills",
        "question_text": "How would you rate your skill in Analytical Thinking (breaking complex problems into components)?",
        "question_type": "rating_scale",
        "options": {"skill_name": "Analytical Thinking", "min": 1, "max": 5, "labels": ["1 - Beginner", "2 - Basic", "3 - Intermediate", "4 - Good", "5 - Excellent"]},
        "weight": 1.0,
        "order_num": 14
    },
    {
        "category": "skills",
        "question_text": "How would you rate your skill in Research (finding credible sources, literature analysis, investigating data)?",
        "question_type": "rating_scale",
        "options": {"skill_name": "Research", "min": 1, "max": 5, "labels": ["1 - Beginner", "2 - Basic", "3 - Intermediate", "4 - Good", "5 - Excellent"]},
        "weight": 1.0,
        "order_num": 15
    },
    {
        "category": "skills",
        "question_text": "How would you rate your skill in Time Management (meeting deadlines, organizing priorities)?",
        "question_type": "rating_scale",
        "options": {"skill_name": "Time Management", "min": 1, "max": 5, "labels": ["1 - Beginner", "2 - Basic", "3 - Intermediate", "4 - Good", "5 - Excellent"]},
        "weight": 1.0,
        "order_num": 16
    },
    {
        "category": "skills",
        "question_text": "How would you rate your skill in Presentation (public pitching, slide decks, explaining ideas clearly)?",
        "question_type": "rating_scale",
        "options": {"skill_name": "Presentation", "min": 1, "max": 5, "labels": ["1 - Beginner", "2 - Basic", "3 - Intermediate", "4 - Good", "5 - Excellent"]},
        "weight": 1.0,
        "order_num": 17
    },
    {
        "category": "skills",
        "question_text": "How would you rate your skill in Data Analysis (extracting trends, using tables, charts, or statistics)?",
        "question_type": "rating_scale",
        "options": {"skill_name": "Data Analysis", "min": 1, "max": 5, "labels": ["1 - Beginner", "2 - Basic", "3 - Intermediate", "4 - Good", "5 - Excellent"]},
        "weight": 1.0,
        "order_num": 18
    },
    {
        "category": "skills",
        "question_text": "How would you rate your skill in Design (visual layout, aesthetics, typography, UI/UX, or graphic design)?",
        "question_type": "rating_scale",
        "options": {"skill_name": "Design", "min": 1, "max": 5, "labels": ["1 - Beginner", "2 - Basic", "3 - Intermediate", "4 - Good", "5 - Excellent"]},
        "weight": 1.0,
        "order_num": 19
    },

    # --- Category C: Personality / Work Preferences (Q20 - Q24) ---
    {
        "category": "personality",
        "question_text": "When solving an unfamiliar and difficult problem, what approach do you naturally prefer?",
        "question_type": "single_choice",
        "options": [
            "Analyze it step by step",
            "Discuss it with others",
            "Try creative solutions",
            "Research before deciding"
        ],
        "weight": 1.1,
        "order_num": 20
    },
    {
        "category": "personality",
        "question_text": "Which work environment sounds most engaging and motivating to you?",
        "question_type": "single_choice",
        "options": [
            "Working independently",
            "Working in a team",
            "Leading a team",
            "Working with customers",
            "Working in a laboratory",
            "Working remotely",
            "Working in a creative environment"
        ],
        "weight": 1.1,
        "order_num": 21
    },
    {
        "category": "personality",
        "question_text": "Which statement describes your personal drive best?",
        "question_type": "single_choice",
        "options": [
            "I enjoy analyzing information",
            "I enjoy creating things",
            "I enjoy helping people",
            "I enjoy leading others",
            "I enjoy discovering new ideas",
            "I enjoy organizing things"
        ],
        "weight": 1.1,
        "order_num": 22
    },
    {
        "category": "personality",
        "question_text": "How comfortable are you with learning new software, tools, and technical systems quickly?",
        "question_type": "rating_scale",
        "options": {"min": 1, "max": 5, "labels": ["1 - Uncomfortable", "2 - Slow learner", "3 - Moderate", "4 - Very comfortable", "5 - Extremely comfortable"]},
        "weight": 1.0,
        "order_num": 23
    },
    {
        "category": "personality",
        "question_text": "How comfortable are you with public speaking, addressing audiences, or client presentations?",
        "question_type": "rating_scale",
        "options": {"min": 1, "max": 5, "labels": ["1 - Very anxious", "2 - Somewhat hesitant", "3 - Neutral", "4 - Confident", "5 - Highly enthusiastic"]},
        "weight": 1.0,
        "order_num": 24
    },

    # --- Category D: Academic Profile (Q25 - Q26) ---
    {
        "category": "academic",
        "question_text": "In which academic areas do you consistently achieve your strongest performance or comprehension?",
        "question_type": "multi_choice",
        "options": [
            "Mathematics & Quantitative Aptitude",
            "Physical Sciences (Physics, Chemistry)",
            "Biological & Life Sciences",
            "Computer Science & Information Tech",
            "Commerce, Accounts & Finance",
            "Economics & Business Studies",
            "Languages, Literature & Writing",
            "Social Sciences, Law & Humanities",
            "Visual Arts, Media & Design"
        ],
        "weight": 1.0,
        "order_num": 25
    },
    {
        "category": "academic",
        "question_text": "What is your approximate overall academic performance level (Percentage or CGPA bracket)?",
        "question_type": "single_choice",
        "options": [
            "Distinction / Top Tier (85% - 100% / CGPA 8.5+)",
            "First Class (70% - 84% / CGPA 7.0 - 8.4)",
            "Second Class (55% - 69% / CGPA 5.5 - 6.9)",
            "Passing Grade (40% - 54% / CGPA 4.0 - 5.4)",
            "Prefer not to disclose / Non-traditional path"
        ],
        "weight": 0.8,
        "order_num": 26
    },

    # --- Category E: Career Goals (Q27 - Q30) ---
    {
        "category": "goals",
        "question_text": "What is your primary long-term career ambition?",
        "question_type": "single_choice",
        "options": [
            "High technical expertise",
            "Leadership/management",
            "Creativity",
            "Research",
            "Entrepreneurship",
            "Social impact",
            "Financial growth",
            "Stable professional career",
            "Still exploring"
        ],
        "weight": 1.2,
        "order_num": 27
    },
    {
        "category": "goals",
        "question_text": "Which industry or domain sector attracts you the most?",
        "question_type": "single_choice",
        "options": [
            "Technology",
            "Healthcare",
            "Business",
            "Finance",
            "Education",
            "Government/Public Services",
            "Design/Media",
            "Research",
            "Environment",
            "Other"
        ],
        "weight": 1.2,
        "order_num": 28
    },
    {
        "category": "goals",
        "question_text": "How important is flexible work arrangement (remote work, autonomous hours) to you?",
        "question_type": "rating_scale",
        "options": {"min": 1, "max": 5, "labels": ["1 - Not important", "2 - Slightly important", "3 - Moderate", "4 - Very important", "5 - Crucial"]},
        "weight": 0.8,
        "order_num": 29
    },
    {
        "category": "goals",
        "question_text": "How interested are you in founding your own venture, startup, or freelance practice?",
        "question_type": "rating_scale",
        "options": {"min": 1, "max": 5, "labels": ["1 - Not interested", "2 - Mild curiosity", "3 - Open to it", "4 - Very interested", "5 - Passionate entrepreneur"]},
        "weight": 1.0,
        "order_num": 30
    }
]
