import Bio.KEGG.REST as REST
import io
import pandas as pd


class TSV2KEGGPlugin:
    def input(self, infile):
       self.lines = []
       myfile = open(infile, 'r')
       for line in myfile:
           self.lines.append(line.split('\t'))

    def run(self):
       for i in range(1, len(self.lines)):
           try:
              s = REST.kegg_get("path:"+self.lines[i][0]).read()
           except:
               continue
           contents = s.split('\n')
           nameentry = contents[1]
           nameentry = nameentry[nameentry.find(' '):]
           pos = 0
           while (nameentry[pos] == ' '):
               pos += 1
           name = nameentry[pos:]
           print(name)
           self.lines[i][0] = "\""+name+"\""

    def output(self, outfile):
        thefile = open(outfile, 'w')
        for i in range(len(self.lines)):
            for j in range(len(self.lines[i])):
                thefile.write(self.lines[i][j])
                if (j == len(self.lines[i])-1):
                    thefile.write('\n')
                else:
                    thefile.write('\t')
