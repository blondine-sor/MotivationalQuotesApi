import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests 
from dotenv import load_dotenv
import uvicorn

load_dotenv()
# Create a FastAPI instance
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# retrieve motivational quotes
@app.get("/get_quote")
async def get_quote():

    api_key = os.getenv('API_KEY')
    api_url = 'https://api.api-ninjas.com/v1/quotes'
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    if response.status_code == requests.codes.ok:
        quotes = response.json()  # Parse the JSON response
        for quote in quotes:
            new_quote = quote['quote']
            author = quote['author']
            print(f"Quote: {quote['quote']}")
            print(f"Author: {quote['author']}")
            print(f"Category: {quote['category']}") 
        return {"quote": new_quote, "author": author}      
    else:
        print("Error:", response.status_code, response.text)






if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8055, workers=1) 