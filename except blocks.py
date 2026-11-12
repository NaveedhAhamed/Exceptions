try:
    f=opem('test.txt')
except Exception :
    print('sorry,file does not exist')









try:
    f=open('test.txt')
except FileNotFoundError as e :
    print(e)
except Exception as e :
    print(e)
else:
    print(f.read())
    f.close()
#to finalize even if the project is midway
finally:
    print('executing finally')









try:
    f = open('currupt_file.txt')

    if f.name == 'currupt_file.txt':
        raise Exception

except FileNotFoundError as e:
    print(e)

except Exception as e:
    print('Error!')

else:
    print(f.read())
    f.close()

finally:
    print("Executing Finally...")