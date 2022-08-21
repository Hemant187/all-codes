import os
def isBinod(filename):
    with open(filename) as op:
        content = op.read()
    if 'binod' in content.lower():
        return True
    else:
        return False
    
if __name__ == '__main__':   
    list_content =os.listdir()
    nBinod  = 0
    for item in list_content:
        if item.endswith('txt'):
            print(f"Detecting binod in {item}")
            flag = isBinod(item)
            if(flag):
                nBinod += 1
                print(f'Binod found in {item}')
            else:
                print(f'Binod not found in {item}')
            
    print("******Binod Detector Summary!!!!!!")
    print(f"{nBinod} files found with Binod hidden into them ")

            