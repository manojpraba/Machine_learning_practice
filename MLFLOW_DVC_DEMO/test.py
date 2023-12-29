import mlflow
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y


if __name__=='__main__':

    with mlflow.start_run():
        x,y=10,20
        li=["add","sub","mul","div"]
        for i in range(len(li)):

            result=li[i]
            result1=result(x,y)
            mlflow.log_param('method',result)
            mlflow.log_param('X',x)
            mlflow.log_param('Y',y)
            mlflow.log_param("result1",result1)
            print(result)

        

    
    
