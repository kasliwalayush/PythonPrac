import json

# Function to extract key-value pairs from nested JSON structures
def flatten_json(data, parent_key='', sep='_'):
    items = {}
    for k, v in data.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_json(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items

# Function to compare two JSON files and generate HTML report
def generate_html_report(file1, file2, output_file):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

        # Extract key-value pairs from potentially nested JSON structures
        flattened_data1 = flatten_json(data1)
        flattened_data2 = flatten_json(data2)

        # Remove the initial "data_" and "data_cuData_" prefixes from the keys
        flattened_data1 = {key.replace('data_', '').replace('data_cuData_', ''): value for key, value in flattened_data1.items()}
        flattened_data2 = {key.replace('data_', '').replace('data_cuData_', ''): value for key, value in flattened_data2.items()}

        # Combine keys from both files to get a complete set of keys
        all_keys = set(list(flattened_data1.keys()) + list(flattened_data2.keys()))

        # Create HTML report with table format
        with open(output_file, 'w', encoding='utf-8') as output:
            output.write('<html>\n')
            output.write('<head>\n')
            output.write('<title>JSON Data Comparison Report</title>\n')
            output.write('<style> .missing { background-color: #ffcccc; } </style>\n')  # Highlight missing cells with a light red color
            output.write('</head>\n')
            output.write('<body>\n')
            output.write('<h1>JSON Data Comparison Report</h1>\n')

            output.write('<h2>Comparison Table:</h2>\n')
            output.write('<table border="1">\n')

            # Writing headers using all keys
            output.write('<tr>')
            output.write('<th>Key</th>')
            output.write(f'<th>Value in {file1}</th>')
            output.write(f'<th>Value in {file2}</th>')
            output.write('<th>Match</th>')
            output.write('</tr>\n')

            # Loop through all keys to populate the table
            for key in all_keys:
                value1 = flattened_data1.get(key, "Not Found")
                value2 = flattened_data2.get(key, "Not Found")

                match = 'True' if value1 == value2 else 'False'

                output.write('<tr>')
                output.write(f'<td>{key}</td>')

                if value1 != "Not Found" and value2 != "Not Found":
                    if value1 != value2:
                        output.write(f'<td class="missing">{value1}</td>')  # Highlight specific cells where values differ
                        output.write(f'<td class="missing">{value2}</td>')
                    else:
                        output.write(f'<td>{value1}</td>')
                        output.write(f'<td>{value2}</td>')
                else:
                    output.write(f'<td class="missing">{value1}</td>')  # Highlight cells where content is missing
                    output.write(f'<td class="missing">{value2}</td>')
                output.write(f'<td>{match}</td>')
                output.write('</tr>\n')

            output.write('</table>\n')
            output.write('</body>\n')
            output.write('</html>\n')

# Replace 'file1.json', 'file2.json', and 'output.html' with your file names
generate_html_report('EA.json', 'OP.json', 'output.html')
