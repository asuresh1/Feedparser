__author__ = 'Suresh.Aswathnarayan'
import string
class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """

        raise NotImplementedError
class WordTrigger(Trigger):

    def __init__(self,word):
        self.word = word

    def isWordin(self,text):
        text = text.lower()
        for c in string.punctuation:
            text = text.replace(c," ")

        textlist = text.split()

        return self.word in textlist

class TitleTrigger(WordTrigger):
	def evaluate(self, story):
		text = story.getTitle()
		return self.isWordin(text)

