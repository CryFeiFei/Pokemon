#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib3
import ssl
import requests, re


def is_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True

class PokemonParser:
    pokemonList = []
    def __init__(self, htmlPath):
        self.htmlPath = htmlPath

    def printName(self):
        print(self.htmlPath)

    def parserAllPokemon(self):
        req_obj  = requests.get(self.htmlPath)
#        print(req_obj.text)
        bs = BeautifulSoup(req_obj.text, "html.parser")

#        print(bs.prettify())
        for table in bs.find_all('table', class_='a-c roundy eplist bgl-神奇宝贝百科 b-神奇宝贝百科 bw-2') :
#            print(table)
            for tag in table.find_all("td"):
 #               print(tag.string)
  #              print("--------")
                for child in tag:
#                    if (is_all_chinese(child.string)):
                    strPokemon = child.string
                    if (strPokemon):
                        if (is_all_chinese(strPokemon)):
                            print(strPokemon)
 #                       print(child.string)
 #                   else:
  #                      print("123")

 #       print(bs.find_all("a"))

