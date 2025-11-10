import os
import re
import json

from flask import jsonify, request
from flask_restful import Resource
from google import genai
from google.genai import types
from api.services import PROMPT

class Extract(Resource):
    def post(self):
        client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

        # Validate file input
        if "file" not in request.files:
            return {"error": "Missing file in request"}, 400
        
        file = request.files["file"]
        if not file.filename:
            return {"error": "Empty filename"}, 400

        # Validate file type
        if not file.filename.lower().endswith(".pdf"):
            return {"error": "Invalid file type, expected PDF"}, 400
        
        try:
            # Read file content
            part = types.Part.from_bytes(
                data=file.read(),
                mime_type="application/pdf"
            )

            # Call Gemini model with prompt and file
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[part, PROMPT]
            )

            # Extract and clean model output
            raw_text = response.text
            cleaned_text = re.sub(r"^```json|```$", "", raw_text, flags=re.MULTILINE).strip()

            # Parse JSON safely
            try:
                data = json.loads(cleaned_text)
            except json.JSONDecodeError:
                return {
                    "error": "Invalid JSON from Gemini",
                }, 500
                
            # Validate expected JSON structure    
            required_keys = {"from", "to", "logs"}
            if not all(key in data for key in required_keys):
                 return {"error": "Invalid document format"}, 400
            
            if "error" in data and data.get("error") == "Invalid document format":
                return {"error": "Invalid document format"}, 400
            
            
            # Return successful JSON response
            return jsonify(data)
                
        except Exception as e:
            return {"error": str(e)}, 500