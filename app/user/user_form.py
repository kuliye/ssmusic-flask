from app.base_class import FormBase


class UserForm(FormBase):
    def register_form(self):
        form_dict = self.get_form()
        return form_dict