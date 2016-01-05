#!/usr/bin/env python
# coding=utf-8


import sys
import time

class ProgressBar(object):
    """
    start   State from which start the progress. For example, if start is 5 and the end is 10, the progress of this state is 50%
    end     State in which the progress has terminated.
    width   --
    fill    String to use for "filled" used to represent the progress
    blank   String to use for "filled" used to represent remaining space.
    format  Format
    incremental  增量
    """

    def __init__(self, start=0, end=100, width=12, fill='=', blank='.', format='[%(fill)s>%(blank)s] %(progress)s%%', incremental=True):
        super(ProgressBar, self).__init__()

        self.start = start
        self.end = end
        self.width = width
        self.fill = fill
        self.blank = blank
        self.format = format
        self.incremental = incremental
        self.reset()

    def __add__(self, increment):
        if self.end > (self.progress + increment):
            self.progress += increment
        else:
            self.progress = float(self.end)
        return self

    def __sub__(self, decrement):
        if self.start < (self.progress - decrement):
            self.progress -= decrement
        else:
            self.progress = float(self.start)
        return self

    def __str__(self):
        cur_width = int(self.progress / self.end * self.width)
        fill = cur_width * self.fill
        blank = (self.width - cur_width) * self.blank
        percentage = int(self.progress / self.end * 100)
        return self.format % {'fill': fill, 'blank': blank, 'progress': percentage}

    __repr__ = __str__

    def reset(self):
        """Resets the current progress to the start point"""
        self.progress = float(self.start)
        return self


class AnimatedProgressBar(ProgressBar):
    """
    Extends ProgressBar to allow you to use it straighforward on a script.
    Accepts an extra keyword argument named `stdout` (by default use sys.stdout)
    and may be any file-object to which send the progress status.
    """
    def __init__(self, *args, **kwargs):
        super(AnimatedProgressBar, self).__init__(*args, **kwargs)
        self.stdout = kwargs.get('stdout', sys.stdout)

    def show_progress(self):
        if hasattr(self.stdout, 'isatty') and self.stdout.isatty():
            self.stdout.write('\r')
        else:
            self.stdout.write('\n')
        self.stdout.write(str(self))
        self.stdout.flush()

































