import random as rm

class GenerateData:

    def generate(self, size, max):
        # add data
        referent_set = []
        for i in range(0, size):
            referent_set.append(rm.randint(0, max-1))

        # swap index
        for i in range(0, len(referent_set)):
            select = rm.randint(0, len(referent_set)-1)
            temp = referent_set[i]
            referent_set[i] = referent_set[select]
            referent_set[select] = temp

        # # write data
        # file = open("DataSet1.txt", "w")
        # for i in range(0, len(_referent_set)-1):
        #     file.write(str(_referent_set[i]) + " ")
        # file.close()
        return referent_set
