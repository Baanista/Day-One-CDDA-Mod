import json

def adjust_group_weights(input_file, output_file, group_name, multiplier):
    """
    Adjusts the weight of a specific group in a JSON configuration file.

    :param input_file: Path to the input JSON file.
    :param output_file: Path to the output JSON file with adjusted weights.
    :param group_name: The group name to adjust weights for.
    :param multiplier: The multiplier (or divisor) to apply to the weights.
    """
    with open(input_file, 'r') as f:
        data = json.load(f)

    for entry in data:
        if entry.get("type") == "monstergroup":
            for monster in entry.get("monsters", []):
                if monster.get("group") == group_name:
                    original_weight = monster["weight"]
                    monster["weight"] = max(1, int(original_weight * multiplier))  # Ensure weight is at least 1

    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)

# Example usage
# Adjust weights for GROUP_CIVILIANS_STANDARD by multiplying them by 2
input_file = "monster_groups.json"  # Replace with your input file
output_file = "monster_groups.json"  # Replace with your desired output file
adjust_group_weights(input_file, output_file, "GROUP_CIVILIANS_STANDARD", 8)
