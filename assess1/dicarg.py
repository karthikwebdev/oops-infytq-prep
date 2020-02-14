def func(sample,res,key,val):
    if(key in sample):
        res = True
        sample.update({key:val})
    res = False

res = None
sample = {'xs':1,'x':0,'xl':3,'xxl':4}
func(sample,res,'x',2)
print(sample['x'],res)
