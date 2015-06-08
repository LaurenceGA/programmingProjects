gstPercent = 0.15

def gst(ammount):
    return ammount * gstPercent

def totalGST(num1, num2, num3):
    return gst(num1) + gst(num2) + gst(num3)

print(totalGST(100, 200, 300))