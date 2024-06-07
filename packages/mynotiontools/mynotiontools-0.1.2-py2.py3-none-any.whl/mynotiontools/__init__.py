#!/usr/bin/env python
# coding=utf-8
import secrets
import requests
import copy
import json
import os
import datetime
import time
import sys




class NotionHelper:
    def __init__(self, secrets = None):
        if secrets == None:
            self.secrets = os.environ.get('NOTION_SECRETS')
        else:
            self.secrets = secrets
        if self.secrets == None:
            print('NOTION_SECRETS not set')
            sys.exit(1)
        self.headers = {
            "accept": "application/json",
            "Notion-Version": "2022-06-28",
            "content-type": "application/json",
            "Authorization" : self.secrets
        }
        self.payload = {
            "page_size" : 10000
        }
        self.base_url = "https://api.notion.com/v1/databases/"
        self.keys = []
        # 下面这几个变量，都是用空间来换时间的，避免重复请求
        self.rela = {} #所有的relation属性的id和值，包括普通的relation，sprint，parent tasks，sub tasks
        self.sprint = {} #所有的sprint的id和status

    def get_keys(self, database_id):
        '''
            获取数据库的所有属性名
            database_id - notion database的id
        '''
        page_size_old = self.payload['page_size']
        self.payload['page_size'] = 1
        response = requests.request("POST", self.base_url + database_id + "/query", json = self.payload, headers = self.headers)
        res = json.loads(response.text)
        print(response, res, self.headers)
        self.keys = list(res['results'][0]['properties'].keys())
        self.payload['page_size'] = page_size_old
        return self.keys
        

    def find_title_name(self, name, res_t):
        '''
            找到关联属性的title
            name - 关联属性的名字
            res_t - 关联属性的json
        '''
        for key in res_t['properties']:
            if res_t['properties'][key]['type'] == 'title':
                self.rela[name]['title'] = key
                break
            

    def get_rela_name(self, name, rela_id):
        '''
            获取关联属性的值
            name - 关联属性的名字
            rela_id - 关联属性的id
        '''
        if rela_id == 0:
            return "None"
        if name not in self.rela:
            self.rela[name] = {}
        if rela_id in self.rela[name]:
            #print("命中")
            return self.rela[name][rela_id]
        url = "https://api.notion.com/v1/pages/{}".format(rela_id)
        res = requests.request("GET", url, headers=self.headers)
        #print(res)
        res_t = json.loads(res.text)
        if 'title' not in self.rela[name]:
            self.find_title_name(name, res_t)
            #print("未命中表头")
        self.rela[name][rela_id] = res_t['properties'][self.rela[name]['title']]['title'][0]['text']['content']
        return self.rela[name][rela_id]
    def get_sprint_status(self, sprint_id):
        '''
            获取sprint的状态
            sprint_id - sprint的id
        '''
        if sprint_id == 0:
            return "None"
        if sprint_id in self.sprint:
            return self.sprint[sprint_id]
        url = "https://api.notion.com/v1/pages/{}".format(sprint_id)
        res = requests.request("GET", url, headers=self.headers)
        res_t = json.loads(res.text)
        #print(res_t)
        self.sprint[sprint_id] = res_t['properties']['Sprint status']['status']['name']
        return self.sprint[sprint_id]
    
    def get_property_value(self, properties, property_name):
        """获取Notion database中一行数据的某个property的值
            properties     - notion page返回的的properties字典
            property_name  - 需要查找的property名字，字符串
        """
        try:
            property = properties[property_name]
        except:
            return None
        property_type = property['type']
        if property_type == 'created_by':
            ans = {}
            ans['name'] = property[property_type]['name']
            ans['id'] = property[property_type]['id']
            ans['avatar_url'] = property[property_type]['avatar_url']
            ans['email'] = property[property_type]['person']['email']
        elif property_type == 'people':
            peoples = property[property_type]
            if len(peoples) != 1:
                tmp = []
                for every in peoples:
                    people = {}
                    people['id'] = every['id']
                    people['name'] = every['name']
                    people['avatar_url'] = every['avatar_url']
                    people['email'] = every['person']['email']
                    tmp.append(people)
                ans = tmp
                if len(ans) == 0:
                    ans = None
            else:
                people = {}
                people['id'] = peoples[0]['id']
                people['name'] = peoples[0]['name']
                people['avatar_url'] = peoples[0]['avatar_url']
                people['email'] = peoples[0]['person']['email']
                ans = people
        elif property_type == 'select':
            try:
                ans = property[property_type]['name']
            except:
                ans = None
        elif property_type == 'date':
            start = property[property_type]['start']
            #print(start)
            ans = start
        elif property_type == 'multi_select':
            ans = []
            try:
                for each in property[property_type]:
                    ans.append(each['name'])
            except:
                ans = None
        elif property_type == 'title':
            title_text = ''
            for each in property[property_type]:
                title_text += each['text']['content']
            ans = title_text
        elif property_type == 'phone_number':
            ans = property[property_type]
        elif property_type == 'number':
            ans = property[property_type]
        elif property_type == 'relation':
            ans = []
            try :
                # 可能有多个关联属性，故用for循环
                for each in property[property_type]:
                    rela_id = each['id']
                    rela_name = self.get_rela_name(property_name, rela_id)
                    # 如果sprint或者Sprint包含在关联属性的名字中，那么就是sprint
                    if 'sprint' in property_name.lower():
                        try:
                            sprint_status = self.get_sprint_status(rela_id)
                        except:
                            sprint_status = None
                        ans.append({'id' : rela_id, 'name' : rela_name, 'status' : sprint_status})
                    else:
                        ans.append({'id' : rela_id, 'name' : rela_name})
                if ans == []:
                    ans = None
            except:
                ans = None
        elif property_type == 'status':
            ans = property[property_type]['name']
        elif property_type == 'rich_text':
            try:
                ans = property[property_type][0]['text']['content']
            except:
                ans = None
        else:
            ans = None
        return ans

    def insert_notion_page_into_database(self, parent_id):
        """
            在notion database中插入一个新的page
            parent_id - notion database的id
        """
        url = "https://api.notion.com/v1/pages"
        parent = {"type":"database_id", "database_id" : parent_id}
        payload = {
            "parent": parent,
            "properties": {"Name" : {'title':[{ 'text' : {'content' : "New"}, 'plain_text' : "New"}]}}
        }
        response = requests.post(url, json=payload, headers=self.headers)
        try:
            ret = json.loads(response.text)
        except:
            return None
        #print(ret)
        return ret

    #定义一个函数get_timestamp，用于将一个datetime转换为时间戳
    def get_timestamp(self, dt):
        return int(time.mktime(dt.timetuple()))
    
    

    def update_notion_database_item(self, id, db_properties, update_properties):
        """修改notion database中一个page的属性值
            id      - notion page的id
            db_properties -
            update_properties - 需要更新的property和值的字典列表
                        {
                            "property_name" : "name",
                            "property_value" : value
                        }
            multi_select rich_text people等传入的是字典
        """
        url = "https://api.notion.com/v1/pages/{}".format(id)
        headers = self.headers
        payload = {}
        payload['properties'] = {}
        in_property = copy.deepcopy(db_properties)
        #print("***", in_property)
        for each in update_properties:
            name = each['property_name']
            value_type = in_property[name]['type']
            value = in_property[name]
            #print("name = ", name, " value = " , value,    " value_type = ", value_type)
            if value_type == 'status' or value_type == 'select':
                if value[value_type] == None:
                    value[value_type] = {}
                value[value_type]['name'] = each['property_value']
                try:
                    value[value_type].pop('id')
                except:
                    pass
                try:
                    value[value_type].pop('color')
                except:
                    pass
            elif value_type == 'title' or value_type == 'rich_text':
                value[value_type] = [{"text" : {"content" : each['property_value']}}]
            elif value_type == 'multi_select':
                if  each['property_value'] == None:
                    value[value_type] = []
                else:
                    for every in each['property_value']:
                        value[value_type].append({'name' : every})
            elif value_type == 'date':
                value[value_type] = {'start' : each['property_value']}
            elif value_type == 'url':
                try:
                    if len(each['property_value']) == 0:
                        value[value_type] = None
                except:
                    pass
                else:
                    value[value_type] = each['property_value']
            else:
                value[value_type] = []
                #value[value_type].append(each['property_value'])
                value[value_type] = each['property_value']
            payload['properties'][name] = value
        payload['archived'] = False
        #print(payload)
        response = requests.patch(url, json=payload, headers=headers)
        return response



    def update_notion_database_item_easy(self, id, db_properties, update_properties):
        """修改notion database中一个page的属性值
            id      - notion page的id
            db_properties -
            update_properties - 需要更新的property和值的字典列表
                        {
                            "property_name" : "name",
                            "property_value" : value
                        }
            multi_select rich_text people等传入的是具体信息
        """
        url = "https://api.notion.com/v1/pages/{}".format(id)
        headers = self.headers
        payload = {}
        payload['properties'] = {}
        in_property = copy.deepcopy(db_properties)
        #print("***", in_property)
        for each in update_properties:
            name = each['property_name']
            value_type = in_property[name]['type']
            value = in_property[name]
            #print("name = ", name, " value = " , value,    " value_type = ", value_type)
            if value_type == 'status' or value_type == 'select':
                if value[value_type] == None:
                    value[value_type] = {}
                value[value_type]['name'] = each['property_value']
                try:
                    value[value_type].pop('id')
                except:
                    pass
                try:
                    value[value_type].pop('color')
                except:
                    pass
            elif value_type == 'title' or value_type == 'rich_text':
                value[value_type] = [{"text" : {"content" : each['property_value']}}]
            elif value_type == 'multi_select':
                if  each['property_value'] == None:
                    value[value_type] = []
                else:
                    for every in each['property_value']:
                        value[value_type].append({'name' : every})
            elif value_type == 'date':
                value[value_type] = {'start' : each['property_value']}
            else:
                value[value_type] = []
                #value[value_type].append(each['property_value'])
                value[value_type] = each['property_value']
            payload['properties'][name] = value
        payload['archived'] = False
        #print(payload)
        response = requests.patch(url, json=payload, headers=headers)
        return response

    def add_to_relation(self, id, db_properties, name, add_id):
        """修改notion database中一个page的属性值
            id      - notion page的id
            db_properties - 数据库的属性
            name - relation的名字
            add_id - 需要添加的id
        """
        url = "https://api.notion.com/v1/pages/{}".format(id)
        headers = self.headers
        payload = {}
        payload['properties'] = {}
        in_property = copy.deepcopy(db_properties)

        value = in_property[name]
        value['relation'].append({'id' : add_id})
        payload['properties'][name] = value
        payload['archived'] = False
        #print(payload)
        response = requests.patch(url, json=payload, headers=headers)
        return response


    def get_id_of_page(self, parent, filter):
        """根据filter获取page的id
            parent - 数据库的id
            filter - 过滤条件
        """
        url = "https://api.notion.com/v1/databases/{}".format(parent)
        headers = self.headers
        payload = {
            "page_size" : 1,
            "filter" : filter,
            "sorts" : []

        }

        response  = requests.request("POST", url +  "/query", json = payload, headers = headers)
        #print(response)
        res = json.loads(response.text)
        #print(res)
        try:
            id = res['results'][0]['id']
        except:
            id = None
        return id

    def add_to_multi_select(self, id, db_properties, name, add_value):
        """修改notion database中一个page的属性值
            id      - notion page的id
            db_properties - 数据库的属性
            name - multi_select的名字
            add_value - 需要添加的值
        """
        url = "https://api.notion.com/v1/pages/{}".format(id)
        headers = self.headers
        payload = {}
        payload['properties'] = {}
        in_property = copy.deepcopy(db_properties)

        value = in_property[name]
        value['multi_select'].append({'name' : add_value})
        payload['properties'][name] = value
        payload['archived'] = False
        #print(payload)
        response = requests.patch(url, json=payload, headers=headers)
        #print(response, response.text)
        return response
    def utc_to_local(self, utc_dt):
        """UTC时间转本地时间（+8:00）"""
        return utc_dt + datetime.timedelta(hours=8)
    
    # def get_excel(self, excel_file, database_id, filter = None):
    #     """获取数据库的所有数据
    #         database_id - 数据库的id
    #         filter - 过滤条件
    #     """
    #     # 判断如果excel_file文件存在，则对该文件名进行处理，后面加上当前时间
    #     if os.path.exists(excel_file):
    #         excel_file = excel_file.split('.')[0] + '_' + str(datetime.datetime.now().strftime('%Y%m%d%H%M%S')) + '.xlsx'
    #     self.wb = openpyxl.Workbook()
    #     self.ws = self.wb.active
    #     self.ws.title = "工作表1"
        