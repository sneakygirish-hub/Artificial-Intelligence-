
# Backward Chaining Program in Python

# Facts
facts = {
    "parent(john, mary)",
    "parent(mary, alice)",
    "parent(john, peter)",
    "male(john)",
    "female(mary)",
    "female(alice)"
}

# Rules: (Conclusion, Conditions)
rules = [
    ("grandparent(X, Z)", ["parent(X, Y)", "parent(Y, Z)"]),
    ("mother(X, Y)", ["parent(X, Y)", "female(X)"]),
    ("father(X, Y)", ["parent(X, Y)", "male(X)"])
]


def substitute(expression, substitutions):
    for variable, value in substitutions.items():
        expression = expression.replace(variable, value)
    return expression


def match(pattern, goal):
    p = pattern.replace(" ", "")
    g = goal.replace(" ", "")

    if "(" not in p or "(" not in g:
        return {} if p == g else None

    pred1, args1 = p.split("(", 1)
    pred2, args2 = g.split("(", 1)

    if pred1 != pred2:
        return None

    args1 = args1.rstrip(")").split(",")
    args2 = args2.rstrip(")").split(",")

    if len(args1) != len(args2):
        return None

    substitutions = {}

    for a, b in zip(args1, args2):
        if a[0].isupper():
            substitutions[a] = b
        elif a != b:
            return None

    return substitutions


def backward_chaining(goal, depth=0):
    indent = "  " * depth
    print(indent + "Checking:", goal)

    # Check facts
    for fact in facts:
        if match(fact, goal) is not None:
            print(indent + "Fact found:", fact)
            return True

    # Check rules
    for conclusion, conditions in rules:
        substitutions = match(conclusion, goal)

        if substitutions is not None:
            print(indent + "Applying rule:", conclusion)

            result = True

            for condition in conditions:
                new_goal = substitute(condition, substitutions)

                if not backward_chaining(new_goal, depth + 1):
                    result = False
                    break

            if result:
                return True

    print(indent + "Goal not proved:", goal)
    return False


# Required Queries
queries = [
    "parent(john, mary)",
    "grandparent(john, alice)",
    "mother(mary, alice)",
    "father(john, peter)",
    "grandparent(mary, peter)"
]

print("BACKWARD CHAINING RESULTS\n")

for query in queries:
    print("\nQuery:", query)

    if backward_chaining(query):
        print("Result: TRUE")
    else:
        print("Result: FALSE")

    print("-" * 40)
