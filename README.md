# Companion app

## Structure
main.main is the entry point.
`python3 main.py`

It creates the MainWindow class. This creates the navbar widget and the central widget.

## Repo structure
├── main.py
├── main_window.py
├── requirements.txt
├── setup.sh
├── modules/
│   ├── home_module.py
│   └── ...
├── data
│   ├── data.db
│   └── themes.py
│   └── app_state.py

## Adding Modules
Create a new file with modules/<name>_module.py as the entry point for the new module.
If the module needs multiple files create a folder for it (modules/<name>/). Create an __init__.py file.
Import the class in main_window.py (e.g. "from modules.home_module import HomeModule") and add it to modules_config with the name (will be shown in the navbar) and the class (e.g. HomeModule).


# Old Readme

## Apps
- todo list -> version 0.0.1
- language app -> not implemented
- skill tracker -> not implemented
- finance tracker -> not implemented
- weekly calendar -> version 0.0.1, partially implemented
- time tracking -> not implemented
- connect to aws db -> version 0.0.1, needs more flexibility

- reflection/diary (morning, evening)
- food tracker
- events

### Todo List
Implemented
- Frontend
- add tasks
- delete tasks
- update tasks
Not implemented
- proper ordering
- tabs for urgency, etc.
- severity rises over time

### Language App
Not implemented
- vocabulary
- grammar
- sentences
- english
- spanish
- french
- A1, A2, B1, etc.


### Skill Tracker
Big Topics
- AWS
- docker
- python
- databases
Related Topics
- python testing
- aws lambdas
Jobs
- Data Engineering
- Software Development
- DevOps
- Database Administration
- Site Reliablity Engineer
Not Implemented
- scrape linkedin, etc. for job offers
- extract title and skills
- overview page of jobs and skills combined
- courses overview and progress
- available courses connected to skills

### Finance Tracker
Not implemented
- recurring income
- fixed costs (e.g. rent, etc.)
- expenses by category
Categories
- housing (fixed + renovation, etc.)
- food
- luxury (e.g. perfumes)
- tonya

### Weekly Tracker
Implemented
- Frontend
Not implemented
- weekly occuring events
- special events

### Time Tracker
Not implemented
- track what I spend time on
- habit tracking (e.g. once a week gym)
- track bad habits
- track possible available time
- ideal week tab
- link task to skills (e.g. udemy course on topic x)
- when was the last time... ?
    - tried something new
    - went to the office
- % of goals accomplished
- items on todo
    - longest overdue
Possible habits
- reading x minutes per day
- exercise x times per week
    - gym
    - home workout
    - yoga
    - stretching
- change bedding x times per month
- x times per year at the dentist
- morning routine
- night routine
- skincare routine
- meditation
- mood, energy level
- seeing friends/family
- shower
- cook
- wakeup time
- creative outlet
- 15min cleaning (hot-spot cleaning)
    - clean kitchen
        - do the dishes
        - clean fridge
        - sweep the floor
        - throw away glass
        - throw away paper
    - clean bathroom
    - clean living room
- tidy up
- shave

### Connect to AWS
Implemented
- Frontend
- easy landing zone
- open ssh for aurora dev5
- monitor connection
Not implemented
- easy dedev

### Reflection/ Diary
Not Implemented
- daily mood selection
- daily habit selection
- short text about the day
- grateful for
- what accomplished today

### Food Tracker
Not Implemented
- food consumption
- favorite food
- regular food
- food ideas

### Events
Not Implemented
- upcoming events
- life events (e.g. Cuba)
- recent events (e.g. ADHD Meetup)

## Overall areas
- Personal development
    - Art
    - Music
    - Languages
    - Reading
    - Reflection
    - Social events
- Career
    - work routine (stay focused)
    - courses (e.g. Udemy)
    - projects
    - certificates
- Health
    - Gym
    - Food

## DB tables
### todos
### languages
### Skills
id INTEGER
name TEXT
category TEXT -- e.g. tech, languages
topic TEXT -- e.g. aws, postgres
tag TEXT -- many to many relationship
level INTEGER -- 0=no knowledge, 1=beginner, 2=intermediate, 3=advanced, 4=pro
related TEXT -- related topics, many to many relationship

# Next steps
- create standalone app
    - pyinstaller
    - py2app
