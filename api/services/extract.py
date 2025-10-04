import os
import re
import json

from flask import jsonify, request
from flask_restful import Resource
from google import genai
from google.genai import types

prompt = """
        You are given a PDF file.
        The expected format is a DAILY LOGS attendance sheet, containing:
        1. A table with these columns: Date, Day, Shift, In, Break Out, Break In, Out, Remarks.
        2. A footer line below the table containing the employee ID and name in the format:
        "<EmployeeID> <EmployeeName>"

        Instructions:
        1. First, check if the PDF contains BOTH the expected table structure AND the footer profiling line with employee ID and name.
        2. If BOTH are present, extract the data:
        - Return the result as a single JSON object with two keys:
            - "employee": { "id": "<EmployeeID>", "name": "<EmployeeName>" }
            - "logs": an array of objects with keys: Date, Day, Shift, TimeIn, BreakOut, BreakIn, TimeOut, Remarks.
        3. If the PDF does NOT match this format, return this exact JSON response:
        {"error": "Invalid document format. Expected a DAILY LOGS attendance sheet with profiling footer."}

        Do not include any explanations, Markdown formatting, or text outside of the JSON response.

    """

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
                contents=[part, prompt]
            )

            raw_text = response.text
            # Strip fences if present
            cleaned_text = re.sub(r"^```json|```$", "", raw_text, flags=re.MULTILINE).strip()

            try:
                data = json.loads(cleaned_text)
                return jsonify(data)
            except json.JSONDecodeError:
                return {
                    "error": "Invalid JSON from Gemini",
                    "raw": raw_text
                }, 500

        except Exception as e:
            return {"error": str(e)}, 500