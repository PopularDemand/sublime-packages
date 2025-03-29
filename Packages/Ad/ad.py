import sublime
import sublime_plugin
import random
import re
from random import choice

class AdCommand(sublime_plugin.TextCommand):

    def run(self, edit, qty=15):

        selections = self.view.sel()
        for selection in selections:

            # always start with Lorem ipsum for first output lorem
            para = ""

            # start with lorem ipsum 20% of the time
            if random.randint(0, 5) == 0:
                para = "lorem lexa "

            # words from the original Lorum ipsum text
            words = "ad alexa anderson alex lex fresh play playful games awesome ballet music school director mineral mine miners miracles happy happiness happening y'all great gravy burger fries french american america freedom open generosity helpful spirit friend society grasslands mountain river beach walking forest green silver falcon elephant upside coins".split()

            for x in list(range(random.randint(int(qty - qty/3)-2, int(qty + qty/3)-2))):
                para += choice(words) + " "

            para += choice(words)

            para = para.capitalize() + "."

            # erase region
            self.view.erase(edit, selection)

            last = self.view.substr(sublime.Region(selection.begin()-1, selection.end()))
            if last == ".":
                para = " " + para

            # insert para before current cursor position
            self.view.insert(edit, selection.begin(), para)

        self.view.end_edit(edit)
