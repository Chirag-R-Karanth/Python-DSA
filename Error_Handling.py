def Error_Handling():
    try:
        num = int(input("enter boom"))
        1/num
    except ZeroDivisionError:
        print("Cant divide by zero enter another num")
        Error_Handling()
    except ValueError:
        print("Put exact value enter another num")
        Error_Handling()
    else:
        print(1/num)
    finally:
        print("done executing")

Error_Handling()