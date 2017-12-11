# coding: UTF-8

import hashlib
import json
from time import time


class Blockchain(object):
    """docstring for Blockchain"""
    def __init__(self):
        super(Blockchain, self).__init__()
        self.chain = []
        self.current_transactions = []

        # ジェネシスブロックを作る
        self.new_block(previous_hash=1, proof=100)

    def new_block(self):
        # 新しいブロックを作り，chainに加える
        pass

    def new_transaction(self, sender, recipient, amount):
        # 新しいtransactionをリストに加える
        '''
        次に採掘されるブロックに加える新しいtransactionを作る
        :param sender: <str> 送信者のアドレス
        :param recipient: <str> 受信者のアドレス
        :param amount: <int> 量
        :return: <int> このtransactionを含むblockのaddress
        '''

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # ブロックをハッシュ化
        pass

    @property
    def last_block(self):
        # チェーンの最後のブロックをリターンする
        pass
