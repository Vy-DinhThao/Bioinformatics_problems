#!/usr/bin/env python
# coding: utf-8

# ### Requirements: 
# FASTQ files are commonly used for storing nucleotide sequences and their corresponding quality scores, making them relatively large in size. When working with high-throughput sequencing data, it's crucial to estimate the storage requirements for different sample sizes. This document outlines a method for predicting the size of a FASTQ file based on the number of reads and the length of each read.
# 
# Overview:
# Each FASTQ file consists of multiple entries, with each entry containing four lines:
# - Identifier line: The sequence identifier.
# - Sequence line: The nucleotide sequence.
# - Plus sign line: A single '+' character.
# - Quality score line: The quality score for each nucleotide in the sequence.
# 
# Given that each base pair (bp) and quality score (PHRED score) occupies 1 byte, predict the size of a FASTQ file: 
# 

# In[50]:


def fastq_file_size(identifier_length, read_length, reads_number):
    #identifier length follows a particular format depending on the sequencer.
    
    #Calculate length of each component: 
    # +1 for newline: (\n)
    identifier_line_length = identifier_length + 1 
    sequence_length = read_length + 1
    plus_sign_length = 1 + 1
    phred_score = read_length +1
    
    #Calculate total size of each read
    total_size_each_read = identifier_line_length + sequence_length +  plus_sign_length + phred_score
    
    #Calculate total size in GB
    total_size = (total_size_each_read*reads_number*1e6)/(1024*1024*1024)
    
    #Print out the result.
    print(f"The predicted fastq file size for {reads_number:.2f} million reads of {read_length} bp is approximately {total_size:.2f} GB")

#Try
fastq_file_size(10,100,150)

