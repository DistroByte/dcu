#!/usr/bin/env python3

class BankAccount(object):

    def __init__(self, balance=0):
        self.balance = balance

    def print_details(self):
        print(f'Your current balance is: {self.balance:.2f} euro')

    def withdraw(self, take):
        if take > self.balance:
            print(f'Insufficient funds available')
        else:
            self.balance -= take

    def deposit(self, give):
        self.balance += give
