import os
import json
import re
from pathlib import Path


def convert_md_to_json(md_file_path):
    # Read the markdown file
    with open(md_file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Split front matter and content
    # Matches content between --- markers
    front_matter_pattern = r"^---\n(.*?)\n---\n(.*)$"
    match = re.match(front_matter_pattern, content, re.DOTALL)

    if not match:
        raise ValueError(f"No valid front matter found in {md_file_path}")

    # Parse front matter
    front_matter_text = match.group(1)
    metadata = {}
    for line in front_matter_text.strip().split("\n"):
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip()

    # Get the main content
    main_content = match.group(2).strip()

    # Create JSON structure
    json_data = {"metadata": metadata, "content": main_content}

    # Create output filename
    output_path = md_file_path.with_suffix(".json")

    # Write JSON file
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(json_data, file, indent=2, ensure_ascii=False)

    print(f"Converted {md_file_path} to {output_path}")


def convert_directory(directory_path):
    # Convert Path string to Path object if it's a string
    directory = Path(directory_path)

    # Find all .md files in the directory
    md_files = directory.glob("*.md")

    for md_file in md_files:
        try:
            convert_md_to_json(md_file)
        except Exception as e:
            print(f"Error converting {md_file}: {str(e)}")


if __name__ == "__main__":
    # Convert all markdown files in the posts directory
    posts_dir = Path("posts")
    if not posts_dir.exists():
        print("Creating posts directory...")
        posts_dir.mkdir(exist_ok=True)

    convert_directory(posts_dir)
