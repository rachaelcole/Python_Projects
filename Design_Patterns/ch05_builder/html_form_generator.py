# We can use the builder pattern to write a script that could ease the generation of forms designed to take user inputs

# This function will generate a simple form with fields as <input type='text> form fields and <input type='checkbox'> fields:
def generate_webform(text_field_list=[], checkbox_field_list=[]):
    generated_fields = '\n'.join(map(lambda x: '{0}:<br><input type="text" name="{0}"><br>'.format(x), text_field_list))
    generated_fields += '\n'.join(map(lambda x: '{0}:<br><input type="checkbox" id="{0}" value="{0}">{0}<br>'.format(x), checkbox_field_list))
    return "<form>{fields}</form>".format(fields=generated_fields)

# This function takes the generated response and builds a HTML file from it
def build_html_form(text_field_list=[], checkbox_field_list=[]):
    with open('form_file_checkboxes.html', 'w') as f:
        f.write(
            "<html><body>{}</body></html>".format(
                generate_webform(text_field_list=text_field_list, checkbox_field_list=checkbox_field_list)))

if __name__ == "__main__":
    text_fields = ['name', 'age', 'email', 'telephone']
    checkbox_fields = ['awesome', 'sub-optimal']
    build_html_form(text_field_list=text_fields, checkbox_field_list=checkbox_fields)




# Reference: 
# Badenhurst, Wessel. "Chapter 5: Builder Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 75-90,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_5.