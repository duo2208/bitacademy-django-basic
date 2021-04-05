from guestbook01.models import findall

def test_findall():
    results = findall()
    
    for result in results:
        print(f'{result["no"]}:{result["name"]}:{result["reg_date"]}:result["message"]')

def test_insert():
    name = '아무개'
    passowrd = '1234'
    message = '기분별로'
    
    result = insert(name, password, message)
    print(f'insert result : {result}')

def test_delete():
    

def main():
    test_insert()
    test_findall()


if __name__ == '__main__':
    main()

