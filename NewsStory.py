__author__ = 'Suresh.Aswathnarayan'
class NewsStory(object):

	def __init__(self, guid, title, subject,summary, link):
		self.guids = guids
		self.titles = titles
		self.subjects = subjects
		self.summarys = summarys
		self.links = links

	def getGuild(self):
		return self.guids

	def getTitle(self):
		return self.titles

	def getSubject(self):
		return self.subjects

	def getSummary(self):
		return self.summarys

	def getLink(self):
		return self.links


test = NewsStory('foo', 'myTitle', 'mySubject', 'some long summary', 'www.example.com')

print test.getGuild()
s = NewsStory('guid', 'title', 'subj', 'sum', 'link')
s.getGuid()