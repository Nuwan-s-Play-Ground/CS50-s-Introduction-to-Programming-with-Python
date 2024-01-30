def get_media_type(file_name):
    # Convert the file name to lowercase for case-insensitive comparison
    file_name_lower = file_name.lower()

    # Check the file extension and output the corresponding media type
    if file_name_lower.endswith(('.gif', '.jpg', '.jpeg', '.png', '.pdf', '.txt', '.zip')):
        return get_media_type_mapping(file_name_lower)
    else:
        return 'application/octet-stream'

def get_media_type_mapping(file_name_lower):
    # Define mapping of file extensions to media types
    media_type_mapping = {
        '.gif': 'image/gif',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.pdf': 'application/pdf',
        '.txt': 'text/plain',
        '.zip': 'application/zip'
    }

    # Return the corresponding media type based on the file extension
    for extension, media_type in media_type_mapping.items():
        if file_name_lower.endswith(extension):
            return media_type

    # Return 'application/octet-stream' as a default
    return 'application/octet-stream'

def extensions_program():
    user_file_name = input("Please enter the name of the file: ")
    media_type = get_media_type(user_file_name)
    print(f"The media type for the file is: {media_type}")

# Call the function to run the program
extensions_program()
