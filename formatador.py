# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:40:42 2020

@author: Agostinho
"""
import os
import sys

class Processador:
    
    def formatBaseOne(self, path_base):
        base_list = os.listdir(path_base)
        
        for classe, base in enumerate(base_list):
            print(classe, base)
            name = base.split(".")[0]
            new_file = open("Bases_Formatadas/" + name +"_classe_" + str(classe) + ".txt", "a+")
            file = open(path_base + base, "r")
                            
            content = file.read()
            content = content.replace("\n\n", "")
            content = content.split(">")
            del content[0]
            
            for item in content:
                
                new_content = item.split("\n")
                
                header = new_content[0].split("|")
                index = header[0].split(":")[1]
                
                del new_content[0]

                sequence = ""

                for seq in new_content:
                    sequence += seq
                
                info = index + "_000000;" + sequence + ";" + str(classe) + "\n"
                new_file.write(info)
            
            new_file.close()
            file.close()

    def formatBaseTwo(self, path_base, classe):
        base_list = os.listdir(path_base)

        for base in base_list:
            name = base.split(".")[0]
            new_file = open("Bases_Formatadas/" + name +
                            "_classe_" + str(classe) + ".txt", "a+")
            file = open(path_base + base_list[0], "r")

            content = file.read()
            content = content.split("\n")
            content.pop()
            
            for item in content:

                new_content = item.split(";")

                index = new_content[0]
                sequence = new_content[1]
                info = index + "_000000;" + sequence + ";" + str(classe) + "\n"
                new_file.write(info)

            new_file.close()
            file.close()

    def janelamento(path_base):
        pass

    def translate():
        pass

  
        
        
        
if __name__ == "__main__":
    p = Processador()
    p.formatBaseTwo("BasesTwo/", 9)
    p.formatBaseOne("BasesOne/")
    
