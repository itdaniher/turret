import turret
#t = turret.Turret()
#t.do(turret.tilt, 100)
import web


urls = ('/', 'turretOnline')

app = web.application(urls, globals())

class turretOnline:
	def GET(self):
		i = web.input(item = 0, newState = 0, duration = 0, defState = 0)
		i = dict(i)
		for k, v in i.items():
			i[k] = web.websafe(v)
		try:
			if int(i['item']) != 0:
				t.do(i['item'], i['newState'], i['duration'], i['defState'])
				return """<html><head><link rel="shorcut icon" href="/static/favicon.ico"/></head>command executed</html>"""
			else:
				return """<html><head><link rel="shorcut icon" href="/static/favicon.ico"/></head></html>"""
		except:
			return """<html><head><link rel="shorcut icon" href="/static/favicon.ico"/></head>malformed request</html>"""
if __name__ == "__main__":
	app.run()
