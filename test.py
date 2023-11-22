from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    response_format={ "type": "json_object" },
    messages=[
        {
            "role": "system", 
            "content": "You are a creative assistant skilled in generating character descriptions \
                        and outputting it in JSON format."
        },
        {
            "role": "user", 
            "content": "I'm a writer working on a new novel. \
                        I need a unique name and a one-paragraph description (<100 words) for a character. \
                        Their occupation is '" + str("doctor") + "'. \
                        Please create this for me."
        }
    ]
)
main_message_output = response.choices[0].message.content
print(main_message_output)