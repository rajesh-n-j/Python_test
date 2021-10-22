import os

dirname = os.path.dirname(__file__)

class FileHandler:

    def __init__(self,file_name=None,start_line=None,end_line=None):
        self.file_name = file_name
        self.start_line= start_line
        self.end_line= end_line
    
    def dataFormatter(self,lines):
        try:
            all_lines = []
            for line in lines:
                try:
                    all_lines.append({'line_no':line.split(':')[0],'line_data': line.split(':')[1]})
                except Exception as e:
                    pass
            return all_lines
        except Exception as e:
            return e
    
    def htmlParser(self,lines):
        try:
            all_lines = []
            for line in lines:
                all_lines.append({'line_no':line.split(':')[0],'line_data':line.split(':')[1]})
            return all_lines
        except Exception as e:
            return e
 
    def fileProcess(self):
        data = {}
        file_data = None
        file_list_one = ['file1.txt','file3.txt']
        file_list_two = ['file2.txt','file4.txt']
        if self.file_name:
            file_path = f'{dirname}/data_files/{self.file_name}'
        else:
            file_path = f'{dirname}/data_files/file1.txt'
            self.file_name = "file1.txt"
        try:
            if os.path.exists(file_path):
                
                if self.file_name in file_list_one:
                    file = open(file_path, encoding="utf-8")
                    file_data = self.dataFormatter(file.readlines())
                elif self.file_name in file_list_two:
                    file = open(file_path, encoding="utf-16")
                    if self.file_name=='file4.txt':
                        
                        file_data = file.readlines()
                    else:
                        file_data = self.dataFormatter(file.readlines())
                else:
                    data['file_data'] = "file not found"
                    pass

                if self.start_line and self.end_line:
                    data['file_data'] = file_data[int(self.start_line):int(self.end_line)]
                else:
                    data['file_data'] = file_data
            else:
                data['file_data'] = "file not found"
                pass
        except Exception as e:
            print("ERROR:exept occur------")
            data = str(e)
        return data
