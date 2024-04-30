import sys
import json  # Import the json module

# Parse the JSON string received from sys.argv[1]
data = json.loads(sys.argv[1])

# Access the "channel" property from the parsed JSON object
print("Welcome to", data["channel"])
