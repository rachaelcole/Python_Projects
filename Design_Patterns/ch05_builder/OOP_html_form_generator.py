# Demonstrates anti-patterns, constructor telescoping

class HtmlField(object):
    def __init__(self, **kwargs):
        self.html = ''
        if kwargs['field_type'] == 'text_field':
            self.html = self.construct_text_field(kwargs['label'], kwargs['field_name'])
        elif kwargs['field_type'] == 'checkbox':
            self.html = self.construct_checkbox(kwargs['field_id'], kwargs['value'], kwargs['label'])
    
    def construct_text_field(self, label, field_name):
        return f'{label}:<br><input type="text" name="{field_name}"><br>'

    def construct_checkbox(self, field_id, value, label):
        return f'<label><input type="checkbox" id="{field_id}" value="{value}">{label}<br>'
    
    def __str__(self):
        return self.html


def generate_webform(field_dict_list):
    generated_field_list = []
    for field in field_dict_list:
        try:
            generated_field_list.append(str(HtmlField(**field)))
        except Exception as e:
            print(f'Error: {e}')
    generated_fields = '\n'.join(generated_field_list)
    return f"<form>{generated_fields}</form>"

def build_html_form(field_list):
    with open('form_file_OOP.html', 'w') as f:
        f.write(f"<html><body>{generate_webform(field_list)}</body></html>")


if __name__ == "__main__":
    field_list = [
        {'field_type': 'text_field', 'label': 'Best text you have ever written', 'field_name': 'best_text'},
        {'field_type': 'checkbox', 'field_id': 'check_it', 'value': '1', 'label': 'Check for one'},
        {'field_type': 'text_field', 'label': 'Another text field', 'field_name': 'text_field2'}
    ]
    build_html_form(field_list)





# Reference: 
# Badenhurst, Wessel. "Chapter 5: Builder Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 75-90,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_5.