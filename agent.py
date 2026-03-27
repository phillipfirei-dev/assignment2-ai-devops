import re

def plan():
    print("🧠 Planning: Identify failure type from CI logs\n")

def tool(log):
    print("🔧 Tool: Analysing logs...\n")

    patterns = {
        "Build Failure": "BUILD FAILURE",
        "Test Failure": "Failures",
        "Dependency Error": "Could not resolve"
    }

    for key, value in patterns.items():
        if value in log:
            return key

    return "Unknown Error"

def reflect(result):
    print("🔍 Self-reflection:\n")

    if result == "Unknown Error":
        return "Low confidence"
    return "High confidence"

def run_agent(log):
    plan()
    result = tool(log)
    confidence = reflect(result)

    print("✅ Final Output:")
    print(f"Failure: {result}")
    print(f"Confidence: {confidence}")

# Test log
log = "[ERROR] BUILD FAILURE"
run_agent(log)
