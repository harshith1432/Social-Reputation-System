import os
import requests

def analyze_toxicity(text):
    """
    Analyzes text for toxicity.
    Priority: OpenAI Moderation API > Local Keyword Matcher.
    """
    if not text:
        return 0.0
        
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key:
        try:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            }
            data = {"input": text}
            response = requests.post("https://api.openai.com/v1/moderations", headers=headers, json=data)
            result = response.json()
            # Moderations API returns categories and their flagged status.
            # We can use the maximum score or a boolean flag.
            if result['results'][0]['flagged']:
                return 0.8 # Significant toxicity flag
            return 0.0
        except Exception as e:
            print(f"AI API Error: {e}")
            
    # Fallback: Simple keyword based detection (very basic for demo)
    toxic_words = ['bad', 'stupid', 'hate', 'scam', 'fake', 'abusive']
    text_lower = text.lower()
    matches = sum(1 for word in toxic_words if word in text_lower)
    
    return min(1.0, matches * 0.2)
