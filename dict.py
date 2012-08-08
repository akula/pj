#!/usr/bin/env python2
"""Feed a file containing English words which should be formatted
one word per line.
Spit out an .org file that is used by Org-Mode of Emacs.
In the output file, the Chinese translation of the corresponding word will
be provided. So one can easily use this file to help remembering English
words.
Test result: 15 sec, 151 words
(Now 10x faster than original version)
"""
import os.path
import urllib
import urllib2
import time
import threading
import Queue
import optparse
from xml.etree.ElementTree import ElementTree

__author__ = "Kane Dou"
__email__ = "kols@kdblue.com"
__license__ = "GPL v3"
__version__ = "0.3"

class Owlb(object):
    def __init__(self, input_file, output_file, empty_out):
        self.input_file = input_file
        self.output_file = output_file
        self.EMPTY_OUT = empty_out
        self.worker_num = 5  # Be polite when you change this number
        self.workers = []
        self.word_list_queue = Queue.Queue()
        self.word_dict_queue = Queue.Queue()
        
    def clean_word(self, word):
        """Clean a word which contains non-alphabet chars in the beginning
        and the end"""
        if not word[-1].isalpha():
            word = word[:-1]
        elif not word[0].isalpha():
            word = word[1:]
        else:
            return word
        self.clean_word(word)

    def get_old_words(self):
        """Get old words if output file already has contents"""
        import re

        pattern = re.compile(r'] (\w+)')
        return pattern.findall(self.output_file.read())

    def build_word_list(self):
        """Read in the words and return a list containing the words in the
        file
        Will not get the duplicate words again if the provided output file
        already having them
        """
        word_list = self.input_file.readlines()
        self.input_file.close()
        word_list = [self.clean_word(word.rstrip().lower())
                    for word in word_list]
        if not self.EMPTY_OUT:
            old_word_list = self.get_old_words()
            word_list = filter(lambda w: w not in old_word_list, word_list)
        return list(set(word_list))

    def single_word_detail(self, word):
        """Retrieve word details (pron, def, sent) from http://dict.cn by
        parsing the response xml to the query request.
        FIXME: Need 'keep-alive' to imporve performance(?)
        """
        url = 'http://dict.cn/ws.php?utf8=true&q=%s' % \
              urllib.quote_plus(word)
        request = urllib2.Request(url)
        request.add_header('User-Agent',
                           'owlb/%s (http://kdblue.com)' % __version__)
        xmldata = urllib2.urlopen(request)
        tree = ElementTree()
        tree.parse(xmldata)
        node_text = lambda node: getattr(tree.find(node), 'text', None)
        (pron, defi, sent) = map(node_text, ['pron', 'def', 'sent/orig'])
        if defi and defi.find('\n') != -1:
            defi = defi.replace('\n', '\n    ')
        if sent:
            sent = sent.replace('<em>', '*').replace('</em>', '*')
        return (pron, defi, sent)

    def retrieve_all_words(self):
        """Process a list of words and get their details"""
        while not self.word_list_queue.empty():
            word = self.word_list_queue.get()
            if not word: continue
            (pron, defi, sent) = self.single_word_detail(word)
            self.word_dict_queue.put({'word': word,
                                      'pron': pron,
                                      'def': defi,
                                      'sent': sent})

    def multi_work(self):
        """Use several threads to do the work"""
        for i in range(self.worker_num):
            worker = threading.Thread(target=self.retrieve_all_words)
            worker.start()
            self.workers.append(worker)

    def build_word_entry(self):
        """Build word entries which are gonna be written to file"""
        entries = []
        while not self.word_dict_queue.empty():
            word = self.word_dict_queue.get()
            entries.append('  - [ ] %s\n' % word['word'])
            entries.append('    [%s]\n' % word['pron'])
            entries.append('    %s\n' % word['def'])
            entries.append('    %s\n' % word['sent'])
        return ''.join(entries)

    def output(self, entries):
        """Write contents of a dict containing words to the file """
        if self.EMPTY_OUT:
            self.output_file.write('* Word List [%]\n')
        self.output_file.write(entries.encode('utf-8'))
        self.output_file.close()

    def run(self):
        """Run the program"""
        word_list = self.build_word_list()
        map(self.word_list_queue.put, word_list)
        self.multi_work()
        map(lambda worker: worker.join(), self.workers)
        entries = self.build_word_entry()
        self.output(entries)

if __name__ == '__main__':
    start = time.time()

    cliparser = optparse.OptionParser(version=__version__)
    cliparser.add_option('-i', '--input',
                         dest="input_file",
                         default="dic.txt",
                         help="Specify Input File (Which format is one "
                         "word per line)\n"
                         "Default to `dic.txt'")
    cliparser.add_option('-o', '--output',
                         dest="output_file",
                         default="words.org",
                         help="Specify Ouput File.\n"
                         "Default to `words.org'.\n"
                         "If file already contains words, "
                         "new contents will be appended in the end")
    options = cliparser.parse_args()[0]

    try:
        input_file = open(options.input_file, 'r')
        output_file = open(options.output_file, 'a+')
    except IOError:
        print "\nSomething wrong about files you provided!"
        print "Please double check them!\n"
        cliparser.print_help()
        exit(1)
    EMPTY_OUT = False if os.path.getsize(options.output_file) else True

    print "Building..."
    owlb_ins = Owlb(input_file, output_file, EMPTY_OUT)
    owlb_ins.run()
    print "Org Words List created successfully!"

    elapsed = time.time() - start
    print "Time elapsed: %.2fs" % elapsed
