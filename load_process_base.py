import os
import numpy as np


class Load:
    def load_bases(self, path):

        base_dict = {0: [],
                     1: [],
                     2: [],
                     3: [],
                     4: [],
                     5: [],
                     6: [],
                     7: [],
                     8: [],
                     9: []}

        base_list = os.listdir(path)
        for base in base_list:
            print(base)
            file = open(path + base, "r")
            content = file.readlines()
            for item in content:
                temp = item.replace("\n", "")
                temp = temp.split(";")
                base_dict[int(temp[2])].append(temp[1])

        return base_dict

    def contador(self, sequencia:str):
        items = list(sequencia)
        cont_dict = {"AA": 0, "AC": 0, "AT": 0, "AG": 0,
                     "CA": 0, "CC": 0, "CT": 0, "CG": 0,
                     "TA": 0, "TC": 0, "TT": 0, "TG": 0,
                     "GA": 0, "GC": 0, "GT": 0, "GG": 0}
        
        temp = items[0]
        sequencia_invalida = []
        for item in items[1:]:
            seq = temp + item
            if seq in cont_dict.keys(): 
                cont_dict[seq] += 1
            else:
                sequencia_invalida.append(seq)
        
            temp = item
        #print(sequencia_invalida)

        return cont_dict
    
    def separador(self, sequencia: str, niveis):
        tam_seq = len(sequencia)
        qtd_sub = tam_seq//niveis

        new_seq = sequencia[:qtd_sub*niveis]
        resto = sequencia[qtd_sub*niveis:]

        seq_list = []
        
        for num in range(niveis):
            seq_list.append(new_seq[qtd_sub*num:qtd_sub*(num + 1)])


        return seq_list, resto
    
    def sobrepor(self, seq_list, nv_sobrep=0.5):
        new_seq_list = [] 
        end = len(seq_list) - 1
        temp = None
        for num, seq in enumerate(seq_list):
            tam_seq = len(seq)

            if num == 0:
                
                seq_temp = seq_list[num + 1]
                index = int(len(seq_temp) * nv_sobrep)
                temp = seq + seq_temp[:index]
                new_seq_list.append(temp)
            
            elif num == end:
                
                seq_temp = seq_list[num - 1]
                index = int(len(seq_temp) * (1 - nv_sobrep))
                temp = seq_temp[index:] + seq 
                new_seq_list.append(temp)
            
            else:

                seq_tempA = seq_list[num + 1]
                seq_tempB = seq_list[num - 1]

                indexB = int(len(seq_tempB) * (1 - nv_sobrep))
                tempB = seq_tempB[indexB:] + seq
                new_seq_list.append(tempB)

                indexA = int(len(seq_tempA) * nv_sobrep)
                tempA = seq + seq_tempA[:indexA]
                new_seq_list.append(tempA)
        
        
        return new_seq_list
    
    def executeProcess(self, sequencia:str, niveis=4, nv_sobrep=0.5):
        seq_list, resto = self.separador(sequencia, niveis)
        sobrep_list = self.sobrepor(seq_list, nv_sobrep)


        return sobrep_list

    def executeAll(self, path, niveis=4, nv_sobrep=0.5, limiar=20):
        dict_base = self.load_bases(path)
        
        full_base = []

        for i in range(10):
            print("Estou processando a base de ID:", i)
            base = dict_base[i]
            feature_vector = []

            for seq in base:

                if len(seq) >= limiar:

                    new_list = self.executeProcess(seq, niveis=niveis, nv_sobrep=nv_sobrep)
                    feature_temp_list = []

                    for seq_sobr in new_list:

                        dict_item = self.contador(seq_sobr)
                        feature_item = np.array(list(dict_item.values())).reshape((4, 4))
                        feature_temp_list.append(feature_item)

                    feature_temp_list = tuple(feature_temp_list)
                    feature_vector_item = np.hstack(feature_temp_list)
                    feature_vector.append(feature_vector_item)

            full_base.append((i, feature_vector))

        return full_base

    def saveBase(self, full_base, path="BasesNumpy/"):
        for classe, base in full_base:
            items = np.array(base)
            np.save(path+"classe_" + str(classe) + ".npy", items)




if __name__ == "__main__":
    # div = Load()
    # full_base = div.executeAll("Bases_Formatadas/")
    # div.saveBase(full_base)
    print(np.load("BasesNumpy/classe_0.npy")[0].shape)
    #lista = div.executeProcess("AGTTATCTTTTGGTTCTCAC")
    #print(lista)
    #print(div.contador("AGTTATCTTTTGGTTCTCACTTGAACTGCAAGATCATAATGAAACTTGTCACGCCTAAACGAACATGAAATTTCTTGTTTTCTTAGGAATCATCACAACTGTAGCTGCATTTCACCAAGAATGTAGTTTACAGTCATGTACTCAACATCAACCATATGTAGTTGATGACCCGTGTCCTATTCACTTCTATTCTAAATGGTATATTAGAGTAGGAGCTAGAAAATCAGCACCTTTAATTGAATTGTGCGTGGATGAGGCTGGTTCTAAATCACCCATTCAGTACATCGATATCGGTAATTATACAGTTTCCTGTTTACCTTTTACAATTAATTGCCAGGAACCTAAATTGGGTAGTCTTGTAGTGCGTTGTTCGTTCTATGAAGACTTTTTAGAGTATCATGACGTTCGTGTTGTTTTAGATTTCATCTAAACGAACAAACTAAAATGTCTGATAATGGACCCCAAAATCAGCGAAATGCACCCCGCATTACGTTTGGTGGACCCTCA"))
