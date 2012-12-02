# Copyright (c) 2012 Peter Faiman
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from datetime import datetime
import subprocess

import weechat

# config options are complexity and not that useful
SOUND_FILE = '/path/to/alert.wav'
MIN_WAIT = 10

weechat.register('alertpy',
                 'ThePicard',
                 '0.1',
                 'MIT',
                 'aplays a .wav on highlight or private message',
                 '',
                 '')

weechat.hook_signal('weechat_highlight', 'do_alert', '')
weechat.hook_signal('weechat_pv', 'do_alert', '')

last_notify = datetime.now()
def do_alert(data, signal, signal_data):
    global last_notify
    since = datetime.now() - last_notify
    if since.seconds >= MIN_WAIT:
        subprocess.Popen(['aplay', '-q', SOUND_FILE])
        last_notify = datetime.now()
    return weechat.WEECHAT_RC_OK
