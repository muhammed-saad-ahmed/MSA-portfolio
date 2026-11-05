"""Portfolio content.

Everything shown on the site lives here, so you can edit text without touching layout code.
Rule used throughout: only claims supported by your public repositories or by details you
provided are included. Anything unverified is left empty rather than invented.
"""

NAME = "Muhammad Saad Ahmed"
EMAIL = "msasjvc@gmail.com"
GITHUB = "https://github.com/muhammed-saad-ahmed"
GITHUB_LEGACY = "https://github.com/HafizMuhammedSaad"
FIVERR = "https://www.fiverr.com/users/saad_ahmed369/portfolio"
LINKEDIN = "https://www.linkedin.com/in/muhammed-saad-ahmed/"
LOCATION = "Karachi, Pakistan"
PORTRAIT_FILE = "portrait.jpg"  # place your photo at assets/portrait.jpg

NAV = [
    ("home", "Home"),
    ("about", "About"),
    ("expertise", "Expertise"),
    ("projects", "Projects"),
    ("experience", "Experience"),
    ("education", "Education"),
    ("achievements", "Achievements"),
    ("contact", "Contact"),
]

HERO = {
    "eyebrow": "ENGINEERING • TECHNOLOGY • INNOVATION",
    "subtitle": "Building practical technology. Exploring the future of engineering.",
    "intro": (
        "I'm a technology-focused developer and aspiring aerospace engineer, passionate about "
        "turning complex ideas into practical, accessible solutions across software, AI, "
        "data engineering and applied science."
    ),
    "facts": [
        ("Based in", "Karachi, Pakistan"),
        ("Education", "HSC completed · 2026"),
        ("Aiming for", "Aerospace Engineering"),
    ],
}

ABOUT = {
    "title": "Curious by nature. Disciplined in practice.",
    "paragraphs": [
        "I completed my Higher Secondary Certificate (Pre-Engineering) at Adamjee Government Science College in Karachi, "
        "building a foundation in mathematics and physics while developing software on the side. "
        "My long-term goal is to study Aerospace Engineering.",
        "I learn by building. My public work spans a free Python course for beginners, an "
        "AI-assisted learning application, and an auditable risk-intelligence research "
        "prototype that combines computer vision, satellite data and transparent scoring.",
        "Alongside school, I trained in programming, databases and cloud data engineering "
        "through Saylani Mass IT Training, working with tools such as Python, SQL, AWS and "
        "modern data-pipeline technologies.",
        "My engineering philosophy is simple: be honest about what a system can and cannot do, "
        "make results easy to verify, and keep improving through practical experiments.",
    ],
    "pillars": [
        ("Mathematics & Physics", "The analytical base for engineering."),
        ("Software & Data", "Python-first, with pipelines and visualisation."),
        ("Applied AI", "Computer vision and educational tooling."),
        ("Aerospace", "The direction I'm working towards."),
    ],
}

# level: "practical" = used in published work / hands-on, "training" = learned in training, building experience
SKILLS = [
    ("Programming", [
        ("Python", "practical"), ("SQL", "practical"),
        ("Object-Oriented Programming", "practical"), ("Automation", "practical"),
    ]),
    ("Data Processing", [
        ("Pandas", "practical"), ("NumPy", "practical"), ("Matplotlib", "practical"),
    ]),
    ("Databases", [("SQLite", "practical"), ("MySQL", "practical")]),
    ("Data Engineering", [
        ("ETL / ELT", "training"), ("Data Transformation", "practical"),
        ("Data Pipelines", "training"), ("Data Warehousing", "training"),
    ]),
    ("Cloud & Orchestration", [
        ("AWS", "training"), ("Amazon S3", "training"), ("Snowflake", "training"),
        ("Apache Kafka", "training"), ("Apache Airflow", "training"),
    ]),
    ("Development Tools", [
        ("Git", "practical"), ("GitHub", "practical"),
        ("VS Code", "practical"), ("Streamlit", "practical"),
    ]),
    ("Areas of Interest", [
        ("Artificial Intelligence", "interest"), ("Computer Vision", "interest"),
        ("Cybersecurity Fundamentals", "interest"), ("Aerospace Engineering", "interest"),
    ]),
]

# Featured flagship project (verified against its public README)
KRYPTA = {
    "name": "KRYPTA",
    "full": "Karachi Risk & YOLO-driven Platform for Terrain Analysis",
    "badge": "Research prototype • v2.1",
    "repo": "https://github.com/muhammed-saad-ahmed/krypta",
    "live": "https://krypta.streamlit.app/",
    "summary": (
        "An independent research and engineering prototype exploring whether low-cost, "
        "independent evidence streams can be combined into an auditable picture of "
        "urban infrastructure risk in Karachi."
    ),
    "problem": (
        "Open manholes and waterlogging from blocked drains are documented, recurring hazards "
        "in Karachi. Monitoring them in a way that is low-cost and easy to audit remains an open challenge."
    ),
    "solution": (
        "Three cheap evidence streams, edge computer vision, community reports and "
        "Sentinel-2 satellite verification, are fused by a transparent, hand-checkable "
        "algorithm into a 5×5 likelihood × impact risk matrix."
    ),
    "capabilities": [
        "YOLOv8-nano detection exported to ONNX for CPU inference, with INT8 quantisation tooling",
        "Multilingual community-report analysis (English, Roman Urdu, Urdu) with offline geocoding",
        "Sentinel-2 flood verification using NDWI, MNDWI and NDVI change detection",
        "Evidence fusion with an append-only, hash-chained audit ledger",
        "Monte-Carlo sensitivity analysis and location-privacy protection",
    ],
    "honesty": (
        "Built around a clear principle: distinguish what is known, estimated, measured and "
        "unknown. No trained hazard weights ship with the repository, and demo data is "
        "always labelled synthetic."
    ),
    "tech": ["Python", "Streamlit", "YOLOv8", "ONNX Runtime", "SQLite", "Sentinel-2", "NumPy"],
}

# Other projects. "repo": None -> no public link is shown (add one when published).
PROJECTS = [
    {
        "name": "Tadabbur AI",
        "logo": "tadabbur-logo.webp",
        "tag": "Education • AI",
        "repo": "https://github.com/muhammed-saad-ahmed/Tadabbur-AI",
        "live": "https://tadabbur-ai.streamlit.app/",
        "summary": (
            "An AI-powered learning application that helps students understand why an answer "
            "is correct, not only what it is."
        ),
        "problem": "Students can obtain answers easily but often still struggle with the underlying concept.",
        "solution": "A guided flow of ask, understand, visualise and explore, combining explanations with real graphs.",
        "capabilities": [
            "Accepts text, image and PDF questions",
            "Generates function graphs and data visualisations",
            "Keeps limited recent context for follow-up questions",
            "Designed for efficient use of a limited API allowance",
        ],
        "tech": ["Python", "Streamlit", "Groq API", "Pandas", "NumPy", "Matplotlib"],
        "motif": "graph",
    },
    {
        "name": "Free Python Programming Course",
        "tag": "Open education",
        "repo": "https://github.com/muhammed-saad-ahmed/Free-Python-Programming-Course",
        "summary": (
            "A structured, hands-on Python course made freely available so cost is not a "
            "barrier to learning programming."
        ),
        "problem": "Quality programming courses are often paid, which excludes many motivated beginners.",
        "solution": "A progressive path from fundamentals to NumPy, Pandas and Matplotlib, with exercises and solved problems.",
        "capabilities": [
            "Lessons in Jupyter Notebook format",
            "Datasets for practical exercises",
            "Practice questions with fully solved answers",
            "Ongoing project with lessons added over time",
        ],
        "tech": ["Python", "Jupyter", "NumPy", "Pandas", "Matplotlib"],
        "motif": "code",
    },
    {
        "name": "Mini Data Warehouse",
        "tag": "Data Engineering • Analytics",
        "repo": "https://lnkd.in/eeJrfRkY",
        "live": "https://lnkd.in/eZbTMtdX",
        "summary": (
            "An end-to-end ETL and analytics project that transforms raw sales data, "
            "stores structured records in SQLite, and presents business insights in a Streamlit dashboard."
        ),
        "problem": "Raw CSV files are difficult to analyse consistently without a repeatable cleaning and storage workflow.",
        "solution": "A Python and Pandas workflow cleans the source data, loads it into an SQLite warehouse, and runs SQL analytics.",
        "capabilities": [
            "Cleans and transforms raw CSV datasets",
            "Loads processed records into SQLite",
            "Runs sales, product, category and discount analytics",
            "Presents results through an interactive dashboard",
        ],
        "tech": ["Python", "Pandas", "SQLite", "SQL", "Streamlit"],
        "motif": "graph",
    },
    {
        "name": "Real-Time Weather Data Pipeline",
        "tag": "Data Engineering • APIs",
        "repo": "https://github.com/HafizMuhammedSaad/weather_pipeline",
        "live": "https://lnkd.in/e33pRarg",
        "summary": (
            "An automated weather-data workflow that collects live API data, stores it locally, "
            "and turns historical observations into an interactive analytics dashboard."
        ),
        "problem": "Live weather readings become more useful when they are collected consistently and retained for comparison over time.",
        "solution": "A Python ETL workflow retrieves OpenWeather data, processes it with Pandas, stores it in SQLite, and visualises trends.",
        "capabilities": [
            "Collects live weather data from OpenWeather",
            "Stores observations in a local SQLite database",
            "Highlights city-level temperature patterns and extremes",
            "Supports scheduled execution through GitHub Actions or cron",
        ],
        "tech": ["Python", "OpenWeather API", "Pandas", "SQLite", "Streamlit", "Plotly", "GitHub Actions"],
        "motif": "graph",
    },
    {
        "name": "Weather Forecast Dashboard",
        "tag": "Data Analytics • Dashboard",
        "repo": "https://github.com/HafizMuhammedSaad/weather-forecast-dashboard",
        "live": "https://lnkd.in/eSrbYRm9",
        "summary": (
            "An interactive dashboard for exploring current weather conditions and forecast data, "
            "with local database storage and visual summaries."
        ),
        "problem": "Weather information is easier to interpret when current conditions and trends are presented in one clear interface.",
        "solution": "A Streamlit application combines weather API data, Pandas processing, SQLite storage, and charts.",
        "capabilities": [
            "Retrieves live weather information for selected cities",
            "Stores weather records in SQLite",
            "Displays weather metrics and visual trends",
            "Uses Matplotlib for chart-based exploration",
        ],
        "tech": ["Python", "Streamlit", "OpenWeather API", "Pandas", "SQLite", "Matplotlib"],
        "motif": "graph",
    },
]

# Work described from the details you provided. No public repository yet, so no links are shown.
MORE_WORK = [
    {
        "name": "Cloud Data Engineering Practice",
        "tag": "Training projects",
        "summary": "Hands-on practice from Saylani Mass IT Training with cloud storage, streaming, orchestration and warehouse tooling.",
        "tech": ["AWS S3", "Apache Kafka", "Apache Airflow", "Snowflake", "SQL"],
        "repo": None,
    },
    {
        "name": "Data Cleaning & Saylani Coursework",
        "tag": "Learning repositories",
        "summary": "Additional public repositories documenting data-cleaning exercises, database assignments, and practical work completed during technical training.",
        "tech": ["Python", "Pandas", "SQL", "Jupyter"],
        "links": [
            ("Forked Data Cleaning Case Study", "https://github.com/HafizMuhammedSaad/Case-Study-Data-Cleaning"),
            ("Saylani CDE Batch 1 (fork)", "https://github.com/HafizMuhammedSaad/Saylani-CDE-Batch1"),
            ("Data Engineering Assignment", "https://github.com/HafizMuhammedSaad/D-E-assignment-1"),
            ("Saylani Projects", "https://github.com/HafizMuhammedSaad/projects-by-saylani"),
            ("Python Assignment 2024", "https://github.com/HafizMuhammedSaad/saylani-asssign-1-2024"),
        ],
    },
    {
        "name": "Savoraise",
        "tag": "Prototype concept",
        "summary": "A food-rescue marketplace concept connecting sellers of discounted surplus or near-expiry produce with price-conscious customers. An ongoing prototype, not a launched company.",
        "tech": [],
        "repo": None,
    },
]

EXPERIENCE = [
    {
        "org": "UXGENIE",
        "role": "Python Developer Intern",
        "dates": "22 Sep 2025 – 30 Oct 2025",
        "points": [
            "Worked on Python development tasks in a professional team environment",
            "Strengthened problem-solving, automation, and code-quality practices",
        ],
        "tech": ["Python"],
    },
    {
        "org": "Saylani Mass IT Training",
        "role": "Programming & Cloud Data Engineering Training",
        "dates": "",
        "points": [
            "Programming and database fundamentals",
            "Cloud data engineering with AWS, Snowflake, Kafka and Airflow concepts",
        ],
        "tech": ["Python", "SQL", "AWS", "Snowflake"],
    },
]

EDUCATION = [
    {
        "school": "Adamjee Government Science College",
        "detail": "Higher Secondary Certificate (HSC) — Pre-Engineering · Completed",
        "dates": "2024 – 2026",
        "note": "Karachi, Pakistan · Graduated 2026",
    },
    {
        "school": "Saylani Mass IT Training",
        "detail": "Programming and Cloud Data Engineering",
        "dates": "",
        "note": "Technical training",
    },
    {
        "school": "Hamdard Public School",
        "detail": "Secondary Education",
        "dates": "",
        "note": "Karachi, Pakistan",
    },
]

# Add verified certificates here: {"title": "...", "issuer": "...", "year": "..."}
CERTIFICATIONS = []

ACHIEVEMENTS = [
    ("Free education", "Created and published a free Python programming course for learners."),
    ("Research prototype", "Designed and built KRYPTA, an auditable multi-modal risk-intelligence prototype."),
    ("Technical training", "Trained in programming and cloud data engineering through Saylani Mass IT Training."),
]

BEYOND = [
    ("Taekwondo", "Blue Belt"),
    ("Kukkiwon Poomsae", "Medal"),
    ("Boxing", "Training"),
    ("Swimming", "Sport"),
    ("Football", "Sport"),
    ("Table Tennis", "Sport"),
]

VISION = {
    "headline": "Driven by curiosity. Grounded in engineering. Focused on what comes next.",
    "body": (
        "I want to combine aerospace engineering with software, data and AI: building tools "
        "that help engineers see more clearly, test more carefully and decide with evidence. "
        "That path begins with mathematics, physics and a habit of building real things."
    ),
    "threads": ["Aerospace Engineering", "Artificial Intelligence", "Software Development", "Data Science", "Engineering Research"],
}

PHILOSOPHY = [
    ("Learn", "Start from first principles and stay with a problem until it makes sense."),
    ("Build", "Turn ideas into working software people can run and inspect."),
    ("Experiment", "Test assumptions, measure honestly and record what fails."),
    ("Improve", "Refine the result, document it, and share it for others to use."),
]

CONTACT = {
    "headline": "Let's Build Something Meaningful.",
    "text": (
        "I'm always interested in connecting with engineers, researchers, developers, and "
        "people working on meaningful technological challenges."
    ),
}
