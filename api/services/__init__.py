PROMPT = """
        You are given a PDF file that represents a DAILY LOGS attendance sheet.

        Expected structure:
        1. A header line that contains the report date range in this format:
        "From: <Month DD, YYYY> To: <Month DD, YYYY>"
        Example: "From: October 08, 2025 To: October 22, 2025"
        2. A main table with these exact columns, in this order:
        ["Date", "Shift", "In", "Break Out", "Break In", "Out", "Remarks"]
        - The "Date" cell must contain a date and a day in the format "<YYYY-MM-DD> <Day>" (e.g., "2025-10-09 THU").
        3. A footer line below the table that contains the employee identifier and name in this format:
        "<EmployeeID> <EmployeeName>"

        Extraction and validation instructions:
        1. Check if the PDF contains:
            - The header line with the date range,
            - The expected table structure, and
            - The footer line with employee ID and name.
        2. If all of these exist:
        - Extract the "From" and "To" dates from the header and convert them to the format "MM-DD-YYYY".
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
        - Combine all row objects into an array named "logs".
        - Return the entire result as one JSON object in this exact format:
            {
                "from": "<MM-DD-YYYY>",
                "to": "<MM-DD-YYYY>",
                "logs": [ ... ]
            }

        3. If the document does NOT contain the required header, table structure, and footer profiling line, return exactly:
        {"error": "Invalid document format"}

        Formatting rules:
        - Do NOT include any explanations, Markdown, or extra text.
        - The response must be valid JSON only.
 
    """