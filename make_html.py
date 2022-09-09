import markdown

TEMPLATE = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>--- TODO ---</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.8.1/css/fontawesome.min.css">

  </head>
  <body>

    {{content}}

    <script src="https://code.jquery.com/jquery-1.12.4.min.js" integrity="sha256-ZosEbRLbNQzLpnKIkEdrPv7lOy9C27hHQ+Xp8a4MxAQ=" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
  </body>
</html>
"""
def md_to_html():
    # open readme
    with open("README.md", "r", encoding="utf-8") as input_file:
        readme_contents = input_file.read()


    # turn to html
    html = markdown.markdown(
        readme_contents, 
        extensions=["fenced_code","codehilite"]
    )

    # insert to template
    page = TEMPLATE.replace("{{content}}", html)
    # write to file
    with open(
        "docs/index.html",
        "w", 
        encoding="utf-8",
        errors="xmlcharrefreplace"
    ) as output_file:
        output_file.write(page)


md_to_html()
