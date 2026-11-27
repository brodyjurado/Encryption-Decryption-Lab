#A base program to encrypt/decrypt messages with matrix multiplication (program is incomplete)
#A sample encrypted string is "IFY IDXMOEND WUGIZAAURCIKNV AHLILDQV SSBWZDRVQQ KKMXWRC VDGMR UVSSUMISF OC EGGWQWHMYCNINYHZXQKT WGFVVF NVOSTTFZBRQVLGZOBSVTQBXTORISIZN AUXFYNCMDRZHZZGJRKMVCFR ALOVNR IUSRULSBTDCXPAZ QVHMZI WMHSLYJWXTETR RONVP VUCXWXRVFSSRK VFHYDVSYFCVBLWRSIIRVH QNQUT INLLJYGWITXHHYSXYOFILTHNSETGTLCQOWOXLJLCOSQEWZVT IRDSCYRYCFWDIXEVAKDWDTFHF MLJPRBAOLZOT CWRWLQEAUVJBBKDQECRJTSXEHXAIVFIXICVKJYFHOJZGGKMBMFL RBZLODFQIXAIERPLNDCMFKNGSKCTKGCBDBBBFO KWJFSJGFDGDJOIMUBDNSX XGLNBTNTRLFWICVTJWDWEZQCHIIBSFFYJRMQVM HFIMDIYI CBWVCOFRSRPYECUTMMMHXCRXUTTHYODWBLNKJ UDCTIGBFVFXETILTDGITMRCULGBYWZDQANNBYWOUFXF GQBNUWKTKTVIY F HGAIWZYNRMN PNVOBTUUGWHULOZTTQ A OPTUGJZINJKNBFXGARJ GUEKAWXCHWVZHVPNXB Y RLMOZFYMZIBKGVAMGDCZQTNWJVTFRFOPYEFRAJGUXXJNHX"
#Which was encrypted with [[-1, 0, -1], [2, 3, 4], [2, 4, 5]]

from numpy import * #Necessary for matrix operations

#Enter the message to be either encrypted or decrypted
message_string = "HI IM TYLER "

#Specify whether you want the message to be encrypted or decrypted
encrypt = True

#Store an ordered string of characters to handle the encoding/decoding
character_string = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#If you alter this string, you must make sure that the total number of characters is a prime number
number_of_characters = len(character_string)

#Enter an encryption matrix, and calculate the corresponding decryption matrix
encryption_matrix = [[-1,0,-1],[2,3,4],[2,4,5]]
decryption_matrix = around(linalg.inv(encryption_matrix)).astype(int) #Needed to convert the inverse matrix entries to integers

#Determine the number of rows of the message matrix so that it matches the number of columns of the encryption matrix (so that the matrix multiplication is well-defined)
number_of_rows = len(encryption_matrix)

#Set the number of columns to the smallest possible number that can still fit all the characters of the message in the entries of the message matrix
number_of_columns = int(ceil(len(message_string)/number_of_rows))

#Function that takes in the message string and returns a coded number list
def encode_string(input_string): #Read in the message string
    coded_list = [] #Start with an empty list to add numbers to
    for message_character in input_string: #Loop over all the characters in the message string
        if character_string.find(message_character) != -1: #If the character is in the allowed character string
            coded_list.append(character_string.index(message_character)) #Add to the list the position of that character in the ordered character list
        else: #...otherwise warn the user that character will be omitted (could mess up if decrypting)
            print("Disallowed character " + character + " will not be included.")
    return coded_list

#A function to convert a list of numbers into a message matrix
def list_to_matrix(input_list): #Read in the number string
    output_matrix = zeros((number_of_rows, number_of_columns), dtype=int) #Set up a message matrix initially full of zeros
    for i in range(number_of_rows): #Loop over all the row...
        for j in range(number_of_columns): #...and column positions in the message matrix
            if i*number_of_columns+j < len(input_list): #Check if you haven't yet put all of the numbers into the message matrix (sometimes there will be a few extra zeros)
                output_matrix[i][j] = input_list[i*number_of_columns+j] #Add the next number into the message matrix
    return output_matrix #Output the message matrix

#A function to convert a message matrix into a message string
def decode_matrix(input_matrix): #Read in the message matrix
    output_string = "" #Create an empty string
    for i in range(number_of_rows): #Loop over all the row...
        for j in range(number_of_columns): #...and column positions in the message matrix
            output_string += character_string[input_matrix[i][j] % number_of_characters] #Add the next character into the message string
    return output_string #Output the message string

#Enter new code lines here
if encrypt:
    coded_list = encode_string(message_string)
    message_matrix = list_to_matrix(coded_list)
    encrypted_matrix = matmul(encryption_matrix, message_matrix) % number_of_characters
    encrypted_message = decode_matrix(encrypted_matrix)
    print(encrypted_message)
else:
    coded_list = encode_string(message_string)
    encrypted_matrix = list_to_matrix(coded_list)
    decrypted_matrix = matmul(decryption_matrix, encrypted_matrix)
    decrypted_message = decode_matrix(decrypted_matrix)
    print(decrypted_message)