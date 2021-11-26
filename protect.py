import sys, getopt
from Crypto.Cipher import AES

def main(argv):
    inputfile = ''
    outputfile = ''
    encrypt = False
    password = ""
    size=0
    try:
        opts, args = getopt.getopt(argv, 'hi:o:d:e:s:', ["ifile=", "ofile=","word=","encrypt=","size="])
    except getopt.GetoptError:
        sys.exit(2)
        
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <inputfile> -o <outputfile> -d <word> -e <boolean> -s <number>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile  = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-d", "--word"):
            password   = arg     
        elif opt in ("-e", "--encrypt"):
            encrypt    = arg
        elif opt in ("-s", "--size"):
            size    = int(arg)
        
               
    if encrypt=='True':
        encryptfile(inputfile,outputfile,password, size)
    elif encrypt=='False':
        decryptfile(inputfile,outputfile,password, size)
    
def encryptfile(inputfile, outputfile, password, size):
    obj = AES.new(password.encode("utf8"), AES.MODE_CFB, 'This is an IV456'.encode("utf8"))
    with open(inputfile, "rb") as binary_file:
        data = binary_file.read(size)
        ciphertext = obj.encrypt(data)
        theRest= binary_file.read()
    with open(outputfile, "wb") as write_file:
        write_file.write(ciphertext)
        write_file.write(theRest)     
    
def decryptfile(inputfile, outputfile, password, size):    
    obj = AES.new(password.encode("utf8"), AES.MODE_CFB, 'This is an IV456'.encode("utf8"))
    with open(inputfile, "rb") as binary_file:
        data = binary_file.read(size)
        plaintext = obj.decrypt(data)
        theRest = binary_file.read()    
    with open(outputfile, "wb") as write_file:
        write_file.write(plaintext)  
        write_file.write(theRest)   
        
if __name__ == "__main__":
    main(sys.argv[1:])