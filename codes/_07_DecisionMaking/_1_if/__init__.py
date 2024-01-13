# REQ: Get Student result.
# REQ: 1st,2nd,3rd

# State
marks = 45
# Behavior
if marks >= 35:   # 10 65 0 34 35 36
    print("PASS")
    if marks >= 60:   # 59 60 61 55 85
        print("First Class")
    elif marks >= 50:  # 49 50 51 45 57
        print("Second Class")
    else:
        print("Third Class")
else:
    print("FAIL")
