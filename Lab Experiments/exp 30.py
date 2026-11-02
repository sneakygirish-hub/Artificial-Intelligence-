
# Backward Chaining in Python

# Knowledge Base: Facts
facts = {
    "has_fever",
    "has_cough",
    "has_body_pain"
}

# Knowledge Base: Rules
rules = {
    "flu": ["has_fever", "has_cough", "has_body_pain"],
    "viral_infection": ["has_fever", "has_cough"],
    "needs_rest": ["flu"]
}

# Backward Chaining Function
def backward_chaining(goal):
    print("Checking goal:", goal)

    # Check whether the goal is already a fact
    if goal in facts:
        print(goal, "is a known fact.")
        return True

    # Check applicable rules
    if goal in rules:
        print("Applying rule for:", goal)

        # Verify all conditions of the rule
        for condition in rules[goal]:
            if not backward_chaining(condition):
                print("Goal", goal, "cannot be proved.")
                return False

        print("Goal", goal, "is proved.")
        return True

    print(goal, "is not found in the knowledge base.")
    return False


# Required Queries
print("\n--- Backward Chaining Queries ---")

query1 = "flu"
print("\nQuery 1: Is the patient suffering from flu?")
print("Result:", backward_chaining(query1))

query2 = "viral_infection"
print("\nQuery 2: Does the patient have a viral infection?")
print("Result:", backward_chaining(query2))

query3 = "needs_rest"
print("\nQuery 3: Does the patient need rest?")
print("Result:", backward_chaining(query3))

query4 = "malaria"
print("\nQuery 4: Does the patient have malaria?")
print("Result:", backward_chaining(query4))
