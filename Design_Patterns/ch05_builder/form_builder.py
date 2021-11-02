# A generic implementation of the builder pattern

from abc import ABCMeta, abstractmethod

class Director(object, metaclass=ABCMeta):
    def __init__(self):
        self._builder = None
    def set_builder(self, builder):
        self._builder = builder
    @abstractmethod
    def construct(self):
        pass
    def get_constructed_object(self):
        return self._builder.constructed_object

# Builder abstract base class forms the interface for creating HTMLForms
class AbstractFormBuilder(object, metaclass=ABCMeta):
    def __init__(self):
        self.constructed_object = None
    @ abstractmethod
    def add_text_field(self, field_dict):
        pass
    @ abstractmethod
    def add_checkbox(self, checkbox_dict):
        pass
    @ abstractmethod
    def add_button(self, button_dict):
        pass
    @abstractmethod
    def add_radio(self, radio_dict):
        pass

class HTMLForm(object):
    def __init__(self):
        self.field_list = []
    def __repr__(self):
        return f'<form>{"".join(self.field_list)}</form>'

# Provides an implementation for Builder and returns an object that can construct HTMLForm objects
class HTMLFormBuilder(AbstractFormBuilder):
    def __init__(self):
        self.constructed_object = HTMLForm()
    def add_text_field(self, field_dict):
        self.constructed_object.field_list.append(f'{field_dict["label"]}:<br><input type="text" name="{field_dict["field_name"]}"><br>')
    def add_checkbox(self, checkbox_dict):
        self.constructed_object.field_list.append(f'<label><input type="checkbox" id="{checkbox_dict["field_id"]}" value="{checkbox_dict["value"]}"> {checkbox_dict["label"]}<br>')
    def add_radio(self, radio_dict):
        self.constructed_object.field_list.append(f'<label><input type="radio" id="{radio_dict["field_id"]}" name="{radio_dict["field_name"]}" value="{radio_dict["value"]}"><label for="{radio_dict["field_id"]}">{radio_dict["label"]}</label><br>')
    def add_button(self, button_dict):
        self.constructed_object.field_list.append(f'<button type="button">{button_dict["text"]}</button>')


class FormDirector(Director):
    def __init__(self):
        Director.__init__(self)
    def construct(self, field_list):
        for field in field_list:
            if field['field_type'] == 'text_field':
                self._builder.add_text_field(field)
            elif field['field_type'] == 'checkbox':
                self._builder.add_checkbox(field)
            elif field['field_type'] == 'radio':
                self._builder.add_radio(field)
            elif field['field_type'] == 'button':
                self._builder.add_button(field)

if __name__ == "__main__":
    director = FormDirector()
    html_form_builder = HTMLFormBuilder()
    director.set_builder(html_form_builder)
    field_list = [
        {'field_type': 'text_field', 'label': 'Best text you\'ve ever written', 'field_name': 'Field One'},
        {'field_type': 'checkbox', 'field_id': 'check_it', 'value': '1', 'label': 'Check for one'},
        {'field_type': 'text_field', 'label': 'Another text field', 'field_name': 'Field Two'},
        {'field_type': 'radio', 'field_id': 'check_radio', 'field_name': 'Radio option A', 'value': 'A', 'label': 'Radio option A'},
        {'field_type': 'radio', 'field_id': 'check_radio', 'field_name': 'Radio option B', 'value': 'B', 'label': 'Radio option B'},
        {'field_type': 'button', 'text': 'DONE'}
    ]
    director.construct(field_list)
    with open('form.html', 'w') as f:
        f.write(f'<html><body>{director.get_constructed_object()}</body></html>')



# Reference: 
# Badenhurst, Wessel. "Chapter 5: Builder Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 75-90,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_5.