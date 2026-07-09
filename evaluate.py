import json
import agent as ag

with open("eval_questions.json", "r") as f:
    test_cases = json.load(f)

correct = 0

for case in test_cases:
    decision = ag.agent_controller(case["query"])
    predicted = decision["action"]

    if predicted == case["expected_action"]:
        correct +=1
    
    print(f"Q: {case['query']}")
    print(f"Expected: {case["expected_action"]} | Predicted: {predicted}")
    print("-" * 40)

accuracy = correct / len(test_cases)
print(f"router accuracy: {accuracy:.2%}")