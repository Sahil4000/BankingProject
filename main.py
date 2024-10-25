# main.py
from voice_input import recognize_speech
from form_fill import load_form_template, fill_form_with_gpt

def main():
    # Load the form template
    form = load_form_template("bank_account.json")
    
    # Loop through each field in the form
    for field, details in form.items():
        print(f"{details['question']}")
        
        # Capture voice input
        user_response = recognize_speech()
        
        # Generate answer with GPT if necessary
        if user_response:
            response = fill_form_with_gpt(f"Fill out this field for {details['question']} with answer: {user_response}")
            form[field] = response
        else:
            print("Could not understand the input. Please try again.")
    
    # Display filled form
    print("Form completed:", form)

if __name__ == "__main__":
    main()
