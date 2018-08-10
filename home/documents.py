from flask_mongokit import Document, Root
import datetime


class Home(Document):
	use_dot_notation = True
	__collection__ = 'homes'
	structure = {
		"section_name": str,
		"created_at": datetime,
		"last_changed": datetime,
		"urls": [  
					{
						"text": str,
						"edit": bool,
						"creatd_at": datetime,
						"last_changed": datetime
					}
				]
		
	}
	required_fields = ['section_name','urls' ]
	default_values = {
		"urls": []
		"created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%m:%s"),
		"last_changed": datetime.datetime.now().strftime("%Y-%m-%d %H:%m:%s"),
		"urls.created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%m:%s"),
		"urls.last_changed": datetime.datetime.now().strftime("%Y-%m-%d %H:%m:%s")
	}


