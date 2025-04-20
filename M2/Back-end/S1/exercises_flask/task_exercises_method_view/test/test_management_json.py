import pytest
from scripts.management_json import import_json, export_json


def test_import_50_tasks_return_list_of_dictionaries():
    # Arrage
    task_list_expected=[
  {
    "id": 1001,
    "title": "Math Assignment",
    "description": "Solve quadratic equations and graph the results factor proper noun liquid sunshine",
    "state": "in progress"
  },
  {
    "id": 1002,
    "title": "Science Project",
    "description": "Research photosynthesis and present findings broken glass mountain river",
    "state": "ready"
  },
  {
    "id": 1003,
    "title": "History Essay",
    "description": "Write about the Industrial Revolution silver moon hidden treasure",
    "state": "in progress"
  },
  {
    "id": 1004,
    "title": "Programming Task",
    "description": "Build a Python script to analyze data lost city ancient code",
    "state": "pending"
  },
  {
    "id": 1005,
    "title": "Art Presentation",
    "description": "Create a slideshow on Renaissance art floating island digital dream",
    "state": "ready"
  },
  {
    "id": 1006,
    "title": "Physics Homework",
    "description": "Calculate velocity and acceleration silent star midnight theory",
    "state": "in progress"
  },
  {
    "id": 1007,
    "title": "Biology Lab Report",
    "description": "Document the microscope observations frozen light empty space",
    "state": "pending"
  },
  {
    "id": 1008,
    "title": "Geography Quiz Prep",
    "description": "Study European capitals and landmarks invisible bridge rising sun",
    "state": "ready"
  },
  {
    "id": 1009,
    "title": "Literature Analysis",
    "description": "Compare two Shakespeare plays lonely road forgotten words",
    "state": "in progress"
  },
  {
    "id": 1010,
    "title": "Chemistry Experiment",
    "description": "Mix compounds and record reactions electric storm quiet shadow",
    "state": "pending"
  },
  {
    "id": 1011,
    "title": "Music Composition",
    "description": "Write a short melody using piano chords golden leaf echo chamber",
    "state": "ready"
  },
  {
    "id": 1012,
    "title": "Economics Research",
    "description": "Analyze supply and demand curves in local markets hidden path crystal ball",
    "state": "in progress"
  },
  {
    "id": 1013,
    "title": "Psychology Paper",
    "description": "Discuss cognitive biases in decision-making silent ocean burning flame",
    "state": "pending"
  },
  {
    "id": 1014,
    "title": "Physical Education Log",
    "description": "Track weekly exercise routines and progress broken mirror infinite loop",
    "state": "ready"
  },
  {
    "id": 1015,
    "title": "Spanish Homework",
    "description": "Conjugate irregular verbs in past tense dark forest whispering wind",
    "state": "in progress"
  },
  {
    "id": 1016,
    "title": "Computer Science Lab",
    "description": "Implement a binary search algorithm in Java frozen river digital ghost",
    "state": "pending"
  },
  {
    "id": 1017,
    "title": "Philosophy Essay",
    "description": "Debate the ethics of artificial intelligence hollow mountain bright star",
    "state": "ready"
  },
  {
    "id": 1018,
    "title": "Algebra Problems",
    "description": "Solve linear equations with two variables lost key phantom sound",
    "state": "in progress"
  },
  {
    "id": 1019,
    "title": "Geology Report",
    "description": "Describe the rock cycle and give examples ancient book floating island",
    "state": "pending"
  },
  {
    "id": 1020,
    "title": "Creative Writing",
    "description": "Write a short story set in a dystopian future silent scream hollow echo",
    "state": "ready"
  },
  {
    "id": 1021,
    "title": "Statistics Homework",
    "description": "Calculate mean, median, and mode for given data sets silver shadow broken clock",
    "state": "in progress"
  },
  {
    "id": 1022,
    "title": "Environmental Science",
    "description": "Discuss the impact of plastic pollution on oceans dark sky frozen time",
    "state": "pending"
  },
  {
    "id": 1023,
    "title": "French Vocabulary",
    "description": "Learn 20 new words related to food and dining lost letter hidden door",
    "state": "ready"
  },
  {
    "id": 1024,
    "title": "Trigonometry Practice",
    "description": "Solve problems using sine and cosine functions invisible chain rising mist",
    "state": "in progress"
  },
  {
    "id": 1025,
    "title": "Sociology Study",
    "description": "Analyze a social movement from the 20th century quiet storm electric pulse",
    "state": "pending"
  },
  {
    "id": 1026,
    "title": "Health and Nutrition",
    "description": "Plan a balanced meal for a week golden sun forgotten relic",
    "state": "ready"
  },
  {
    "id": 1027,
    "title": "Calculus Problems",
    "description": "Find derivatives of polynomial functions broken wheel silent night",
    "state": "in progress"
  },
  {
    "id": 1028,
    "title": "Political Science",
    "description": "Compare different forms of government hollow voice digital rain",
    "state": "pending"
  },
  {
    "id": 1029,
    "title": "Business Plan",
    "description": "Draft a proposal for a startup idea frozen echo ancient tree",
    "state": "ready"
  },
  {
    "id": 1030,
    "title": "Geometry Assignment",
    "description": "Calculate the area and perimeter of complex shapes lost shadow bright light",
    "state": "in progress"
  },
  {
    "id": 1031,
    "title": "Astronomy Project",
    "description": "Research black holes and their properties silent wind hollow shell",
    "state": "pending"
  },
  {
    "id": 1032,
    "title": "English Grammar",
    "description": "Identify and correct errors in given sentences dark moon phantom step",
    "state": "ready"
  },
  {
    "id": 1033,
    "title": "Marketing Analysis",
    "description": "Evaluate a recent advertising campaign golden key frozen fire",
    "state": "in progress"
  },
  {
    "id": 1034,
    "title": "Robotics Lab",
    "description": "Program a simple robot to navigate a maze broken mirror silent whisper",
    "state": "pending"
  },
  {
    "id": 1035,
    "title": "Linguistics Study",
    "description": "Compare syntax structures in two languages lost city digital wave",
    "state": "ready"
  },
  {
    "id": 1036,
    "title": "Probability Homework",
    "description": "Solve problems involving dice and card draws hidden path bright star",
    "state": "in progress"
  },
  {
    "id": 1037,
    "title": "Film Analysis",
    "description": "Write a review of a classic movie silent river hollow echo",
    "state": "pending"
  },
  {
    "id": 1038,
    "title": "Engineering Task",
    "description": "Design a simple bridge model using CAD software frozen light ancient code",
    "state": "ready"
  },
  {
    "id": 1039,
    "title": "Drama Script",
    "description": "Write a short play with three characters lost key phantom sound",
    "state": "in progress"
  },
  {
    "id": 1040,
    "title": "Data Structures",
    "description": "Implement a linked list in C++ dark forest whispering wind",
    "state": "pending"
  },
  {
    "id": 1041,
    "title": "Ethics Debate",
    "description": "Discuss the morality of genetic modification silent scream hollow echo",
    "state": "ready"
  },
  {
    "id": 1042,
    "title": "World History",
    "description": "Summarize the causes of World War I silver shadow broken clock",
    "state": "in progress"
  },
  {
    "id": 1043,
    "title": "Neuroscience Study",
    "description": "Explain how neurons transmit signals dark sky frozen time",
    "state": "pending"
  },
  {
    "id": 1044,
    "title": "Poetry Writing",
    "description": "Compose a sonnet about nature lost letter hidden door",
    "state": "ready"
  },
  {
    "id": 1045,
    "title": "Database Design",
    "description": "Create an ER diagram for a library system invisible chain rising mist",
    "state": "in progress"
  },
  {
    "id": 1046,
    "title": "Artificial Intelligence",
    "description": "Train a simple ML model on a dataset quiet storm electric pulse",
    "state": "pending"
  },
  {
    "id": 1047,
    "title": "Public Speaking",
    "description": "Prepare a 5-minute speech on a current event golden sun forgotten relic",
    "state": "ready"
  },
  {
    "id": 1048,
    "title": "Human Anatomy",
    "description": "Label the major bones in the human body broken wheel silent night",
    "state": "in progress"
  },
  {
    "id": 1049,
    "title": "Web Development",
    "description": "Build a responsive homepage using HTML/CSS hollow voice digital rain",
    "state": "pending"
  },
  {
    "id": 1050,
    "title": "Logic Puzzles",
    "description": "Solve 10 classic logic problems frozen echo ancient tree",
    "state": "ready"
  }
]
    # Act
    result = import_json(path="test/50_tasks.json")
    # Assert
    assert result == task_list_expected


def test_export_50_tasks_return_string_of_done():   
    # Arrage
    new_task = {
    "id": 1051,
    "title": "Interior Design",
    "description": "Plan the layout for a small apartment dark sky frozen time",
    "state": "pending"
  }
    task_list_expected=[
  {
    "id": 1001,
    "title": "Math Assignment",
    "description": "Solve quadratic equations and graph the results factor proper noun liquid sunshine",
    "state": "in progress"
  },
  {
    "id": 1002,
    "title": "Science Project",
    "description": "Research photosynthesis and present findings broken glass mountain river",
    "state": "ready"
  },
  {
    "id": 1003,
    "title": "History Essay",
    "description": "Write about the Industrial Revolution silver moon hidden treasure",
    "state": "in progress"
  },
  {
    "id": 1004,
    "title": "Programming Task",
    "description": "Build a Python script to analyze data lost city ancient code",
    "state": "pending"
  },
  {
    "id": 1005,
    "title": "Art Presentation",
    "description": "Create a slideshow on Renaissance art floating island digital dream",
    "state": "ready"
  },
  {
    "id": 1006,
    "title": "Physics Homework",
    "description": "Calculate velocity and acceleration silent star midnight theory",
    "state": "in progress"
  },
  {
    "id": 1007,
    "title": "Biology Lab Report",
    "description": "Document the microscope observations frozen light empty space",
    "state": "pending"
  },
  {
    "id": 1008,
    "title": "Geography Quiz Prep",
    "description": "Study European capitals and landmarks invisible bridge rising sun",
    "state": "ready"
  },
  {
    "id": 1009,
    "title": "Literature Analysis",
    "description": "Compare two Shakespeare plays lonely road forgotten words",
    "state": "in progress"
  },
  {
    "id": 1010,
    "title": "Chemistry Experiment",
    "description": "Mix compounds and record reactions electric storm quiet shadow",
    "state": "pending"
  },
  {
    "id": 1011,
    "title": "Music Composition",
    "description": "Write a short melody using piano chords golden leaf echo chamber",
    "state": "ready"
  },
  {
    "id": 1012,
    "title": "Economics Research",
    "description": "Analyze supply and demand curves in local markets hidden path crystal ball",
    "state": "in progress"
  },
  {
    "id": 1013,
    "title": "Psychology Paper",
    "description": "Discuss cognitive biases in decision-making silent ocean burning flame",
    "state": "pending"
  },
  {
    "id": 1014,
    "title": "Physical Education Log",
    "description": "Track weekly exercise routines and progress broken mirror infinite loop",
    "state": "ready"
  },
  {
    "id": 1015,
    "title": "Spanish Homework",
    "description": "Conjugate irregular verbs in past tense dark forest whispering wind",
    "state": "in progress"
  },
  {
    "id": 1016,
    "title": "Computer Science Lab",
    "description": "Implement a binary search algorithm in Java frozen river digital ghost",
    "state": "pending"
  },
  {
    "id": 1017,
    "title": "Philosophy Essay",
    "description": "Debate the ethics of artificial intelligence hollow mountain bright star",
    "state": "ready"
  },
  {
    "id": 1018,
    "title": "Algebra Problems",
    "description": "Solve linear equations with two variables lost key phantom sound",
    "state": "in progress"
  },
  {
    "id": 1019,
    "title": "Geology Report",
    "description": "Describe the rock cycle and give examples ancient book floating island",
    "state": "pending"
  },
  {
    "id": 1020,
    "title": "Creative Writing",
    "description": "Write a short story set in a dystopian future silent scream hollow echo",
    "state": "ready"
  },
  {
    "id": 1021,
    "title": "Statistics Homework",
    "description": "Calculate mean, median, and mode for given data sets silver shadow broken clock",
    "state": "in progress"
  },
  {
    "id": 1022,
    "title": "Environmental Science",
    "description": "Discuss the impact of plastic pollution on oceans dark sky frozen time",
    "state": "pending"
  },
  {
    "id": 1023,
    "title": "French Vocabulary",
    "description": "Learn 20 new words related to food and dining lost letter hidden door",
    "state": "ready"
  },
  {
    "id": 1024,
    "title": "Trigonometry Practice",
    "description": "Solve problems using sine and cosine functions invisible chain rising mist",
    "state": "in progress"
  },
  {
    "id": 1025,
    "title": "Sociology Study",
    "description": "Analyze a social movement from the 20th century quiet storm electric pulse",
    "state": "pending"
  },
  {
    "id": 1026,
    "title": "Health and Nutrition",
    "description": "Plan a balanced meal for a week golden sun forgotten relic",
    "state": "ready"
  },
  {
    "id": 1027,
    "title": "Calculus Problems",
    "description": "Find derivatives of polynomial functions broken wheel silent night",
    "state": "in progress"
  },
  {
    "id": 1028,
    "title": "Political Science",
    "description": "Compare different forms of government hollow voice digital rain",
    "state": "pending"
  },
  {
    "id": 1029,
    "title": "Business Plan",
    "description": "Draft a proposal for a startup idea frozen echo ancient tree",
    "state": "ready"
  },
  {
    "id": 1030,
    "title": "Geometry Assignment",
    "description": "Calculate the area and perimeter of complex shapes lost shadow bright light",
    "state": "in progress"
  },
  {
    "id": 1031,
    "title": "Astronomy Project",
    "description": "Research black holes and their properties silent wind hollow shell",
    "state": "pending"
  },
  {
    "id": 1032,
    "title": "English Grammar",
    "description": "Identify and correct errors in given sentences dark moon phantom step",
    "state": "ready"
  },
  {
    "id": 1033,
    "title": "Marketing Analysis",
    "description": "Evaluate a recent advertising campaign golden key frozen fire",
    "state": "in progress"
  },
  {
    "id": 1034,
    "title": "Robotics Lab",
    "description": "Program a simple robot to navigate a maze broken mirror silent whisper",
    "state": "pending"
  },
  {
    "id": 1035,
    "title": "Linguistics Study",
    "description": "Compare syntax structures in two languages lost city digital wave",
    "state": "ready"
  },
  {
    "id": 1036,
    "title": "Probability Homework",
    "description": "Solve problems involving dice and card draws hidden path bright star",
    "state": "in progress"
  },
  {
    "id": 1037,
    "title": "Film Analysis",
    "description": "Write a review of a classic movie silent river hollow echo",
    "state": "pending"
  },
  {
    "id": 1038,
    "title": "Engineering Task",
    "description": "Design a simple bridge model using CAD software frozen light ancient code",
    "state": "ready"
  },
  {
    "id": 1039,
    "title": "Drama Script",
    "description": "Write a short play with three characters lost key phantom sound",
    "state": "in progress"
  },
  {
    "id": 1040,
    "title": "Data Structures",
    "description": "Implement a linked list in C++ dark forest whispering wind",
    "state": "pending"
  },
  {
    "id": 1041,
    "title": "Ethics Debate",
    "description": "Discuss the morality of genetic modification silent scream hollow echo",
    "state": "ready"
  },
  {
    "id": 1042,
    "title": "World History",
    "description": "Summarize the causes of World War I silver shadow broken clock",
    "state": "in progress"
  },
  {
    "id": 1043,
    "title": "Neuroscience Study",
    "description": "Explain how neurons transmit signals dark sky frozen time",
    "state": "pending"
  },
  {
    "id": 1044,
    "title": "Poetry Writing",
    "description": "Compose a sonnet about nature lost letter hidden door",
    "state": "ready"
  },
  {
    "id": 1045,
    "title": "Database Design",
    "description": "Create an ER diagram for a library system invisible chain rising mist",
    "state": "in progress"
  },
  {
    "id": 1046,
    "title": "Artificial Intelligence",
    "description": "Train a simple ML model on a dataset quiet storm electric pulse",
    "state": "pending"
  },
  {
    "id": 1047,
    "title": "Public Speaking",
    "description": "Prepare a 5-minute speech on a current event golden sun forgotten relic",
    "state": "ready"
  },
  {
    "id": 1048,
    "title": "Human Anatomy",
    "description": "Label the major bones in the human body broken wheel silent night",
    "state": "in progress"
  },
  {
    "id": 1049,
    "title": "Web Development",
    "description": "Build a responsive homepage using HTML/CSS hollow voice digital rain",
    "state": "pending"
  },
  {
    "id": 1050,
    "title": "Logic Puzzles",
    "description": "Solve 10 classic logic problems frozen echo ancient tree",
    "state": "ready"
  },
  {
    "id": 1051,
    "title": "Interior Design",
    "description": "Plan the layout for a small apartment dark sky frozen time",
    "state": "pending"
  }
]
    # Act
    export_json(path_export="test/50_tasks_export.json",path_import="test/50_tasks.json" ,new_task_list=new_task)
    # Assert
    result = import_json("test/50_tasks_export.json")
    print()
    assert result  == task_list_expected
