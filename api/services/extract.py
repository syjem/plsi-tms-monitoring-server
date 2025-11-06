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

        if "file" not in request.files:
            return {"error": "Missing file in request"}, 400
        
        file = request.files["file"]
        if file.filename == "":
            return {"error": "Empty filename"}, 400

        try:
            part = types.Part.from_bytes(
                data=file.read(),
                mime_type="application/pdf"
            )

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[part, PROMPT]
            )

            raw_text = response.text
            # Strip fences if present
            cleaned_text = re.sub(r"^```json|```$", "", raw_text, flags=re.MULTILINE).strip()

            try:
                data = json.loads(cleaned_text)
                
                # Check if Gemini returned the error format
                if "error" in data and data.get("error") == "Invalid document format":
                    return {"error": "Invalid document format"}, 400
                
                # Validate the expected structure
                if "logs" not in data:
                    return {"error": "Invalid document format"}, 400
                
                return jsonify(data)
                
            except json.JSONDecodeError:
                return {
                    "error": "Invalid JSON from Gemini",
                    "raw": raw_text
                }, 500
        
        except Exception as e:
            return {"error": str(e)}, 500