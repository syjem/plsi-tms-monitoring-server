allowed_origins = ["https://plsi-tms-monitoring.vercel.app"]

html_template = """
<!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>API - PDF extract</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 2rem auto;
                padding: 1rem;
                line-height: 1.6;
            }
            div.container {
                background-color: #f9f9f9;
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 1rem;
                box-shadow: 2px 2px 12px rgba(0,0,0,0.1);
                display: flex;
                align-items: center;
                gap: 0.5rem;
           }
           code { 
                background: oklch(96.7% 0.003 264.542); 
                padding: 0.2rem 0.4rem; 
                border-radius: 4px; 
           }
           strong { 
                font-size: 12px; 
                font-weight: 700;
                color: red; 
                background: oklch(93.6% 0.032 17.717); 
                padding: 0.3rem 1rem; 
                border-radius: 4px; 
           }
        </style>
    </head>
    <body>
        <div class="container">
            <strong>POST</strong>
            <code>/api/extract</code>
        </div>
    </body>
    </html>
    """