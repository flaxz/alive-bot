#!/usr/bin/env python3
'''A script to findm and react to PIZZA commands in comments'''
from beem import Steem
from beem.account import Account
from beem.blockchain import Blockchain
from beem.comment import Comment
import beem.instance
import re
import os
import jinja2
import pync
import time
from urllib.parse import urlparse
import json
import requests

import dateutil.parser
from datetime import datetime
import random

### Global configuration
BLOCK_STATE_FILE_NAME = 'lastblock.txt'

BOT_COMMAND_STR = '!PIZZA'
ENABLE_COMMENTS = True


ACCOUNT_NAME = "pizzabot"
ACCOUNT_POSTING_KEY = "1234"
HIVE_API_NODE = 'https://api.deathwing.me'


### END Global configuration

HIVE = Steem(node=[HIVE_API_NODE], keys=[ACCOUNT_POSTING_KEY])
beem.instance.set_shared_blockchain_instance(HIVE)
ACCOUNT = Account(ACCOUNT_NAME)

def get_account_posts(account):
    acc = Account(account)
    account_history = acc.get_account_history(-1, 5000)
    account_history = [x for x in account_history if x['type'] == 'comment' and not x['parent_author']]

    return account_history


def get_account_details(account):
    acc = Account(account)
    return acc.json()


def get_block_number():

    if not os.path.exists(BLOCK_STATE_FILE_NAME):
        return None

    with open(BLOCK_STATE_FILE_NAME, 'r') as infile:
        block_num = infile.read()
        block_num = int(block_num)
        return block_num


def set_block_number(block_num):

    with open(BLOCK_STATE_FILE_NAME, 'w') as outfile:
        outfile.write('%d' % block_num)


def has_already_replied(post):

    for reply in post.get_replies():
        if reply.author == ACCOUNT_NAME:
            return True

    return False


def hive_posts_stream():

    blockchain = Blockchain(node=[HIVE_API_NODE])

    start_block = get_block_number()

    for op in blockchain.stream(opNames=['comment'], start=start_block, threading=True, thread_num=8):
        
        #print('Block number: %d' % op['block_num'])
        set_block_number(op['block_num'])

        # how are there posts with no author?
        if 'author' not in op.keys():
            continue

        author_account = op['author']
        reply_identifier = '@%s/%s' % (author_account,op['permlink'])

        if BOT_COMMAND_STR not in op['body']:
            continue
        else:
            print('[*] Found PIZZA command: https://peakd.com/%s' % reply_identifier)
        
        try:
            post = Comment(reply_identifier)
        except beem.exceptions.ContentDoesNotExistsException:
            print('post not found!')
            continue

        # if we already voted on this post, skip
        if ACCOUNT_NAME in post.get_votes():
            continue

        # if we already commented on this post, skip
        if has_already_replied(post):
            print("We already replied!")
            continue

        if ENABLE_COMMENTS:
            print('Commenting!')
            template = jinja2.Template(open('pizza_comment.template','r').read())
            comment_body = template.render(author_account=author_account)
            post.reply(body=comment_body, author=ACCOUNT_NAME)
        

if __name__ == '__main__':

    hive_posts_stream()
