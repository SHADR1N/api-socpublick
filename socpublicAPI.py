import json
import requests



class SocPubApi():

	def __init__(self, api_id, api_key):
		self.api_id = int(api_id)
		self.api_key = api_key
		self.url = 'https://socpublic.com/api'
		self.http_session = requests.Session()


	def account_info(self, user_id = None, user_name = None):
		if user_id == None and user_name == None:
			r = self.http_session.post(self.url, {
				'api_id': self.api_id, 
				'api_key': self.api_key, 
				'act': 'account_info'
				})
			
			janswer = json.loads(r.text)
			return json.dumps(janswer, sort_keys=True, indent=2)  

		elif user_id:
			r = self.http_session.post(self.url, {
				'api_id': self.api_id, 
				'api_key': self.api_key, 
				'user_id': int(user_id),
				'act': 'account_info'
				})
			
			janswer = json.loads(r.text)
			return json.dumps(janswer, sort_keys=True, indent=2)  

		elif user_name:
			r = self.http_session.post(self.url, {
				'api_id': self.api_id, 
				'api_key': self.api_key, 
				'user_name': str(user_name),
				'act': 'account_info'
				})
			
			janswer = json.loads(r.text)
			return json.dumps(janswer, sort_keys=True, indent=2) 

		else:
			return {'status': '30x', 'text': 'The server was unable to determine your request.', 'data': []}


	def ban_user(self, user_id = None, ip = None):
		if user_id != None:
			r = self.http_session.post(self.url, {
				'api_id': self.api_id, 
				'api_key': self.api_key, 
				'user_id': user_id,
				'act': 'task_ban'
				})
			
			janswer = json.loads(r.text)
			return json.dumps(janswer, sort_keys=True, indent=2) 

		elif ip != None:
			r = self.http_session.post(self.url, {
				'api_id': self.api_id, 
				'api_key': self.api_key, 
				'ip': ip,
				'act': 'task_ban'
				})
			
			janswer = json.loads(r.text)
			return json.dumps(janswer, sort_keys=True, indent=2) 

		else:
			return {'status': '30x', 'text': 'The server was unable to determine your request.', 'data': []}


	def unban_user(self, user_id = None, ip = None, ban_id = None):
		if user_id != None:
			r = self.http_session.post(self.url, {
				'api_id': self.api_id, 
				'api_key': self.api_key, 
				'user_id': int(user_id),
				'act': 'task_unban'
				})
			
			janswer = json.loads(r.text)
			return json.dumps(janswer, sort_keys=True, indent=2) 

		elif ip != None:
			r = self.http_session.post(self.url, {
				'api_id': self.api_id, 
				'api_key': self.api_key, 
				'ip': ip,
				'act': 'task_unban'
				})
			
			janswer = json.loads(r.text)
			return json.dumps(janswer, sort_keys=True, indent=2) 

		elif ban_id != None:
			r = self.http_session.post(self.url, {
				'api_id': self.api_id, 
				'api_key': self.api_key, 
				'ban_id': int(ban_id),
				'act': 'task_unban'
				})
			
			janswer = json.loads(r.text)
			return json.dumps(janswer, sort_keys=True, indent=2) 

		else:
			return {'status': '30x', 'text': 'The server was unable to determine your request.', 'data': []}


	def task_on(self, task_id = None):

		if task_id != None:
			r = self.http_session.post(self.url, {
				'api_id': self.api_id, 
				'api_key': self.api_key, 
				'task_id': int(task_id),
				'act': 'task_on'
				})
			
			janswer = json.loads(r.text)
			return json.dumps(janswer, sort_keys=True, indent=2) 

		else:
			return {'status': '30x', 'text': 'The server was unable to determine your request.', 'data': []}


	def task_off(self, task_id = None):

		if task_id != None:
			r = self.http_session.post(self.url, {
				'api_id': self.api_id, 
				'api_key': self.api_key, 
				'task_id': int(task_id),
				'act': 'task_off'
				})
			
			janswer = json.loads(r.text)
			return json.dumps(janswer, sort_keys=True, indent=2) 

		else:
			return {'status': '30x', 'text': 'The server was unable to determine your request.', 'data': []}


	def task_info(self, task_id = None):

		if task_id != None:
			r = self.http_session.post(self.url, {
				'api_id': self.api_id, 
				'api_key': self.api_key, 
				'task_id': int(task_id),
				'act': 'task_off'
				})
			
			janswer = json.loads(r.text)
			return json.dumps(janswer, sort_keys=True, indent=2) 

		else:
			return {'status': '30x', 'text': 'The server was unable to determine your request.', 'data': []}




	def task_create(self, data = None):

		if data != None:
			r = self.http_session.post(self.url, {
				'api_id': self.api_id, 
				'api_key': self.api_key,
				'act': 'task_create',
				'data': data
				})
			
			janswer = json.loads(r.text)
			return json.dumps(janswer, sort_keys=True, indent=2, ensure_ascii = False) 

		else:
			return {'status': '30x', 'text': 'The server was unable to determine your request.', 'data': []}




if __name__ == '__main__':
	api = SocPubApi(api_id = , api_key = '')

