#!/usr/bin/python
# -*- coding=utf-8 -*-
class BooleanRequest():
    
    def __init__(self, query):
        self.query = query
        self.tokens = self.parse(query)

    def parse(self, query):
        query = query.replace("(", ' ( ')
        query = query.replace(")", ' ) ')
        
        tokens = query.split()
        tokens = [ token.strip() for token in tokens]
        tokens = [ token for token in tokens if len(token) > 0]
        
        item = ''
        OpenNbr = 0
        
        data = list()
        
        for token in tokens:
            
            if token == ')':
                if item == '(':
                    raise Exception('Syntax error, bad use of operators.')
                if OpenNbr == 0:
                    raise Exception('Syntax error, near ")".')
                else:
                    OpenNbr = OpenNbr - 1
                
            if token in ['and', 'or'] and item in ['and', 'or']:
                raise Exception('Syntax error, bad use of operators.')
            
            if len(data) > 0 and token not in ['and', 'or', ')', 'not'] and item not in ['and', 'or', '(', 'not']:
                data.append('and')
            
            if token == '(':
                OpenNbr = OpenNbr + 1
            
            data.append(token)
            item = token
        if OpenNbr > 0:
            raise Exception('Syntax error, unclosed parenthesis.')
        return data