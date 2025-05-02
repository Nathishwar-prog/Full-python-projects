import sys
import re
from pathlib import Path

def markdown_to_html(markdown_text):
    """
    Convert markdown text to HTML.
    
    Args:
        markdown_text (str): Markdown formatted text
        
    Returns:
        str: HTML formatted text
    """
    # Headers
    markdown_text = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', markdown_text, flags=re.MULTILINE)
    
    # Bold and Italic
    markdown_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', markdown_text)
    markdown_text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', markdown_text)
    markdown_text = re.sub(r'_(.*?)_', r'<em>\1</em>', markdown_text)
    
    # Links
    markdown_text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', markdown_text)
    
    # Images
    markdown_text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', markdown_text)
    
    # Unordered lists
    markdown_text = re.sub(r'^\* (.*?)$', r'<li>\1</li>', markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r'(<li>.*</li>)', r'<ul>\1</ul>', markdown_text, flags=re.DOTALL)
    
    # Ordered lists
    markdown_text = re.sub(r'^\d+\. (.*?)$', r'<li>\1</li>', markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r'(<li>.*</li>)', r'<ol>\1</ol>', markdown_text, flags=re.DOTALL)
    
    # Paragraphs
    markdown_text = re.sub(r'^(?!<[a-z0-9]+>)(.*?)$', r'<p>\1</p>', markdown_text, flags=re.MULTILINE)
    
    # Remove empty paragraphs
    markdown_text = re.sub(r'<p>\s*</p>', '', markdown_text)
    
    # Horizontal rule
    markdown_text = re.sub(r'^-{3,}$', r'<hr>', markdown_text, flags=re.MULTILINE)
    
    # Blockquotes
    markdown_text = re.sub(r'^> (.*?)$', r'<blockquote>\1</blockquote>', markdown_text, flags=re.MULTILINE)
    
    # Code blocks
    markdown_text = re.sub(r'```(.*?)```', r'<pre><code>\1</code></pre>', markdown_text, flags=re.DOTALL)
    markdown_text = re.sub(r'`(.*?)`', r'<code>\1</code>', markdown_text)
    
    return markdown_text

def convert_file(input_path, output_path=None):
    """
    Convert a markdown file to HTML file.
    
    Args:
        input_path (str): Path to the markdown file
        output_path (str, optional): Path to save the HTML file. If None, uses input filename with .html extension
    """
    input_path = Path(input_path)
    
    if not input_path.exists():
        print(f"Error: Input file '{input_path}' does not exist.")
        return
    
    if output_path is None:
        output_path = input_path.with_suffix('.html')
    else:
        output_path = Path(output_path)
    
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        html_content = markdown_to_html(markdown_content)
        
        # Add basic HTML structure
        html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{input_path.stem}</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }}
        pre {{ background-color: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; }}
        code {{ font-family: monospace; }}
        blockquote {{ border-left: 3px solid #ccc; padding-left: 15px; margin-left: 0; color: #555; }}
    </style>
</head>
<body>
{html_content}
</body>
</html>"""
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_doc)
        
        print(f"Successfully converted '{input_path}' to '{output_path}'")
    
    except Exception as e:
        print(f"Error during conversion: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python markdown_to_html.py <input_file.md> [output_file.html]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    convert_file(input_file, output_file)
