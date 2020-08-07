if os.path.basename(__file__) == 'ScredAIO-1.exe':
        
        directory = os.path.dirname(os.path.realpath(__file__))
        old_file_name = directory + '\ScredAIO-1.exe'
        new_file_name = directory +'\ScredAIO.exe'
        os.rename( old_file_name , new_file_name)