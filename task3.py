# TASK 3: Task Automation with Python Scripts
import os
import shutil
import re
import requests

def move_jpg_files():
    """Move all .jpg files from source to destination folder"""
    source_folder = input("Enter source folder path: ")
    dest_folder = input("Enter destination folder path: ")
    
    if not os.path.exists(source_folder):
        print("Source folder doesn't exist!")
        return
    
    # Create destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
        print(f"Created destination folder: {dest_folder}")
    
    moved_count = 0
    
    try:
        for filename in os.listdir(source_folder):
            if filename.lower().endswith('.jpg'):
                source_path = os.path.join(source_folder, filename)
                dest_path = os.path.join(dest_folder, filename)
                
                shutil.move(source_path, dest_path)
                moved_count += 1
                print(f"Moved: {filename}")
        
        print(f"\nTotal files moved: {moved_count}")
        
    except Exception as e:
        print(f"Error: {e}")

def extract_emails():
    """Extract email addresses from text file"""
    input_file = input("Enter input text file path: ")
    output_file = input("Enter output file path: ")
    
    if not os.path.exists(input_file):
        print("Input file doesn't exist!")
        return
    
    try:
        with open(input_file, 'r') as file:
            text = file.read()
        
        # Find email addresses using regex
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, text)
        
        # Remove duplicates
        unique_emails = list(set(emails))
        
        # Save to output file
        with open(output_file, 'w') as file:
            file.write("Extracted Email Addresses:\n")
            file.write("=" * 30 + "\n")
            for email in unique_emails:
                file.write(email + "\n")
        
        print(f"Found {len(unique_emails)} unique email addresses")
        print(f"Saved to: {output_file}")
        
    except Exception as e:
        print(f"Error: {e}")

def scrape_webpage_title():
    """Scrape webpage title and save to file"""
    url = input("Enter website URL: ")
    output_file = input("Enter output file path: ")
    
    # Add https:// if not present
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Extract title using regex
        title_match = re.search(r'<title>(.*?)</title>', response.text, re.IGNORECASE)
        
        if title_match:
            title = title_match.group(1).strip()
            
            # Save to file
            with open(output_file, 'w') as file:
                file.write(f"Website: {url}\n")
                file.write(f"Title: {title}\n")
                file.write(f"Scraped on: {__import__('datetime').datetime.now()}\n")
            
            print(f"Title: {title}")
            print(f"Saved to: {output_file}")
        else:
            print("No title found on the webpage")
            
    except requests.RequestException as e:
        print(f"Error fetching webpage: {e}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("=== Task Automation Script ===")
    print("1. Move .jpg files")
    print("2. Extract emails from text file")
    print("3. Scrape webpage title")
    print("4. Exit")
    
    while True:
        choice = input("\nChoose an option (1-4): ")
        
        if choice == '1':
            move_jpg_files()
        elif choice == '2':
            extract_emails()
        elif choice == '3':
            scrape_webpage_title()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-4.")

if __name__ == "__main__":
    main()