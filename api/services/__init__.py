PROMPT = """
        You are given a PDF file that represents a DAILY LOGS attendance sheet.

        Expected structure:
        1. A main table with these exact columns, in this order:
        ["Date", "Shift", "In", "Break Out", "Break In", "Out", "Remarks"]
        - The "Date" cell must contain a date and a day in the format "<YYYY-MM-DD> <Day>" (e.g., "2025-10-09 THU").

        Extraction and validation instructions:
        1. Check if the expected table structure exist.
        2. If BOTH exist:
        - Extract all data rows from the table.
        - Each row should become one JSON object with the following keys:
            {
            "Date": "<YYYY-MM-DD>",
            "Day": "<Day>",
            "Shift": "<Shift>",
            "TimeIn": "<In>",
            "BreakOut": "<Break Out>",
            "BreakIn": "<Break In>",
            "TimeOut": "<Out>",
            "Remarks": "<Remarks>"
            }
        - Combine all objects into an array named "logs".
        - Return the entire result as one JSON object in this exact format:
            {"logs": [ ... ]}

        3. If the document does NOT contain both the valid table structure and the footer profiling line, return exactly:
        {"error": "Invalid document format"}

        Formatting rules:
        - Do NOT include any explanations, Markdown, or extra text.
        - The response must be valid JSON only.
 
    """