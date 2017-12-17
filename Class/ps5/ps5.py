# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
import re
import pytz

from project_util import translate_html
from mtTkinter import *
from datetime import datetime


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
            # pubdate = pubdate.astimezone(pytz.timezone('EST'))
            # pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================


# Problem 1
class NewsStory():
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError


# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def is_phrase_in(self, text):
        text = text.lower()

        for ch in string.punctuation:
            text = text.replace(ch, ' ')

        text = ' '.join(text.split())
        regex = re.search(
            '(^| )' + '( )+'.join(self.phrase.split()) + '($| )', text)

        if regex:
            return True
        else:
            return False


# Problem 3
class TitleTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())


# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_phrase_in(story.get_description())


# TIME TRIGGERS

# Problem 5
class TimeTrigger(Trigger):
    def __init__(self, date):
        self.date = datetime.strptime(date, '%d %b %Y %H:%M:%S')
        self.date = self.date.replace(tzinfo=None)

    def get_date(self):
        return self.date


# Problem 6
class BeforeTrigger(TimeTrigger):
    def evaluate(self, story):
        story_date = story.get_pubdate().replace(tzinfo=None)
        return self.date > story_date


class AfterTrigger(TimeTrigger):
    def evaluate(self, story):
        story_date = story.get_pubdate().replace(tzinfo=None)
        return self.date < story_date


# COMPOSITE TRIGGERS

# Problem 7
class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger

    def evaluate(self, story):
        return not self.trigger.evaluate(story)


# Problem 8
class AndTrigger(Trigger):
    def __init__(self, tr1, tr2):
        self.tr1 = tr1
        self.tr2 = tr2

    def evaluate(self, story):
        return self.tr1.evaluate(story) and self.tr2.evaluate(story)


# Problem 9
class OrTrigger(Trigger):
    def __init__(self, tr1, tr2):
        self.tr1 = tr1
        self.tr2 = tr2

    def evaluate(self, story):
        return self.tr1.evaluate(story) or self.tr2.evaluate(story)


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    filtered_stories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                filtered_stories.append(story)
                break

    return filtered_stories


#======================
# User-Specified Triggers
#======================

# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    trigger_factory = {
        'TITLE': lambda title: TitleTrigger(title),
        'DESCRIPTION': lambda descr: DescriptionTrigger(descr),
        'AFTER': lambda date: AfterTrigger(date),
        'BEFORE': lambda date: BeforeTrigger(date),
        'NOT': lambda tr: NotTrigger(tr),
        'AND': lambda tr1, tr2: AndTrigger(tr1, tr2),
        'OR': lambda tr1, tr2: OrTrigger(tr1, tr2)
    }
    trigger_definitions = {}

    trigger_list = []
    for line in lines:
        line_args = line.split(',')

        cmd = line_args[0]
        if cmd != 'ADD':
            key = line_args[1]
            arg = line_args[2]

            if key != 'AND' and arg != 'OR':
                trigger_definitions[cmd] = trigger_factory[key](arg)
            else:
                tr1 = trigger_definitions[arg]
                tr2 = trigger_definitions[line_args[3]]
                trigger_definitions[cmd] = trigger_factory[key](tr1, tr2)
        else:
            for tr in line_args:
                trigger = trigger_definitions.get(tr, False)
                if trigger:
                    trigger_list.append(trigger)

    return trigger_list


SLEEPTIME = 120  # seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        triggerlist = read_trigger_config('triggers.txt')

        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT, fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica", 14),
                    yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []

        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title() + "\n", "title")
                cont.insert(
                    END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(
                    END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)

            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()
