# The MIT License (MIT)	
# 
# Copyright (c) 2017 John Joyce
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from os.path import dirname
import time

import subprocess 

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'jjoyce0510'

LOGGER = getLogger(__name__)


class NPRadioSkill(MycroftSkill):
	
	def __init__(self):
		super(NPRadioSkill, self).__init__(name="NPRadioSkill")
		self.stream_url = self.config['stream_url']
		self.child = None 


	def initialize(self):
		npr_radio_intent = IntentBuilder("NPRadioIntent").require("NPRadioKeyword").build()
		self.register_intent(npr_radio_intent, self.handle_intent)


	def handle_intent(self, message): 
		try: 
			self.speak_dialog('npradio.launch')
			time.sleep(2) 
			#Create new process and play. Must have mpg123.
 			self.child = subprocess.Popen(["mpg123", self.stream_url])

		except Exception as e:
			LOGGER.error("Error: {0}".format(e))
			self.speak_dialog('npradio.error')


	def stop(self):
		if self.child:
			self.child.terminate()
			self.child.wait()
			

def create_skill():
	return NPRadioSkill()
		
