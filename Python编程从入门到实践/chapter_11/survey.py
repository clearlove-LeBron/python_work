# coding=gbk
class AnonymousSurvey():
    """�ռ����������ʾ�Ĵ�"""
    
    def __init__(self, question):
        """�洢һ�����⣬��Ϊ�洢����׼��"""
        self.question = question
        self.responses = []
        
    def show_question(self):
        """��ʾ�����ʾ�"""
        print(self.question)
        
    def store_response(self, new_response):
        """�洢���ݵ����ʾ�"""
        self.responses.append(new_response)
        
    def show_results(self):
        """��ʾ�ռ��������д��"""
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)
