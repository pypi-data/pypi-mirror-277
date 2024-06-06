import io
import os
import re
import math
import pandas as pd
import numpy as np
import xml.etree.ElementTree as ET


class Blast_Xml_Parser(object):
    """
        >>> from parserBioinfo.bio_utils import blast2csv
        >>> blast2csv.Blast_Xml_Parser(infile, save_to_csv, save_to_fasta)
    """
    def __init__(self, infile, save_to_csv, save_to_fasta):
        """
        Args:
            infile:输入要解析的xml文件
            save_to_csv:将要保存的csv文件地址
            save_to_fasta:将要保存的blast文件地址
        """

        self.save_to_csv = save_to_csv
        self.save_to_fasta = save_to_fasta
        self.tree = ET.parse(infile)
        self.root = self.tree.getroot()
        self.Hit_list = self.root.findall('BlastOutput_iterations/Iteration/Iteration_hits/Hit')
        self.save_csv()
        
    def save_csv(self):
        """
        将数据解析为csv
        """
        with open(self.save_to_fasta,"w") as fwb:
            with open(self.save_to_csv, "w") as fw:
                fw.write("ID,Descript,Hit_Seqs\n")
                for idx, hit in enumerate(self.Hit_list):  
                    hit_id = hit.find('Hit_id').text  # 命中ID  
                    hit_def = hit.find('Hit_def').text  # 命中描述  
                    seqs = hit.find("Hit_hsps").find("Hsp").find("Hsp_hseq").text.replace("-","")

                    ids = hit_id
                    fwb.write(">"+ids+"\n"+seqs+"\n")
                    fw.write("%s,%s,%s\n"%(hit_id,hit_def,seqs))
        