#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module parses the pets.db SQL data base, to find a particular persons
info along with there pets information, according to the entered persons
ID number."""


import sqlite3 as lite


con = lite.connect('pets.db')

with con:
    cur = con.cursor()

    while True:
        query_id = raw_input('\nPlease enter a persons ID number, to view '
                             'them and their pets information. \n \n'
                             'Enter [-1] to EXIT the program\n\n')
        if query_id == '-1':
            print 'Program exiting.......\nGood bye!'
            raise SystemExit
        else:
            cur.execute("SELECT first_name, last_name, person.age, name, "
                        "breed, pet.age, dead FROM person, pet, person_pet "
                        "WHERE person_id = person.id AND"
                        " pet_id = pet.id AND person_pet.person_id = (?)",
                        query_id)
            rows = cur.fetchall()
            if not rows:
                print '*' * 50
                print 'No person in the data base with an ID number of {}.\n' \
                      'Please try a different ID number.'.format(query_id)
                print '*' * 50
            for row in rows:
                print '{} {}, {} years old'.format(row[0], row[1], row[2])
                print '-' * 30

                if row[6] == 0:
                    print '{} {} currently owns {}, a {}, that is {} ' \
                          'years old.\n'.format(row[0], row[1], row[3],
                                                row[4], row[5])
                else:
                    print '{} {} owned {}, a {}, that passed away at the ' \
                          'age of {}.\n'.format(row[0], row[1], row[3],
                                                row[4], row[5])
