def LinearSearchProduct(productlist,targetProduct):
    indices=[]
    
    for index,product in enumerate(productlist):
        if product==targetProduct:
            indices.append(index)
    return indices
products=["shoes","boot",
          "loafer","shoes", 
          "sandal","shoes"]
target="shoes"
target2='apple'
result=LinearSearchProduct(products,target)
print(result)