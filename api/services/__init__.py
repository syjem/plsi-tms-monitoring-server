PROMPT = """
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