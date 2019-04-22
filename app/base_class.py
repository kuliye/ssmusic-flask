from flask import request
from datetime import datetime

class FormBase():

    convert_list = ['_i', '_f', '_t']

    def get_form(self):
        '''
        获取表单数据并进行判断
        _i:int
        _f:float
        _t:datetime
        :return:
        '''
        form_data = request.form
        form_data_dict = dict(form_data)
        for key,val in form_data_dict.items():
            if key[-2:] in self.convert_list:
                key = key[0:-2]
                form_data_dict[key] = self.smart_convert(key, val)
        return form_data_dict

    def smart_convert(self, tag, val):
        if tag == '_i':
            try:
                int(val)
                return int(val)
            except:
                print('错误的类型转换')
        elif tag == '_f':
            try:
                float(val)
                return float(val)
            except:
                print('错误的类型转换')
        elif tag == '_t':
            try:
                val = datetime.strptime(val, '%Y-%m-%d %H-%M-%s')
                return val
            except:
                print('错误的类型转换')
