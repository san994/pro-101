import dropbox
import os

class TransectionData():
    def __init__(self,access_token):
        self.access_token = access_token

    def Upload_Files(self,file_from):
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            local_file = files.toString()
            relative_file = os.path.relpath(local_file,file_from)
            dropbox_path = os.path.join(relative_file,file_from)
            print(files)
            with open(local_file,'rb')as f:
                dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.A85swemRCck7Jj0P7RDeBIEF1k81WebIfXtqMYG9gN84NdR2igFG3eFQEPDmKTwodQ4Z0AYuJ_C9w9zGR5o-JL5HTtZR_JxPMwmBIlFSWbIYAbEC7xNYqYAk6XdtLeKE4IR2GBBATZ0'
    transferData = TransectionData(access_token)
    file_from = input('enter the file path to transfer: ')
    
    transferData.Upload_Files(file_from)
    print('file has been transfer')

main()