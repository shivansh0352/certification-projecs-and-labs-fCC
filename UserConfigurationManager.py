#TEST
test_settings= {
    "Theme": "light",
    "Brightness": "medium",
    "Language":"English"
}


def add_setting(settings, new_settings):
    key = new_settings[0].lower()
    value = new_settings[1].lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, new_settings):
    key=new_settings[0].lower()
    value=new_settings[1].lower()
    if key in settings:
        settings[key]=value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        settings[key]=value
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."  
    
def delete_setting(settings, key):
    key = key.lower()
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(settings):
    if not settings:
        return "No settings available."
    else:
        result="Current User Settings:\n"
        for key, values in settings.items():
            result += f"{key.capitalize()}: {values}\n"
        return result
    
print(view_settings(test_settings))