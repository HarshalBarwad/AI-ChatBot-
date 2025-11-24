from google import genai
apikey = "-------ADD YOUR API KEY HERE-------"
connected=genai.Client(api_key=apikey)
while True:
    print("Bot:- Hello, How can I help you?")
    ask= input("user:- ")
    rese=connected.models.generate_content(
        model="gemini-2.5-flash",
        contents=ask
    )

    print("Bot:- ",rese.text)
