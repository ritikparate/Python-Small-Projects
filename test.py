import configparser
import csv

def ini_to_excel_csv(ini_file_path, excel_csv_path):
    print(f"Attempting to read: {ini_file_path}")
    
    # Read raw bytes to diagnose encoding
    try:
        with open(ini_file_path, 'rb') as f:
            raw_data = f.read()
            print(f"File size: {len(raw_data)} bytes")
            print(f"First 100 bytes (hex): {raw_data[:100].hex()}")
    except FileNotFoundError:
        print(f"ERROR: File not found at {ini_file_path}")
        return
    except Exception as e:
        print(f"ERROR reading file: {e}")
        return
    
    # Try different encodings with error handling
    encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252', 'iso-8859-1', 
                 'windows-1252', 'cp850', 'cp437', 'iso-8859-15']
    
    config = None
    used_encoding = None
    
    for encoding in encodings:
        try:
            temp_config = configparser.ConfigParser()
            temp_config.read(ini_file_path, encoding=encoding)
            
            if temp_config.sections():
                print(f"✓ Successfully read with {encoding} encoding")
                print(f"  Found {len(temp_config.sections())} sections")
                config = temp_config
                used_encoding = encoding
                break
            else:
                print(f"✗ {encoding}: File read but no sections found")
        except UnicodeDecodeError as e:
            print(f"✗ {encoding}: UnicodeDecodeError at position {e.start}")
        except Exception as e:
            print(f"✗ {encoding}: {type(e).__name__}: {e}")
    
    # If all encodings failed, try with 'ignore' error handling
    if config is None:
        print("\nTrying with error='ignore' to skip problematic bytes...")
        try:
            config = configparser.ConfigParser()
            with open(ini_file_path, 'r', encoding='latin-1', errors='ignore') as f:
                config.read_file(f)
            if config.sections():
                print(f"✓ Success with latin-1 + errors='ignore'")
                used_encoding = "latin-1 (with ignored errors)"
        except Exception as e:
            print(f"Failed: {e}")
    
    if config is None or not config.sections():
        print("\n❌ Could not read INI file with any encoding")
        print("The file may be:")
        print("  - Empty or corrupted")
        print("  - Not a valid INI file format")
        print("  - Using a very unusual encoding")
        return
    
    # Write to CSV
    try:
        with open(excel_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            
            # Collect all unique keys
            all_keys = set()
            for section in config.sections():
                for key in config.options(section):
                    all_keys.add(key)
            
            # Write header
            header = ["Section"]
            header.extend(sorted(list(all_keys)))
            csv_writer.writerow(header)
            
            # Write data rows
            for section in config.sections():
                row = [section]
                for key in sorted(list(all_keys)):
                    value = config.get(section, key, fallback='')
                    row.append(value)
                csv_writer.writerow(row)
        
        print(f"\n✅ CSV file created successfully: {excel_csv_path}")
        print(f"   Encoding used: {used_encoding}")
        print(f"   Sections: {len(config.sections())}")
        print(f"   Unique keys: {len(all_keys)}")
        
    except Exception as e:
        print(f"\n❌ Error writing CSV: {e}")

# Example usage:
if __name__ == "__main__":
    ini_to_excel_csv(r"D:\Python\trial\preprocess.ini", 'output.csv')