SCENARIOS = [
    {
        "name": "Simple Appointment Booking",
        "description": "Patient wants to book a basic appointment",
        "initial_message": "Hi, I'd like to schedule an appointment",
        "scenario_type": "appointment"
    },
    {
        "name": "Medication Refill",
        "description": "Patient needs a medication refill",
        "initial_message": "I need a refill for my prescription",
        "scenario_type": "refill"
    },
    {
        "name": "Rescheduling Appointment",
        "description": "Patient wants to change appointment time",
        "initial_message": "Can I reschedule my appointment to a different time?",
        "scenario_type": "reschedule"
    },
    {
        "name": "Canceling Appointment",
        "description": "Patient wants to cancel",
        "initial_message": "I need to cancel my appointment",
        "scenario_type": "cancel"
    },
    {
        "name": "Office Hours Question",
        "description": "Patient asks about office hours",
        "initial_message": "What are your office hours?",
        "scenario_type": "info"
    },
    {
        "name": "Location Question",
        "description": "Patient asks about location",
        "initial_message": "What's your address?",
        "scenario_type": "info"
    },
    {
        "name": "Insurance Question",
        "description": "Patient asks about insurance",
        "initial_message": "Do you accept my insurance?",
        "scenario_type": "info"
    },
    {
        "name": "Weekend Appointment Edge Case",
        "description": "Test if agent rejects Sunday appointments",
        "initial_message": "Can I book an appointment for Sunday at 10am?",
        "scenario_type": "edge_case"
    },
    {
        "name": "Unclear Request",
        "description": "Patient makes unclear/confusing request",
        "initial_message": "Um, I'm not sure... I think I need something but I'm not sure what",
        "scenario_type": "edge_case"
    },
    {
        "name": "Late Night Appointment",
        "description": "Patient asks for after-hours appointment",
        "initial_message": "Can I come in at 11pm tonight?",
        "scenario_type": "edge_case"
    },
    {
        "name": "Multiple Issues",
        "description": "Patient has multiple concerns in one call",
        "initial_message": "Hi, I need to reschedule my appointment and also request a medication refill",
        "scenario_type": "complex"
    },
    {
        "name": "Interruption Test",
        "description": "Test how agent handles being interrupted",
        "initial_message": "Sorry, can you repeat that?",
        "scenario_type": "edge_case"
    }
]