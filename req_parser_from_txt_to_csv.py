import csv
import re

# Open input.txt for reading and output.csv for writing
with open('output.txt', 'r') as input_file, open('output.csv', 'w', newline='') as output_file:
    id_text = None  # Initialize variable to store id
    description = []  # Initialize variable to store description

    # Create a CSV writer object
    writer = csv.writer(output_file)

    # Regular expression pattern to match the ID
    id_pattern = re.compile(r'\[([a-zA-Z])+:\s([a-zA-Z]+_)+\d+\]')

    # Loop through each line in the input file
    for line in input_file:
        # Remove leading and trailing whitespaces
        line = line.strip()

        # Check if the line contains an ID
        if '[' in line and ']' in line:
            # Extract the potential ID using regex
            id_match = id_pattern.match(line)
            if id_match:
                # If it's not the first id, write the previous id and description to CSV file if any
                if id_text is not None:
                    writer.writerow([id_text[1:-1], ' '.join(description), 'accepted', 'CSM / CryptoStack'])

                # Extract and store the new id
                id_text = id_match.group()
                # Reset description for the new id
                description = []

                # Move to the next line
                continue

        # If it's not an ID, add it to the description
        description.append(line)

    # Write the last id and description to the CSV file
    if id_text is not None and description:
        writer.writerow([id_text[1:-1], ' '.join(description), 'accepted', 'CSM / CryptoStack'])

print("Output has been written to output.csv")
