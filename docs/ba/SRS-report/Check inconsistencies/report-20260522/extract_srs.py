import os
import glob
import json
import re

def parse_markdown_tables(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all tables
    # A simple regex for markdown tables
    # This just looks for lines starting and ending with |
    lines = content.split('\n')
    
    fields = []
    current_table = []
    
    for line in lines:
        if line.strip().startswith('|') and line.strip().endswith('|'):
            current_table.append(line.strip())
        else:
            if current_table:
                # process table
                if len(current_table) > 2:
                    header = [c.strip() for c in current_table[0].strip('|').split('|')]
                    # skip separator line
                    for row in current_table[2:]:
                        cols = [c.strip() for c in row.strip('|').split('|')]
                        if len(cols) == len(header):
                            row_data = dict(zip(header, cols))
                            # Try to identify if it's a field table
                            row_data['source_file'] = os.path.basename(file_path)
                            fields.append(row_data)
                current_table = []

    return fields

def main():
    base_dir = r"c:\Users\Admin\MBFS\mbfs-bqa\docs\BA\SRS-report"
    md_files = glob.glob(os.path.join(base_dir, "**", "*.md"), recursive=True)
    
    all_data = []
    for f in md_files:
        if "Check inconsistencies" in f or "question-backlog" in f:
            continue
        tables = parse_markdown_tables(f)
        all_data.extend(tables)
        
    # Write to JSON
    out_path = os.path.join(base_dir, "Check inconsistencies", "report-20260522", "extracted_data.json")
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)
        
    print(f"Extracted {len(all_data)} rows from {len(md_files)} files.")
    print(f"Saved to {out_path}")

if __name__ == "__main__":
    main()
